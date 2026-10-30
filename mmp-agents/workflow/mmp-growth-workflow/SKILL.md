---
name: mmp-growth-workflow
description: Runs the MMP AI team end to end (measure → signals → protect → analyze → activate loop) for AppsFlyer, Adjust or another mobile measurement partner using the mmp-* agents. Use when the user says "run the MMP workflow", wants an AppsFlyer or Adjust audit, asks why numbers don't match, or wants a weekly app-growth check.
---

# MMP AI growth workflow

```
            ┌───────────────────────────┐
            │     mmp-orchestrator      │  finds the biggest measurement
            │  (routes + ranks actions) │  or growth gap, briefs agents
            └─────────────┬─────────────┘
                          ▼
 1 MEASURE      mmp-attribution · mmp-san-reconciliation · mmp-lookback-windows · mmp-skan-aak
                          ▼
 2 SIGNALS      mmp-postbacks · mmp-in-app-events · mmp-ad-revenue · mmp-raw-data-export
                          ▼
 3 PROTECT      mmp-fraud-realtime · mmp-fraud-post-attribution · mmp-privacy-consent · mmp-clean-room
                          ▼
 4 ANALYZE      mmp-cost-roas · mmp-cohort-ltv · mmp-creative-analytics · mmp-incrementality-mmm
                          ▼
 5 ACTIVATE     mmp-deep-linking · mmp-cross-platform · mmp-audiences · mmp-ai-copilot ──▶ back to orchestrator (weekly)
```

## Steps
1. **Measure** – `mmp-attribution` and `mmp-san-reconciliation` first. If installs are double-counted or SAN integrations are broken, stop and fix that: every later number depends on it. Then `mmp-lookback-windows` and, for iOS, `mmp-skan-aak`.
2. **Signals** – `mmp-in-app-events` cleans the event taxonomy, `mmp-postbacks` sends the right events to each network, `mmp-ad-revenue` adds ad revenue and `mmp-raw-data-export` lands it all in the warehouse.
3. **Protect** – `mmp-fraud-realtime` and `mmp-fraud-post-attribution` remove fake installs and events before ROAS is read. `mmp-privacy-consent` checks consent and deletion handling; `mmp-clean-room` only when a question needs user-level joins.
4. **Analyze** – `mmp-cost-roas` and `mmp-cohort-ltv` show what each source is worth, `mmp-creative-analytics` ranks creatives by value, `mmp-incrementality-mmm` checks what was truly incremental.
5. **Activate** – `mmp-deep-linking`, `mmp-cross-platform` and `mmp-audiences` turn the findings into better journeys and campaigns (as drafts). `mmp-ai-copilot` sets daily anomaly alerts. The orchestrator turns everything into next week's ranked actions. Schedule this with the `schedule` skill if the user asks.

## Guardrails (apply to every agent)
- Every change in the MMP needs explicit user approval in chat. Show the full list of changes first.
- Never change ad budgets or bids, never touch the app SDK, never message users.
- No user-level data in chat or reports; respect consent; never re-identify users.
- Name created assets with the prefix `AI · `.
- Save outputs in `outputs/` so later steps and weekly runs can read them.

## Single requests
- "Meta and the MMP don't match" → `mmp-san-reconciliation`
- "iOS numbers look wrong" → `mmp-skan-aak`
- "networks optimize to the wrong event" → `mmp-postbacks`
- "is this partner fraud?" → `mmp-fraud-realtime` + `mmp-fraud-post-attribution`
- "what is our ROAS / payback?" → `mmp-cost-roas` + `mmp-cohort-ltv`
- "would these installs have happened anyway?" → `mmp-incrementality-mmm`
- "links open the wrong screen" → `mmp-deep-linking`
- "GDPR / consent check" → `mmp-privacy-consent`
