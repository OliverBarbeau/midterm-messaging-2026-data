# sonnet vs. hand labels (test set)

Items: 96 of 96 hand-labeled; prompt versions: {'p1-b617b8fe': 96}

## Whose words (`usable`)

Accuracy 94% (n=96).

| human \ model | own | prompted | third_party | no_content |
|---|---|---|---|---|
| own | 82 | 3 | 1 | 0 |
| prompted | 0 | 6 | 0 | 0 |
| third_party | 1 | 0 | 1 | 0 |
| no_content | 0 | 1 | 0 | 1 |

Content items: 92. Topic micro-F1: 0.66

- D: 47 items, topic micro-F1 0.66
- R: 45 items, topic micro-F1 0.66

## Parent topics

| label | human positives | false positives | precision | recall | F1 | 95% CI |
|---|---|---|---|---|---|---|
| econ | 49 | 1 | 0.97 | 0.61 | 0.75 | 0.63–0.85 |
| col | 40 | 4 | 0.89 | 0.78 | 0.83 | 0.73–0.91 |
| hc | 31 | 1 | 0.95 | 0.58 | 0.72 | 0.56–0.84 |
| dem | 30 | 7 | 0.74 | 0.67 | 0.70 | 0.57–0.83 |
| edu | 25 | 4 | 0.71 | 0.40 | 0.51 | 0.30–0.69 |
| culture | 21 | 1 | 0.92 | 0.57 | 0.71 | 0.50–0.86 |
| foreign | 21 | 1 | 0.92 | 0.52 | 0.67 | 0.44–0.83 |
| imm | 20 | 1 | 0.94 | 0.75 | 0.83 | 0.69–0.95 |
| env | 19 | 0 | 1.00 | 0.74 | 0.85 | 0.70–0.97 |
| safety | 13 | 2 | 0.80 | 0.62 | 0.70 | 0.40–0.89 |
| infrastructure | 12 | 0 | 1.00 | 0.58 | 0.74 | 0.44–0.93 |
| tech | 12 | 1 | 0.91 | 0.83 | 0.87 | 0.70–1.00 |
| agri_rural | 11 | 1 | 0.86 | 0.55 | 0.67 | 0.33–0.88 |
| veterans | 10 | 1 | 0.88 | 0.70 | 0.78 | 0.50–0.95 |
| abortion | 6 | 1 | 0.83 | 0.83 | 0.83 | 0.44–1.00 |
| disasters | 6 | 0 | 1.00 | 0.50 | 0.67 | 0.00–1.00 |
| guns | 4 | 1 | 0.80 | 1.00 | 0.89 | 0.40–1.00 |
| tribal | 3 | 0 | 1.00 | 0.67 | 0.80 | 0.00–1.00 |
| other | 1 | 0 | 0.00 | 0.00 | 0.00 |  |
| safety_net | 1 | 2 | 0.33 | 1.00 | 0.50 |  |

## Leaf topics

