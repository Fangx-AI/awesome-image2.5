"""Ensure showcased outputs remain reproducible and traceable."""
import json
from pathlib import Path
import unittest
from PIL import Image
R=Path(__file__).resolve().parents[1]
class ShowcaseTests(unittest.TestCase):
 def test_every_case_has_matching_prompt_and_real_asset(self):
  entries=json.loads((R/'catalog/showcase.json').read_text(encoding='utf-8'))
  self.assertEqual(len(entries),len({e['id'] for e in entries}))
  for e in entries:
   with self.subTest(case=e['id']):
    base=R/'assets/showcase'/e['id']
    self.assertEqual(base.with_suffix('.txt').read_text(encoding='utf-8').strip(),e['prompt'].strip())
    with Image.open(base.with_suffix('.png')) as image:
     self.assertGreaterEqual(min(image.size),512)
    self.assertIn(e['status'],['host-model-unknown','api-verified'])
    if e['status']=='host-model-unknown':self.assertIsNone(e['model'])
    for input_path in e.get('input_images',[]):
     self.assertTrue((R/'assets/showcase'/Path(input_path).name).exists())
    self.assertTrue(e['use'] and e['learn'] and e['change'] and e['check'])

