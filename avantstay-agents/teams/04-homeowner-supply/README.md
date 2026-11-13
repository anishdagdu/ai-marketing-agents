# Team 4: Homeowner Supply

![Homeowner Supply workflow](workflow.gif)

**Goal:** Lower the cost per signed homeowner.

**Part of the role it answers:** Cost per qualified owner and per signed owner; LinkedIn; direct mail

**Offerings and audience:** Management, Airbnb management, calculator, AI audit, comparison pages (homeowner)

## Agents (10)

| Agent | One-line job | Inputs / tools | Output |
|---|---|---|---|
| [`av-owner-owner-icp-and-market-scorer`](../../agents/av-owner-owner-icp-and-market-scorer.md) | Ranks markets and home types by expected value of a signed owner | BQ, SF, AirDNA-type data | Priority market list |
| [`av-owner-owner-search-agent`](../../agents/av-owner-owner-search-agent.md) | Builds "airbnb management [city]" and income-estimate search | 605 local pages, Google Ads API | Campaign drafts |
| [`av-owner-calculator-funnel-agent`](../../agents/av-owner-calculator-funnel-agent.md) | Tests showing an instant range before the SMS step | Calculator events, Statsig | Test design and lead-quality readout |
| [`av-owner-linkedin-owner-agent`](../../agents/av-owner-linkedin-owner-agent.md) | Targets second-home owners and investors | LinkedIn API, SF segments | Campaign drafts |
| [`av-owner-switcher-agent`](../../agents/av-owner-switcher-agent.md) | Builds campaigns for owners leaving named competitors | Comparison pages, ledger | Ads and pages, legal-reviewed |
| [`av-owner-direct-mail-agent`](../../agents/av-owner-direct-mail-agent.md) | Builds address lists with a holdout and a trackable response path | Property records, SF | Mail file, holdout list, creative |
| [`av-owner-owner-lead-scorer`](../../agents/av-owner-owner-lead-scorer.md) | Scores leads on fit and sends a value back to ad platforms | SF, BQ | Score field and conversion values |
| [`av-owner-speed-to-lead-agent`](../../agents/av-owner-speed-to-lead-agent.md) | Drafts the first reply and books the call | SF, calendar | Reply drafts and response-time report |
| [`av-owner-owner-proof-miner`](../../agents/av-owner-owner-proof-miner.md) | Pulls testimonials and case numbers that the ledger approves | Homeowner reviews, case studies | Proof library |
| [`av-owner-ai-visibility-agent`](../../agents/av-owner-ai-visibility-agent.md) | Runs the audit promise honestly, starting with the missing llms.txt | Site crawl, AI answer tests | Fix list and weekly visibility report |



[Back to all teams](../../README.md)
