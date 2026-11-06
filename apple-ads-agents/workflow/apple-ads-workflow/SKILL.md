---
name: apple-ads-workflow
description: Runs the Apple Ads AI team end to end across the App Store, Apple News and Apple Maps (route → measure → discover → win the search → optimise and prove loop) using the aa-* agents and the JEV model router. Use when the user says "run the Apple Ads workflow", wants to grow App Store installs, audit an Apple Ads account, or wants a weekly Apple Ads check.
---

# Apple Ads AI workflow with JEV routing

```
          ┌───────────────────────────┐      ┌───────────────────────────┐
          │      aa-orchestrator      │ ───▶ │   aa-jev-router (JEV)     │
          │   finds the biggest gap   │ ◀─── │ fast · standard · deep    │
          └─────────────┬─────────────┘      └───────────────────────────┘
                        ▼
 1 MEASURE         aa-attribution · aa-account-architect      (stop here if attribution is broken)
                        ▼
 2 DISCOVER        aa-keyword-researcher · aa-search-match-miner
                        ▼
 3 WIN THE SEARCH  aa-brand-defender · aa-competitor-conquest · aa-cpp-creative · aa-placements
                        ▼
 4 OPTIMISE+PROVE  aa-bid-budget · aa-incrementality-tester · aa-geo-expansion · aa-reporter
                        ▼
                   you approve ──▶ back to orchestrator (weekly)
```

## Steps
0. **Route** – the orchestrator lists the tasks and asks `aa-jev-router` for a tier per task. Fast = haiku, standard = sonnet, deep = opus.
1. **Measure** – `aa-attribution` checks AdServices, the MMP and App Store Connect agree. `aa-account-architect` makes the structure readable (brand, category, competitor, discovery, placements).
2. **Discover** – keyword research from Search Popularity and recommendations; Search Match and broad match mined weekly for winners and negatives.
3. **Win the search** – defend the brand in both ad slots, conquest rivals where the app wins, match every ad group to a custom product page, and extend to Today tab, Search tab and product pages, then Apple News (brand reach) and Apple Maps (local visits) where they fit the goal.
4. **Optimise and prove** – bids and budgets to target CPA, incrementality tests on brand, new countries, and the weekly readout with JEV's cost summary. Schedule with the `schedule` skill if the user asks.

## JEV efficiency rules
- Start low, escalate on evidence. Split cheap counting from expensive deciding.
- Read Apple's free signals (Search Popularity, impression share, recommendations) before paid model time.
- Reuse outputs from the last 7 days; batch fast checks; at most 2 deep tasks per weekly run.
- Log every decision to `outputs/jev-routing-log.csv`.

## Guardrails (apply to every agent)
- Every write in Apple Ads needs explicit approval in chat. Show the full list of changes and the cost impact first.
- Bids and budgets move at most 20% per step and never past the user's cap. New campaigns start paused.
- No age or gender targeting unless asked (no attribution since September 2026). No rival trademarks in creative.
- Never delete; pause. Name created items `AI · ` and tag them `ai-workflow`.

## Single requests
- "competitors are showing on my brand" → `aa-brand-defender`
- "find me keywords" → `aa-keyword-researcher`
- "installs don't match AppsFlyer" → `aa-attribution`
- "CPI went up" → `aa-bid-budget` + `aa-search-match-miner`
- "conversion is low" → `aa-cpp-creative`
- "is brand spend worth it" → `aa-incrementality-tester`
- "where should we launch next" → `aa-geo-expansion`
- "Today tab / Apple News / Maps ads" → `aa-placements`
- "why is the AI bill high" → `aa-jev-router`
