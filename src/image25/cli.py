"""One explicit Images API request, with local validation and no automatic retries."""
import argparse
import base64
import binascii
from contextlib import ExitStack
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import re
import sys

MODELS = {name: "gpt-image-2.5-" + name for name in ("flare", "sunburst")}
QUALITIES = ("auto", "low", "medium", "high", "xhigh", "max")


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    prompt = p.add_mutually_exclusive_group(required=True)
    prompt.add_argument("-p", "--prompt")
    prompt.add_argument("--prompt-file", type=Path)
    prompt.add_argument("--recipe", help="Use an offline catalog recipe ID")
    p.add_argument("--model", choices=tuple(MODELS) + tuple(MODELS.values()), default="flare")
    p.add_argument("-i", "--image", action="append", type=Path, default=[])
    p.add_argument("--mask", type=Path)
    p.add_argument("--size", default="1024x1024")
    p.add_argument("--quality", choices=QUALITIES, default="auto")
    p.add_argument("--background", choices=("auto", "opaque", "transparent"), default="auto")
    p.add_argument("--format", choices=("png", "jpeg", "webp"), default="png")
    p.add_argument("-o", "--output", type=Path, default=Path("generated/image.png"))
    p.add_argument("--dry-run", action="store_true", help="Validate and print request; no key or network needed")
    return p


def prepare(args):
    if args.recipe:
        from .catalog import find_recipe
        recipe = find_recipe(args.recipe)
        prompt = recipe["prompt"]
        if recipe["mode"] == "edit" and len(args.image) < recipe["requires"]:
            raise ValueError(f"Recipe requires at least {recipe['requires']} reference image(s).")
    else:
        prompt = args.prompt if args.prompt is not None else args.prompt_file.read_text(encoding="utf-8")
    if not prompt.strip():
        raise ValueError("Prompt cannot be empty.")
    if args.size != "auto":
        match = re.fullmatch(r"([1-9][0-9]*)x([1-9][0-9]*)", args.size)
        if not match:
            raise ValueError("Size must be auto or WIDTHxHEIGHT.")
        w, h = map(int, match.groups())
        if (w % 16 or h % 16 or max(w, h) > 3840 or max(w, h) > 3 * min(w, h)
                or not 655360 <= w * h <= 8294400):
            raise ValueError("Unsupported size: use multiples of 16, edges <=3840, ratio <=3:1, 655360–8294400 pixels.")
    if args.background == "transparent" and args.format == "jpeg":
        raise ValueError("Transparent output requires png or webp.")
    extensions = {"png": (".png",), "jpeg": (".jpg", ".jpeg"), "webp": (".webp",)}
    if args.output.suffix.lower() not in extensions[args.format]:
        raise ValueError("Output extension must match --format.")
    sidecar = args.output.with_suffix(args.output.suffix + ".json")
    if args.output.exists() or sidecar.exists():
        raise ValueError("Output or metadata already exists; choose a new --output path.")
    inputs = args.image + ([args.mask] if args.mask else [])
    if args.mask and not args.image:
        raise ValueError("--mask requires at least one --image.")
    if inputs:
        from PIL import Image
        sizes = []
        for path in inputs:
            if not path.is_file():
                raise ValueError("Input does not exist: " + str(path))
            with Image.open(path) as im:
                im.verify()
            with Image.open(path) as im:
                if im.format not in ("PNG", "JPEG", "WEBP"):
                    raise ValueError("Inputs must be PNG, JPEG or WebP.")
                sizes.append(im.size)
                if path == args.mask:
                    if im.format != "PNG" or "A" not in im.getbands():
                        raise ValueError("Mask must be a PNG with an alpha channel.")
                    if im.getchannel("A").getextrema()[0] == 255:
                        raise ValueError("Mask has no transparent edit region.")
        if args.mask and sizes[-1] != sizes[0]:
            raise ValueError("Mask must match the first reference image dimensions.")
    payload = dict(model=MODELS.get(args.model, args.model), prompt=prompt,
                   size=args.size, quality=args.quality, background=args.background,
                   output_format=args.format, n=1)
    return payload, sidecar


def make_client():
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        raise ValueError("Set OPENAI_API_KEY locally, or use --dry-run.")
    from openai import OpenAI
    return OpenAI(api_key=key, base_url="https://api.openai.com/v1",
                  max_retries=0, timeout=600.0)


def run(args, client=None):
    payload, sidecar = prepare(args)
    operation = "edit" if args.image else "generate"
    if args.dry_run:
        print(json.dumps({"operation": operation, "request": payload,
                          "images": [str(p) for p in args.image],
                          "mask": str(args.mask) if args.mask else None,
                          "output": str(args.output)}, ensure_ascii=False, indent=2))
        return
    if client is None:
        client = make_client()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    # Reserve both paths before a billable request, and never overwrite existing files.
    with ExitStack() as stack:
        output = stack.enter_context(args.output.open("xb"))
        try:
            metadata = stack.enter_context(sidecar.open("x", encoding="utf-8"))
        except Exception:
            output.close()
            args.output.unlink()
            raise
        try:
            if args.image:
                request = dict(payload)
                request["image"] = [stack.enter_context(p.open("rb")) for p in args.image]
                if args.mask:
                    request["mask"] = stack.enter_context(args.mask.open("rb"))
                result = client.images.edit(**request)
            else:
                result = client.images.generate(**payload)
            if not result.data or not result.data[0].b64_json:
                raise ValueError("API returned no base64 image.")
            raw = base64.b64decode(result.data[0].b64_json, validate=True)
            from PIL import Image
            with Image.open(io.BytesIO(raw)) as im:
                im.verify()
                actual_format = im.format.lower()
            if actual_format != args.format:
                raise ValueError("Returned image format does not match the requested format.")
            output.write(raw)
            record = {"created_at": datetime.now(timezone.utc).isoformat(),
                      "operation": operation, "request": payload,
                      "reference_names": [p.name for p in args.image],
                      "mask_name": args.mask.name if args.mask else None,
                      "request_id": getattr(result, "_request_id", None)}
            metadata.write(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
        except Exception:
            output.close()
            metadata.close()
            args.output.unlink(missing_ok=True)
            sidecar.unlink(missing_ok=True)
            raise
    print(str(args.output.resolve()))


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "catalog":
        from .catalog import main as catalog_main
        return catalog_main(argv[1:])
    if argv and argv[0] == "batch":
        from .batch import main as batch_main
        return batch_main(argv[1:])
    args = parser().parse_args(argv)
    try:
        run(args)
    except (ValueError, OSError, binascii.Error) as exc:
        print("image25: " + str(exc), file=sys.stderr)
        return 1
    except Exception as exc:
        # Do not dump request bodies, reference images or credentials on API failures.
        status = getattr(exc, "status_code", None)
        request_id = getattr(exc, "request_id", None)
        print(f"image25: {type(exc).__name__}; status={status}; request_id={request_id}. "
              "No automatic retry. Check access, limits and request parameters.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
