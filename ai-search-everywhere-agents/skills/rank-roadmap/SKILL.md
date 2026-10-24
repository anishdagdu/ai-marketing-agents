---
name: rank-roadmap
description: Rankings layer - finds a site's current organic positions for its top keywords and builds a keyword-by-keyword plan to reach top 5 in 2-3 months and top 3 in 6 months, with a realism check per keyword. Use for "where do we rank", ranking targets, keyword roadmaps or "how do we get to page 1 / top 3".
---
# Rank Roadmap (layer 6 - Rankings)

Shared rules: see `search-everywhere-workflow`. Needs SEO findings (clusters, technical issues) and SXO findings (page-type match) as inputs.

## 1. Get current rankings (best source first)
1. **Google Search Console** export (Queries + Pages, last 3 months): average position, clicks, impressions, CTR. Most accurate for the site's own data.
2. **Semrush / Ahrefs** (if connected and the user approves the call): organic positions report for the domain in the right country database (e.g. `fi` for Finland), plus keyword difficulty (KD), volume, intent, SERP features, and the URL ranking.
3. **Manual fallback**: the user's keyword list + a rank check (WebSearch is personalised and not location-precise - label "approximate").
Always set country + language (e.g. Finland, Finnish and English) and device (mobile first). Record the date of the data.

## 2. Pick the top keywords (20-50)
Score each: `priority = volume x intent weight x (1 / current-position band)`. Intent weights: transactional 1.0, commercial 0.8, informational 0.4, navigational (own brand) - track only.
Include: keywords already in positions 4-30 ("striking distance"), core product/category terms, and high-value terms where the site doesn't rank yet but has a fitting page.

## 3. Classify each keyword into a tier
| Current position | Tier | Typical lever |
|---|---|---|
| 1-3 | Defend | Freshness, CTR (title/meta), keep links |
| 4-10 | Quick win | On-page, internal links, snippet targeting, CTR |
| 11-20 | Push | Content depth, page-type fix, more internal links, a few quality links |
| 21-50 | Build | Rewrite/expand or new dedicated page, topical cluster, links |
| Not ranking | New | Create the right page type first |

## 4. Realism check (be honest)
For each keyword estimate the chance of hitting the target in time, using: KD, gap vs the current top 5 (their referring domains, content depth, brand strength), SERP features taking space (ads, shopping, maps, AI Overview), and whether the right page type exists (from SXO).
Label each target **Likely / Possible / Stretch / Unrealistic**. Never promise a position; Google updates and competitors can change results. Typical guide (adjust to the data):
- Position 4-10, KD < 30 -> top 5 in 2 months: Likely.
- Position 11-20, KD < 40 -> top 5 in 3 months: Possible.
- Position 21-50 or KD 40-60 -> top 3 in 6 months: Stretch, needs content + links.
- KD > 70 vs big brands / marketplaces -> top 3 in 6 months: usually Unrealistic; suggest a long-tail variant instead.

## 5. Roadmap per keyword
For each keyword: current pos · URL · volume · KD · tier · targets (top 5 by month 2 or 3, top 3 by month 6) · realism label · actions with owner and week.

Time-boxed plan:
- **Weeks 1-2**: fix technical blockers from SEO/AIO on target URLs; rewrite titles/metas for CTR; add internal links from strong pages using exact/partial anchor text; fix keyword cannibalisation (one URL per keyword).
- **Weeks 3-8 (top 5 by month 2-3)**: on-page and content depth vs the top 5 (cover their subtopics, add FAQs/answer blocks, original data, images/video); fix page-type mismatches; schema; target featured snippets.
- **Months 3-6 (top 3 by month 6)**: earn links to target pages (local press, suppliers, partners, guides, reviews); build supporting cluster articles that link to the money page; refresh content monthly; keep improving CTR and engagement.

## 6. Tracking
- Track weekly: position, URL ranking, clicks, CTR. Checkpoints at week 4, month 2, month 3, month 6.
- If a keyword hasn't moved 5+ positions by week 6, re-diagnose (wrong page type? links gap? cannibalisation?).

## Score (0-100)
Share of top keywords in top 3 (40) · in top 10 (30) · striking-distance count trend (15) · CTR vs expected for position (15).

## Output -> `findings/rankings.md` and `rankings.csv`
`rankings.csv` columns: keyword, volume, kd, intent, current_position, url, tier, target_m2, target_m3, target_m6, realism, main_actions.
