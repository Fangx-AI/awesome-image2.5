"""Import an attributed, pinned snapshot of the upstream MIT reference atlas."""
import concurrent.futures as cf,json,posixpath,re,subprocess
from pathlib import Path
from urllib.request import Request,urlopen
ROOT=Path(__file__).resolve().parents[1]
UP="wuyoscar/GPT-Image2-Skill"
def api(path):
 return json.loads(subprocess.check_output(["gh","api",path],text=True,encoding="utf-8"))
def fetch(path):
 with urlopen(Request(f"https://raw.githubusercontent.com/{UP}/{sha}/{path}",headers={"User-Agent":"awesome-image25-atlas"}),timeout=40) as response:
  return path,response.read(4000000).decode("utf-8")
def remote(path,current):
 if path.startswith(("#","http:","https:","data:","mailto:")):return path
 full=posixpath.normpath(posixpath.join(posixpath.dirname(current),path))
 return f"https://raw.githubusercontent.com/{UP}/{sha}/{full}"
def convert(text,current):
 text=re.sub(r'(src|href)="([^"]+)"',lambda m:m[1]+'="'+remote(m[2],current)+'"',text)
 return re.sub(r'\]\(([^)]+)\)',lambda m:']('+remote(m[1],current)+')',text)
if __name__=="__main__":
 sha=api(f"repos/{UP}/commits/main")["sha"]
 tree=api(f"repos/{UP}/git/trees/{sha}?recursive=1")["tree"]
 paths=[x["path"] for x in tree if x["path"].startswith("skills/gpt-image/references/") and x["path"].endswith(".md")]+["LICENSE","README.zh.md"]
 with cf.ThreadPoolExecutor(max_workers=8) as pool: files=dict(pool.map(fetch,paths))
 vendor=ROOT/"vendor/gpt-image2";vendor.mkdir(parents=True,exist_ok=True)
 dest=ROOT/"docs/reference-atlas";dest.mkdir(parents=True,exist_ok=True)
 (vendor/"LICENSE").write_text(files["LICENSE"],encoding="utf-8")
 (vendor/"UPSTREAM.json").write_text(json.dumps({"repository":UP,"commit":sha,"license":"MIT","files":paths,"original_model":"gpt-image-2","images":"Immutable upstream URLs; third-party rights remain with their authors."},indent=2)+"\n",encoding="utf-8")
 entries=[];categories=[]
 for path,body in files.items():
  if not path.startswith("skills/"):continue
  name=Path(path).name
  (vendor/name).write_text(body,encoding="utf-8")
  banner=f"> 上游 GPT Image 2 参考资料，尚未由本项目验证为 Image 2.5 输出。来源：[Wuyoscar / {name}](https://github.com/{UP}/blob/{sha}/{path}) · [MIT 许可](../../vendor/gpt-image2/LICENSE)。原作者及第三方来源标注保留。\n\n"
  (dest/name).write_text(banner+convert(body,path),encoding="utf-8")
  if not name.startswith("gallery-"):continue
  category=body.splitlines()[0].lstrip("# ");group=[]
  for match in re.finditer(r"(?m)^### No\. (\d+) · (.+)\n([\s\S]*?)(?=^### No\. |\Z)",body):
   num,title,section=match.groups()
   blocks=[{"language":m[1] or "text","text":m[2].strip()} for m in re.finditer(r"\x60{3}([^\n]*)\n([\s\S]*?)\x60{3}",section) if m[1].strip() not in ("bash","sh")]
   images=[remote(x,path) for x in re.findall(r'<img[^>]+src="([^"]+)"',section)]
   metadata=next((l.lstrip("- ") for l in section.splitlines() if l.startswith("- Metadata:")),"")
   id="reference-"+num.zfill(3)
   e={"id":id,"number":int(num),"title":title,"category":category,"category_file":name,"original_model":"gpt-image-2","verification":"upstream-reference-not-image25-verified","upstream":f"https://github.com/{UP}/blob/{sha}/{path}","images":images,"metadata":metadata,"prompts":blocks,"license":"MIT; third-party source rights retained"}
   entries.append(e);group.append(id)
   pd=dest/"prompts";pd.mkdir(exist_ok=True)
   for n,b in enumerate(blocks):(pd/f"{id}-{n+1}.txt").write_text(b["text"]+"\n",encoding="utf-8")
  categories.append({"title":category,"file":name,"entries":group})
 if len(entries)!=162:raise ValueError(f"Expected 162 cases, got {len(entries)}; inspect upstream changes.")
 if any(not e["prompts"] or not e["images"] for e in entries):raise ValueError("A case has no prompt or preview; manual review required.")
 index={"upstream":UP,"commit":sha,"original_model":"gpt-image-2","categories":categories,"entries":sorted(entries,key=lambda x:x["number"])}
 (ROOT/"catalog/reference-atlas.json").write_text(json.dumps(index,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 (vendor/"README.zh.md").write_text(files["README.zh.md"],encoding="utf-8")
 print(json.dumps({"commit":sha,"categories":len(categories),"cases":len(entries),"images":sum(len(e["images"]) for e in entries),"prompts":sum(len(e["prompts"]) for e in entries)}))

