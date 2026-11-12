"""Fetch the text of the release's X posts with your own X API access. X's Developer Policy lets this release
share post ids but not post text, so each user fetches the text under their own agreement with X.

    set X_BEARER_TOKEN=...                        # your app's bearer token (Windows; `export` elsewhere)
    python hydrate_x.py --party D                 # prints the number of posts and stops
    python hydrate_x.py --party D --yes           # fetches them

X bills reads per post under its pay-per-use plan, so check your plan's price before running: the first run
without --yes prints how many posts would be read. Reads ../items.csv.gz; writes item_id, text, created_at and
text_matches (1 when the text is exactly the text that was labeled). A post deleted or made private since
collection is listed with an empty text; X's policy asks you to delete stored posts that are deleted on X.
Long posts take their full text (`note_tweet`), as the corpus did. Standard library only.
"""
import argparse
import csv
import gzip
import hashlib
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.x.com/2/tweets"
BATCH = 100  # the lookup endpoint takes at most 100 ids
UA = "midterm-messaging-corpus-hydrate/1.0"


def text_sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def get(ids: list[str], token: str) -> list[dict]:
    q = urllib.parse.urlencode({"ids": ",".join(ids), "tweet.fields": "created_at,author_id,note_tweet"})
    req = urllib.request.Request(f"{API}?{q}", headers={"Authorization": f"Bearer {token}", "User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r).get("data") or []
        except urllib.error.HTTPError as e:
            if e.code == 429:  # wait for the window X names, then retry
                reset = int(e.headers.get("x-rate-limit-reset") or time.time() + 60)
                time.sleep(max(5, reset - time.time() + 1))
                continue
            if e.code >= 500:
                time.sleep(10 * (attempt + 1))
                continue
            raise SystemExit(f"X answered {e.code}: {e.read()[:300]!r}")
    raise SystemExit("X kept refusing; try again later")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--items", default=str(Path(__file__).resolve().parents[1] / "items.csv.gz"))
    ap.add_argument("--party", choices=["D", "R", "I"], help="only this party's candidates")
    ap.add_argument("--since", help="only posts on or after this date (YYYY-MM-DD)")
    ap.add_argument("--out", default="x_text.csv.gz")
    ap.add_argument("--yes", action="store_true", help="fetch (without it, only count)")
    args = ap.parse_args()

    with gzip.open(args.items, "rt", encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["channel"] == "x" and (not args.party or r["party"] == args.party)
                and (not args.since or r["published_at"] >= args.since)]
    by_id = {r["native_id"]: r for r in rows}
    ids = list(by_id)
    print(f"{len(ids):,} posts in {-(-len(ids) // BATCH):,} requests")
    if not args.yes:
        print("dry run: add --yes to fetch (X bills each post read)")
        return
    token = os.environ.get("X_BEARER_TOKEN")
    if not token:
        raise SystemExit("set X_BEARER_TOKEN first")
    found = {}
    for i in range(0, len(ids), BATCH):
        for post in get(ids[i:i + BATCH], token):
            text = (post.get("note_tweet") or {}).get("text") or post.get("text", "")
            found[post["id"]] = (text, post.get("created_at", ""))
        if (i // BATCH) % 20 == 0:
            print(f"  {min(i + BATCH, len(ids)):,} / {len(ids):,}")
    with gzip.open(args.out, "wt", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_id", "text", "created_at", "text_matches"])
        for pid, r in by_id.items():
            text, created = found.get(pid, ("", ""))
            w.writerow([r["item_id"], text, created, int(bool(text) and text_sha(text) == r["text_sha"])])
    print(f"wrote {args.out}: {len(found):,} of {len(ids):,} posts still available")


if __name__ == "__main__":
    main()
