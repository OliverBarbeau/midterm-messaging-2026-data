"""Recompute the Midterm Messaging Tracker's labeling accuracy from labels.csv. Standard library only.

    python score.py                          both blind sets, areas as the tracker publishes them
    python score.py --public-health-apart    public health counted apart from health care
    python score.py --without-proposed       leave out test items whose hand label changed on an assistant-proposed fix
    python score.py --set test               the first blind set only
    python score.py --set test2              the second blind set only (X posts and website passages)
    python score.py --set tune               the items the prompt was tuned on (optimistic by construction)

A message counts only if the hand label calls it the campaign's own words or the candidate's answers
(`own`, `prompted`). For each topic: n = messages the hand label tags with it, found = those the labeler
also tagged, false tags = messages the labeler tagged and the hand label did not. An area is tagged when
any of its topics is. With no options, the counts are checked against expected.json, the figures the
tracker's Method tab shows.
"""
import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).parent
APART = {"hc.public_health"}


def prf(tp: int, fp: int, fn: int) -> tuple[float, float, float]:
    p = tp / (tp + fp) if tp + fp else 0.0
    r = tp / (tp + fn) if tp + fn else 0.0
    return p, r, (2 * p * r / (p + r) if p + r else 0.0)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--set", default="published", choices=["published", "test", "test2", "tune"])
    ap.add_argument("--public-health-apart", action="store_true")
    ap.add_argument("--without-proposed", action="store_true")
    args = ap.parse_args()

    area = (lambda t: t if t in APART else t.split(".")[0]) if args.public_health_apart else (lambda t: t.split(".")[0])
    with (HERE / "labels.csv").open(encoding="utf-8", newline="") as f:
        wanted = {"test", "test2"} if args.set == "published" else {args.set}
        rows = [r for r in csv.DictReader(f) if r["set"] in wanted]
    if args.without_proposed:
        rows = [r for r in rows if r["assistant_proposed_fix"] != "1"]
    for r in rows:
        r["hand"] = set(filter(None, r["hand_topics"].split(";")))
        r["labeler"] = set(filter(None, r["labeler_topics"].split(";")))
    content = [r for r in rows if r["hand_usable"] in ("own", "prompted")]
    if not content:
        raise SystemExit(f"no '{args.set}' items in labels.csv yet")

    def tags(topics: set[str]) -> set[str]:  # topics and the areas they count toward
        return topics | {area(t) for t in topics}

    def counts(items) -> dict[str, Counter]:
        out = defaultdict(Counter)
        for r in items:
            h, m = tags(r["hand"]), tags(r["labeler"])
            for k in h | m:
                out[k]["tp"] += k in h and k in m
                out[k]["fp"] += k in m and k not in h
                out[k]["fn"] += k in h and k not in m
        return out

    def micro(items) -> float:  # over topics, not areas
        tp = sum(len(r["hand"] & r["labeler"]) for r in items)
        fp = sum(len(r["labeler"] - r["hand"]) for r in items)
        fn = sum(len(r["hand"] - r["labeler"]) for r in items)
        return round(prf(tp, fp, fn)[2], 3)

    def cell(c: Counter) -> str:
        return f"{c['tp']}/{c['tp'] + c['fn']}"

    party = {p: [r for r in content if r["party"] == p] for p in ("D", "R")}
    web = {p: [r for r in party[p] if r["channel"] == "website"] for p in ("D", "R")}
    # Round 2 drew only messages the labeler called the campaign's own words, so it can't score that call.
    scored = [r for r in rows if r["set"] != "test2"]
    agree = sum(r["hand_usable"] == r["labeler_usable"] for r in scored)
    print(f"set '{args.set}': {len(rows)} items, {len(content)} with campaign content; whose-words agreement "
          + (f"{agree}/{len(scored)}" if scored else "not scored (round 2 only)"))
    print(f"topic micro-F1: {micro(content)} overall, {micro(party['D'])} Democrats ({len(party['D'])} items), "
          f"{micro(party['R'])} Republicans ({len(party['R'])})")
    for ch in sorted({r["channel"] for r in content}):
        parts = [f"{p} {micro(items)} ({len(items)})" for p in ("D", "R") for items in [[r for r in party[p] if r["channel"] == ch]] if items]
        print(f"  within {ch}: " + ", ".join(parts))

    total, by_p, by_w = counts(content), {p: counts(v) for p, v in party.items()}, {p: counts(v) for p, v in web.items()}
    areas = sorted(k for k in total if area(k) == k)
    print(f"\n{'area / topic':22s} {'n':>3s} {'found':>5s} {'false':>5s} {'prec':>5s} {'rec':>5s} {'F1':>5s}   {'D found/of':>10s} {'R found/of':>10s}   websites: {'D':>5s} {'R':>6s}")
    for a in areas:
        for k in [a] + sorted(k for k in total if k != a and area(k) == a):
            c = total[k]
            p, r, f = prf(c["tp"], c["fp"], c["fn"])
            print(f"{('  ' if k != a else '') + k:22s} {c['tp'] + c['fn']:3d} {c['tp']:5d} {c['fp']:5d} {p:5.2f} {r:5.2f} {f:5.2f}   "
                  f"{cell(by_p['D'][k]):>10s} {cell(by_p['R'][k]):>10s}   {'':9s} {cell(by_w['D'][k]):>6s} {cell(by_w['R'][k]):>6s}")

    if args.set != "published" or args.without_proposed:
        print("\nnot compared with expected.json (it holds both blind sets, as the tracker publishes them)")
        return
    exp = json.loads((HERE / "expected.json").read_text(encoding="utf-8"))["public_health_apart" if args.public_health_apart else "as_published"]
    wrong = [k for k, v in exp["topics"].items()
             if (v["n"], v["tp"], v["fp"]) != (total[k]["tp"] + total[k]["fn"], total[k]["tp"], total[k]["fp"])]
    wrong += [k for k in ("content_items",) if exp[k] != len(content)] + (["topic_micro_f1"] if exp["topic_micro_f1"] != micro(content) else [])
    print(f"\nmatches the published figures: {'yes' if not wrong else 'NO: ' + ', '.join(wrong)} "
          f"({len(exp['topics'])} topics and areas, micro-F1 {exp['topic_micro_f1']})")


if __name__ == "__main__":
    main()
