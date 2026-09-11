"""Build searchable gallery, skill references and package data from the catalog."""
import csv
import html
import io
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(path, text):
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def build():
    data = json.loads((ROOT / "catalog/recipes.json").read_text(encoding="utf-8"))
    entries = data["entries"]
    ids = [e["id"] for e in entries]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate recipe IDs")
    categories = {c["id"]: c for c in data["categories"]}
    for e in entries:
        if e["category"] not in categories or not e["prompt"].strip():
            raise ValueError("Invalid category or empty prompt: " + e["id"])
    encoded = json.dumps(data, ensure_ascii=False, indent=2)
    write("src/image25/data/recipes.json", encoded)
    write("catalog/recipes.jsonl", "\n".join(json.dumps(e, ensure_ascii=False) for e in entries))
    stream = io.StringIO(newline="")
    fields = ["id", "title", "category", "mode", "kind", "family_id", "variant", "status", "size", "model", "requires", "prompt"]
    writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore", lineterminator="\n")
    writer.writeheader()
    writer.writerows(entries)
    write("catalog/recipes.csv", stream.getvalue())
    original = sum(e["kind"] == "original" for e in entries)
    index = ["# Image 2.5 提示词总览", "",
             f"{len(entries)} 条完整提示词 · {len(categories)} 个分类 · {original} 个基础案例 + {len(entries)-original} 个任务侧重变体。",
             "", "变体共享基础场景，分别强调边缘、材质、版式、可辨识性或编辑保真；不视为独立出图实测。",
             "全部条目的验证状态目前为 prompt-only。", "",
             "[实图分类](gallery.md) · [仓库首页](https://github.com/Fangx-AI/awesome-image2.5) · [JSON](https://github.com/Fangx-AI/awesome-image2.5/blob/main/catalog/recipes.json) · [CSV](https://github.com/Fangx-AI/awesome-image2.5/blob/main/catalog/recipes.csv)", "",
             "| 分类 | 条目数 | 基础案例 |", "| :--- | ---: | ---: |"]
    for cid, cat in categories.items():
        group = [e for e in entries if e["category"] == cid]
        index.append(f"| [{cat['title']} / {cat['en']}](categories/{cid}.md) | {len(group)} | {sum(e['kind']=='original' for e in group)} |")
        page = [f"# {cat['title']} · {cat['en']}", "", "[返回实验区](../prompt-lab-index.md) · [实图分类](../gallery.md)", "",
                "所有条目均未经过指定模型出图验证。以“变体”标记的条目共享同一基础场景。", ""]
        for e in group:
            label = "基础案例" if e["kind"] == "original" else "任务侧重变体"
            page += [f"## {e['title']}", "",
                     f"ID: `{e['id']}` · {label} · `{e['mode']}` · 建议尺寸 `{e['size']}`",
                     f"参考图：{e['requires']} 张（最低） · 状态：`{e['status']}`", "",
                     "```text", e["prompt"], "```", "",
                     f"[下载文本](../prompts/{e['id']}.txt)", "",
                     "检查：" + "；".join(e["checks"]) + "。", ""]
            write(f"skills/image25/references/prompts/{e['id']}.txt", e["prompt"])
        write(f"skills/image25/references/categories/{cid}.md", "\n".join(page))
    write("skills/image25/references/gallery.md", "\n".join(index))
    template = (ROOT / "scripts/gallery-template.html").read_text(encoding="utf-8")
    safe_data = json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")
    write("docs/prompt-lab.html", template.replace("__CATALOG_JSON__", safe_data).replace("__TOTAL__", str(len(entries))))
    print(f"Built {len(entries)} recipes, {original} original cases, {len(categories)} categories.")


if __name__ == "__main__":
    build()
