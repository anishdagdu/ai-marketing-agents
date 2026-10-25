---
name: klaviyo-growth-workflow
description: Runs the Klaviyo AI sales workflow end to end (data foundation → segments → flows → campaigns → performance loop) using the kl-* agents. Use when the user says "run the Klaviyo workflow", wants high-converting email/SMS, better use of first-party data, or asks where to start with Klaviyo.
---

# Klaviyo AI growth workflow

```
 ┌──────────────────┐   ┌────────────────────┐   ┌─────────────────┐
 │ 1 kl-data-       │──▶│ 2 kl-segment-      │──▶│ 3 kl-flow-      │
 │   foundation     │   │   architect        │   │   builder       │
 │ (1PD audit/setup)│   │ (audiences)        │   │ (automations)   │
 └──────────────────┘   └────────────────────┘   └────────┬────────┘
          ▲                                               │
          │             ┌────────────────────┐   ┌────────▼────────┐
          └─────────────│ 5 kl-performance-  │◀──│ 4 kl-campaign-  │
            fixes       │   analyst (weekly) │   │   strategist    │
                        └────────────────────┘   └─────────────────┘
```

## Steps
1. **Foundation** – run `kl-data-foundation`. If the readiness score is under 50 or Placed Order is missing, stop. Present the setup plan, because the flows and segments would have nothing to trigger on.
2. **Segments** – run `kl-segment-architect` with the audit. Show the proposed table, then **ask before creating anything**.
3. **Flows** – run `kl-flow-builder` in priority order, building only flows whose trigger event exists. Create them as drafts. The user turns them on.
4. **Campaigns** – run `kl-campaign-strategist` for a 4-week calendar on the new segments. Create the campaigns as drafts. The user sends.
5. **Loop** – run `kl-performance-analyst` weekly and route each problem to the agent it names. You can schedule this with the `schedule` skill if the user asks.

## Guardrails (apply to every agent)
- Every write needs explicit user approval in chat. Show the full list of changes first.
- Never send campaigns, never set flows live, never suppress, delete or merge profiles.
- Only mail profiles with valid consent. Exclude unengaged profiles (180d) from campaigns.
- Name created assets with the prefix `AI · ` and tag them `ai-workflow` so they're easy to audit or roll back.
- Save outputs in `outputs/` so later steps and weekly runs can read them.

## Single requests
- "who should I email" → step 2
- "set up abandoned cart" → step 3
- "what should I send this week" → step 4
- "how did last week go" → step 5
- "flows not triggering" → step 1
