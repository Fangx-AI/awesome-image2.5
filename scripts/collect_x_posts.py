"""Read public X post records from FxTwitter; export minimal provenance, not copied long posts."""
import argparse,concurrent.futures as cf,datetime,hashlib,json,re
from pathlib import Path
from urllib.request import Request,urlopen
def fetch(url,cache):
 id=re.search(r"/status/(\d{15,22})",url).group(1)
 try:
  with urlopen(Request("https://api.fxtwitter.com/status/"+id,headers={"User-Agent":"awesome-image25-source-research"}),timeout=25) as response:data=json.load(response)
  tweet=data.get("tweet",{})
  if data.get("code")!=200 or not tweet:raise ValueError("Post unavailable")
  cache.mkdir(parents=True,exist_ok=True)
  (cache/(id+".json")).write_text(json.dumps(data,ensure_ascii=False),encoding="utf-8")
  body=tweet.get("text","")
  claim=re.search(r"(?:GPT[- ]?Images?|ChatGPT Images?)[- ]?2\.5",body,re.I)
  photos=[{"url":p["url"],"width":p.get("width"),"height":p.get("height")} for p in tweet.get("media",{}).get("photos",[])]
  return {"id":id,"url":"https://x.com/"+tweet.get("author",{}).get("screen_name","i")+"/status/"+id,"author":tweet.get("author",{}).get("screen_name"),"published_at":tweet.get("created_at"),"model_evidence":claim.group() if claim else None,"verification":"author-claim-via-public-mirror" if claim else "model-unverified","prompt_available":bool(re.search(r"prompt|提示词",body,re.I)),"images":photos,"text_sha256":hashlib.sha256(body.encode()).hexdigest(),"retrieval":"FxTwitter public API","rights":"Original author; no license inferred from public availability"}
 except Exception as e:return {"id":id,"url":url,"verification":"fetch-failed","error":str(e)}
def main():
 p=argparse.ArgumentParser();p.add_argument("seeds",type=Path);p.add_argument("--output",type=Path,required=True);p.add_argument("--cache",type=Path,default=Path(".cache/x-posts"));a=p.parse_args()
 seeds=json.loads(a.seeds.read_text(encoding="utf-8"))
 urls=sorted(set(u for u in seeds if re.fullmatch(r"https://(?:x|twitter)\.com/[^/]+/status/\d{15,22}",u)))
 with cf.ThreadPoolExecutor(max_workers=6) as pool:records=list(pool.map(lambda u:fetch(u,a.cache),urls))
 a.output.parent.mkdir(parents=True,exist_ok=True)
 a.output.write_text(json.dumps({"collected_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),"records":records},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
 print(json.dumps({"posts":len(records),"with_model_claim":sum(r["verification"]=="author-claim-via-public-mirror" for r in records),"photos":sum(len(r.get("images",[])) for r in records),"failures":sum(r["verification"]=="fetch-failed" for r in records)}))
if __name__=="__main__":main()