| label | human positives | false positives | precision | recall | F1 | 95% CI |
|---|---|---|---|---|---|---|
| col.inflation | 32 | 3 | 0.87 | 0.62 | 0.73 | 0.58–0.85 |
| edu | 25 | 4 | 0.71 | 0.40 | 0.51 | 0.30–0.69 |
| econ.jobs | 20 | 3 | 0.62 | 0.25 | 0.36 | 0.11–0.58 |
| econ.taxes | 20 | 2 | 0.89 | 0.80 | 0.84 | 0.70–0.95 |
| hc.care | 20 | 1 | 0.93 | 0.70 | 0.80 | 0.64–0.93 |
| econ.labor | 18 | 1 | 0.00 | 0.00 | 0.00 | 0.00–0.00 |
| dem.corruption | 18 | 4 | 0.69 | 0.50 | 0.58 | 0.36–0.77 |
| dem.governance | 17 | 3 | 0.62 | 0.29 | 0.40 | 0.12–0.62 |
| econ.spending | 16 | 3 | 0.67 | 0.38 | 0.48 | 0.21–0.70 |
| foreign.other | 16 | 2 | 0.80 | 0.50 | 0.62 | 0.34–0.80 |
| imm.enforcement | 15 | 1 | 0.92 | 0.80 | 0.86 | 0.70–0.97 |
| culture.other | 14 | 0 | 1.00 | 0.36 | 0.53 | 0.18–0.76 |
| econ.corporate | 13 | 0 | 1.00 | 0.31 | 0.47 | 0.12–0.75 |
| col.housing | 12 | 1 | 0.90 | 0.75 | 0.82 | 0.57–0.96 |
| col.childcare | 12 | 0 | 1.00 | 0.25 | 0.40 | 0.00–0.71 |
| safety.crime | 12 | 2 | 0.80 | 0.67 | 0.73 | 0.44–0.92 |
| infrastructure | 12 | 0 | 1.00 | 0.58 | 0.74 | 0.44–0.93 |
| imm.border | 11 | 0 | 1.00 | 0.73 | 0.84 | 0.60–1.00 |
| agri_rural | 11 | 1 | 0.86 | 0.55 | 0.67 | 0.33–0.88 |
| hc.public_health | 10 | 0 | 0.00 | 0.00 | 0.00 | 0.00–0.00 |
| env.energy | 10 | 0 | 1.00 | 0.70 | 0.82 | 0.57–1.00 |
| veterans | 10 | 1 | 0.88 | 0.70 | 0.78 | 0.50–0.95 |
| col.utilities | 9 | 1 | 0.86 | 0.67 | 0.75 | 0.44–0.95 |
| hc.medicare_ss | 9 | 0 | 1.00 | 0.89 | 0.94 | 0.77–1.00 |
| imm.reform | 9 | 0 | 1.00 | 0.22 | 0.36 | 0.00–0.67 |
| dem.elections | 8 | 1 | 0.89 | 1.00 | 0.94 | 0.75–1.00 |
| culture.gender | 8 | 2 | 0.78 | 0.88 | 0.82 | 0.57–1.00 |
| env.water | 7 | 0 | 1.00 | 0.43 | 0.60 | 0.00–0.91 |
| foreign.iran | 7 | 0 | 1.00 | 0.29 | 0.44 | 0.00–0.80 |
| abortion | 6 | 1 | 0.83 | 0.83 | 0.83 | 0.44–1.00 |
| env.environment | 6 | 0 | 1.00 | 0.67 | 0.80 | 0.00–1.00 |
| tech.data_centers | 6 | 0 | 1.00 | 1.00 | 1.00 | 1.00–1.00 |
| disasters | 6 | 0 | 1.00 | 0.50 | 0.67 | 0.00–1.00 |
| col.gas | 5 | 0 | 1.00 | 1.00 | 1.00 | 1.00–1.00 |
| hc.medicaid | 4 | 0 | 1.00 | 1.00 | 1.00 | 1.00–1.00 |
| tech.ai | 4 | 0 | 1.00 | 0.75 | 0.86 | 0.00–1.00 |
| foreign.israel_gaza | 4 | 0 | 1.00 | 0.25 | 0.40 | 0.00–1.00 |
| guns | 4 | 1 | 0.80 | 1.00 | 0.89 | 0.40–1.00 |
| tech.online | 3 | 1 | 0.50 | 0.33 | 0.40 | 0.00–1.00 |
| tribal | 3 | 0 | 1.00 | 0.67 | 0.80 | 0.00–1.00 |
| col.tariffs | 2 | 1 | 0.67 | 1.00 | 0.80 |  |
| safety_net | 1 | 2 | 0.33 | 1.00 | 0.50 |  |
| safety.guard | 1 | 0 | 0.00 | 0.00 | 0.00 |  |
| dem.epstein | 1 | 0 | 0.00 | 0.00 | 0.00 |  |
| other | 1 | 0 | 0.00 | 0.00 | 0.00 |  |

## Tone

- Tone agreement: 65% (n=92)

## Targets (mentioned at all)

| label | human positives | false positives | precision | recall | F1 | 95% CI |
|---|---|---|---|---|---|---|
| opponent | 20 | 2 | 0.90 | 0.95 | 0.93 | 0.83–1.00 |
| trump | 10 | 6 | 0.60 | 0.90 | 0.72 | 0.48–0.90 |
| washington_elites | 10 | 1 | 0.90 | 0.90 | 0.90 | 0.71–1.00 |
| state_gov | 7 | 1 | 0.67 | 0.29 | 0.40 | 0.00–0.75 |
| biden_harris | 6 | 1 | 0.86 | 1.00 | 0.92 | 0.67–1.00 |
| dem_party | 5 | 8 | 0.33 | 0.80 | 0.47 | 0.15–0.74 |
| corporations | 5 | 5 | 0.38 | 0.60 | 0.46 | 0.00–0.77 |
| trump_admin | 4 | 3 | 0.40 | 0.50 | 0.44 | 0.00–0.80 |
| gop_party | 3 | 0 | 1.00 | 0.67 | 0.80 | 0.00–1.00 |
| gop_leaders | 2 | 0 | 1.00 | 1.00 | 1.00 |  |
| other | 1 | 1 | 0.00 | 0.00 | 0.00 |  |
| musk_doge | 0 | 1 | 0.00 | 0.00 | 0.00 |  |

