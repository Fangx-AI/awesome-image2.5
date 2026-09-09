"""Collect source links through GitHub API; never equate discovery with verification."""
import concurrent.futures as cf
import datetime, json, re, subprocess
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
REPO = "wuyoscar/GPT-Image2-Skill"

def api(path):
    return json.loads(subprocess.check_output(["gh", "api", path], text=True, encoding="utf-8"))

def fetch(item):
    url = "https://raw.githubusercontent.com/" + REPO + "/" + commit + "/" + item["path"]
    try:
        with urlopen(Request(url, headers={"User-Agent":"awesome-image25-source-index"}), timeout=25) as response:
            body = response.read(3000000).decode("utf-8")
        links = sorted(set(re.findall(r'https?://[^\s<>\)\]"}]+', body)))
        return {"file":item["path"], "links":links}
    except Exception as exc:
        return {"file":item["path"], "error":str(exc), "links":[]}

if __name__ == "__main__":
    commit = api("repos/" + REPO + "/commits/main")["sha"]
    tree = api("repos/" + REPO + "/git/trees/" + commit + "?recursive=1")["tree"]
    files = [i for i in tree if i["path"].endswith(".md") and ("gallery" in i["path"] or "community-prompt-index" in i["path"])]
    with cf.ThreadPoolExecutor(max_workers=8) as pool:
        pages = list(pool.map(fetch, files))
    sources = {}
    for page in pages:
        for url in page["links"]:
            if re.search(r"https?://(?:www\.)?(?:x\.com|twitter\.com)/[^/]+/status/\d+", url):
                key = re.sub(r"\?.*$", "", url).replace("twitter.com/", "x.com/")
                kind = "x-post"
            else:
                key, kind = url, "web"
            sources.setdefault(key, {"url":key, "kind":kind, "discovered_in":[], "verification":"unreviewed", "model":"unverified"})
            sources[key]["discovered_in"].append(page["file"])
    report = {"collected_at":datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "upstream":REPO, "commit":commit, "files_requested":len(files),
              "files_read":sum("error" not in p for p in pages),
              "errors":[p for p in pages if "error" in p], "sources":list(sources.values())}
    target = ROOT / "catalog" / "source-candidates.json"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(json.dumps({"files_read":report["files_read"], "unique_links":len(sources),
                      "x_posts":sum(s["kind"]=="x-post" for s in sources.values()),
                      "errors":len(report["errors"]), "output":str(target)}))

