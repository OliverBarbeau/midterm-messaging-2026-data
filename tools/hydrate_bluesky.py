"""Fetch the text of the release's Bluesky posts from Bluesky's public API. No account or key is needed.

    python hydrate_bluesky.py                     # writes bluesky_text.csv.gz in the current folder
    python hydrate_bluesky.py --party D --out d.csv.gz

Reads ../items.csv.gz (the release's item table). Writes item_id, text, created_at and text_matches, which is 1
when the fetched text is exactly the text that was labeled (it hashes to the release's text_sha). A post deleted
since collection is listed with an empty text. Text is rebuilt the way the corpus built it: the post's text, then
"[link: <title>]" on a new line when the post embeds a link card. Standard library only.
"""
import argparse
import csv
import gzip
import hashlib
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://public.api.bsky.app/xrpc/app.bsky.feed.getPosts"
BATCH = 25  # getPosts takes at most 25 URIs
UA = "midterm-messaging-corpus-hydrate/1.0"


def text_sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def get(uris: list[str]) -> list[dict]:
    q = urllib.parse.urlencode([("uris", u) for u in uris])
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": UA})
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.load(r)["posts"]
        except urllib.error.HTTPError as e:
            if e.code != 429 and e.code < 500:
                raise
            time.sleep(10 * (attempt + 1))
    raise SystemExit("Bluesky's API kept refusing; try again later")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--items", default=str(Path(__file__).resolve().parents[1] / "items.csv.gz"))
    ap.add_argument("--party", choices=["D", "R", "I"], help="only this party's candidates")
    ap.add_argument("--out", default="bluesky_text.csv.gz")
    args = ap.parse_args()

    with gzip.open(args.items, "rt", encoding="utf-8", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r["channel"] == "bluesky" and (not args.party or r["party"] == args.party)]
    by_uri = {r["native_id"]: r for r in rows if r["native_id"]}
    uris = list(by_uri)
    print(f"{len(uris):,} posts to fetch, {BATCH} per request")
    found = {}
    for i in range(0, len(uris), BATCH):
        for post in get(uris[i:i + BATCH]):
            ext = (post.get("embed") or {}).get("external") or {}
            text = post["record"].get("text", "") + (f"\n[link: {ext['title']}]" if ext.get("title") else "")
            found[post["uri"]] = (text, post["record"].get("createdAt", ""))
        time.sleep(0.3)  # be polite: about three requests a second
        if (i // BATCH) % 40 == 0:
            print(f"  {min(i + BATCH, len(uris)):,} / {len(uris):,}")
    with gzip.open(args.out, "wt", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item_id", "text", "created_at", "text_matches"])
        for uri, r in by_uri.items():
            text, created = found.get(uri, ("", ""))
            w.writerow([r["item_id"], text, created, int(bool(text) and text_sha(text) == r["text_sha"])])
    print(f"wrote {args.out}: {len(found):,} of {len(uris):,} posts still online")


if __name__ == "__main__":
    main()
