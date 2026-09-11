"""Discover public source leads; write only to a review workspace, never the gallery."""
import argparse
import base64
import concurrent.futures
import datetime
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QUERIES = ['"gpt-image-2.5"', '"image2.5" prompts', '"chatgpt images 2.5"']

def api(path):
    raw = subprocess.check_output(['gh', 'api', path], timeout=40)
    return json.loads(raw)

def search(query):
    from urllib.parse import urlencode
    return api('search/repositories?' + urlencode({'q': query, 'sort': 'updated', 'per_page': 10}))['items']

def inspect(repo):
    name = repo['full_name']
    try:
        result = api('repos/' + name + '/readme')
        body = base64.b64decode(result['content']).decode('utf-8', errors='replace')
        posts = sorted(set(re.findall(r'https://(?:x|twitter)\.com/[A-Za-z0-9_]+/status/\d{15,22}', body)))
        return {'repository': name, 'url': repo['html_url'], 'readme_sha': result['sha'],
                'license': (repo.get('license') or {}).get('spdx_id'), 'x_posts': posts,
                'status': 'discovery-only-not-model-verified'}
    except Exception as error:
        return {'repository': name, 'error': str(error)}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=Path, default=ROOT/'.cache/update-review')
    args = parser.parse_args()
    out = args.output_dir.resolve()
    if out == ROOT or out == ROOT/'catalog' or ROOT/'catalog' in out.parents:
        raise ValueError('Discovery output must stay outside the published catalog')
    out.mkdir(parents=True, exist_ok=True)
    repos, errors = {}, []
    for query in QUERIES:
        try:
            for item in search(query):
                if item['full_name'].lower() != 'fangx-ai/awesome-image2.5':
                    repos[item['full_name']] = item
        except Exception as error:
            errors.append({'query': query, 'error': str(error)})
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(inspect, list(repos.values())[:20]))
    known = set(json.loads((ROOT/'catalog/x-seeds.json').read_text(encoding='utf-8')))
    posts = sorted({url for result in results for url in result.get('x_posts', [])} - known)
    report = {'collected_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'repositories': results, 'search_errors': errors, 'new_x_posts': posts,
              'review_required': 'Read original evidence and inspect images before publishing. Repository names are not model evidence.'}
    (out/'discovery.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    (out/'new-x-seeds.json').write_text(json.dumps(posts[:50], indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'repositories': len(results), 'new_x_posts': len(posts), 'errors': len(errors), 'output': str(out)}))
    if not repos and errors:
        raise SystemExit('All discovery searches failed; previous catalog was not changed.')

if __name__ == '__main__':
    main()
