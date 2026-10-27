---
name: uplift-readout
description: Calculates incremental uplift of a CRM campaign against its control group, with a 95% confidence interval, incremental revenue and cost per incremental player. Use when asked if a campaign worked, for incrementality, or for holdout results.
---

# Uplift readout

## Input
A CSV with one row per player: `group` (treatment or control), `converted` (0/1), and optionally `revenue` and `cost`.

## Run
```bash
python3 scripts/uplift.py results.csv
```
(The path is relative to this skill's folder.) Add `--min-lift 2` to also print the sample size needed to detect a 2-point lift.

## Read the result
- **Uplift (pts):** treatment conversion rate minus control conversion rate, in percentage points
- **95% CI:** if it includes 0, say "not significant yet", never "a win"
- **Incremental players:** uplift × treated players
- **Incremental revenue:** (treatment revenue per player − control revenue per player) × treated players
- **Cost per incremental player:** campaign cost ÷ incremental players

## Verdict
| Result | Verdict |
|---|---|
| CI fully above 0 | Keep, and consider making it always-on |
| CI includes 0, first cycle | Test again (check the sample size first) |
| CI includes 0, second cycle in a row | Flag to stop |
| CI fully below 0 | Stop now |
