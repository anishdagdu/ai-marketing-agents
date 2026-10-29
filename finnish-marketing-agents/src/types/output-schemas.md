# Output schemas

## Ad copy table (finnish-ads-copywriter)
`| # | Copy (fi) | Chars / limit | English back-translation | Angle |`
- "Chars / limit" must be `N/LIMIT` so `src/utils/char_count.py` can check it; the copy must be in the column directly before it.

## Translation table
- en → fi: `| # | Original (en) | Finnish (fi) | Chars / limit | Note |`
- fi → en: `| # | Original (fi) | Literal (en) | Natural (en) | Chars / limit | Note |`

## calendar.csv (finnish-content-calendar), `;` separated, UTF-8
`Date;Weekday;Channel;Organic/Paid;Format;Pillar;Funnel stage;Topic;Hook (fi);Hook (en);Caption (fi);Caption (en);CTA (fi);CTA (en);Visual brief;Hashtags;Insight;KPI;Campaign type;Objective;Audience;Budget share`
(last four only for paid rows)

## Competitor sentiment table
`| Competitor | Sample size | % pos / neu / neg | Top praised themes | Top complaints | Ad angles they run | Opportunity for us |`

## Meta Ad Library table
`| Competitor | Active ads | Longest-running ad (days) | Main formats | Top 3 angles | Offers / CTAs | Gaps we can own |`
