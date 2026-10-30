# MMP Agents: An AI Team for AppsFlyer, Adjust and Every Mobile Measurement Partner

![MMP agents workflow](mmp-agents-workflow.gif)

Twenty-one Claude Code agents and one workflow skill: one orchestrator plus one specialist for each of the 20 most important things a mobile measurement partner (MMP) like AppsFlyer, Adjust, Singular, Branch or Kochava does. Together they check that attribution is right, signals reach the ad networks, fraud and privacy risks are handled, ROAS and LTV are clear, and the findings turn into better links, audiences and alerts.

> **AI recommends. You approve.** The agents read and diagnose. Any change in your MMP (attribution windows, postbacks, fraud rules, partner permissions, conversion values, links, audiences, exports) is shown to you first and only made after your OK in chat. They never change ad budgets, never touch the app SDK, never message users and never paste user-level data into chat.

## How it works

| Stage | Agent | What it does |
|---|---|---|
| Lead | [`mmp-orchestrator`](agents/mmp-orchestrator.md) | Finds the biggest measurement or growth gap, briefs the right agents, returns one ranked action list |
| 1 Measure | [`mmp-attribution`](agents/mmp-attribution.md) | Deduplication and last-touch attribution: the MMP as neutral referee |
| | [`mmp-san-reconciliation`](agents/mmp-san-reconciliation.md) | Meta, Google, TikTok, Snap and Apple Ads claims vs MMP numbers |
| | [`mmp-lookback-windows`](agents/mmp-lookback-windows.md) | Click and view-through windows per channel |
| | [`mmp-skan-aak`](agents/mmp-skan-aak.md) | SKAdNetwork and AdAttributionKit, conversion value schemas, ATT |
| 2 Signals | [`mmp-postbacks`](agents/mmp-postbacks.md) | The right events and values sent back to each ad network |
| | [`mmp-in-app-events`](agents/mmp-in-app-events.md) | Event taxonomy, purchases, subscriptions, uninstalls |
| | [`mmp-ad-revenue`](agents/mmp-ad-revenue.md) | Impression-level ad revenue from AppLovin MAX, LevelPlay, AdMob |
| | [`mmp-raw-data-export`](agents/mmp-raw-data-export.md) | Data Locker / raw exports into S3, BigQuery or Snowflake |
| 3 Protect | [`mmp-fraud-realtime`](agents/mmp-fraud-realtime.md) | Protect360 / Fraud Prevention Suite: click spam, injection, SDK spoofing, bots |
| | [`mmp-fraud-post-attribution`](agents/mmp-fraud-post-attribution.md) | Fake events, low-quality sources, partner reconciliation |
| | [`mmp-privacy-consent`](agents/mmp-privacy-consent.md) | GDPR, DMA, Consent Mode v2, TCF, ATT, data deletion |
| | [`mmp-clean-room`](agents/mmp-clean-room.md) | Privacy-safe joins of first-party and attribution data |
| 4 Analyze | [`mmp-cost-roas`](agents/mmp-cost-roas.md) | Cost aggregation, CPI, CPA and ROAS by source and campaign |
| | [`mmp-cohort-ltv`](agents/mmp-cohort-ltv.md) | Cohorts, retention, payback and predicted LTV |
| | [`mmp-creative-analytics`](agents/mmp-creative-analytics.md) | Creatives ranked by valuable users, fatigue checks |
| | [`mmp-incrementality-mmm`](agents/mmp-incrementality-mmm.md) | Holdout tests and media mix modeling |
| 5 Activate | [`mmp-deep-linking`](agents/mmp-deep-linking.md) | OneLink / Adjust Links, deferred deep links, fallbacks |
| | [`mmp-cross-platform`](agents/mmp-cross-platform.md) | Web-to-app, email, SMS, QR, influencers, CTV, PC and console |
| | [`mmp-audiences`](agents/mmp-audiences.md) | Retargeting, suppression and lookalike seed audiences |
| | [`mmp-ai-copilot`](agents/mmp-ai-copilot.md) | MMP AI assistants, anomaly alerts and a daily digest |

The [`mmp-growth-workflow`](workflow/mmp-growth-workflow/SKILL.md) skill runs the stages in order. It stops at stage 1 if installs are double-counted or SAN integrations are broken, because every later number depends on them.

**Works with the rest of this repo:** `mmp-creative-analytics` hands creative production to [AI UGC Ad Agents](../ai-ugc-ad-agents/), `mmp-cost-roas` and `mmp-audiences` feed [AI Paid Traffic](../ai-paid-traffic-agents/), `mmp-audiences` shares consented segments with [Klaviyo 1PD Agents](../klaviyo-1pd-agents/) and [CRM Agents](../crm-agents/), and web-to-app tracking checks go to the [GTM Health Agent](../gtm-health-agent/).

**Guardrails in every agent**
- Show the full list of changes before any change in the MMP
- Never change budgets or bids, never touch the SDK, never message users
- No user-level data in chat or reports; consent is respected
- Name everything created with the prefix `AI · `, so it's easy to audit or roll back
- Every number comes from a tool call or a shared file, never from memory

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Access to your MMP data: AppsFlyer or Adjust exports or API (Pull API, Master API, Data Locker; Adjust Report API, Datascape), or the matching **Windsor.ai** connector
- Optional: the AppsFlyer MCP server, ad network connectors and your data warehouse

## Install

```bash
./install.sh
```

Then, in a new Claude Code session, say **"run the MMP workflow"**. Or ask one agent directly, for example "use mmp-san-reconciliation, Meta shows twice our AppsFlyer installs" or "use mmp-skan-aak, review our conversion value schema".

## Files

- `agents/`: the 21 agent definitions
- `workflow/mmp-growth-workflow/SKILL.md`: the orchestrator skill
- `mmp-agents-workflow.gif`: workflow infographic
- `docs/make_gif.py`: regenerates the GIF (needs Pillow)
