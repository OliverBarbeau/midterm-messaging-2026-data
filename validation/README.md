# Midterm Messaging Tracker: checking the labels

> **In the corpus release:** this folder was first published on its own, so its "What is not here" section below describes that packet. The release adds `hand_labels_all_fields.csv` (every field the person judged, tone, targets, blame, frames and flags included, beside the labeler's label on the same text; `fields_judged` lists which fields each row's person labeled), the accuracy reports `accuracy_first_sample.md` and `accuracy_second_sample.txt`, and, one level up, the whole corpus with its labels and, for Bluesky, YouTube and websites, its text.

The [Midterm Messaging Tracker](https://barbeau.dev/midterms-2026) reports what 2026 House, Senate and governor candidates talk about. An AI model assigns each message its topics. This folder lets you check how well it does that, using the same messages a person labeled by hand.

It answers one question: **can you reproduce the accuracy figures on the tracker's Method tab?** Yes:

```
python score.py
```

The script needs only Python 3.9 or later. It recomputes every accuracy figure from `labels.csv` and ends by comparing them with `expected.json`, the figures the page shows.

## What is here

| File | What it is |
|---|---|
| `labels.csv` | One row per hand-labeled message: a link to it, the hand label and the labeler's label |
| `score.py` | Recomputes accuracy by topic and area, by party, and by party within a channel |
| `expected.json` | The figures the tracker publishes, for the comparison |
| `codebook_v1.4_rules.md` | The written rules both the person and the model followed, as they stood on 2026-09-29 when this labeler was chosen. Its change history and working appendices are not included |
| `system_prompt.txt` | The exact instructions the model received (generated from the codebook) |
| `output_schema.json` | The structure the model had to answer in |

## How the labels were made

- **The sample.** 150 messages were drawn on 2026-09-26 from campaign websites, YouTube captions and Bluesky posts: 110 at random (one per candidate within each channel and party) and 40 picked by keyword so that rarer topics would have examples. The `stratum` column says which. A third went to a tuning set and the rest to a test set. One message could not be judged and was set aside, which leaves 149 rows.
- **The hand labels.** One person, the tracker's author, labeled every message from its text, on a page that showed no model output. One person means one reading: there is no second labeler to measure agreement against.
- **The labeler.** `claude-sonnet-5`, ten messages per request, answering in a fixed structure. Several model setups and a keyword baseline were compared on the tuning set. The two finalists and the baseline were then each scored once on the test set, and the more accurate one was kept.
- **A second blind set** was drawn on 2026-10-13 for the two channels that carry party comparisons, X posts and website passages, because the first sample had no X posts. Candidates were drawn with equal probability within channel and party, then one of each candidate's messages, from the messages the labeler had called the campaign's own words. It was labeled for whose words and topics only, 114 of the 150 drawn (19 whole blocks of six, so balanced by party and channel). Its rows have `set` = `test2`. Because it was drawn only from messages the labeler called the campaign's own, it doesn't count toward whose-words agreement.
- **The codebook changed twice before it was frozen**, and hand labels were carried over by fixed mappings of old topics to new ones. On 19 test items the hand label also changed after the author reviewed a fix an AI assistant proposed. Those rows are marked `assistant_proposed_fix`, and `python score.py --without-proposed` scores the test set without them.

## Reading labels.csv

- `set`: `tune` (used to adjust the prompt, so accuracy on it flatters the model), `test` (the first blind set, scored once) and `test2` (the second blind set). The tracker's accuracy figures rest on `test` and `test2` together.
- `hand_usable`, `labeler_usable`: whose words the message is. `own` is the campaign speaking on a subject it chose; `prompted` is the candidate answering someone's question; `third_party` and `no_content` are not campaign messaging. Accuracy is computed on messages the hand label calls `own` or `prompted`.
- `hand_topics`, `labeler_topics`: topic ids from the codebook, separated by semicolons. A message can have several, or none.
- `text_sha`: the first 16 hex digits of the SHA-256 of the text that was labeled.
- `source_later_excluded`: 1 for the two messages drawn from a senator's official office accounts (a page of the office's website and a video from its YouTube channel), which the candidate list carried by mistake when the sample was drawn and which were removed from the tracker's data afterwards. They stay here because the published figures were computed on every sampled message; one is in the test set.

## What is not here, and why

- **The messages' text.** The words belong to the campaigns. Each row links to its source, and the tracker itself shows only short excerpts with links. For a website or a video, the link leads to the whole page or video; the labeled passage is one part of it, which `text_sha` identifies but does not let you rebuild.
- **Other label fields.** The codebook also defines tone, targets and a few flags. The tracker's published figures use whose-words and topics only, so those are the labels in this folder.
- **The rest of the corpus.** About 27,000 messages are labeled by the model alone. This folder covers the ones with a hand label to compare against.

## Limits worth knowing

- **Small counts.** Many topics have fewer than ten hand-labeled examples, so their accuracy is a rough guide. The tracker marks each topic by how well it was checked.
- **The model misses more than it invents.** Its tags are usually right (high precision) and it leaves out some a person would add (lower recall), mostly on long passages that touch many subjects. Shares on the tracker are best read as comparisons between groups, not as exact levels.
- **Party comparisons of accuracy need a common channel.** The Democratic test items include Bluesky posts and the Republican ones lean toward websites, so pooled figures by party mix two things. `score.py` prints each party's counts within websites for that reason.
- **Rerunning the model will not give identical labels.** This model accepts no temperature setting; on a repeat run about 17% of its topic tags changed while overall accuracy stayed the same. The labels here are the stored ones the tracker uses.

## Contact

Oliver Barbeau built the tracker. The page's footer has an address for corrections.
