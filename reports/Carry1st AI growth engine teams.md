# Twelve AI teams power Carry1st's commerce flywheel

Carry1st should build its growth engine as twelve AI teams (139 agent roles) under one orchestrator, organised around a single commercial event: a player's first, second and third purchase on the Carry1st Shop. That choice follows from the business as it stands in November 2026. Carry1st now describes itself as "a commerce platform for Africa and the Middle East", its one senior open growth role is scoped to the Shop with CAC and payback accountability, and web-store evidence shows 97% of revenue comes from repeat buyers ([Carry1st press](https://www.carry1st.com/press/africas-games-market-set-to-outpace-global-growth-in-2026); [Workable job ad](https://jobs.workable.com/jobs/15b713f6-1201-4b17-a6c1-400a1a2f1109.md); [Appcharge](https://appcharge.com/blog/inside-700-m-of-mobile-game-dtc-transactions-2026-report)). The twelve teams are Growth Command, Measurement and Data Truth, Market and Player Intelligence, Creative Studio, Google Ads, Meta Ads, TikTok Ads, Lifecycle and CRM, Shop Conversion and Payments, Store and Search Discovery, Creators Community and Esports, and B2B Partner Growth. Three rules hold them together as one engine: one shared data layer that every agent reads, exactly one write-holding agent per ad platform with every change recorded in a ledger, and a human approving anything that spends money, sends a paid message, changes a price or speaks publicly. The paid channels are Google, Meta and TikTok only, and their constraints are designed in: Google's official agent connector is read-only, Meta's creates entities paused, and TikTok self-serve accounts exist in only five African countries ([Digital Applied](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook); [TikTok Business Help Center](https://ads.tiktok.com/help/article/available-countries-and-regions-for-ad-account-creation-in-bc)). The team names, agent rosters and workflows below are a recommended design, not a description of anything Carry1st runs today; where the research found no public data (Carry1st's revenue, CRM stack, African CPI benchmarks) the report says so and the design avoids depending on it. A count of 139 roles sits at the high-risk end of what the evidence on multi-agent systems supports, so most roles should ship as skills or pipeline steps inside a team lead, and the engine should roll out over 90 days from read-only reporting to gated writes.

## Thin margins and scarce cards make the third purchase the north star

