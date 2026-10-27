---
name: rg-risk-check
description: Scores responsible-gaming risk for players from five behaviour signals and returns a score, a band and the signals that fired. Use before any promotional send, or when asked whether a player or audience is at risk.
---

# RG risk check

## Score (0–1)
| Signal | Weight | Fires when |
|---|---|---|
| Limit raised | 0.25 | Deposit or loss limit raised in the last 30 days |
| Late-night play | 0.25 | Share of sessions 00:00–06:00, scaled: 40% or more = full weight |
| Chasing losses | 0.20 | Deposit within 30 minutes of a loss, 3+ times in 14 days |
| Faster deposits | 0.15 | Deposit frequency up 50% or more vs the 8-week average (full weight at 2×) |
| Longer sessions | 0.15 | Average session length up 50% or more vs the 8-week average (full weight at 2×) |

## Bands (defaults, change only with written approval)
- **Low:** below 0.3. Promotions allowed
- **Medium:** 0.3 to 0.6. No promotions. Care message or limit suggestion
- **High:** 0.6 or more. No promotions. Care message and escalation to player care
- **Missing data:** treat as high for promotions

## Output per player
`player_id, rg_score, band, signals_fired, reason`

The reason is one plain sentence, for example: "Limit raised 12 days ago and 45% of play after midnight."

## Care messages to swap in
- "Want to set a weekly limit? It takes two taps." (link to limit tools)
- "Here are your results from this week." (no offer)
- "Your play this year has supported Finnish sport, culture and science." (charity impact)