Stance agreement where both saw the target: 97% (n=58)

## Blame (who is blamed, any topic)

| label | human positives | false positives | precision | recall | F1 | 95% CI |
|---|---|---|---|---|---|---|
| corporations | 7 | 0 | 1.00 | 0.14 | 0.25 | 0.00–0.67 |
| opponent | 5 | 1 | 0.00 | 0.00 | 0.00 | 0.00–0.00 |
| congress | 4 | 0 | 0.00 | 0.00 | 0.00 | 0.00–0.00 |
| state_gov | 4 | 1 | 0.75 | 0.75 | 0.75 | 0.00–1.00 |
| trump_admin | 4 | 1 | 0.67 | 0.50 | 0.57 | 0.00–1.00 |
| other | 3 | 4 | 0.00 | 0.00 | 0.00 | 0.00–0.00 |
| gop_party | 2 | 0 | 0.00 | 0.00 | 0.00 |  |
| biden_harris | 1 | 1 | 0.50 | 1.00 | 0.67 |  |
| dem_party | 1 | 0 | 0.00 | 0.00 | 0.00 |  |
| iran_war | 1 | 1 | 0.00 | 0.00 | 0.00 |  |

## Frames

| label | human positives | false positives | precision | recall | F1 | 95% CI |
|---|---|---|---|---|---|---|
| tech.data_centers:land_local | 2 | 1 | 0.67 | 1.00 | 0.80 |  |
| tech.ai:race_china | 1 | 0 | 1.00 | 1.00 | 1.00 |  |
| tech.data_centers:water | 1 | 1 | 0.00 | 0.00 | 0.00 |  |
| tech.data_centers:energy_supply | 1 | 0 | 0.00 | 0.00 | 0.00 |  |
| tech.ai:jobs | 0 | 2 | 0.00 | 0.00 | 0.00 |  |
| tech.ai:other | 0 | 1 | 0.00 | 0.00 | 0.00 |  |
| tech.data_centers:bills | 0 | 2 | 0.00 | 0.00 | 0.00 |  |
| tech.data_centers:tax_breaks | 0 | 1 | 0.00 | 0.00 | 0.00 |  |
| edu:parents_rights | 0 | 1 | 0.00 | 0.00 | 0.00 |  |

Frames added after hand labeling began are scored only on items whose hand label covers them: {'edu': 67}

## Flags

| label | human positives | false positives | precision | recall | F1 | 95% CI |
|---|---|---|---|---|---|---|
| local_reference | 58 | 7 | 0.82 | 0.55 | 0.66 | 0.53–0.77 |
| credit_claim | 30 | 3 | 0.86 | 0.60 | 0.71 | 0.56–0.83 |
| is_fundraising_ask | 2 | 2 | 0.33 | 0.50 | 0.40 |  |

## Parent-topic shares on the random draw, websites + YouTube (what a party chart would show)

| parent | party | human share | model share |
|---|---|---|---|
| abortion | D | 7% | 7% |
| agri_rural | D | 11% | 0% |
| col | D | 52% | 48% |
| culture | D | 11% | 4% |
| dem | D | 48% | 44% |
| disasters | D | 4% | 0% |
| econ | D | 41% | 22% |
| edu | D | 30% | 19% |
| env | D | 11% | 11% |
| foreign | D | 15% | 11% |
| guns | D | 4% | 4% |
| hc | D | 41% | 26% |
| imm | D | 15% | 7% |
| infrastructure | D | 11% | 4% |
| safety | D | 4% | 7% |
| safety_net | D | 4% | 7% |
| tech | D | 11% | 11% |
| veterans | D | 4% | 4% |
| abortion | R | 3% | 7% |
| agri_rural | R | 17% | 10% |
| col | R | 45% | 31% |
| culture | R | 31% | 21% |
| dem | R | 24% | 24% |
| disasters | R | 7% | 0% |
| econ | R | 69% | 52% |
| edu | R | 31% | 17% |
| env | R | 21% | 17% |
| foreign | R | 17% | 10% |
| guns | R | 7% | 7% |
| hc | R | 45% | 28% |
| imm | R | 21% | 21% |
| infrastructure | R | 21% | 17% |
| other | R | 3% | 0% |
| safety | R | 31% | 24% |
| tech | R | 3% | 3% |
| tribal | R | 3% | 3% |
| veterans | R | 14% | 10% |

Cleanup fixes applied to model output: {'blame': 1}
