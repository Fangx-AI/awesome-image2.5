"""Run independent image jobs sequentially after validating the entire manifest."""
import argparse
import json
import os
from pathlib import Path
import sys

from .cli import parser, prepare, run


def load_jobs(path):
    path = Path(path).resolve()
    manifest = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict) or set(manifest) != {"jobs"}:
        raise ValueError("Manifest must contain exactly a jobs array.")
    jobs = manifest["jobs"]
    if not isinstance(jobs, list) or not jobs:
        raise ValueError("jobs must be a non-empty array.")
    allowed = {"id", "prompt", "prompt_file", "recipe", "model", "images", "mask",
               "size", "quality", "background", "format", "output"}
    parsed, reserved, names = [], set(), set()
    for index, job in enumerate(jobs, 1):
        if not isinstance(job, dict) or set(job) - allowed:
            raise ValueError(f"Job {index}: unknown fields or invalid object.")
        name = job.get("id", str(index))
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError(f"Job {index}: id must be a unique non-empty string.")
        names.add(name)
        sources = [field for field in ("prompt", "prompt_file", "recipe") if field in job]
        if len(sources) != 1 or "output" not in job:
            raise ValueError(f"Job {name}: provide one prompt source and an output.")
        images = job.get("images", [])
        if not isinstance(images, list) or not all(isinstance(v, str) and v for v in images):
            raise ValueError(f"Job {name}: images must be an array of paths.")
        argv = []
        for field, value in job.items():
            if field in ("id", "images"):
                continue
            if not isinstance(value, str) or not value:
                raise ValueError(f"Job {name}: {field} must be a non-empty string.")
            if field in ("prompt_file", "mask", "output"):
                value = str((path.parent / value).resolve())
            argv += ["--" + field.replace("_", "-"), value]
        for image in images:
            argv += ["--image", str((path.parent / image).resolve())]
        args = parser().parse_args(argv)
        payload, sidecar = prepare(args)
        for output in (args.output, sidecar):
            key = os.path.normcase(str(output.resolve()))
            if key in reserved:
                raise ValueError("Duplicate output or metadata path in manifest: " + str(output))
            reserved.add(key)
        parsed.append((name, args, payload))
    return parsed


def run_batch(path, dry_run=False, client=None):
    jobs = load_jobs(path)
    if dry_run:
        print(json.dumps([{"id": name, "operation": "edit" if args.image else "generate",
                           "request": payload, "images": [str(p) for p in args.image],
                           "mask": str(args.mask) if args.mask else None,
                           "output": str(args.output)} for name, args, payload in jobs],
                         ensure_ascii=False, indent=2))
        return
    for index, (name, args, _) in enumerate(jobs, 1):
        print(f"[{index}/{len(jobs)}] {name}", file=sys.stderr)
        run(args, client=client)


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("manifest", type=Path)
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args(argv)
    try:
        run_batch(args.manifest, args.dry_run)
    except (ValueError, OSError) as exc:
        print("image25 batch: " + str(exc), file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"image25 batch: {type(exc).__name__}; stopped. Completed outputs remain. "
              "No automatic retry.", file=sys.stderr)
        return 1
    return 0
