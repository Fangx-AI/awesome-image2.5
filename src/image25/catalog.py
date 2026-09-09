"""Offline catalog search and recipe retrieval."""
import argparse
import json
from pathlib import Path

CATALOG = Path(__file__).parent / "data" / "recipes.json"


def load_catalog():
    return json.loads(CATALOG.read_text(encoding="utf-8"))


def find_recipe(recipe_id):
    for entry in load_catalog()["entries"]:
        if entry["id"] == recipe_id:
            return entry
    raise ValueError("Unknown recipe ID: " + recipe_id)


def search(query="", category=None, mode=None, kind=None):
    words = query.lower().split()
    return [e for e in load_catalog()["entries"]
            if (not category or e["category"] == category)
            and (not mode or e["mode"] == mode)
            and (not kind or e["kind"] == kind)
            and all(w in (e["id"] + " " + e["title"] + " " + e["prompt"] + " "
                          + e["category_title"] + " " + e["category_en"]).lower() for w in words)]


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("query", nargs="?", default="")
    p.add_argument("--category")
    p.add_argument("--mode", choices=("generate", "edit"))
    p.add_argument("--kind", choices=("original", "variation"))
    p.add_argument("--show", metavar="ID")
    p.add_argument("--json", action="store_true")
    p.add_argument("--limit", type=int, default=20)
    args = p.parse_args(argv)
    if args.limit < 1:
        p.error("--limit must be positive")
    try:
        if args.show:
            entry = find_recipe(args.show)
            print(json.dumps(entry, ensure_ascii=False, indent=2) if args.json else entry["prompt"])
            return 0
        matches = search(args.query, args.category, args.mode, args.kind)
        if args.json:
            print(json.dumps(matches, ensure_ascii=False, indent=2))
        else:
            for entry in matches[:args.limit]:
                print(entry["id"] + " | " + entry["title"] + " | " + entry["kind"])
            print(f"{len(matches)} results; showing up to {args.limit}. Use --json for all.")
        return 0
    except ValueError as exc:
        p.error(str(exc))
