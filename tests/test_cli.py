import base64
import contextlib
import io
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from PIL import Image
from image25.cli import parser, prepare, run, main


def png_bytes():
    b = io.BytesIO()
    Image.new("RGB", (16, 16), "blue").save(b, "PNG")
    return b.getvalue()


class CliTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.output = self.root / "result.png"

    def tearDown(self):
        self.tmp.cleanup()

    def args(self, *extra):
        return parser().parse_args(["-p", "一只猫", "-o", str(self.output), *extra])

    def client(self):
        client = Mock()
        result = SimpleNamespace(data=[SimpleNamespace(b64_json=base64.b64encode(png_bytes()).decode())],
                                 _request_id="test-request")
        client.images.generate.return_value = result
        client.images.edit.return_value = result
        return client

    def test_model_and_new_quality(self):
        payload, _ = prepare(self.args("--model", "sunburst", "--quality", "max"))
        self.assertEqual(payload["model"], "gpt-image-2.5-sunburst")
        self.assertEqual(payload["quality"], "max")

    def test_generation_and_metadata(self):
        client = self.client()
        run(self.args(), client)
        self.assertEqual(self.output.read_bytes(), png_bytes())
        info = json.loads(self.output.with_suffix(".png.json").read_text(encoding="utf-8"))
        self.assertEqual(info["request"]["prompt"], "一只猫")
        self.assertEqual(info["request_id"], "test-request")
        client.images.generate.assert_called_once()
        client.images.edit.assert_not_called()

    def test_edit_reference_order_and_mask(self):
        refs = [self.root / "first.png", self.root / "second.png"]
        for ref in refs:
            ref.write_bytes(png_bytes())
        mask = self.root / "mask.png"
        Image.new("RGBA", (16, 16), (0, 0, 0, 0)).save(mask)
        client = self.client()
        run(self.args("-i", str(refs[0]), "-i", str(refs[1]), "--mask", str(mask)), client)
        sent = client.images.edit.call_args.kwargs
        self.assertEqual([Path(f.name) for f in sent["image"]], refs)
        self.assertEqual(Path(sent["mask"].name), mask)
        self.assertTrue(all(f.closed for f in sent["image"]))
        client.images.generate.assert_not_called()

    def test_dry_run_without_key_or_network(self):
        with patch.dict("os.environ", {}, clear=True), patch("image25.cli.make_client") as constructor:
            with contextlib.redirect_stdout(io.StringIO()) as out:
                run(self.args("--dry-run"))
            constructor.assert_not_called()
        self.assertEqual(json.loads(out.getvalue())["operation"], "generate")
        self.assertFalse(self.output.exists())

    def test_existing_output_not_overwritten_or_billed(self):
        self.output.write_text("keep")
        client = self.client()
        with self.assertRaises(ValueError):
            run(self.args(), client)
        self.assertEqual(self.output.read_text(), "keep")
        client.images.generate.assert_not_called()

    def test_validation(self):
        for flags in (("--size", "0x1024"), ("--size", "1000x1000"),
                      ("--size", "16x16"), ("--size", "3840x3840"),
                      ("--mask", "missing.png"),
                      ("--background", "transparent", "--format", "jpeg")):
            with self.subTest(flags=flags), self.assertRaises(ValueError):
                prepare(self.args(*flags))

    def test_invalid_mask_dimensions(self):
        ref = self.root / "ref.png"
        ref.write_bytes(png_bytes())
        mask = self.root / "mask.png"
        Image.new("RGBA", (32, 16), (0, 0, 0, 0)).save(mask)
        with self.assertRaisesRegex(ValueError, "dimensions"):
            prepare(self.args("-i", str(ref), "--mask", str(mask)))

    def test_api_error_cleans_reserved_files_and_no_retry(self):
        client = self.client()
        client.images.generate.side_effect = TimeoutError("timeout")
        with self.assertRaises(TimeoutError):
            run(self.args(), client)
        self.assertFalse(self.output.exists())
        self.assertFalse(self.output.with_suffix(".png.json").exists())
        self.assertEqual(client.images.generate.call_count, 1)

    def test_invalid_response_cleans_files(self):
        client = self.client()
        client.images.generate.return_value.data[0].b64_json = "not-base64!"
        with self.assertRaises(ValueError):
            run(self.args(), client)
        self.assertFalse(self.output.exists())

    def test_prompt_file_utf8(self):
        prompt = self.root / "prompt.txt"
        prompt.write_text("中文海报", encoding="utf-8")
        args = parser().parse_args(["--prompt-file", str(prompt), "-o", str(self.output)])
        self.assertEqual(prepare(args)[0]["prompt"], "中文海报")

    def test_missing_key_returns_failure(self):
        with patch.dict("os.environ", {}, clear=True), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(["-p", "cat", "-o", str(self.output)]), 1)


if __name__ == "__main__":
    unittest.main()
