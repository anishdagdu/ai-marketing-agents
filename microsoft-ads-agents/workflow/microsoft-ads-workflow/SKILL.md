---
name: microsoft-ads-workflow
description: Runs the Microsoft Ads AI team end to end across Bing, Copilot, the Yahoo/AOL/DuckDuckGo syndication network and the Microsoft Audience Network (route → import and measure → win search → expand reach → optimise and prove loop) using the ms-* agents and the JEV model router. Use when the user says "run the Microsoft Ads workflow", wants to launch or audit Microsoft Advertising (Bing Ads), or wants a weekly Microsoft Ads check.
---

# Microsoft Ads AI workflow with JEV routing

```
          ┌───────────────────────────┐      ┌───────────────────────────┐
          │      ms-orchestrator      │ ───▶ │   ms-jev-router (JEV)     │
          │   finds the biggest gap   │ ◀─── │ fast · standard · deep    │
          └─────────────┬─────────────┘      └───────────────────────────┘
                        ▼
 1 IMPORT + MEASURE  ms-import-tracking                       (stop here if UET or conversions are broken)
                        ▼
 2 WIN SEARCH        ms-search-optimizer · ms-linkedin-b2b
                        ▼
 3 EXPAND REACH      ms-copilot-ai · ms-audience-network · ms-shopping-pmax
                        ▼
 4 OPTIMISE+PROVE    ms-optimizer-reporter
                        ▼
                   you approve ──▶ back to orchestrator (weekly)
```

## Steps
0. **Route** – the orchestrator lists the tasks and asks `ms-jev-router` for a tier per task. Fast = haiku, standard = sonnet, deep = opus.
1. **Import and measure** – `ms-import-tracking` imports the profitable Google campaigns (paused), sets up scheduled sync that keeps Microsoft-only changes, and checks UET, conversion goals, enhanced and offline conversions and Clarity. Conversions must match the store or CRM within 10%.
2. **Win search** – `ms-search-optimizer` shifts budget to themes that are cheaper per conversion than on Google, uses ad-group level location, language and schedule, device adjustments and partner site exclusions. `ms-linkedin-b2b` layers company, industry and job function targeting for B2B.
3. **Expand reach** – `ms-copilot-ai` tests ads in Copilot and AI answers, `ms-audience-network` runs native and remarketing on MSN, Outlook and Edge, `ms-shopping-pmax` runs the feed, Shopping, Performance Max and dynamic remarketing.
4. **Optimise and prove** – `ms-optimizer-reporter` sets bids and budgets, reads Microsoft against Google, uses the account rep for betas and credits, and writes the weekly readout with JEV's cost summary. Schedule with the `schedule` skill if the user asks.

## JEV efficiency rules
- Start low, escalate on evidence. Split cheap counting from expensive deciding.
- Copy what already works on Google (imported keywords, ads, search terms) before paying for fresh research.
- Read Microsoft's free signals (recommendations, share of voice, Keyword Planner, Clarity) first.
- Reuse outputs from the last 7 days; batch fast checks; at most 2 deep tasks per weekly run.
- Log every decision to `outputs/jev-routing-log.csv`.

## Guardrails (apply to every agent)
- Every write in Microsoft Advertising needs explicit approval in chat. Show the full list of changes and the cost impact first.
- Bids, budgets and bid adjustments move at most 20% per step and never past the user's cap. Imports and new campaigns start paused.
- Scheduled import never overwrites Microsoft-only changes. No bid strategy kept automated without about 30 conversions in 30 days.
- No targeting that singles out protected groups. Never delete; pause. Name created items `AI · ` and label them `ai-workflow`.

## Single requests
- "get us live on Bing" / "import from Google" → `ms-import-tracking`
- "conversions don't match" → `ms-import-tracking`
- "CPC or CPA went up" / "partner traffic is junk" → `ms-search-optimizer`
- "target decision makers" / "lead quality is poor" → `ms-linkedin-b2b`
- "ads in Copilot" → `ms-copilot-ai`
- "retargeting" / "MSN or Outlook ads" → `ms-audience-network`
- "products disapproved" / "Shopping" / "PMax" → `ms-shopping-pmax`
- "is Microsoft worth it" / "weekly report" → `ms-optimizer-reporter`
- "why is the AI bill high" → `ms-jev-router`
