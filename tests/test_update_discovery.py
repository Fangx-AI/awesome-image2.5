import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('discover_updates', ROOT/'scripts/discover_updates.py')
discovery=importlib.util.module_from_spec(spec)
spec.loader.exec_module(discovery)

class DiscoveryTests(unittest.TestCase):
    def test_discovery_is_deduplicated_and_never_changes_catalog(self):
        before=(ROOT/'catalog/web-image25.json').read_bytes()
        repo={'full_name':'sample/new-gallery','html_url':'https://github.com/sample/new-gallery'}
        lead={'repository':repo['full_name'],'x_posts':['https://x.com/example/status/2999999999999999999']}
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(discovery,'search',return_value=[repo]), patch.object(discovery,'inspect',return_value=lead), patch('sys.argv',['discover_updates','--output-dir',folder]):
                discovery.main()
            report=json.loads((Path(folder)/'discovery.json').read_text(encoding='utf-8'))
            self.assertEqual(len(report['repositories']),1)
            self.assertEqual(len(report['new_x_posts']),1)
        self.assertEqual(before,(ROOT/'catalog/web-image25.json').read_bytes())

    def test_total_source_failure_is_not_reported_as_empty_success(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(discovery,'search',side_effect=RuntimeError('network unavailable')), patch('sys.argv',['discover_updates','--output-dir',folder]):
                with self.assertRaises(SystemExit):discovery.main()
            report=json.loads((Path(folder)/'discovery.json').read_text(encoding='utf-8'))
            self.assertEqual(len(report['search_errors']),len(discovery.QUERIES))
