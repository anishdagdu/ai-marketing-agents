---
name: hubspot-growth-workflow
description: Runs the HubSpot AI team end to end (fix the CRM → capture and convert → bring traffic → bring them back → measure revenue) using the hs-* agents, with Shopify, Stripe and Slack integrations. Use when the user says "run the HubSpot workflow", wants more pipeline or revenue from HubSpot, or wants a weekly HubSpot check.
---

# HubSpot AI growth workflow

```
            ┌───────────────────────────┐
            │     hs-orchestrator       │  finds the biggest funnel leak,
            │  (routes + ranks actions) │  briefs the right agents
            └─────────────┬─────────────┘
                          ▼
 1 FIX THE CRM        hs-crm-setup · hs-data-hygiene · hs-integrations (Shopify · Stripe · Slack)
                          ▼
 2 CONVERT            hs-forms-landing-pages · hs-lead-scoring · hs-sales-pipeline
                          ▼
 3 BRING TRAFFIC      hs-seo-aeo · hs-social · hs-ads
                          ▼
 4 BRING THEM BACK    hs-email-marketing · hs-workflows · hs-service-helpdesk
                          ▼
 5 MEASURE REVENUE    hs-reporting-attribution · hs-revenue-stripe ──▶ back to orchestrator (weekly)
```

## Steps
1. **Fix the CRM** – `hs-crm-setup` and `hs-data-hygiene` first. `hs-integrations` checks that Shopify orders and Stripe payments land on the right records and sets up Slack alerts. If data is broken, stop here: bad data makes every later step wrong.
2. **Convert** – `hs-forms-landing-pages` captures leads, `hs-lead-scoring` decides who is sales-ready, `hs-sales-pipeline` unsticks deals with sequences and meeting links.
3. **Bring traffic** – `hs-seo-aeo` and `hs-social` for organic, `hs-ads` for paid audiences and ROI.
4. **Bring them back** – `hs-email-marketing` drafts campaigns, `hs-workflows` builds nurture, Shopify and Stripe-triggered flows (turned off), `hs-service-helpdesk` cuts repeat tickets.
5. **Measure revenue** – `hs-reporting-attribution` writes the weekly readout and `hs-revenue-stripe` checks MRR, churn and failed payments. The orchestrator turns both into next week's ranked actions and, after a yes, posts the summary to Slack.

## Guardrails (apply to every agent)
- Every write, send and Slack post needs explicit user approval in chat. Show the full list of changes first.
- Emails, pages, workflows and sequences are drafts or turned off. The user publishes, sends and turns on.
- Never enter credentials or payment details, never refund or charge in Stripe, never delete records.
- Name created assets with the prefix `AI · ` and tag them `ai-workflow`.
- Save outputs in `outputs/` so later steps and weekly runs can read them.

## Single requests
- "our data is a mess" → `hs-data-hygiene`
- "Shopify orders aren't in HubSpot" → `hs-integrations`
- "not enough leads" → `hs-forms-landing-pages`
- "sales says leads are bad" → `hs-lead-scoring`
- "deals are stuck" → `hs-sales-pipeline`
- "automate follow-up" → `hs-workflows`
- "churn / failed payments" → `hs-revenue-stripe`
- "how did last week go" → `hs-reporting-attribution`
