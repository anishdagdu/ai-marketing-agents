---
name: carry1st-growth-workflow
description: Runs the Carry1st growth engine end to end (growth command → measurement → intelligence → creative → Google, Meta and TikTok → lifecycle → shop → discovery → creators → B2B) using the c1-* agents. Use when the user says "run the Carry1st workflow", wants a growth plan for the Carry1st Shop, Pay1st or Flow1st, or asks which c1-* agent should handle a task.
---

# Carry1st growth workflow

Route the request to the right team, or run the teams in order for a full plan.

## Order

1. **Growth Command** (11 agents): orchestrate the engine, allocate budget and govern every change. Agents: `c1-command-engine-orchestrator`, `c1-command-beat-calendar-keeper`, `c1-command-budget-allocator`, `c1-command-change-ledger-clerk`, `c1-command-guardrail-sentinel`, `c1-command-consent-and-privacy-gatekeeper`, `c1-command-experiment-registrar`, `c1-command-agent-evaluator`, `c1-command-cost-controller`, `c1-command-incident-responder`, `c1-command-weekly-readout-writer`.
2. **Measurement and Data Truth** (12 agents): build one shared view of spend, purchases and customer value. Agents: `c1-measure-measurement-lead`, `c1-measure-event-taxonomy-steward`, `c1-measure-mmp-integrity-monitor`, `c1-measure-server-side-signal-agent`, `c1-measure-identity-stitcher`, `c1-measure-fx-normaliser`, `c1-measure-blended-roas-modeller`, `c1-measure-pltv-forecaster`, `c1-measure-incrementality-designer`, `c1-measure-media-mix-analyst`, `c1-measure-anomaly-detector`, `c1-measure-platform-reconciler`.
3. **Market and Player Intelligence** (11 agents): watch demand, competitors, payment rails and rules. Agents: `c1-intel-intelligence-lead`, `c1-intel-country-market-analyst`, `c1-intel-competitor-shop-watcher`, `c1-intel-price-and-bonus-benchmarker`, `c1-intel-payment-rail-scout`, `c1-intel-title-demand-ranker`, `c1-intel-voice-of-customer-miner`, `c1-intel-community-listener`, `c1-intel-policy-and-regulation-watcher`, `c1-intel-fx-and-macro-watcher`, `c1-intel-insight-librarian`.
4. **Creative Studio** (12 agents): ship distinct, localised, on-policy creative every week. Agents: `c1-creative-creative-lead`, `c1-creative-concept-strategist`, `c1-creative-hook-and-script-writer`, `c1-creative-localisation-adapter`, `c1-creative-static-producer`, `c1-creative-video-assembler`, `c1-creative-footage-repurposer`, `c1-creative-similarity-screener`, `c1-creative-policy-and-brand-checker`, `c1-creative-format-packager`, `c1-creative-creative-analyst`, `c1-creative-fatigue-forecaster`.
5. **Google Ads** (12 agents): run Search, Performance Max, Demand Gen and App campaigns through one writer. Agents: `c1-google-google-lead`, `c1-google-search-and-ai-max-builder`, `c1-google-keyword-and-negative-curator`, `c1-google-feed-and-pmax-agent`, `c1-google-app-campaign-manager`, `c1-google-bid-readiness-checker`, `c1-google-demand-gen-and-shorts-planner`, `c1-google-asset-rotation-agent`, `c1-google-web-to-app-agent`, `c1-google-experiment-runner`, `c1-google-pacing-monitor`, `c1-google-google-writer`.
6. **Meta Ads** (12 agents): feed Advantage+ and click-to-WhatsApp campaigns with clean signal. Agents: `c1-meta-meta-lead`, `c1-meta-structure-architect`, `c1-meta-sales-campaign-manager`, `c1-meta-app-campaign-manager`, `c1-meta-whatsapp-ads-manager`, `c1-meta-catalog-agent`, `c1-meta-creative-slotting-agent`, `c1-meta-signal-quality-monitor`, `c1-meta-audience-and-exclusion-agent`, `c1-meta-learning-guard`, `c1-meta-fatigue-monitor`, `c1-meta-meta-writer`.
7. **TikTok Ads** (11 agents): run Smart+ and Spark Ads in the five eligible African markets. Agents: `c1-tiktok-tiktok-lead`, `c1-tiktok-country-eligibility-guard`, `c1-tiktok-smart-builder`, `c1-tiktok-asset-group-packager`, `c1-tiktok-spark-ads-coordinator`, `c1-tiktok-symphony-operator`, `c1-tiktok-trend-and-hook-scout`, `c1-tiktok-events-pipeline-monitor`, `c1-tiktok-placement-controller`, `c1-tiktok-creative-reporter`, `c1-tiktok-tiktok-writer`.
8. **Lifecycle and CRM** (12 agents): move buyers from their first purchase to their third. Agents: `c1-crm-lifecycle-lead`, `c1-crm-segment-builder`, `c1-crm-onboarding-agent`, `c1-crm-repeat-purchase-nudger`, `c1-crm-season-reminder-agent`, `c1-crm-payment-recovery-agent`, `c1-crm-win-back-agent`, `c1-crm-cross-sell-agent`, `c1-crm-channel-mix-optimiser`, `c1-crm-message-writer`, `c1-crm-send-governor`, `c1-crm-lifecycle-analyst`.
9. **Shop Conversion and Payments** (12 agents): fix the checkout, offers and prices where spend is lost. Agents: `c1-shop-shop-lead`, `c1-shop-funnel-analyst`, `c1-shop-payment-method-sequencer`, `c1-shop-payment-success-monitor`, `c1-shop-delivery-and-id-monitor`, `c1-shop-offer-designer`, `c1-shop-price-refresh-agent`, `c1-shop-merchandiser`, `c1-shop-whatsapp-shop-operator`, `c1-shop-loyalty-economist`, `c1-shop-fraud-and-abuse-flagger`, `c1-shop-support-triage-agent`.
10. **Store and Search Discovery** (11 agents): win app store listings, game-by-country pages and AI answers. Agents: `c1-discover-discovery-lead`, `c1-discover-store-listing-builder`, `c1-discover-listing-experiment-runner`, `c1-discover-review-responder`, `c1-discover-promotional-content-scheduler`, `c1-discover-programmatic-page-builder`, `c1-discover-keyword-opportunity-agent`, `c1-discover-guide-writer`, `c1-discover-site-hygiene-agent`, `c1-discover-ai-visibility-tracker`, `c1-discover-third-party-proof-agent`.
11. **Creators, Community and Esports** (12 agents): turn creators, communities and the Africa Cup into Shop demand. Agents: `c1-community-community-lead`, `c1-community-creator-scout`, `c1-community-creator-brief-writer`, `c1-community-affiliate-ops-agent`, `c1-community-affiliate-integrity-checker`, `c1-community-spark-rights-broker`, `c1-community-tournament-ops-agent`, `c1-community-content-repurposer`, `c1-community-community-moderator`, `c1-community-campus-programme-coordinator`, `c1-community-sponsor-pipeline-agent`, `c1-community-community-analyst`.
12. **B2B Partner Growth** (11 agents): grow the Pay1st, Flow1st and Publishing partner pipeline. Agents: `c1-b2b-partner-lead`, `c1-b2b-account-researcher`, `c1-b2b-payment-gap-modeller`, `c1-b2b-flow1st-prospector`, `c1-b2b-outreach-drafter`, `c1-b2b-case-study-builder`, `c1-b2b-event-pipeline-agent`, `c1-b2b-inbound-lead-router`, `c1-b2b-integration-concierge`, `c1-b2b-co-marketing-planner`, `c1-b2b-partner-health-monitor`.

