"""Verify evidence separation and navigable generated source galleries."""
import html
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]

class SourceGalleryTests(unittest.TestCase):
    def test_source_links_survive_html_generation(self):
        data = json.loads((ROOT / 'catalog/image25-index.json').read_text(encoding='utf-8'))
        entries = data['entries']
        self.assertEqual(len(entries), len({entry['id'] for entry in entries}))
        gallery = (ROOT / 'docs/gallery.html').read_text(encoding='utf-8')
        for entry in entries:
            with self.subTest(case=entry['id']):
                self.assertIn('2.5', entry['model_claim'])
                self.assertTrue(entry['author'] and entry['rights'] and entry['images'])
                self.assertIn(entry['verification'], data['evidence_counts'])
                for key in ('source_url', 'prompt_url'):
                    self.assertTrue(entry[key].startswith('https://'))
                self.assertIn('href="' + html.escape(entry['prompt_url'], quote=True) + '"', gallery)
                for suffix in ('md', 'html'):
                    self.assertTrue((ROOT / 'docs/image25/cases' / (entry['id'] + '.' + suffix)).is_file())
        self.assertEqual(len(entries), sum(data['evidence_counts'].values()))

    def test_legacy_and_unknown_model_outputs_are_separate(self):
        gallery = (ROOT / 'docs/gallery.html').read_text(encoding='utf-8')
        self.assertIn('value="image25" selected', gallery)
        self.assertTrue((ROOT / 'vendor/gpt-image2/LICENSE').is_file())
        originals = json.loads((ROOT / 'catalog/showcase.json').read_text(encoding='utf-8'))
        for entry in originals:
            if entry['status'] == 'host-model-unknown':
                self.assertIsNone(entry['model'])

    def test_reference_input_is_available_in_browser(self):
        page = (ROOT / 'docs/image25/cases/simon-raccoon-chart.html').read_text(encoding='utf-8')
        self.assertIn('openai-agent-usage.webp', page)
        self.assertIn('add a raccoon scientist', page)