Carry1st has four partner-facing products and one consumer front door. The Carry1st Shop sells direct game top-ups, game gift cards and lifestyle vouchers on web, app and, since 2026, WhatsApp in Nigeria and South Africa; Pay1st is a merchant-of-record payment gateway; Flow1st is a wholesale API for telcos, fintechs and marketplaces that resell game credits; Publishing offers localised creative, user acquisition, live operations and influencer work to global publishers ([shop.carry1st.com](https://shop.carry1st.com/); [carry1st.com/pay1st](https://www.carry1st.com/pay1st); [flow1st.carry1st.com](https://flow1st.carry1st.com/); [carry1st.com/publishing](https://www.carry1st.com/publishing)). Every corporate page ends in a Shop call to action, and Carry1st's own executive describes esports as "the flagship" that feeds Shop, Pay1st and Flow1st ([PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)). The engine therefore treats the Shop as the consumer growth target and the three B2B lines as monetisation layers on the same catalogue and payment rails. A de-emphasis of first-party games looks likely (the Games navigation link is dead and /games returns a 404) but is unconfirmed, so the design keeps app-install capability for the Shop app and partner titles without building a team around owned games ([carry1st.com](https://www.carry1st.com/)).

The core markets are **Nigeria, South Africa, Kenya, Ghana, Egypt and Morocco**, with Algeria and Tunisia named on the Shop and a push into the Gulf visible in hiring and in Flow1st's focus regions ([carry1st.com/pay1st](https://www.carry1st.com/pay1st); [carry1st.com/shop](https://www.carry1st.com/shop)). Carry1st's own published forecast puts Africa at **$1.98bn in games revenue and 406M players in 2026**, led by Egypt ($458.1M), South Africa ($263.0M) and Nigeria ($226.6M), with the Middle East at $6.55bn ([Carry1st press](https://www.carry1st.com/press/africas-games-market-set-to-outpace-global-growth-in-2026)). That works out to roughly $5 of revenue per gamer per year across the continent, which is why install volume is the wrong target: cheap installs prove little when monetisation per player is this low.

Three constraints shape every team. First, payment access rather than willingness to pay limits spend: Carry1st's Guillaume Noe says fewer than 10% of African consumers have access to international credit cards, and credit cards are about 3% of transactions in the region ([PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/); [African Business](https://african.business/2026/05/african-banker/is-africa-leapfrogging-credit-and-debit-cards)). Carry1st's answer is 120+ local methods (its homepage says 200+; the two counts conflict) and merchant-of-record status ([carry1st.com/pay1st](https://www.carry1st.com/pay1st)). Second, margins are thin: discounts visible on the Shop on 14 November 2026 ran from 2% to 8%, so growth has to come from repeat purchase, loyalty points and affiliate reach, not deep promotion ([shop.carry1st.com](https://shop.carry1st.com/)). Third, the Shop cannot count on in-game links. Court-ordered link-out rights apply in the US and no African country appears in the rollout lists found, so traffic must come from outside the game: paid social, search, creators, esports, community and CRM ([PocketGamer.biz](https://www.pocketgamer.biz/google-play-opens-up-third-party-payments-in-the-us-marking-a-turning-point-for-developer-revenue)).

The north-star metric follows directly. Appcharge's analysis of about $700M of web-store volume found that repeat rates exceed roughly 84% after a player's third purchase, so **the share of new buyers who reach a third purchase** is the habit threshold the whole engine optimises, with blended first-purchase CAC and payback as the cost side ([Appcharge](https://appcharge.com/blog/inside-700-m-of-mobile-game-dtc-transactions-2026-report)). That data comes from the US, Europe and Asia, not Africa, so the threshold is a hypothesis to validate on Carry1st's own cohorts. The Head of Growth job ad asks for "one shared view" of acquisition and lifecycle plus incrementality testing, which implies neither exists today; the engine's first deliverable is that view ([Workable job ad](https://jobs.workable.com/jobs/15b713f6-1201-4b17-a6c1-400a1a2f1109.md)). Call of Duty: Mobile is the anchor title across payments, esports, creators and blog output, which makes it both the strongest owned audience and a concentration risk the Intelligence team must track.

## One orchestrator, twelve teams, one writer per ad platform

The architecture is a two-level supervisor hierarchy. An engine-level orchestrator routes requests and triggers to twelve team leads; each lead runs its own agents as an orchestrator-worker fan-out (for analysis) or a sequential pipeline with a critic stage (for creative and messaging). The evidence favours this shape. A Google Research study across 180 configurations found independent multi-agent systems amplified errors about 17.2x against single-agent baselines, while centralised systems held that to about 4.4x ([Google Research](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)). Anthropic reports multi-agent systems use about 15x the tokens of chat and fit "valuable tasks that involve heavy parallelization", not work with many inter-agent dependencies ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)). Two consequences follow. No team hands work sideways to another team for anything that writes to an ad account, a price list or a customer inbox; those proposals go up to Growth Command. And "10 to 12 agents per team" means 10 to 12 defined roles with written contracts, most of them implemented as skills loaded by the team lead, with only a minority running concurrently. Gartner predicts more than 40% of agentic AI projects will be cancelled by the end of 2027 over cost and unclear value, so the design treats agent count as a ceiling on role definitions, not a target for running processes ([Reuters via The Star](https://www.thestar.com.my/tech/tech-news/2025/06/25/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says)).

Every agent carries the same contract: a single responsibility, a trigger, typed inputs with a named source of truth, an output stored as an artifact and passed by reference, a permission scope (read, draft or write), explicit boundaries, an escalation rule and evaluation criteria. Anthropic found that subagents without an objective, output format, tool guidance and task boundaries duplicated each other's work, and the MAST study of 1,600+ traces locates most multi-agent failures in specification, inter-agent misalignment and verification ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system); [arXiv 2503.13657](https://arxiv.org/html/2503.13657v2)). No published mechanism was found for stopping two agents changing the same budget, so the engine builds one from first principles: a single writer per platform, a change ledger, per-entity cool-downs and orchestrator arbitration.

The platform connectors set the write rules. Google's official Ads MCP server (launched 28 April 2026) is read-only, so Google writes go through a custom wrapper on the Google Ads API where spend caps are enforced in code. Meta's official server (open beta from 29 April 2026) is read/write and creates entities paused, which is a ready-made approval gate; its CLI creates entities active by default and must not be used by agents. TikTok's Ads MCP was announced on 13 May 2026 as read/write, but sources conflict on whether it is generally available, so TikTok writes stay human-executed until that is verified ([Digital Applied](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook); [ContentGrip](https://www.contentgrip.com/ad-platform-mcp-rollout/)). The platforms' own automation (Performance Max and App campaigns, Advantage+, Smart+) keeps in-campaign bidding, targeting and creative selection. Custom agents own what the platforms cannot see or will not judge impartially: cross-platform allocation, warehouse-based truth, creative supply, policy pre-checks, lifecycle and commerce.

| # | Team | Mission | Permission scope | Main hand-offs |
|---|------|---------|------------------|----------------|
| 1 | Growth Command | Orchestrate, allocate budget, govern | Approves and arbitrates; no direct platform writes | All teams |
| 2 | Measurement and Data Truth | One shared view of spend, purchases and LTV | Read; writes to warehouse only | Feeds every team |
| 3 | Market and Player Intelligence | Demand, competitor, payment and policy signals | Read; drafts briefs | Creative, Shop, Discovery, B2B |
| 4 | Creative Studio | Volume of distinct, localised, on-policy creative | Draft | Google, Meta, TikTok, Lifecycle, Discovery |
| 5 | Google Ads | Search, PMax, Demand Gen, App campaigns | One writer via API wrapper | Command, Measurement, Creative, Discovery |
| 6 | Meta Ads | Sales, App and click-to-WhatsApp campaigns | One writer, paused by default | Command, Measurement, Creative, Shop |
| 7 | TikTok Ads | Smart+ and Spark Ads in eligible markets | Draft until connector verified | Command, Creative, Creators |
| 8 | Lifecycle and CRM | First-to-third purchase, recovery, win-back | Draft; sends behind consent gate | Shop, Measurement, Creative |
| 9 | Shop Conversion and Payments | Checkout, offers, pricing, WhatsApp Shop | Draft; price and offer changes gated | Lifecycle, paid teams, Intelligence |
| 10 | Store and Search Discovery | ASO, SEO, AI-search visibility, reviews | Draft; public replies gated | Creative, Creators, Shop |
| 11 | Creators, Community and Esports | Affiliates, Africa Cup, Tribe communities | Draft; contracts and payouts gated | TikTok, Creative, Discovery, B2B |
| 12 | B2B Partner Growth | Pay1st, Flow1st and Publishing pipeline | Draft; outreach gated | Intelligence, Creators, Command |

## Twelve teams, 139 agents and their workflows

Each team below lists its agents with a one-line role, then its workflows with trigger, inputs, hand-offs, output and human gate, then its KPIs. Numeric thresholds quoted from platform guidance are starting rules to calibrate on Carry1st's own account data, since no current Africa-specific CPI, CPM or ROAS benchmarks were found in open sources.

### Team 1: Growth Command arbitrates every budget, send and price change

Growth Command is the engine's validation bottleneck and the only place cross-team conflicts are resolved. It owns the beat calendar that the research identifies as the natural coordination device for a regional publisher: partner seasons and battle-pass resets, Africa Cup dates, creator moments, local paydays and holidays ([PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)). The Head of Growth is its human owner.

| Agent | Role |
|-------|------|
| Engine Orchestrator | Routes requests and triggers to team leads and resolves competing proposals before anything is written. |
| Beat Calendar Keeper | Maintains one calendar of game seasons, battle-pass resets, Africa Cup stages, paydays and holidays per country. |
| Budget Allocator | Proposes the weekly spend split across Google, Meta and TikTok by country and title on blended first-purchase CAC and payback. |
| Change Ledger Clerk | Records every proposed and applied change with entity, old value, new value, proposer and approver. |
| Guardrail Sentinel | Enforces spend caps, per-entity edit cool-downs and country-eligibility tables in code, not in prompts. |
| Consent and Privacy Gatekeeper | Blocks any send or audience upload that lacks a valid consent record and keeps the impact-assessment register. |
| Experiment Registrar | Holds the single test backlog, prevents overlapping tests and stores hypotheses and results. |
| Agent Evaluator | Scores agent outputs by end-state checks using an LLM judge plus a human-reviewed sample. |
| Cost Controller | Sets token budgets per team and assigns cheaper models to worker roles. |
| Incident Responder | Pauses, rolls back and writes the post-mortem when a cap, policy or data incident fires. |
| Weekly Readout Writer | Produces one growth readout for the Head of Growth from all team outputs. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Weekly budget allocation | Monday, after Measurement publishes the blended view | Blended CAC, payback, pLTV by country and channel; beat calendar; platform pacing | Allocator proposes; Orchestrator checks ledger and guardrails; approved plan goes to the three platform writers | Signed weekly budget plan | Head of Growth approves every reallocation |
| Beat planning | 21 days before each calendar beat | Calendar entry, last comparable beat's results, stock of offers and creative | Brief fans out to Creative, Shop, Lifecycle, Discovery, Creators and paid teams | One beat brief with owners and dates | Human team leads confirm scope |
| Change arbitration | Any write proposal from any team | Proposal, ledger history, entity locks | Approve, queue or reject back to the proposing lead | Ledger entry and decision | Human approval above set thresholds |

KPIs: blended first-purchase CAC and payback by country; share of new buyers reaching a third purchase; duplicate or conflicting actions; human override and rollback rate; cost per completed task in tokens; incidents (cap breaches, policy rejections).

### Team 2: Measurement and Data Truth builds the one shared view

The job ad's demand for a shared acquisition and lifecycle view with attribution and incrementality is this team's charter. The Shop sells on web, app and WhatsApp, so the team joins three purchase streams to ad spend. Carry1st's site uses Singular deep links and its job ad names AppsFlyer and Adjust as example MMPs; which is in production is not public, and that matters because AppsFlyer has an official MCP server in beta while only community servers were found for Adjust ([carry1st.com](https://www.carry1st.com/); [AppsFlyer support](https://support.appsflyer.com/hc/en-us/articles/36349070304785--Beta-AppsFlyer-MCP)). Android's Privacy Sandbox attribution API was retired in Google's 17 October 2025 announcement, so advertising-ID attribution through an MMP remains the Android default, which suits a market where 92% of surveyed players download from Google Play ([Privacy Sandbox blog](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies); [GeoPoll](https://www.geopoll.com/resources/gaming-africa-report/)).

| Agent | Role |
|-------|------|
| Measurement Lead | Plans the team's work and publishes the weekly blended view to Growth Command. |
| Event Taxonomy Steward | Keeps one event and UTM naming standard across web, app and WhatsApp. |
| MMP Integrity Monitor | Checks install and in-app event flow, link health and app-ID mappings daily. |
| Server-Side Signal Agent | Verifies web purchases reach Meta, Google and TikTok server-side with value, currency and deduplication IDs. |
| Identity Stitcher | Links Shop account, app user and WhatsApp number into one customer record. |
| FX Normaliser | Converts naira, rand, shilling, cedi, pound and dirham purchase values to one reporting currency at dated rates. |
| Blended ROAS Modeller | Computes CAC, payback and contribution margin after payment fees by country, channel and title. |
| pLTV Forecaster | Predicts customer value from early purchase behaviour and exposes it for value bidding. |
| Incrementality Designer | Designs and reads geo holdout tests by country or region. |
| Media Mix Analyst | Maintains a mix model as a sanity check once spend history allows. |
| Anomaly Detector | Flags spend, conversion and payment-success breaks within hours. |
| Platform Reconciler | Compares platform-reported results against warehouse truth and reports the gap. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Daily signal health | 06:00 daily | Event logs, platform diagnostics, MMP data | Faults to the owning platform team and to Shop engineering | Signal scorecard per platform and country | Data owner signs off schema changes |
| Blended view build | Weekly, and on demand | Spend, attributed purchases, FX, fees, pLTV | Published to Command and all team leads by reference | CAC, payback and repeat tables | Finance confirms margin inputs monthly |
| Incrementality test | Experiment Registrar schedules it | Test design, holdout geography, spend plan | Paid teams hold out the region; results back to Budget Allocator | Lift estimate with confidence range | Head of Growth approves holdouts |

KPIs: share of web purchases received server-side with value and currency; identity match rate between Shop and app; gap between platform-reported and warehouse-attributed purchases; number of completed lift tests per quarter. The research found no source on how to post back mobile-money or agent-cash payments as conversions, so that pipeline needs original engineering.

### Team 3: Market and Player Intelligence watches demand, rivals and rules

Global rivals are closing Carry1st's payment-method gap in Nigeria: Xsolla integrated the Paga wallet, bank transfer and agent cash in December 2025, Codashop lists Egypt, Morocco, Kenya, Nigeria and South Africa, and Eneba is expanding into Africa through dLocal ([Xsolla blog](https://xsolla.com/blog/xsolla-paga-integration-nigeria-payments); [Codashop](https://www.codashop.com/international); [dLocal](https://dlocal.com/success-stories/powering-seamless-checkout-for-emerging-market-gamers-eneba-and-dlocal)). This team turns those movements, plus player and policy signals, into briefs other teams act on.

| Agent | Role |
|-------|------|
| Intelligence Lead | Sets the research agenda from Command's questions and publishes the weekly brief. |
| Country Market Analyst | Tracks market size, player counts and spend per player for each core country. |
| Competitor Shop Watcher | Monitors Codashop, Eneba, Razer Gold and web-shop vendors for catalogue, price and payment changes. |
| Price and Bonus Benchmarker | Compares Carry1st's price and bonus per top-up SKU with rivals and in-app prices. |
| Payment Rail Scout | Tracks new wallets, bank rails and card rules per country. |
| Title Demand Ranker | Ranks games by top-up demand using Shop sales, search interest and community chatter. |
| Voice of Customer Miner | Extracts themes from app reviews, support tickets and chat transcripts. |
| Community Listener | Summarises sentiment and questions from Discord, the Facebook group and creator comments. |
| Policy and Regulation Watcher | Tracks store billing rules, ad policies, privacy law and WhatsApp pricing changes. |
| FX and Macro Watcher | Alerts on currency moves that require repricing. |
| Insight Librarian | Stores every finding with date and source so agents cite it by reference. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Weekly intelligence brief | Friday | Competitor scans, voice-of-customer themes, demand ranking | Angles to Creative; price gaps to Shop; rail gaps to B2B | One dated brief | Lead reviews before distribution |
| Repricing alert | Currency moves beyond a set band | FX feed, current price list, margin floor | To Shop's Price Refresh Agent via Command | Repricing recommendation | Commercial lead approves prices |
| New-title assessment | Publisher launch or demand spike | Demand rank, partner status, SKU availability | To Shop Merchandiser, Discovery and B2B | Go or wait recommendation | Partnerships lead decides |

KPIs: time from competitor change to brief; share of creative concepts and offers traceable to a logged insight; forecast accuracy of the title demand rank.

### Team 4: Creative Studio ships distinct concepts sized to each platform's limits

Creative supply is the engine's main lever on paid performance. Meta's retrieval system groups visually similar creatives so they compete with each other, and practitioner guidance converges on 8 to 12 conceptually distinct concepts per campaign with 2 to 3 variations each, refreshed every 2 to 3 weeks; these figures come from vendor sources and need testing on Carry1st's accounts ([Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)). Batch sizes are set by platform limits: 20 images and 20 videos per Google App ad group, and up to 50 assets per TikTok Smart+ asset group ([Admiral Media](https://admiral.media/google-app-campaigns-best-practices/); [TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)). The documented AI gain is throughput and cycle time, with one vendor case cutting concept-to-test from weeks to days; CPI reductions of 30% to 45% appear only in vendor material and are not planning targets ([Segwise](https://segwise.ai/blog/ai-tools-create-ua-ads-mobile-games-apps)). No evidence was found on Pidgin, Arabic, French or Swahili variant performance, so localisation keeps a human or creator reviewer.

| Agent | Role |
|-------|------|
| Creative Lead | Turns beat briefs and insights into a weekly production plan. |
| Concept Strategist | Proposes distinct angles such as local payment proof, delivery speed, price versus in-app and season hype. |
| Hook and Script Writer | Writes openers, scripts and ad copy per concept and platform. |
| Localisation Adapter | Adapts copy and voice for English, Pidgin, Arabic, French and Swahili audiences for human review. |
| Static Producer | Builds image and carousel variants from approved concepts. |
| Video Assembler | Cuts short vertical videos from gameplay, screen recordings and creator footage. |
| Footage Repurposer | Mines Africa Cup, Creators College and affiliate content for ad-ready clips. |
| Similarity Screener | Rejects near-duplicates before upload so concepts do not cannibalise each other. |
| Policy and Brand Checker | Pre-checks every asset against platform policy, partner brand rules and Carry1st's guidelines. |
| Format Packager | Sizes and bundles assets to each platform's limits and naming standard. |
| Creative Analyst | Tags assets and joins them to performance by creative ID across platforms. |
| Fatigue Forecaster | Predicts which live concepts need replacing and when. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Weekly creative sprint | Monday plan, or a beat brief | Insights, last week's creative results, partner asset kits | Concept, script, production, similarity screen, policy check, packaging, then to platform teams | Packaged batches per platform and country | Creative director approves concepts; brand sign-off before release |
| Fatigue replacement | Platform fatigue flag | Asset-level trends | Request back to Concept Strategist; replacement to the flagged platform | Replacement concepts | Same sign-off |
| Localisation pass | New market or language | Winning concepts | Adapter drafts; native reviewer or creator edits | Localised variants | Native-speaker approval |

KPIs: distinct concepts shipped per week; time from brief to live test; share of spend on creative under three weeks old; policy rejection rate; win rate of new concepts against the control.

### Team 5: Google Ads runs web shop search and app campaigns through one writer

Google is two linked systems for Carry1st: Search with AI Max, Performance Max and Demand Gen for the web shop, and App campaigns for the Shop app, joined by Web to App Connect. The Google Ads API added Performance Max channel-level reporting in v23 (28 January 2026) and API-created experiments in v24.1, which widens what agents can read and test ([Google Ads Developer Blog](https://ads-developers.googleblog.com/2026/01/announcing-v23-of-google-ads-api.html?m=1); [ppc.land](https://ppc.land/google-ads-api-v24-1-adds-mobile-segments-passkeys-and-new-experiment-types/)). Two rules need encoding. Target-ROAS bidding needs a budget that allows at least 30 in-app conversions a day, per Google guidance as relayed by practitioners ([Adapty](https://adapty.io/blog/google-app-campaigns-playbook-2025/)). And since 17 August 2026 Google has pulled budget-limited target-based campaigns back to their stated targets, so pacing rules must not leave such campaigns chronically capped ([ppc.land](https://ppc.land/google-ads-gets-promotion-mode-and-a-major-bidding-overhaul-this-august/)). Whether digital top-ups are eligible for Shopping placements in each African market was not verified, and Google Ads does not accept naira as a billing currency, so billing entity and currency are a finance decision made before launch ([Grey](https://grey.co/blog/pay-for-google-ads-in-nigeria)).

| Agent | Role |
|-------|------|
| Google Lead | Plans the Google programme and submits proposals to Growth Command. |
| Search and AI Max Builder | Drafts game-plus-currency search campaigns per country, such as CP, UC and diamonds terms. |
| Keyword and Negative Curator | Mines search-term reports for new keywords and waste. |
| Feed and PMax Agent | Maintains the SKU feed by game, denomination, country and currency and drafts Performance Max asset groups. |
| App Campaign Manager | Drafts install, in-app action and value campaigns for the Shop app. |
| Bid Readiness Checker | Blocks moves to target-based bidding until conversion volume and value data qualify. |
| Demand Gen and Shorts Planner | Drafts video-led Demand Gen and YouTube Shorts activity from Creative Studio batches. |
| Asset Rotation Agent | Replaces low-rated assets using asset reports and top-combination data on traffic sufficiency, not a calendar. |
| Web to App Agent | Keeps deep links and app conversion credit working for web campaigns. |
| Experiment Runner | Sets up API-created experiments registered with Command. |
| Pacing Monitor | Watches budget-limited status and spend against plan. |
| Google Writer | Holds the only Google write scope and applies approved changes through the capped API wrapper. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Search waste sweep | Weekly | Search-term report, blended CAC by keyword theme | Curator proposes; Writer applies after approval | Negative and keyword changes | UA manager approves the batch |
| Campaign launch | Beat brief or new title | Budget plan, creative batch, feed, eligibility check | Draft to Command; Writer creates after approval; Measurement confirms events | Live campaign with ledger entry | Human activates spend |
| Bid strategy change | Readiness check passes | Conversion volume, value quality, mature comparable results | Proposal to Command; Writer applies; 7 to 14 day stabilisation lock | Bid strategy change | UA manager approves |

KPIs: cost per first purchase and payback by country; share of spend on non-converting search terms; impression share on brand-plus-game terms; share of campaigns budget-limited; asset replacement rate.

### Team 6: Meta Ads feeds Advantage+ and click-to-WhatsApp with clean signal

Meta's legacy Advantage+ Shopping and App campaign types can no longer be created or updated through the Marketing API; Advantage+ is now a state of an ordinary Sales, App or Leads campaign with budget, audience and placement automation enabled, and Existing Customer Budget Caps are unavailable in the new structure ([Meta for Developers](https://developers.facebook.com/blog/post/2026/02/13/asc-and-aac-deprecation-mapi-v25/)). Agent effort therefore goes to creative slotting and signal quality, not audience segmentation. Click-to-WhatsApp ads matter here because Carry1st runs a WhatsApp Shop in Nigeria and South Africa, but in-chat sales are invisible to the Pixel and conversation-optimised campaigns find chatters unless purchase events are posted back through the Conversions API for Business Messaging ([Wati](https://www.wati.io/en/blog/track-ctwa-conversions-capi/); [CustomerLabs](https://www.customerlabs.com/blog/why-meta-algorithm-chases-chatters-not-buyers-for-ctwa-ads)). A practitioner report says editing a Meta budget or audience more than about once a day can reset learning, which becomes a one-edit-per-entity-per-day lock ([Digital Applied](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)). No source was found on Meta's catalog-ad or policy treatment of game credits and vouchers, so that needs checking before the Catalog Agent goes live.

| Agent | Role |
|-------|------|
| Meta Lead | Plans the Meta programme and submits proposals to Growth Command. |
| Structure Architect | Keeps one consolidated campaign per objective and country cluster with the three automation levers set. |
| Sales Campaign Manager | Drafts web shop purchase and value-optimised campaigns. |
| App Campaign Manager | Drafts Shop app install and in-app purchase campaigns. |
| WhatsApp Ads Manager | Drafts click-to-WhatsApp campaigns and switches optimisation to purchases once events flow. |
| Catalog Agent | Maintains the product catalog for dynamic top-up and voucher ads, subject to policy confirmation. |
| Creative Slotting Agent | Places Creative Studio batches into ad sets and retires clustered duplicates. |
| Signal Quality Monitor | Uses Meta's dataset diagnostics to check event match, deduplication and value completeness. |
| Audience and Exclusion Agent | Builds consent-cleared buyer exclusions and re-engagement audiences. |
| Learning Guard | Enforces the daily edit lock and minimum conversion volume per ad set. |
| Fatigue Monitor | Flags falling click-through, rising cost per purchase and rising frequency. |
| Meta Writer | Holds the only Meta write scope and creates entities paused for human activation. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Creative refresh | Fatigue flag or weekly batch | Creative batch, asset-level results | Slotting Agent drafts; Writer creates paused ads; Command logs | Refreshed ad sets | Human activates in Ads Manager |
| WhatsApp purchase switch | Messaging purchase events reach a stable volume | Event counts from Measurement and the WhatsApp Shop | Proposal to Command; Writer applies | Optimisation goal change | UA manager approves |
| Audience upload | New consent-cleared segment | Segment from Lifecycle, consent check result | Gatekeeper clears; Writer uploads | Audience in account | Privacy owner approves every upload |

KPIs: cost per first purchase by country; purchases through messaging per click-to-WhatsApp spend; event match and deduplication rates; distinct concepts live per campaign; edits blocked by the learning lock.

### Team 7: TikTok Ads works inside a five-country footprint

TikTok self-serve ad accounts can be created in only **Egypt, Kenya, Morocco, Nigeria and South Africa** among African countries, and available targeting depends on the account's registration country; Ghana, a core Carry1st market, is absent ([TikTok Business Help Center](https://ads.tiktok.com/help/article/available-countries-and-regions-for-ad-account-creation-in-bc); [TikTok Business Help Center](https://ads.tiktok.com/help/article/placements-available-locations)). The team holds that table as a hard guardrail. The upgraded Smart+ flow supports Sales and App Promotion with up to 50 asset groups per campaign, catalog ads alongside standard ads, creative reporting by material ID and built-in Symphony tools for generating, resizing, translating and dubbing ([TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)). A survey of gamers in Egypt, Kenya, Nigeria and South Africa found about 74% use TikTok daily, and African creators are largely excluded from TikTok's payout programmes, which makes paid creator content through Spark Ads a natural supply line ([PocketGamer.biz](https://www.pocketgamer.biz/report-egypt-leads-africas-games-market-with-368m-in-revenue); [OkayAfrica](https://okayafrica.com/tiktok-africa-creator-economy-monetization-exclusion)). TikTok's policy on advertising game credits and vouchers was not found and must be confirmed.

| Agent | Role |
|-------|------|
| TikTok Lead | Plans the TikTok programme and submits proposals to Growth Command. |
| Country Eligibility Guard | Blocks any plan for a country not confirmed in the live account's location list. |
| Smart+ Builder | Drafts Sales and App Promotion campaigns with the chosen level of automation. |
| Asset Group Packager | Organises creative into asset groups with the right URL and product set per group. |
| Spark Ads Coordinator | Requests creator post authorisations and turns organic posts into ads. |
| Symphony Operator | Uses platform tools for resizing, dubbing and variants, routing outputs through the policy check. |
| Trend and Hook Scout | Feeds native trends, sounds and openers to Creative Studio. |
| Events Pipeline Monitor | Checks web events and app events arrive against the right app ID. |
| Placement Controller | Reviews placement mix, including Pangle, and brand-safety settings. |
| Creative Reporter | Reports by material ID to the shared creative taxonomy. |
| TikTok Writer | Holds the only TikTok write scope; prepares change sets a human applies until the connector is verified. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Spark pipeline | Creator post passes a view or engagement bar | Post list from Creators team, authorisation status | Coordinator requests code; Packager adds to asset group; Writer prepares change | Spark ad ready to launch | Human launches; creator consent on file |
| Country launch | Budget plan names a TikTok market | Eligibility table, creative batch, events check | Guard clears; Builder drafts; Command approves | Campaign change set | Human applies and activates |
| Weekly creative read | Monday | Material-ID results | To Creative Analyst and Fatigue Forecaster | Creative ranking | None (read-only) |

KPIs: cost per first purchase in the five eligible markets; share of spend on creator-made content; time from creator post to Spark ad; events pipeline completeness.

### Team 8: Lifecycle and CRM moves buyers from purchase one to purchase three

The job ad lists onboarding, repeat purchase, cross-sell, win-back and re-engagement over push, email, SMS and WhatsApp, and Carry1st's loyalty mechanics supply the hooks: Discount Points are earned on purchases, require sign-in and a verified email to claim, and can part-pay future orders ([Workable job ad](https://jobs.workable.com/jobs/15b713f6-1201-4b17-a6c1-400a1a2f1109.md); [Carry1st press](https://carry1st.com/press/introducing-carry1st-discount-points-your-new-loyalty-system)). WhatsApp has charged per delivered template message since 1 July 2025, with marketing templates costing more than utility ones and reported rates differing sharply by country (sources conflict on the exact figures), so channel choice is an economic decision per country and segment ([Meta developer docs](https://developers.facebook.com/docs/whatsapp/pricing); [Techpoint Africa](https://techpoint.africa/?p=358292)). Consent is a hard gate: South Africa's amended POPIA regulations state that opt-out does not amount to consent for electronic direct marketing, and Nigeria's GAID requires express consent for direct marketing, according to law-firm summaries that should be checked against the statutory texts ([Michalsons](https://www.michalsons.com/blog/popia-amendment-regulations-commence/77824); [Mondaq](https://www.mondaq.com/nigeria/privacy-protection/1700306/gaid-2025-unpacked-series-ii-data-protection-officers-mandatory-consents-and-emerging-technologies)). Carry1st's CRM platform is not public; Braze has an official MCP server, and whether it supports writes was not confirmed ([Braze docs](https://www.braze.com/docs/user_guide/brazeai/mcp_server/)).

| Agent | Role |
|-------|------|
| Lifecycle Lead | Plans journeys against the beat calendar and the third-purchase target. |
| Segment Builder | Maintains segments by purchase count, title, country, payment method and points balance. |
| Onboarding Agent | Drives account creation and email verification at first purchase so points can be claimed. |
| Repeat Purchase Nudger | Times second and third purchase prompts using points balance and usual top-up interval. |
| Season Reminder Agent | Schedules top-up reminders for season starts and battle-pass resets. |
| Payment Recovery Agent | Follows up abandoned bank-transfer and mobile-money payments with utility messages. |
| Win-back Agent | Re-engages lapsed buyers with points or bonus offers. |
| Cross-sell Agent | Recommends adjacent products such as vouchers after a game top-up. |
| Channel Mix Optimiser | Chooses push, email, SMS or WhatsApp per user by cost, consent and response. |
| Message Writer | Drafts templates and copy in the brand voice per language. |
| Send Governor | Applies consent checks, frequency caps and quiet hours before any send. |
| Lifecycle Analyst | Measures every journey against a holdout group. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| First-to-third purchase journey | First purchase event | Customer record, points balance, title, country | Onboarding, then Nudger; offers requested from Shop's Offer Designer | Sequenced messages with holdout | CRM manager approves each new journey and template |
| Payment recovery | Payment pending or failed beyond a time limit | Order state, method, consent | Recovery Agent sends a utility message; unresolved cases to support | Recovered orders | Template pre-approved once; no per-send gate |
| Season campaign | Beat brief | Segment sizes, channel costs, creative | Channel Mix selects; Send Governor clears; Analyst reads | Campaign with cost and lift report | Human approves any paid WhatsApp marketing send |

KPIs: share of first-time buyers reaching purchase two and three within a set window; recovered payment rate; reactivation rate; messaging cost per incremental purchase; opt-out rate; sends blocked for missing consent.

### Team 9: Shop Conversion and Payments fixes the checkout where spend is lost

The Shop's model is direct top-up: the player selects a product, enters an in-game ID, pays and receives currency with no voucher code ([Carry1st press](https://carry1st.com/press/carry1st-teams-up-with-call-of-duty-r-mobile-to-enable-local-payments-across-africa)). The job ad makes "store-to-first-purchase conversion" a named responsibility. Web-shop practice points to web-exclusive value, browsing before login and full local-payment coverage, and warns that a missing local method can effectively close a market ([Xsolla](https://xsolla.com/blog/build-a-better-path-to-direct-to-player-profit); [Stash](https://www.stash.gg/blog/how-to-analyze-and-optimize-your-games-web-shop); [Appcharge](https://appcharge.com/blog/inside-700-m-of-mobile-game-dtc-transactions-2026-report)). In a South African consumer survey, 71% of respondents reported abandoning a purchase after a payment failure, a self-reported figure, not a transaction failure rate ([Stitch](https://stitch.money/blog/report-the-state-of-consumer-payments-in-south-africa)). No Africa-specific web-shop conversion or fraud benchmarks were found, so this team's baselines come from Carry1st's own funnel. Customer support stays hybrid: Klarna rehired human agents in May 2025 after cutting too far, with AI handling routine queries and people handling complex cases ([Tech.co](https://tech.co/news/klarna-reverses-ai-overhaul)).

| Agent | Role |
|-------|------|
| Shop Lead | Prioritises conversion work and coordinates with engineering and commercial owners. |
| Funnel Analyst | Measures drop-off from landing to first purchase by country, device and method. |
| Payment Method Sequencer | Orders checkout methods per country by success rate and cost. |
| Payment Success Monitor | Tracks success and timeout rates per method and provider in near real time. |
| Delivery and ID Monitor | Watches player-ID validation errors and top-up delivery times. |
| Offer Designer | Drafts points multipliers, first-purchase bonuses, third-purchase rewards and season bundles within margin floors. |
| Price Refresh Agent | Proposes local-currency price updates when FX or supplier cost moves. |
| Merchandiser | Arranges storefront categories, banners and deals for each beat and country. |
| WhatsApp Shop Operator | Maintains the chat catalogue and flow and reports chat-to-purchase conversion. |
| Loyalty Economist | Models points cost, liability and effect on repeat rate. |
| Fraud and Abuse Flagger | Flags suspicious order, promo and affiliate patterns to the risk team. |
| Support Triage Agent | Answers routine order questions and routes payment disputes to human agents. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Payment incident | Success rate for a method drops below its normal band | Method-level success data | Sequencer demotes the method; paid teams and Lifecycle notified via Command | Incident note and checkout change proposal | Payments owner approves checkout changes |
| Offer design for a beat | Beat brief | Margin by SKU, past offer results, competitor benchmark | Offer to Lifecycle, Creative and Merchandiser | Offer sheet with margin impact | Commercial lead approves every offer and price |
| Funnel test | Experiment Registrar slot | Funnel data, hypothesis | Variant spec to engineering; result to Registrar | Test result | Product owner approves release |

KPIs: landing-to-first-purchase conversion; payment success rate by method and country; delivery time; contribution margin after fees and points; WhatsApp chat-to-purchase rate; share of support contacts resolved without a human, tracked beside satisfaction on escalated cases.

### Team 10: Store and Search Discovery owns app listings, game-by-country pages and AI answers

Three organic surfaces feed the Shop. On Google Play, up to 50 custom store listings can be tailored by country and linked to App campaign ad groups, and Play Console can now generate keyword-tailored listings with Gemini ([Google Play Console](https://play.google.com/console/about/customstorelistings/); [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)). Ratings are a visible gap: the Shop storefront claims 4.45, while a third-party tracker shows the Android app at 3.81 from 15.7K ratings (capture date not shown), and vendor benchmarks associate review replies with a rating lift of about 0.42 stars ([shop.carry1st.com](https://shop.carry1st.com/); [AppGoblin](https://appgoblin.info/apps/com.carry1st.shop); [AppFollow](https://appfollow.io/blog/gaming-reply-rate-benchmarks-2026)). In search, Codashop reports 90 localised pages in 25 countries and claims 90%+ impression share on key terms, while Carry1st's blog already works as a search channel with about 100 posts between September 2025 and October 2026, published in bursts ([Coda](https://www.coda.co/blog/app-monetization-and-marketing/); [Carry1st blog](https://www.carry1st.com/blog)). In AI search, traffic is still small and engines agree little: one study found the highest domain overlap between any two engines was 17% ([Digital Authority](https://www.digitalauthority.me/?p=88331)). The corporate site also needs repair, with placeholder text on the homepage and careers page and a broken Games link, which costs credibility with B2B visitors ([carry1st.com](https://www.carry1st.com/)). No keyword-volume data for African top-up queries was retrieved, so the page matrix starts from Shop sales and search-term reports.

| Agent | Role |
|-------|------|
| Discovery Lead | Plans listing, content and visibility work against the beat calendar. |
| Store Listing Builder | Drafts country custom listings showing local payment methods, prices and esports imagery. |
| Listing Experiment Runner | Runs store listing tests registered with Command. |
| Review Responder | Drafts replies to app reviews and escalates payment or delivery complaints. |
| Promotional Content Scheduler | Submits in-store events and offers timed to beats. |
| Programmatic Page Builder | Generates game-by-country-by-payment-method pages with live prices, steps and FAQs. |
| Keyword Opportunity Agent | Finds query gaps from search-term data, Search Console and competitor pages. |
| Guide Writer | Drafts game guides, season reviews and esports recaps on a steady cadence. |
| Site Hygiene Agent | Finds broken links, placeholder copy, stale events and inconsistent claims across Carry1st sites. |
| AI Visibility Tracker | Runs a prompt set per engine, country and game and logs where Carry1st is cited. |
| Third-Party Proof Agent | Builds review-site profiles and tracks press and creator mentions that answer engines cite. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Review response | New review | Review text, order lookup, response policy | Routine replies drafted; disputes to Support Triage; themes to Intelligence | Published reply | Human approves any reply on a payment dispute |
| Page matrix build | New title, country or method | SKU and price feed, payment steps, partner status | Page draft to editor; internal links to guides; Google team told of new landing pages | Published page | Editor approves templates and spot-checks pages |
| AI visibility sweep | Monthly | Prompt set, engine responses | Gaps to Guide Writer and Third-Party Proof Agent | Citation scorecard per engine | None (read-only) |

KPIs: store listing conversion by country; app rating and reply rate; non-brand organic sessions and first purchases from organic; ranking coverage of game-plus-currency queries per country; AI citation share per engine; site defects open.

### Team 11: Creators, Community and Esports turns the Africa Cup into Shop demand

Carry1st's esports flagship grew in 2026 to a $30,000 prize pool, two titles and Call of Duty: Mobile entry open to 38 countries, and the company says it does not profit from the event ([PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)). Around it sit an affiliate programme paying up to 10% commission with a $10 minimum payout, a Tribe Discord, more than 50 campus communities and a Creators College in Lagos ([carry1st.com/affiliate-program](https://www.carry1st.com/affiliate-program); [carry1st.com/community](https://www.carry1st.com/community); [Esports Africa News](https://esportsafricanews.com/codm-creators-college-empowering-africas-next-generation-of-gaming-creators/?amp=1)). The team's job is to convert that attention into measurable Shop purchases and reusable content. Follower counts and broadcast viewership were not retrieved, and no measured AI results exist for creator or esports operations, so this team starts with heavier human oversight than the others.

| Agent | Role |
|-------|------|
| Community Lead | Plans creator, community and event activity against the beat calendar. |
| Creator Scout | Finds and scores micro and mid-size gaming creators per country and title. |
| Creator Brief Writer | Drafts monthly content briefs tied to seasons, offers and tournaments. |
| Affiliate Ops Agent | Onboards affiliates, issues links, answers dashboard questions and prepares payout files. |
| Affiliate Integrity Checker | Flags self-referral, coupon leakage and abnormal conversion patterns. |
| Spark Rights Broker | Collects usage rights and ad authorisations and passes cleared posts to TikTok and Creative. |
| Tournament Ops Agent | Handles registration queries, schedules, bracket communications and results posts. |
| Content Repurposer | Turns matches, recaps and creator posts into clips, articles and CRM content. |
| Community Moderator | Answers routine questions in Discord and groups and escalates abuse or payment issues. |
| Campus Programme Coordinator | Supports campus leaders with kits, calendars and reporting. |
| Sponsor Pipeline Agent | Researches and drafts proposals for brand sponsors of events and content. |
| Community Analyst | Attributes purchases to creators and events and maps registrations by country. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Creator cycle | Monthly, and each beat | Scout list, briefs, offers, affiliate results | Briefs out; cleared posts to TikTok Spark and Creative; results to Measurement | Creator content and affiliate sales | Human signs creator agreements and approves payouts |
| Event content pipeline | Each tournament stage | Match footage, results, player stories | Clips to Creative; recaps to Discovery; highlights to Lifecycle | Content pack per stage | Community manager approves public posts |
| Registration to market map | After each registration window | Registration data by country, with consent | Country demand to Intelligence and B2B | Demand map for payment expansion | Privacy owner approves data use |

KPIs: affiliate-attributed first purchases and repeat rate; active affiliates; cost per creator-driven purchase; content pieces reused by other teams; community response time; sponsor revenue against event cost.

### Team 12: B2B Partner Growth sells payments and distribution on consumer proof

Pay1st's visible sales assets are reference partners (Activision, Riot, Supercell, Garena, MPL, Tinder, Nanobit) and two integration paths, a listing on the Shop or a gateway inside the partner's own checkout; the page publishes no conversion-uplift numbers and no pricing ([carry1st.com/pay1st](https://www.carry1st.com/pay1st)). Flow1st targets a second audience, telcos, fintech wallets, super-apps and marketplaces, with volume tiers on its lead form from under $10k to $1M+ a month and focus regions that include MENA and Latin America ([flow1st.carry1st.com](https://flow1st.carry1st.com/)). Telcos already sell gamer data bundles, which makes them partners more than rivals ([The African Mirror](https://theafricanmirror.africa/news/telcos-race-to-win-over-africas-smartphone-gamers/)). This team runs no paid media by default; its inputs are the engine's consumer results, which become its proof. No measured AI results were found for B2B payments sales, and Carry1st's sales tooling and cycle are not public.

| Agent | Role |
|-------|------|
| Partner Lead | Prioritises target accounts across Pay1st, Flow1st and Publishing. |
| Account Researcher | Profiles publishers, subscription apps, telcos and wallets against fit criteria. |
| Payment Gap Modeller | Estimates per title and country the payers a partner cannot reach with card-based billing. |
| Flow1st Prospector | Builds and qualifies reseller targets by region and volume tier. |
| Outreach Drafter | Drafts personalised emails and meeting notes for sales staff to send. |
| Case Study Builder | Turns anonymised engine results into proof points and decks. |
| Event Pipeline Agent | Prepares meeting lists and follow-ups for industry conferences. |
| Inbound Lead Router | Scores and routes form submissions from the Pay1st, Shop and Flow1st pages. |
| Integration Concierge | Answers documentation questions and tracks partners from Shop listing to gateway upgrade. |
| Co-marketing Planner | Packages esports, creator and paid support into partner launch proposals. |
| Partner Health Monitor | Tracks partner volumes and flags expansion or churn risk. |

| Workflow | Trigger | Inputs | Hand-offs | Output | Human gate |
|----------|---------|--------|-----------|--------|------------|
| Target account build | Quarterly, or a new-title alert from Intelligence | Demand rank, partner list, payment-gap model | Researcher and Modeller to Outreach Drafter | Account brief and draft outreach | Sales lead sends all outreach |
| Partner launch | Signed partner | SKU list, countries, launch date | Co-marketing plan to Command, which adds a calendar beat | Launch plan across teams | Partnerships lead and Head of Growth approve |
| Proof refresh | Monthly | Blended results, payment success by method | Case Study Builder to Discovery for site updates | Updated proof points | Legal and partner approval before publishing |

KPIs: qualified pipeline by product; lead response time; pilot-to-gateway conversion; partner volume growth; proof points published.

## A single Call of Duty season shows the hand-offs working as one engine

The connections matter more than the rosters. Take a Call of Duty: Mobile season start, the kind of beat Carry1st already promotes with Double CP offers ([Carry1st blog](https://www.carry1st.com/blog)). Three weeks out, the Beat Calendar Keeper opens the beat and the Orchestrator issues one brief. Intelligence supplies the price and bonus benchmark against rivals and in-app prices. Shop's Offer Designer drafts a points multiplier and a third-purchase reward inside margin floors, and the commercial lead approves it. Creative Studio produces distinct concepts on local payment proof and delivery speed, localised and policy-checked, packaged to each platform's limits. Discovery refreshes the country pages and store listings so they match the ads. Creators brief affiliates and clear posts for Spark Ads. The Budget Allocator proposes the week's split across Google, Meta and TikTok by country, the Head of Growth approves, and each platform's single writer applies its share: Google through the capped API wrapper, Meta as paused entities a human activates, TikTok as a change set a human applies. Lifecycle schedules reminders to consent-cleared segments and holds out a control group. During the beat, Measurement's Anomaly Detector and Shop's Payment Success Monitor watch for breaks; if a bank-transfer provider times out in Nigeria, the Sequencer demotes the method and Command throttles Nigerian spend until it recovers. Afterwards, Measurement publishes blended CAC, payback and progress to purchase three, the Experiment Registrar files what was learned, and B2B turns the result into a proof point for the next publisher conversation.

Two loops run through that sequence. The fast loop is paid and owned media feeding first purchases, checkout and lifecycle converting them to third purchases, and measurement returning value signals to the platforms and to the allocator. The slow loop is consumer scale becoming B2B proof: more buyers and better payment success make Pay1st and Flow1st easier to sell, new partners add catalogue and seasons, and those add beats to the calendar. Carry1st describes its own strategy in the same two parts, growing the player base through esports, communities and creators and growing revenue through commerce and payments ([PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)).

| Shared asset | Owner | Read by |
|--------------|-------|---------|
| Blended view (spend, purchases, pLTV, margin) | Measurement | All teams |
| Beat calendar | Growth Command | All teams |
| Change ledger and entity locks | Growth Command | Platform writers, Shop, Lifecycle |
| Consent record | Growth Command | Lifecycle, Meta, TikTok, Google, Creators |
| Insight library | Intelligence | Creative, Shop, Discovery, B2B |
| Creative library with shared IDs | Creative Studio | Paid teams, Lifecycle, Discovery |
| SKU, price and offer feed | Shop Conversion and Payments | Google, Meta, TikTok, Discovery, Lifecycle |

## Ninety days from read-only reporting to gated writes

The rollout follows the one sourced template: days 1 to 30 read-only reporting, days 31 to 60 write access limited to paused campaigns and test ad sets with human review, days 61 to 90 live budget and bid changes behind approval gates and change caps on a single account, with every action logged ([Digital Applied](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)). That source is a practitioner playbook, not an audited case, and no published rollout of 100+ agents in a growth organisation was found. Teams should come online in order of risk. Measurement, Intelligence and Growth Command's read-only functions go first, because every other team depends on the shared view. Creative Studio and Discovery follow, since their outputs are drafts a human reviews and review replies have the best-documented automation results. Lifecycle drafting and Shop analysis come next. Meta is the first paid team to write, because its paused-by-default behaviour is a built-in gate; TikTok follows once its connector status is verified; Google writes come after the API wrapper and its caps are built. Cross-channel budget allocation goes last. Creators and B2B run as research and drafting assistants throughout.

Governance is tiered by reversibility and money at risk. Reading and drafting are autonomous. Creating paused entities is autonomous. Activation, budget increases, audience uploads, price and offer changes, paid WhatsApp marketing sends, public replies on payment disputes, creator contracts and B2B outreach each need a named human approver. Consent checks and spend caps run in code. Agents that personalise offers per user in Nigeria may fall under GAID's automated decision-making rule, so a data protection impact assessment for the engine as a whole is the prudent default ([Mondaq](https://www.mondaq.com/nigeria/privacy-protection/1700306/gaid-2025-unpacked-series-ii-data-protection-officers-mandatory-consents-and-emerging-technologies)). Each team's evaluation starts with about 20 real cases scored on end state by an LLM judge and a human, the approach Anthropic describes for its own system ([Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)). The humans who remain are the Head of Growth as engine owner, one lead per team as approver and evaluator, an automation engineer for tools and guardrails, a data owner, and creative and brand sign-off. Third-party estimates put Carry1st's headcount at roughly 167 to 181 with a team reported down 22.2% over a year (capture dates not shown), so framing matters: Duolingo's "AI-first" announcement drew a public backlash, and the engine should be presented internally as leverage for a small team ([Built In](https://builtin.com/company/carry1st/jobs); [Dealroom](https://dealroom.co/companies/adg-technology-inc-/); [TechCrunch](https://www.techcrunch.com/2025/08/07/the-backlash-against-duolingo-going-ai-first-didnt-even-matter/)).

Three assumptions deserve a challenge before build. The third-purchase threshold comes from non-African web stores and needs confirming on Carry1st cohorts. The case for many specialised agents is weaker than the case for a few well-equipped ones; McKinsey data quoted by CIO.com says only 37% of companies attribute any positive EBIT impact to their AI programmes, so each team should prove value in its read-only phase before gaining roles ([CIO.com](https://www.cio.com/article/4226418/ai-agents-a-lot-of-effort-but-still-little-return.html)). And the Google, Meta and TikTok restriction leaves Ghana without a TikTok self-serve route and excludes the Snapchat and app-network channels the job ad names, so owned channels and creators carry more weight in Ghana and in any market the three platforms serve poorly.

## Conclusion

The design's main bet is that Carry1st's growth problem is a commerce problem with a payments bottleneck, so the engine spends its intelligence where the platforms are blind: on which payment method fails in which country tonight, which buyer is one nudge from a third purchase, and which creator's post sold top-ups. Bidding and targeting are left to Google, Meta and TikTok, whose own agents now do that work inside their walls. What they cannot do is see a mobile-money timeout, a points balance or an Africa Cup registration, and that first-party view is Carry1st's durable advantage over global rivals who are matching its payment-method count.

The second implication is organisational. Twelve teams and 139 roles describe the work to be covered, not the number of processes to run. The engine earns trust in the order it gains permissions, and its first measurable product is the shared view of acquisition and lifecycle that the company's own job ad says it lacks. If that view shows the third-purchase habit holds in Nigeria and Egypt as it does elsewhere, the rest of the engine has a target worth automating toward; if it does not, the same view will show which threshold should replace it.
