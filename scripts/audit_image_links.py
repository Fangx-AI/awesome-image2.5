"""Audit remote preview links with HEAD requests; never download the images."""
import concurrent.futures as cf,json
from pathlib import Path
from urllib.request import Request,urlopen
R=Path(__file__).resolve().parents[1]
urls=sorted({i['url'] for e in json.loads((R/'catalog/image25-index.json').read_text(encoding='utf-8'))['entries'] for i in e['images']})
def check(url):
 try:
  with urlopen(Request(url,method='HEAD',headers={'User-Agent':'awesome-image25-link-audit'}),timeout=15) as response:
   return {'url':url,'status':response.status,'content_type':response.headers.get('Content-Type')}
 except Exception as e:return {'url':url,'error':str(e)}
with cf.ThreadPoolExecutor(max_workers=8) as pool:rows=list(pool.map(check,urls))
(R/'catalog/image-link-audit.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'urls':len(rows),'ok':sum(r.get('status')==200 for r in rows),'errors':[r for r in rows if r.get('status')!=200]}))

