---
name: linkedin-ads-workflow
description: Runs the LinkedIn Ads AI team end to end (foundations → target → create → launch and optimise → prove pipeline) using the li-* agents. Use when the user says "run the LinkedIn workflow", wants more B2B leads or pipeline from LinkedIn, asks why LinkedIn CPL is high, or wants a weekly LinkedIn Ads check.
---

# LinkedIn Ads AI workflow

```
            ┌───────────────────────────┐
            │      li-orchestrator      │  finds the biggest pipeline leak,
            │  (routes + ranks actions) │  briefs the right agents
            └─────────────┬─────────────┘
                          ▼
 1 FOUNDATIONS         li-account-setup · li-tracking-capi
                          ▼
 2 TARGET              li-icp-persona · li-abm-lists · li-audience-builder
                          ▼
 3 CREATE              li-copywriter · li-creative-formats · li-thought-leader · li-lead-gen-forms
                          ▼
 4 LAUNCH + OPTIMISE   li-campaign-builder · li-bid-budget-pacing · li-fatigue-frequency
                          ▼
 5 PROVE PIPELINE      li-crm-pipeline · li-reporting-attribution ──▶ back to orchestrator (weekly)
```

## Steps
1. **Foundations** – run `li-account-setup` and `li-tracking-capi`. If the Insight Tag, conversions or CRM sync are broken, stop and fix those first: LinkedIn clicks are expensive, and spend you can't measure can't be optimised.
2. **Target** – `li-icp-persona` defines the ICP and buying committee. `li-abm-lists` builds tiered company and contact lists. `li-audience-builder` turns both into prospecting, retargeting and predictive audiences with exclusions. The user approves the audiences.
3. **Create** – `li-copywriter` and `li-creative-formats` make ads per persona and stage. `li-thought-leader` plans posts to promote from leaders. `li-lead-gen-forms` sharpens the offer and the form. The user approves copy and offers.
4. **Launch and optimise** – `li-campaign-builder` builds everything as drafts or paused. After the user launches: `li-bid-budget-pacing` checks delivery and cost per result; `li-fatigue-frequency` refreshes tired ads.
5. **Prove pipeline** – `li-crm-pipeline` checks follow-up and sends outcomes back to LinkedIn. `li-reporting-attribution` writes the weekly report on pipeline and revenue. The orchestrator turns it into next week's ranked actions. Schedule this with the `schedule` skill if the user asks.

## Guardrails (apply to every agent)
- Every write needs explicit user approval in chat. Show the full list of changes first.
- Campaigns and ads are built as drafts or paused. The user launches, unpauses and changes budgets.
- Never enter credentials or billing details, never accept terms on the user's behalf, never delete anything.
- Upload only consented first-party lists; never scrape LinkedIn.
- Name created items with the prefix `AI · `.
- Save outputs in `outputs/` so later steps and weekly runs can read them.

## Single requests
- "leads don't show up / numbers don't match" → `li-tracking-capi`
- "who should we target" → `li-icp-persona` + `li-audience-builder`
- "run ABM on these accounts" → `li-abm-lists`
- "write new ads" → `li-copywriter` + `li-creative-formats`
- "promote our CEO's posts" → `li-thought-leader`
- "lead quality is bad" → `li-lead-gen-forms` + `li-crm-pipeline`
- "CPL is too high / budget won't spend" → `li-bid-budget-pacing`
- "CTR is dropping" → `li-fatigue-frequency`
- "is LinkedIn worth it" → `li-reporting-attribution`
