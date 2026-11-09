---
name: prospecting-signals-workflow
description: Runs the prospecting and signals AI team end to end on Clay, Common Room and Apollo (route → target → enrich → signals → score → engage, with a reply loop) using the pr-* agents and the JEV router. Use when the user says "run the prospecting workflow", wants a target list, wants to know who to contact this week, or wants a weekly signals run.
---

# Prospecting and signals AI workflow (Clay · Common Room · Apollo) with JEV routing

```
          ┌───────────────────────────┐      ┌────────────────────────────────┐
          │      pr-orchestrator      │ ───▶ │      pr-jev-router (JEV)       │
          │ goal · play · budget      │ ◀─── │ model tier + cheapest data path│
          └─────────────┬─────────────┘      └────────────────────────────────┘
                        ▼
 1 TARGET      pr-icp-builder · pr-list-builder · pr-buying-committee        (Apollo · Clay)
                        ▼
 2 ENRICH      pr-contact-waterfall · pr-enrichment · pr-ai-researcher       (Clay waterfall · Claygent)
                        ▼
 3 SIGNALS     pr-intent-signals · pr-community-signals · pr-trigger-alerts  (Common Room · Apollo intent)
                        ▼
 4 SCORE       pr-lead-scorer (fit × intent, routing)
                        ▼
 5 ENGAGE      pr-crm-sync ──▶ pr-outreach-writer ──▶ you approve and send
                        │
                        └──▶ replies and meetings feed back into 4 SCORE (weekly)
```

## Steps
0. **Route** – the orchestrator sets the play and credit budget; `pr-jev-router` picks a model tier and the cheapest data path for every task.
1. **Target** – ICP and lookalikes, a clean list (customers, open deals and do-not-contact removed), and the buying committee per account.
2. **Enrich** – verified work emails through the waterfall, firmographics and tech stack, then AI research only on accounts with fit 70+.
3. **Signals** – intent topics and website visitors, community and product activity, trigger events (job changes, funding, hiring).
4. **Score** – fit × intent priority with a one-line reason, and draft routing to the right rep.
5. **Engage** – `pr-crm-sync` checks duplicates and opt-outs, `pr-outreach-writer` drafts first lines and sequences. The user approves, sends and enrolls. Replies and meetings tune next week's scores. Schedule with the `schedule` skill if the user asks.

## Signal-first or list-first
- **Warm play (default weekly):** 3 → 4 → 2 (enrich only what scored) → 5. Cheapest per meeting.
- **New market:** 1 → 2 → 3 → 4 → 5.
- **Clean-up:** `pr-crm-sync` + `pr-enrichment` only.

## JEV efficiency rules
- Reuse CRM and recent outputs, then Apollo built-in data, then the Clay waterfall cheapest-first, then Claygent.
- Never enrich accounts that fail the ICP filter. At most 2 deep tasks and the agreed credit budget per run.
- Log every decision and credit spend to `outputs/jev-routing-log.csv`.

## Guardrails (apply to every agent)
- Nothing is sent, enrolled or written to the CRM without a clear yes in chat. Outreach is saved as drafts.
- Business contact data only; respect opt-outs, customers, open deals, GDPR and platform terms.
- Never delete records; name created items `AI · ` and tag them `ai-workflow`.

## Single requests
- "who is our ideal customer" → `pr-icp-builder`
- "find me 200 heads of growth at Series B SaaS" → `pr-list-builder` + `pr-contact-waterfall`
- "who decides at Acme" → `pr-buying-committee`
- "who visited our pricing page" → `pr-intent-signals`
- "who's active in our community" → `pr-community-signals`
- "any champions changed jobs" → `pr-trigger-alerts`
- "who should we call first" → `pr-lead-scorer`
- "write the outreach" → `pr-outreach-writer`
- "our CRM is a mess" → `pr-crm-sync`
- "why are credits / AI costs high" → `pr-jev-router`