## Workflows by team

- **Growth Command:** Weekly budget allocation (Monday, after Measurement publishes the blended view); Beat planning (21 days before each calendar beat); Change arbitration (Any write proposal from any team).
- **Measurement and Data Truth:** Daily signal health (06:00 daily); Blended view build (Weekly, and on demand); Incrementality test (Experiment Registrar schedules it).
- **Market and Player Intelligence:** Weekly intelligence brief (Friday); Repricing alert (A currency moves beyond a set band); New-title assessment (Publisher launch or demand spike).
- **Creative Studio:** Weekly creative sprint (Monday plan, or a beat brief); Fatigue replacement (A platform team flags fatigue); Localisation pass (New market or language).
- **Google Ads:** Search waste sweep (Weekly); Campaign launch (Beat brief or new title); Bid strategy change (Readiness check passes).
- **Meta Ads:** Creative refresh (Fatigue flag or weekly batch); WhatsApp purchase switch (Messaging purchase events reach a stable volume); Audience upload (New consent-cleared segment).
- **TikTok Ads:** Spark pipeline (A creator post passes a view or engagement bar); Country launch (The budget plan names a TikTok market); Weekly creative read (Monday).
- **Lifecycle and CRM:** First-to-third purchase journey (First purchase event); Payment recovery (A payment is pending or failed beyond a time limit); Season campaign (Beat brief).
- **Shop Conversion and Payments:** Payment incident (Success rate for a method drops below its normal band); Offer design for a beat (Beat brief); Funnel test (Experiment Registrar slot).
- **Store and Search Discovery:** Review response (New review); Page matrix build (New title, country or method); AI visibility sweep (Monthly).
- **Creators, Community and Esports:** Creator cycle (Monthly, and each beat); Event content pipeline (Each tournament stage); Registration to market map (After each registration window).
- **B2B Partner Growth:** Target account build (Quarterly, or a new-title alert from Intelligence); Partner launch (Signed partner); Proof refresh (Monthly).

## Rules

- Start with Team 2 if tracking, the blended view or identity matching is missing or stale. Scaling spend on bad numbers wastes money.
- Paid media is Google, Meta and TikTok only. Each platform has one writer agent; every account change goes through Growth Command first.
- TikTok plans must pass `c1-tiktok-country-eligibility-guard` before any other TikTok work.
- Brief one to four agents per request. Give each the goal, the data it may read and the output you need.
- Collect every output into one ranked proposal list: what to change, expected effect, evidence, and who approves.
- Nothing is changed, sent or published without a clear yes from the user in chat.
- Label each figure as measured or estimated.
