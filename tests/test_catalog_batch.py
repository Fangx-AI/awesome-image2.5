import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from image25.catalog import load_catalog, search, find_recipe
from image25.batch import load_jobs, run_batch
from image25.cli import parser, prepare


class CatalogTests(unittest.TestCase):
    def test_catalog_integrity(self):
        data = load_catalog()
        entries = data["entries"]
        ids = [e["id"] for e in entries]
        self.assertEqual(len(ids), len(set(ids)))
        categories = {c["id"] for c in data["categories"]}
        originals = {e["id"] for e in entries if e["kind"] == "original"}
        for e in entries:
            with self.subTest(id=e["id"]):
                self.assertIn(e["category"], categories)
                self.assertIn(e["family_id"], originals)
                self.assertIn(e["status"], ("prompt-only", "host-model-unknown", "api-verified"))
                self.assertGreater(len(e["prompt"]), 60)
                if e["mode"] == "edit":
                    self.assertGreaterEqual(e["requires"], 1)

    def test_search_combines_filters(self):
        results = search("杯", category="product", mode="generate", kind="original")
        self.assertTrue(results)
        self.assertTrue(all(e["category"] == "product" and e["kind"] == "original" for e in results))
        self.assertEqual(search("this-word-does-not-exist-abc123"), [])

    def test_recipe_matches_prompt(self):
        args = parser().parse_args(["--recipe", "product-radio", "--dry-run"])
        self.assertEqual(prepare(args)[0]["prompt"], find_recipe("product-radio")["prompt"])

    def test_edit_recipe_requires_references(self):
        args = parser().parse_args(["--recipe", "reference-composite", "--dry-run"])
        with self.assertRaisesRegex(ValueError, "at least 2"):
            prepare(args)

    def test_unknown_recipe(self):
        with self.assertRaises(ValueError):
            find_recipe("missing-recipe")


class BatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.manifest = self.root / "batch.json"

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, jobs):
        self.manifest.write_text(json.dumps({"jobs": jobs}), encoding="utf-8")

    def test_paths_relative_to_manifest(self):
        self.write([{"prompt": "cat", "output": "images/cat.png"}])
        args = load_jobs(self.manifest)[0][1]
        self.assertEqual(args.output, self.root / "images/cat.png")

    def test_entire_batch_prevalidated_before_api(self):
        self.write([{"prompt": "cat", "output": "cat.png"},
                    {"prompt": "dog", "output": "dog.png", "size": "1x1"}])
        with patch("image25.batch.run") as call:
            with self.assertRaises(ValueError):
                run_batch(self.manifest)
            call.assert_not_called()

    def test_duplicate_output_rejected(self):
        self.write([{"prompt": "cat", "output": "same.png"},
                    {"prompt": "dog", "output": "./same.png"}])
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            load_jobs(self.manifest)

    def test_dry_run_no_execution(self):
        self.write([{"recipe": "product-radio", "output": "radio.png"}])
        with patch("image25.batch.run") as call, contextlib.redirect_stdout(io.StringIO()) as stream:
            run_batch(self.manifest, dry_run=True)
            call.assert_not_called()
        self.assertEqual(json.loads(stream.getvalue())[0]["operation"], "generate")
        self.assertFalse((self.root / "radio.png").exists())

    def test_stop_on_failure(self):
        self.write([{"id": "a", "prompt": "cat", "output": "a.png"},
                    {"id": "b", "prompt": "dog", "output": "b.png"}])
        with patch("image25.batch.run", side_effect=TimeoutError("timeout")) as call:
            with self.assertRaises(TimeoutError):
                run_batch(self.manifest)
            self.assertEqual(call.call_count, 1)

    def test_unknown_manifest_field_rejected(self):
        self.write([{"prompt": "cat", "output": "cat.png", "quallity": "high"}])
        with self.assertRaisesRegex(ValueError, "unknown"):
            load_jobs(self.manifest)
