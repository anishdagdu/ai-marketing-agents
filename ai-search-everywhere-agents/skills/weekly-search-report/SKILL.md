---
name: weekly-search-report
description: Weekly search progress report - compares this week's rankings, clicks, AI visibility and conversions with last week and with the 2/3/6-month ranking targets, and lists next week's actions. Use for "weekly report", "how did we do this week", or after a new Search Console export.
---
# Weekly Search Report

Shared rules: see `search-everywhere-workflow`. Runs after the first full audit exists (`<domain>-search-audit/`).

## Inputs (all free)
- **Required**: this week's Google Search Console export (Queries + Pages, last 7 days, compared with previous 7 days).
- Baseline: `rankings.csv` and `ACTION-PLAN.md` from the audit; last week's `weekly/<date>.md` if any.
- Optional: GA4 (organic + AI referrers: chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai), Bing Webmaster export, the GEO prompt sheet (re-run monthly, or weekly for 5 key prompts), PageSpeed results.
If an input is missing, say "not checked" - never fill gaps with guesses.

## Steps
1. **Rankings delta** per tracked keyword: last week -> this week position, change, URL ranking (flag if the ranking URL changed = possible cannibalisation).
2. **Target progress**: for each keyword, status vs its month-2 / month-3 / month-6 target: On track / At risk / Off track / Hit.
   - Off track = needed pace not met (e.g. must gain 6 positions in 8 weeks but moved 0 in 4).
   - Apply the week-6 rule: no movement of 5+ positions by week 6 -> mark "Re-diagnose" and say why (page type, links, cannibalisation, technical).
3. **Traffic**: clicks, impressions, CTR, avg position (site + top 10 pages), week over week. Flag CTR below what the position should get -> title/meta test.
4. **AI visibility**: AI-referral sessions, plus share-of-voice change if prompts were re-run.
5. **Work done**: tick off `ACTION-PLAN.md` items completed this week (ask the user or read their notes).
6. **Context**: check the Google Search Status Dashboard for updates this week before blaming a drop.
7. **Next week**: 3-5 actions max, highest impact first, each tied to a keyword or finding.

## Output -> `<domain>-search-audit/weekly/<YYYY-MM-DD>.md` + append a row to `weekly/history.csv`
```
# Weekly search report - <domain> - week of <date>
## Headline (3 bullets: biggest win, biggest risk, one decision needed)
## Scorecard (this week vs last: clicks, impressions, CTR, avg pos, keywords in top 3 / top 5 / top 10, AI referrals)
## Keyword targets (table: keyword, last, now, change, target, status)
## Wins / Drops (with likely cause)
## Done this week
## Next week (3-5 actions)
## Not checked
```
`history.csv` columns: week, clicks, impressions, ctr, avg_position, kw_top3, kw_top5, kw_top10, ai_referrals.
Keep it to one page; plain language for a business owner.
