# Midterm Messaging 2026: corpus and labels (midterm-messaging-2026-corpus-v1)

What about 300 candidates for the U.S. House, Senate and governor said on their own campaign channels in the 2026 midterms, August 1 to Election Day (November 3, 2026), with a topic, tone and target label on every message. This is the data behind the live tracker at https://barbeau.dev/midterms-2026, built by Oliver Barbeau.

DOI: [10.5281/zenodo.24150903](https://doi.org/10.5281/zenodo.24150903) (all versions). Built 2026-11-11: 48,805 messages from 298 candidates in 147 races; 48,805 of them labeled.

## Contents

| File | One row per | What it holds |
|---|---|---|
| `items.csv.gz` | message | IDs, links, dates and the candidate. No text (see "Getting the text") |
| `labels.csv.gz` | message | The labeler's topics, tone, targets and stance, blame, frames and flags |
| `candidates.csv` | candidate | Party, race, incumbency, campaign accounts, Kalshi market and its price on Election Day morning |
| `races.csv` | race | Office, state, district, Sabato's Crystal Ball rating on Election Day, 2024 presidential margin |
| `topics.csv` | topic | The 45 topic IDs, their names, the area each counts toward, what each includes and its frames |
| `codebook/` | | The frozen codebook (v1.4), the labeler's system prompt and its output schema |
| `validation/` | hand-labeled message | 263 hand labels beside the labeler's, a script that recomputes the published accuracy figures, and the accuracy reports |
| `text/` | message | Campaign text for Bluesky, YouTube and websites (one file per channel; join on `item_id`) |
| `tools/` | | Scripts that fetch X and Bluesky text from the IDs |

Join everything on `item_id` and `candidate_id`. Files are UTF-8 CSV; lists inside a cell are joined with `;`.

## Channels

| Channel | Messages | Candidates | D / R / I messages | Dates |
|---|---|---|---|---|
| x | 26,243 | 222 | 12,398 / 13,461 / 384 | 2026-08-01 to 2026-11-03 |
| bluesky | 12,766 | 77 | 12,342 / 0 / 424 | 2026-08-01 to 2026-11-03 |
| youtube | 6,313 | 96 | 3,813 / 2,240 / 260 | 2026-08-01 to 2026-11-03 |
| website | 3,483 | 279 | 2,085 / 1,333 / 65 | 2026-09-25 to 2026-10-30 |

- **X:** posts from campaign accounts through X's official API, without reposts or replies to other accounts (thread continuations are kept). **Coverage is uneven before September 29:** 38 accounts in competitive races were collected back to August 1; every other account has its 10 most recent posts as of September 29, then every post from that day on. Compare candidates over August–September only within the competitive set. Fifteen accounts that X marks as government accounts, or whose bio calls them official, were reviewed by hand and kept because they post campaign material (`x_official_flag_reviewed` = 1).
- **Bluesky:** posts from campaign accounts through Bluesky's public API, without reposts. Replies that continue a candidate's own thread are not included (about 15% of their posts). **Bluesky has no Republican posts in this window** (one Republican candidate has an account), so it can't carry party comparisons; use it for Democrats and independents.
- **YouTube:** videos uploaded to campaign channels, transcribed from their English captions and cut into passages of up to about 2,000 characters, each starting with the video's title. A video without captions contributes its title and description (`youtube_has_captions` = 0). `youtube_likely_ad` marks videos of 15, 30 or 60 seconds, or up to 65 seconds with a "paid for by" or "approve this message" line: a heuristic, not a record of airing.
- **Websites:** campaign homepages and up to eight linked pages, crawled weekly from September 25, respecting robots.txt. Each row is a passage of up to about 2,000 characters from **the version of the page held on Election Day** (in practice the October 30 crawl), with sign-up, donation and "paid for by" boilerplate removed and paragraphs a candidate repeats across pages kept once. `published_at` is the day that version of the page was first seen. A few sites behind bot walls, or whose robots.txt disallows crawlers, were not read.
- **Not included:** Facebook and Instagram ads (no access to Meta's Ad Library API), campaign emails, debates, X engagement counts, earlier versions of website pages, and messages after November 3 (collection continued; a later version may add them).

Who is in it: all 35 Senate races (including the Ohio and Florida specials), all 36 governor races, and the 76 House districts Kalshi listed individual markets for on September 25 (in effect, the competitive ones), with the Democratic and Republican nominees and independents whose Kalshi price reached 5%. `track` = yes for the 298 candidates the tracker follows. Accounts belong to campaigns; official office accounts and `.gov` sites are excluded. Dates are UTC days.

## Labels

Every message was labeled once by Claude Sonnet 5 (`claude-sonnet-5`, Anthropic) through the Message Batches API, 10 messages per request, under codebook v1.4 (frozen September 29, 2026; prompt version `p1-b617b8fe`). Each request gave the model the candidate's name, party, office and race. The model takes no temperature setting, so a repeat run would differ: about 17% of topic labels changed between two identical runs on the tuning set, with the same accuracy. Each stored label is final.

| Column | Values |
|---|---|
| `usable` | Whose words: `own` (the campaign's), `prompted` (the candidate answering someone else, e.g. an interview), `third_party` (someone else's words, such as reprinted news), `no_content`. **Most analyses should keep `own` only**, as the tracker does |
| `topics`, `primary_topic` | Topic IDs from `topics.csv` (a message can have several) |
| `areas` | The areas those topics count toward on the tracker (the topic's parent; public health is its own area) |
| `tone` | `promote`, `contrast`, `attack`, `none` |
| `targets` | `target:stance` pairs, stance `pos`, `neg` or `neutral`; targets are `trump`, `trump_admin`, `biden_harris`, `opponent`, `dem_party`, `gop_party`, `dem_leaders`, `gop_leaders`, `musk_doge`, `corporations`, `washington_elites`, `state_gov`, `other`. `trump_stance` and `opponent_stance` repeat the two most used |
| `blame` | `topic:blamed` pairs: who the message blames for a problem in that topic |
| `frames` | `topic:frame` pairs for the topics that have frames (education, AI, data centers) |
| `local_reference`, `credit_claim`, `is_fundraising_ask` | 0/1 flags |
| `other_note` | The model's few words on a message whose only topic is `other` |

`labeled` = 0 marks the few messages without a label (the model mis-copied their IDs).

### How accurate the labels are

Two blind samples were labeled by hand without seeing the model's labels. The first (96 messages from websites, YouTube and Bluesky, drawn in late September) was scored on every field; the second (114 messages, 76 from X and 38 from websites, drawn October 13) on whose words and topics only. `validation/` has every hand label, the labeler's label on the same text, and the full reports.

| Field | Accuracy |
|---|---|
| Topics, first sample | micro-F1 0.66 (Democrats 0.66, Republicans 0.66) |
| Topics, X (second sample) | micro-F1 0.66 (precision 0.76, recall 0.57; Democrats 0.66, Republicans 0.65) |
| Topics, websites (second sample) | micro-F1 0.52 (lower mostly because the model called 11 of 38 passages the campaign's own words that were reprinted news) |
| Whose words | 94% agreement |
| Tone | 65% agreement |
| Targets | opponent F1 0.93, `washington_elites` 0.90, `biden_harris` 0.92, Trump 0.72 (precision 0.60); stance agrees 97% where both saw the target |
| Blame, frames | **Not validated**: too few hand-labeled examples. Use with care |

The model **under-labels** more than it mislabels: precision is high and recall lower, especially on long messages that touch many topics. Accuracy varies a lot by topic: public health (vaccines, pandemic response) was found in 1 of 18 hand-labeled examples, and "Workers / unions" (`econ.labor`) in none of 18, so areas are more reliable than single topics. The reports in `validation/` give precision and recall by topic and by party within each channel.

An independent check on the main party differences: for every headline area on the tracker, the gap between parties has the same sign counted by plain keywords as by the labeler's tags (on websites and on X).

### How the model was chosen

Before the corpus was labeled, seven labelers were compared on a tuning set of 53 hand-labeled messages, each given the same codebook and output format: Claude Haiku 4.5, Sonnet 5 and Opus 5; Gemini 3.1 and 3.5 Flash-Lite; Jev, a classifier that answers one typed question per codebook decision; and a keyword baseline. On topics, Sonnet 5, Opus 5 and Gemini 3.1 Flash-Lite reached about 0.65–0.67, Haiku 4.5 about 0.60–0.62, Jev 0.52 and the keywords 0.38 (on 51 messages, gaps under about 0.03 are noise). That the largest model, Opus 5, did no better suggests the hand labels themselves cap agreement near that level. Packing ten messages into one request made Haiku label each one more thinly (0.53, against 0.60 at one per request), while Sonnet 5 held its level at ten, which brought its cost down to about Haiku's at one. No model repeated itself exactly: between identical runs, 6–10% of topic labels changed for Haiku, about 17% for Sonnet 5 and 19% for Gemini, with steady accuracy, so each message was labeled once and that label is final. The two finalists, Sonnet 5 at ten messages per request and Haiku 4.5 at one, were then scored once on the blind test set. Sonnet 5 led on topics (0.66 against 0.61), whose words (94% against 86%), tone (65% against 57%) and the opponent target (0.93 against 0.81), and was chosen on accuracy alone. Labeling the corpus cost about $0.001 per message.

## Getting the text

| Channel | How |
|---|---|
| Bluesky | `text/bluesky.csv.gz`, or fetch it fresh with `tools/hydrate_bluesky.py` (Bluesky's public API, no key, a few minutes) |
| YouTube | `text/youtube.csv.gz` |
| Websites | `text/website.csv.gz` (these pages have changed since; this is the only copy of many of them) |
| X | **IDs only.** X's Developer Policy lets this release share post and user IDs but not post text. `tools/hydrate_x.py` fetches the text with your own X API access (X bills per post read; run it once without `--yes` to see the count). Researchers with access under Article 40 of the EU Digital Services Act can request X data through that route |

Both tools write `text_matches` = 1 when the fetched text is exactly what was labeled (it hashes to `text_sha`, the first 16 hex digits of the SHA-256 of the UTF-8 text). Posts deleted since collection come back empty.

## Other columns

- `candidates.csv`: `kalshi_prob_election_day` is the last daily snapshot of the candidate's Kalshi market on November 3 (UTC), as a probability (bid/ask midpoint when the spread was tight, else the last trade). `incumbent` is from Wikipedia.
- `races.csv`: `sabato_rating` and `sabato_score_d` (positive favors the Democrat) as published in Wikipedia's tables of race ratings on Election Day, with `sabato_as_of`; `pres_2024_margin_d` is Harris's margin over Trump in points, by district on the 2026 lines (from The Downballot) or by state.

## Terms

- Labels, the codebook, the candidate and race tables and this documentation: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Please cite as below.
- `tools/` and `validation/score.py`: MIT license.
- **Campaign text belongs to the campaigns.** It is shared for research and reporting; it is not licensed by this project. X content is subject to X's Developer Agreement and Policy when you fetch it.
- Race ratings: Sabato's Crystal Ball, through Wikipedia (CC BY-SA 4.0). 2024 presidential results by district: The Downballot. Market prices: Kalshi.

## Citation

> Barbeau, Oliver. 2026. *Midterm Messaging 2026: corpus and labels*, version 1.0.1. Zenodo. https://doi.org/10.5281/zenodo.24150903

That DOI always resolves to the latest version; Zenodo lists each version's own DOI. The files are also at https://github.com/OliverBarbeau/midterm-messaging-2026-data.

The tracker built on this data is at https://barbeau.dev/midterms-2026. Corrections and questions: the email address in its footer, or an issue on this repository.

## Changes

- **v1.0.1 (2026-11-11):** documentation only: how the labeling model was chosen, and metadata for a Zenodo DOI. The data files are unchanged.
- **v1 (2026-11-11):** first release. Messages August 1 – November 3, 2026.
