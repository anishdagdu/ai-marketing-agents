---
name: avantstay-growth-workflow
description: Runs the AvantStay performance marketing team end to end (measurement → guest demand → members → homeowners → buyers → hotels → corporate → creative and reporting) using the av-* agents. Use when the user says "run the AvantStay workflow", wants a full paid acquisition plan for guests or homeowners, or asks which av-* agent should handle a task.
---

# AvantStay growth workflow

Route the request to the right team, or run the teams in order for a full plan.

## Order

1. **Signal and Measurement** (10 agents): rebuild tracking and attribution leadership trusts. Agents: `av-signal-terms-and-claims-ledger`, `av-signal-tag-and-consent-auditor`, `av-signal-event-spec-writer`, `av-signal-sgtm-and-capi-planner`, `av-signal-enhanced-conversions-validator`, `av-signal-salesforce-stage-mapper`, `av-signal-attribution-policy-writer`, `av-signal-geo-holdout-designer`, `av-signal-lift-readout-agent`, `av-signal-discrepancy-monitor`.
2. **Guest Demand** (10 agents): fill homes through search, pmax and meta. Agents: `av-guest-market-and-occasion-keyword-agent`, `av-guest-search-builder`, `av-guest-per-guest-price-agent`, `av-guest-pmax-and-feed-agent`, `av-guest-demand-gen-and-youtube-agent`, `av-guest-meta-catalogue-agent`, `av-guest-microsoft-mirror-agent`, `av-guest-abandoned-search-retargeter`, `av-guest-snowbird-and-long-stay-agent`, `av-guest-waste-and-negatives-agent`.
3. **Member and Loyalty** (9 agents): grow members club and referrals. Agents: `av-member-member-savings-calculator`, `av-member-checkout-upsell-tester`, `av-member-repeat-guest-prospector`, `av-member-referral-loop-agent`, `av-member-renewal-and-churn-agent`, `av-member-coupon-intent-agent`, `av-member-concierge-upsell-agent`, `av-member-app-adoption-agent`, `av-member-affirm-and-protection-agent`.
4. **Homeowner Supply** (10 agents): lower the cost per signed homeowner. Agents: `av-owner-owner-icp-and-market-scorer`, `av-owner-owner-search-agent`, `av-owner-calculator-funnel-agent`, `av-owner-linkedin-owner-agent`, `av-owner-switcher-agent`, `av-owner-direct-mail-agent`, `av-owner-owner-lead-scorer`, `av-owner-speed-to-lead-agent`, `av-owner-owner-proof-miner`, `av-owner-ai-visibility-agent`.
5. **Buyer, Investor and Agent** (8 agents): sell the homes for sale and recruit agents. Agents: `av-buyer-listing-feed-agent`, `av-buyer-yield-explainer-agent`, `av-buyer-buyer-search-and-social-agent`, `av-buyer-investor-outreach-agent`, `av-buyer-seller-lead-agent`, `av-buyer-agent-recruiter`, `av-buyer-agent-enablement-agent`, `av-buyer-report-refresher`.
6. **Hotel, OTA and Metasearch** (9 agents): run hotel, ota and metasearch ads. Agents: `av-hotel-hotel-feed-and-price-accuracy-agent`, `av-hotel-free-booking-links-agent`, `av-hotel-metasearch-bid-agent`, `av-hotel-travelads-agent`, `av-hotel-booking-sponsored-ads-agent`, `av-hotel-ota-vs-direct-margin-agent`, `av-hotel-hotel-launch-agent`, `av-hotel-group-buyout-agent`, `av-hotel-hotel-owner-lead-agent`.
7. **Corporate, Events and Groups** (8 agents): win company retreats and events. Agents: `av-corp-retreat-account-finder`, `av-corp-retreat-campaign-agent`, `av-corp-retreat-quote-agent`, `av-corp-rebook-agent`, `av-corp-occasion-page-agent`, `av-corp-occasion-search-agent`, `av-corp-event-calendar-agent`, `av-corp-quote-form-tester`.
8. **Creative, CRO and Reporting Ops** (12 agents): ship creative, site tests and reporting. Agents: `av-ops-hook-and-angle-agent`, `av-ops-video-and-gif-brief-agent`, `av-ops-claims-guard`, `av-ops-fatigue-agent`, `av-ops-landing-page-agent`, `av-ops-booking-flow-test-designer`, `av-ops-bigquery-model-builder`, `av-ops-pacing-and-anomaly-agent`, `av-ops-budget-and-forecast-agent`, `av-ops-ooh-and-mail-measurement-agent`, `av-ops-leadership-readout-agent`, `av-ops-change-log-keeper`.

## Rules

- Start with Team 1 if tracking, attribution or the Terms and Claims Ledger is missing or stale. Scaling spend on bad numbers wastes money.
- Brief one to four agents per request. Give each the goal, the data it may read and the output you need.
- Collect every output into one ranked proposal list: what to change, expected effect, evidence, and who approves.
- Nothing is changed, sent or published without a clear yes from the user in chat.
- Label each figure as measured or estimated. Hooks and offers are test ideas until a test proves them.
