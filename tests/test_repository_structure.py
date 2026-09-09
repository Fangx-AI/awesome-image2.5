"""Ensure the GitHub showcase and independently installed Skill stay aligned."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RepositoryStructureTests(unittest.TestCase):
    def test_every_reference_category_is_accessible_from_readme_and_skill(self):
        upstream = json.loads((ROOT/'catalog/reference-atlas.json').read_text(encoding='utf-8'))
        categories = json.loads((ROOT/'catalog/category-index.json').read_text(encoding='utf-8'))
        self.assertEqual({c['file'] for c in categories}, {c['file'] for c in upstream['categories']})
        router = (ROOT/'skills/image25/references/gallery.md').read_text(encoding='utf-8')
        for c in categories:
            with self.subTest(category=c['file']):
                self.assertIn(c['file'], router)
                category = (ROOT/'skills/image25/references'/c['file']).read_text(encoding='utf-8')
                self.assertIn('不是下方来源作品的原始提示词', category)
                self.assertIn('GPT Image 2 学习图谱', category)
                for name in ['README.md','README.en.md']:
                    readme = (ROOT/name).read_text(encoding='utf-8')
                    self.assertIn('id="gallery-'+c['slug']+'"', readme)
                    self.assertIn('skills/image25/references/'+c['file'], readme)

    def test_unique_source_counts_exclude_official_cross_reference(self):
        categories = json.loads((ROOT/'catalog/category-index.json').read_text(encoding='utf-8'))
        source = json.loads((ROOT/'catalog/image25-index.json').read_text(encoding='utf-8'))
        count = sum(c['current_count'] for c in categories if c['slug']!='official-openai-cookbook-examples')
        self.assertEqual(count, len(source['entries']))
        self.assertEqual(sum(c['own_count'] for c in categories), 14)
        self.assertEqual(sum(c['legacy_count'] for c in categories), 162)

    def test_bilingual_readmes_show_identical_images_and_anchors(self):
        zh=(ROOT/'README.md').read_text(encoding='utf-8')
        en=(ROOT/'README.en.md').read_text(encoding='utf-8')
        self.assertEqual(re.findall(r'<img src="([^"]+)"',zh),re.findall(r'<img src="([^"]+)"',en))
        self.assertEqual(re.findall(r'<a id="([^"]+)"',zh),re.findall(r'<a id="([^"]+)"',en))
