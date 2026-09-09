"""Collect author-reported Image 2.5 case metadata; link original prompts without copying them."""
import concurrent.futures as cf,json,posixpath,re,subprocess
from pathlib import Path
from urllib.request import Request,urlopen
R=Path(__file__).resolve().parents[1];REPO="LaplaceYoung/awesome-gpt-image-2.5"
def api(p):return json.loads(subprocess.check_output(["gh","api",p]))
def fetch(path):
 with urlopen(Request(f"https://raw.githubusercontent.com/{REPO}/{sha}/{path}",headers={"User-Agent":"awesome-image25-research"}),timeout=30) as response:return path,response.read(2000000).decode("utf-8")
if __name__=="__main__":
 sha=api("repos/"+REPO+"/commits/main")["sha"]
 tree=api("repos/"+REPO+"/git/trees/"+sha+"?recursive=1")["tree"];blobs={i["path"]:i for i in tree}
 paths=[i["path"] for i in tree if i["path"].startswith("docs/cases/") and i["path"].endswith(".md")]
 with cf.ThreadPoolExecutor(max_workers=8) as pool:pages=dict(pool.map(fetch,paths))
 records=[]
 for path,text in pages.items():
  title=text.splitlines()[0].lstrip("# ")
  category=re.search(r"\| Category \| ([^|]+)\|",text)
  model=re.search(r"\| Model \| ([^|]+)\|",text)
  image_paths=sorted(set(re.findall(r"(?:\]\(|href=[\"'])(\.\./\.\./assets/generated/[^)\"'\s]+)",text)))
  imgs=[]
  for p in image_paths:
   full=posixpath.normpath(posixpath.join(posixpath.dirname(path),p))
   if full in blobs:imgs.append({"url":f"https://raw.githubusercontent.com/{REPO}/{sha}/{full}","upstream_path":full,"git_blob_sha":blobs[full]["sha"]})
  if not imgs:continue
  records.append({"id":"laplace-"+Path(path).stem,"title":title,"category":category[1].strip() if category else "Uncategorized","author":"LaplaceYoung","source_url":f"https://github.com/{REPO}/blob/{sha}/{path}","prompt_url":f"https://github.com/{REPO}/blob/{sha}/{path}","model_claim":model[1].strip() if model else "GPT Image 2.5 (repository-level declaration)","verification":"author-reported-not-independently-tested","model_evidence_url":f"https://github.com/{REPO}/blob/{sha}/README.md","images":imgs,"rights":"Images linked to publisher; underlying third-party rights not reassigned","prompt_republished":False})
 (R/"catalog/community-image25.json").write_text(json.dumps({"source_repository":REPO,"commit":sha,"records":records},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"pages":len(pages),"image_backed_cases":len(records),"images":sum(len(r["images"]) for r in records),"explicit_case_model":sum("repository-level" not in r["model_claim"] for r in records)}))

