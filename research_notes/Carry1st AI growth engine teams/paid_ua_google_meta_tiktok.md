# Paid UA and paid commerce traffic on Google Ads, Meta Ads and TikTok Ads for a mobile games publisher with a D2C top-up web shop in Africa (Carry1st)

Research date: 14 November 2026. Source-quality note for the report writer: primary sources reached directly were the Android Developers I/O 2026 post, TikTok Business Help Center pages, the Meta developer blog on ASC/AAC deprecation, and Adjust's Gaming App Insights 2026 (via a Substack digest). Most other 2026 detail comes from agency, vendor and trade blogs (ppc.land, Segwise, Admiral Media, Adapty, Playio and similar) reached via search summaries. Those items are marked "(secondary)" and should be verified against platform documentation before they are hard-coded into agent rules. The TikTok Q2 2026 Product Preview page returned HTTP 451 and could not be read.

## Google: App campaigns, Performance Max, Search, Demand Gen, YouTube/Shorts, Web to App Connect, 2025-2026 changes, API and scripts

### Takeaway
Google is run as two linked systems: App campaigns (install, in-app action, value, pre-registration bidding, fed by Firebase/GA4 or MMP events) for the games, and Search/AI Max + Performance Max + Demand Gen for the web shop, joined by Web to App Connect, which by 2026 covers YouTube and Demand Gen as well as Search, Shopping and PMax (secondary). The agent-automatable surface widened materially in 2026: Google Ads API v23-v26 added PMax channel-level reporting, target-less App bidding goals, an App top-asset-combination view, product-level reporting for App/Demand Gen/Video, and API-created experiments.

### Cited Findings

App campaigns: structure, bidding, budgets
- App campaign types "cover installs, engagement and pre-registration"; install bidding options are Target CPI and Maximize conversions; Target CPA is used for a selected in-app action (secondary, page reviewed 20 Sept 2026) — [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- Google's recommended bid-to-budget ratios: about 50x the bid for Target CPI and pre-registration campaigns, 10x for App-campaigns-for-installs Target CPA, 15x for App-campaigns-for-engagement Target CPA; allow 7-14 days to stabilise after significant changes (secondary) — [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- tROAS is for acquiring high-value users at a set target; daily budget should allow at least 30 unique in-app conversions per day (per Google guidance as relayed in search summary) — [Google Accelerate "The Apps Four"](https://business.google.com/us/accelerate/resources/articles/the-apps-four/); [Adapty playbook](https://adapty.io/blog/google-app-campaigns-playbook-2025/)
- tROAS requires verified values and measurement sources; "30 days of tracking alone" is not a sufficient readiness test; set the initial target from mature results of a comparable campaign; moving to tROAS before stable deep-conversion data can stall the campaign in learning (secondary) — [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- App campaigns for installs support up to 20 images and 20 videos per ad group; asset reports rate assets Low/Good/Best; near-duplicate assets are not a testing strategy; do not rotate assets on a fixed 7-day deadline, wait for adequate traffic (secondary) — [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- Standard App campaigns offer no manual keyword targeting; a separate Search campaign is needed for keyword control (secondary) — [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- Google Ads API release notes: new App campaign bidding goals without a target CPA or ROAS were added (optimise for installs or total value); `Campaign.view_through_conversion_optimization_enabled` (default false) enables view-through-conversion optimisation for Demand Gen and App campaigns (v24, April 2026); a read-only `AppTopCombinationView` exposes top-performing asset combinations in App campaigns (per search summary of release notes) — [Google Ads API release notes](https://developers.google.com/google-ads/api/docs/release-notes)

Smart Bidding change, 17 August 2026
- From 17 August 2026 Google changed target-based Smart Bidding (tCPA, tROAS) for campaigns that were budget-limited in the last 12 months, pulling them back to their stated targets; Google warned of temporary performance and traffic fluctuation; a "promotion mode" was introduced in the same overhaul (secondary; exact mechanics not confirmed) — [ppc.land](https://ppc.land/google-ads-gets-promotion-mode-and-a-major-bidding-overhaul-this-august/); [ppc.land](https://ppc.land/google-ads-forces-some-cpas-to-double-starting-august-17/); [TechWyse](https://www.techwyse.com/news/platform-updates/google-smart-bidding-august-2026-update-clarification)

Web to App Connect and iOS measurement (ODM)
- Web to App Connect expanded from Search, Shopping and PMax (GML 2025) to YouTube, Hotel Ads and Demand Gen; Search and Shopping campaigns can now be credited with new app installs and in-app conversions (secondary) — [Adapty playbook](https://adapty.io/blog/google-app-campaigns-playbook-2025/); [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- App Connect is a measurement and deep-link setup for web campaigns; it does not convert a web campaign into an App campaign (secondary) — [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- On-device conversion measurement (ODM) for iOS requires a recent Firebase SDK (Google's Accelerate article names 12.12.1 as minimum, per search summary); Google also expanded web-to-app acquisition measurement for iOS and extended Maximize Conversions for iOS — [Google Accelerate](https://business.google.com/us/accelerate/resources/articles/the-apps-four/); [ppc.land](https://ppc.land/google-launches-enhanced-measurement-tools-for-ios-app-campaigns/); [Search Engine Journal](https://www.searchenginejournal.com/google-expands-ios-app-marketing-capabilities/553914/)
- ODM is also available via MMP integrations, e.g. Adjust iOS SDK 5.4.1 with an ODM plugin (secondary) — [ppc.land](https://ppc.land/google-launches-enhanced-measurement-tools-for-ios-app-campaigns/)

AI Max for Search, Performance Max, Demand Gen (web shop side)
- AI Max for Search became globally available (2025) and has its own reporting, including campaign-level and ad-level asset reports — [Google Ads Help](https://support.google.com/google-ads/answer/16470459?hl=en-GB); [Search Engine Roundtable](https://www.seroundtable.com/google-ads-ai-max-more-40087.html)
- PMax channel-level reporting was added to the Google Ads API in v23 (28 January 2026), for dates from 1 June 2025 onward — [Google Ads Developer Blog](https://ads-developers.googleblog.com/2026/01/announcing-v23-of-google-ads-api.html?m=1); [Search Engine Land](https://searchengineland.com/google-ads-api-v23-kicks-off-faster-releases-for-2026-468104); [ppc.land](https://ppc.land/google-finally-lets-developers-see-where-performance-max-ads-actually-run/)
- PMax asset reporting gained impressions, clicks and cost in 2025, and conversion volume/value alongside performance labels afterwards (secondary for the latter) — [Google 2025 Ads recap](https://business.google.com/us/accelerate/resources/announcements/2025-google-ads-recap/); [Swipe Insight](https://web.swipeinsight.app/posts/google-ads-expands-performance-max-reporting-with-new-asset-and-channel-features-19812)
- From 15 June 2026, product-level cost and conversion metrics return for Video, Demand Gen and App campaigns linked to Merchant Center feeds, not only Shopping and PMax (secondary) — [ppc.land](https://ppc.land/google-ads-api-to-expand-product-reporting-for-all-campaign-types-on-june-15/)
- Some PMax advertisers can switch off Search partners and Display (secondary) — [ppc.land](https://ppc.land/google-lets-some-pmax-advertisers-switch-off-search-partners-and-display/)
- PMax gender exclusions were enabled via the API in v24 (secondary) — [ppc.land](https://ppc.land/google-ads-api-v24-cart-data-sales-view-lead-gen-conversions-retail-filters/)
- Demand Gen: API v23 added surface-specific conversion-rate suggestions (e.g. Gmail, YouTube Shorts); v24.1 added static image uploads for Display serving within Demand Gen; in v26 new Demand Gen video responsive ads default to opted-in for asset automation (earlier versions default to opted-out) (per search summary of release notes) — [Google Ads API release notes](https://developers.google.com/google-ads/api/docs/release-notes)

Google Ads API cadence and experiments
- v23 launched 28 January 2026 and started a faster release cadence; v24 on 22 April 2026, v24.1 on 13 May, v24.2 on 24 June; v26 dated 14 October 2026 (adds Search-lift metrics, secondary) — [Search Engine Land](https://searchengineland.com/google-ads-api-v23-kicks-off-faster-releases-for-2026-468104); [Google Ads API release notes](https://developers.google.com/google-ads/api/docs/release-notes); [ppc.land](https://ppc.land/google-ads-api-v26-adds-15-search-lift-metrics-to-measure-ad-driven-searches/)
- v24.1 supports AI Max experiments, Video experiments, Demand Gen experiments and PMax experiments via the API (secondary) — [ppc.land](https://ppc.land/google-ads-api-v24-1-adds-mobile-segments-passkeys-and-new-experiment-types/)

Google Play (I/O 2026, 19 May 2026, primary)
- Clicking a keyword recommendation on the Play Console Grow overview page makes Gemini create a custom store listing tailored to that keyword, deployable in one click — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)
- Play Console can pre-populate localized store listings from an uploaded CSV/Google Sheet using Gemini models — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)
- New Play Console reporting: a "reach" metric, indirect store-listing value, traffic-source breakdowns with downstream engagement/retention/monetisation, and cart conversion rate — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)
- Play Games Sidekick (in-game overlay with AI game tips, rewards, achievements) debuted in 100+ titles, expands to all participating titles in summer 2026; enabling it satisfies a core Level Up program guideline — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)
- Engage SDK surfaces reach 30M+ MAU, extend to 80+ Play markets, and from June 2026 show content on store listings to existing users — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)
- Play Shorts (portrait short-video feed in the store) is rolling out to US users and select developers; app discovery inside the Gemini app was announced — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)
- "Agentic catalog management" for one-time products (bulk price changes, SKU import, metadata) announced as coming soon — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)
- October 2026 follow-up: the You tab has 250M+ MAU and the unified gaming platform connects 700M+ gamer profiles — [Android Developers](https://developer.android.com/blog/posts/google-play-discovery-engagement-growth)
- Up to 50 custom store listings per app; custom listings can be built for pre-registration and for win-back of inactive users — [Google Play Console](https://play.google.com/console/about/customstorelistings/)
- Custom store listing targeting is expanding to buyer states (non-buyers, one-time, repeat, lapsed buyers), testable via experiments for select developers; the You tab carries Play Points, quests and streaks (secondary) — [AppTweak](https://www.apptweak.com/en/aso-blog/google-playtime-2025); [AppTweak ASO news](https://www.apptweak.com/aso-blog/app-store-optimization-news-app-store-updates)
- Store listing experiments: run at least 7 days; one default-graphics experiment or up to five localized experiments at once; up to 3 variants plus control (secondary) — [AppScreens](https://appscreens.com/blog/google-play-store-listing-experiments)
- Google Play published "Expanded billing choice and lower fees" (24 June 2026) and a "new era for choice and openness" business-model post (March 2026) — [Android Developers](https://developer.android.com/blog/posts/expanded-billing-choice-and-lower-fees-on-google-play)

### Inferences
- An agent team for Google needs separate roles for (1) App campaign bid/budget and event-readiness checks (30 conversions/day gate before tROAS, bid-to-budget ratios), (2) asset rotation using asset reports and AppTopCombinationView, (3) web-shop Search/AI Max/PMax with channel-level and product-level reporting, and (4) a Play Console/ASO role for custom store listings and listing experiments mapped to ad groups.
- For a top-up shop, the product-level reporting change (June 2026) makes a Merchant Center feed of top-up SKUs (game x denomination x country/currency) worth maintaining, since Demand Gen and App campaigns can now report by product. Whether digital vouchers/game credits are eligible for Shopping in each African market was not verified.
- Because the 17 August 2026 Smart Bidding change affects budget-limited target-based campaigns, automated budget pacing rules should avoid leaving tCPA/tROAS campaigns chronically budget-capped.
- Android dominates African device share, so ODM/iOS items are lower priority for Carry1st than GA4/Firebase or MMP event quality on Android (inference; device-share data not sourced here).

### Gaps
- No source reached on Google Ads scripts changes in 2026 or on what scripts can and cannot do for App campaigns; verify in Google Ads scripts documentation.
- No primary confirmation of pre-registration campaign mechanics in 2026, Play Points promotion mechanics for advertisers, or Play Games promotions pricing/eligibility in African markets.
- YouTube/Shorts-specific guidance for games (formats, Shorts-only controls in Demand Gen) was not retrieved beyond surface-level conversion-rate suggestions.
- AI Max for Search 2026 feature changes (beyond reporting) were not confirmed from a primary source.
- Firebase SDK minimum for ODM (12.12.1) is from a search summary of Google's page; verify.
- Details of Google Play's 2026 fee and external-payment programme, and whether it applies in African countries, were not read.

## Meta: Advantage+ app and sales campaigns, value optimisation, AEM, Conversions API, catalog ads, click-to-WhatsApp, Andromeda/GEM creative diversification, Marketing API

### Takeaway
By late 2026 the legacy Advantage+ Shopping (ASC) and Advantage+ App (AAC) campaign types are gone from the API; "Advantage+" is now a state of any Sales/App/Leads campaign in which three automation levers (budget, audience, placements) are enabled. Performance is driven mainly by creative diversity under the Andromeda retrieval system and GEM ranking model plus clean server-side signal (Conversions API with dedup and value); practitioner guidance converges on fewer, consolidated ad sets holding many conceptually distinct creatives.

### Cited Findings

Campaign structure and API deprecations
- Meta announced the unified Advantage+ campaign structure on 29 May 2025; Advantage+ status derives from three levers: Advantage+ campaign budget, Advantage+ audience and Advantage+ placements, all of which must be enabled (secondary) — [ppc.land](https://ppc.land/meta-launches-unified-api-structure-for-advantage-campaigns/)
- Marketing API v25.0: ASC and AAC campaigns can no longer be created or updated via the API; applies to all API versions by 19 May 2026. v26.0 (estimated September 2026): all remaining ASC and AAC campaigns are paused. Affected endpoints: `POST /{campaign-id}` and `POST /{campaign-id}/copies`. App, Sales and Leads campaigns default to the Advantage+ setup under "Automation Unification" — [Meta for Developers blog, Feb 2026](https://developers.facebook.com/blog/post/2026/02/13/asc-and-aac-deprecation-mapi-v25/)
- Existing Customer Budget Caps are not available in the new Advantage+ campaigns; campaigns using them stayed editable until v26.0 and must be replicated (manual duplication, API replication, or a one-time managed bulk migration); each duplication creates a new campaign ID — [Meta for Developers blog](https://developers.facebook.com/blog/post/2026/02/13/asc-and-aac-deprecation-mapi-v25/)
- ASC campaigns could be migrated with an optional `migrate_to_advantage_plus` field; AAC campaigns cannot be copied (secondary) — [ppc.land](https://ppc.land/meta-deprecates-legacy-campaign-apis-for-advantage-structure/); earlier notice: [Meta for Developers blog, Oct 2025](https://developers.facebook.com/blog/post/2025/10/08/upcoming-asc-and-aac-mapi-deprecation-migration-options-to-advantage-plus/)
- v26.0 also requires an explicit `advantage_audience` flag for Housing/Employment/Financial special-ad-category campaigns using targeting automation, applying to all versions on 27 October 2026 (per search summary) — [Meta Marketing API changelog v26.0](https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog/version26.0)
- Source conflict: the v24.0 changelog is summarised as already blocking ASC/AAC creation, duplication and updates, while the developer blog places that at v25.0 — [v24.0 changelog](https://developers.facebook.com/documentation/ads-commerce/marketing-api/marketing-api-changelog/version24.0); contradicted by [Meta for Developers blog](https://developers.facebook.com/blog/post/2026/02/13/asc-and-aac-deprecation-mapi-v25/)

Andromeda, GEM and creative volume
- Andromeda is Meta's ads retrieval engine (engineering post dated 2 December 2024; global rollout reportedly complete by October 2025); GEM (Generative Ads Recommendation Model) is the ranking foundation model, credited with up to 5% conversion lift on Instagram (secondary, citing Meta Engineering and Search Engine Land) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- Sources disagree on GEM's role: most describe it as a ranking model; some describe it as generating creative variations, and one says it is in limited rollout — [Moburst](https://www.moburst.com/blog/meta-advantage-andromeda-lattice-and-gem-explained/); [Wallaroo Media](https://wallaroomedia.com/meta-gem-algorithm/)
- Andromeda groups visually/conceptually similar creatives under one "Entity ID" so they compete with each other instead of extending reach; changing copy on the same hero image does not avoid this (secondary) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- Ads Manager shows a Creative Similarity Score; third parties claim scores above 60% trigger retrieval suppression and recommend staying below 40% (secondary, unverified with Meta) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- Recommended structure: one campaign per conversion objective; 8-12 conceptually distinct concepts per campaign with 2-3 variations each; broad targeting with exclusions; roughly 50 conversion events per week as the stability heuristic; small separate campaign for structural tests (secondary) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- One ad set with 25 diverse creatives beat five ad sets of five by 17% on conversions and 16% on cost (Logical Position test, via secondary) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- Meta's Advantage+ app campaigns guidance reportedly recommends up to 50 creatives and puts "creative diversification and differentiation" first (secondary) — [Moburst](https://www.moburst.com/blog/meta-advantage-andromeda-lattice-and-gem-explained/)
- Fatigue windows reportedly shortened from 6+ weeks to 2-3 weeks; refresh every 2-3 weeks; fatigue flags: CTR down >10% week on week, CPA up >15%, prospecting frequency >3.0, falling spend share; teams spending over $5K/month need 5-15 new creatives per week; brands testing 20+ new ads per month reportedly see 65% higher ROAS than those testing under 10 (all secondary, vendor-cited) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- "22% ROAS lift" for Advantage+ creative versus manual is a Meta internal-testing figure relayed by secondary sites; treat as directional — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)

Signals: AEM, Conversions API, value optimisation
- Meta's June 2025 update removed the need to configure and rank eight web conversion events; the AEM tab in Events Manager was removed; domain verification/conversion-domain selection and Value Sets for value optimisation are no longer required; AEM itself continues and "will continue to evolve" — [Jon Loomer](https://www.jonloomer.com/meta-announces-big-changes-to-website-conversion-campaigns/); [Jon Loomer](https://www.jonloomer.com/qvt/aggregated-event-measurement-isnt-going-away/)
- AEM extends to App promotion campaigns; an update rolling out from 10 June (year not stated in snippet) changed how AEM data is shared with MMPs; events sent via Conversions API may also be processed under AEM limits — [Adjust](https://www.adjust.com/blog/meta-adjust-aem/?utm_channel=0); [Adjust on Advanced Mobile Measurement](https://www.adjust.com/blog/meta-advanced-mobile-measurement/)
- Recommended signal hygiene: Conversions API alongside the Pixel, deduplicated by a shared `event_id`, with purchase value and currency; value-maximising bids; conservative cost caps loosened over time (secondary) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- One 2026 post states view-through attribution windows were removed, making event priority decisive (single secondary source, unverified) — [Two Owls](https://twoowls.io/blogs/meta-attribution-window-changes/)

Click-to-WhatsApp (CTWA)
- Meta optimises CTWA campaigns on conversions reported back; in-chat sales are invisible to the Pixel and need the Conversions API for Business Messaging; rule of thumb is to optimise for conversations until real purchase events flow, then switch to purchase optimisation (secondary) — [Wati](https://www.wati.io/en/blog/track-ctwa-conversions-capi/); [Kanal](https://getkanal.com/blog/click-to-whatsapp-ads-guide-2026)
- A Meta-published case reports 3.9x more purchases for CTWA ads optimised for "purchases through messaging" versus conversation optimisation (single non-African advertiser, per search summary) — [WhatsApp Business](https://whatsappbusiness.com/?p=5256)
- Risk: conversation-optimised CTWA finds "chatters, not buyers" unless downstream purchase events are returned (secondary) — [CustomerLabs](https://www.customerlabs.com/blog/why-meta-algorithm-chases-chatters-not-buyers-for-ctwa-ads)
- WhatsApp per-message pricing by category and country reportedly changed on 1 October 2026 (vendor blog, unverified) — [Kanal](https://getkanal.com/blog/click-to-whatsapp-ads-guide-2026)

### Inferences
- Agent design for Meta should centre on a creative pipeline (concept generation, similarity screening before upload, weekly refresh) and a signal-quality monitor (CAPI dedup, value/currency completeness, event match), with little effort spent on audience segmentation.
- Any automation written against ASC/AAC objects is dead code as of v26.0; agents must create ordinary Sales/App campaigns and set the three Advantage+ levers, and must not rely on Existing Customer Budget Caps.
- For the web shop, purchase value in local currency (NGN, KES, ZAR, EGP and others) must be sent consistently to enable value optimisation; FX normalisation is an agent task (inference).
- CTWA is a plausible assisted-checkout channel for top-ups where card penetration is low, but only if order events from the WhatsApp flow are posted back via the business-messaging Conversions API.

### Gaps
- No primary Meta documentation reached on Advantage+ app campaign limits in 2026 (ad set and creative caps, country grouping), app value optimisation requirements (minimum purchase volumes), or app events via Conversions API versus SDK/MMP.
- No 2026 source reached on Advantage+ catalog ads for digital goods (top-ups/gift cards) or on Meta policy for selling game credits and vouchers.
- No Africa-specific Meta performance data (CPM, CPI, ROAS) found.
- Exact fields for creating Advantage+ campaigns via the API were not on the page read; see Meta developer docs.
- Rate limits, ad-creation limits and generative creative endpoints in the Marketing API were not researched.
- The view-through attribution removal claim needs confirmation from Meta.

## TikTok: Smart+, App Promotion, Spark Ads, Pangle, Symphony, Events API, TikTok One, playables, and African availability

### Takeaway
TikTok's 2026 "upgraded Smart+" merges manual and automated campaign creation into one flow with module-level automation (budget, targeting, placement, creative) across Traffic, Sales, Lead Generation and App Promotion, with Symphony generative tools embedded. Self-serve ad accounts can be created in only five African countries (Egypt, Kenya, Morocco, Nigeria, South Africa), and targeting options depend on the account's registration country, which is the main structural constraint for a pan-African advertiser.

### Cited Findings

Smart+ (primary: TikTok Business Help Center, page dated October 2026)
- Upgraded Smart+ merges the manual and Smart+ flows; a campaign can be fully automated, partially automated or fully manual; supported objectives are Traffic, Sales, Lead Generation and App Promotion; the page notes the feature may not yet be available to all accounts — [TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)
- Budget: automatic campaign budget across ad groups (all ad groups must then share budget and bid strategy) or custom per-ad-group budgets — [TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)
- Targeting: audience controls or manual targeting, with more options and enforceable settings; placement is automatic by default but specific placements and brand-safety settings can be chosen — [TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)
- Limits: up to 50 asset groups per campaign; each ad is an asset group with its own URL, product set and up to 50 creative assets; multiple destination URLs; creative-level reporting grouped by material ID; Catalog Ads can be added at ad level alongside non-catalog ads — [TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)
- Symphony automation in Smart+: "Recommended Creatives" generates new assets; "Automatic Enhancements" resizes, improves quality, translates and dubs; simplified Spark Ads setup at ad level — [TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)
- Selectable placements include TikTok, Lemon8 and Global App Bundle (which includes CapCut and Pangle apps); Smart+ automatic placement can be overridden at setup; Music Autofix is available for Smart+ App campaigns (Q2 2026 Product Preview, via search summary; page itself unreadable) — [TikTok Product Preview](https://ads.tiktok.com/business/en/blog/tiktok-product-preview); [TikTok blog on Smart+](https://ads.tiktok.com/business/en/blog/smart-plus-ai-performance-solution)
- TikTok announced new automation updates for advertisers on 7 October 2025 — [TikTok Newsroom](https://newsroom.tiktok.com/tiktok-announces-new-automation-updates-for-advertisers-ca?lang=en-CA)
- Symphony also works standalone to produce assets for manual campaigns, organic posts or export (secondary) — [Dataslayer](https://www.dataslayer.ai/blog/tiktok-smart-symphony-2026)

Events API and app measurement
- Events API is a server-to-server integration for app, web and CRM events; app measurement runs through an MMP, the App Events SDK or the App Events API, all keyed to a TikTok App ID (June 2026 guidance); TikTok's April 2026 standard-events page lists 20 standard events; incomplete App ID/MMP mapping is the usual cause of missing app events (secondary) — [The Ad Spend](https://theadspend.com/blog/tiktok-conversion-tracking); [Stape](https://stape.io/blog/tiktok-server-side-tracking); [WeltPixel](https://weltpixel.com/blogs/magento/tiktok-events-api-on-magento-2-server-side-setup-and-the-event-name-churn)

African availability and restrictions (primary)
- Self-serve ad account creation in Business Center is available in Egypt, Kenya, Morocco, Nigeria and South Africa (the only African countries listed); Middle East entries include Iraq, Israel, Kuwait, Oman, Qatar, Saudi Arabia and UAE; page last updated November 2025 — [TikTok Business Help Center](https://ads.tiktok.com/help/article/available-countries-and-regions-for-ad-account-creation-in-bc)
- Available location-targeting options depend on the country/region used to register the Ads Manager account; if a country is not listed, TikTok may be unavailable there or unable to deliver ads (page last updated June 2025) — [TikTok Business Help Center](https://ads.tiktok.com/help/article/placements-available-locations)
- Pangle's Middle East and Africa location list includes Egypt, Kenya, Nigeria and South Africa (per search summary) — [TikTok Business Help Center](https://ads.tiktok.com/help/article/available-locations-for-pangle-ads)
- Older third-party material says Nigerian advertisers may need to work through a registered TikTok agency and describes VPN workarounds; this conflicts with the current official list and should be treated as outdated, and workarounds risk account action — [Tabcut](https://tabcut.com/blog/post/how-to-run-tiktok-ads-in-nigeria-tiktok-ads-tutorial-2024); contradicted by [TikTok Business Help Center](https://ads.tiktok.com/help/article/available-countries-and-regions-for-ad-account-creation-in-bc)

### Inferences
- A TikTok agent team should hold a country-eligibility table as a hard guardrail: confirmed markets are Egypt, Kenya, Morocco, Nigeria and South Africa; other Carry1st markets (e.g. Ghana, Francophone West Africa, Tanzania, Uganda) must be checked inside the live account's location list before planning.
- Smart+ limits (50 asset groups x 50 assets) define the batch size for creative agents; material-ID reporting gives the join key for creative analytics.
- With app measurement via MMP and web-shop purchases via Events API, two separate event pipelines must be monitored; one Smart+ Sales campaign can mix catalog and non-catalog ads for top-up SKUs.

### Gaps
- No source reached for TikTok One (creator marketplace) 2026 mechanics, Spark Ads authorisation flows in 2026, playable/interactive format specs, or Pangle performance for gaming.
- The per-country targeting matrix is behind a dropdown on TikTok's page and could not be extracted; which African countries can be targeted from, say, a South Africa- or UK-registered account is unconfirmed.
- No source on TikTok ad policy for selling game credits, vouchers or gift cards, or on local restrictions (gambling-adjacent content, age rules) in African markets.
- Bidding options for App Promotion in Smart+ (value-based optimisation, ROAS bidding, minimum event volumes) were not on the page read.
- TikTok Marketing API capabilities and limits for automation were not researched.
- Deprecation dates for legacy Smart Performance Campaigns/App campaigns were not found.

## Measurement: MMPs, SKAN/AdAttributionKit, Android Privacy Sandbox, incrementality, MMM, LTV/pLTV, web-to-app and web-shop attribution

### Takeaway
Android Privacy Sandbox is effectively dead: Google announced on 17 October 2025 that it is retiring the Attribution Reporting API on Chrome and Android (plus Topics and Protected Audience), so GAID-based deterministic attribution through an MMP remains the Android default, which suits an Android-heavy African footprint. The harder problem for Carry1st is the web shop: store-reported revenue understates true ROAS, so web purchases must be joined to app users (player ID login, MMP web SDK/links, server-side events to each ad platform) and validated with incrementality tests and MMM.

### Cited Findings
- Google's "Update on Plans for Privacy Sandbox Technologies" (17 October 2025, Anthony Chavez) retires the Attribution Reporting API for Chrome and Android citing low adoption; Topics and Protected Audience were retired in the same announcement; no sunset dates were given; Google will contribute to an interoperable Attribution standard at the W3C — [Privacy Sandbox blog](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies); [Search Engine Land](https://searchengineland.com/google-officially-shuts-down-privacy-sandbox-463561); [AdExchanger](https://www.adexchanger.com/privacy/google-pulls-the-plug-on-topics-paapi-and-other-major-privacy-sandbox-apis-as-the-cma-says-cheerio/); [Singular](https://www.singular.net/blog/rip-privacy-sandbox/)
- The advertising ID remains the basis of Android attribution and Google has offered no replacement (secondary, August 2026) — [Playio](https://blog.playio.co/privacy-sandbox-shutdown-android-game-marketing); contradicted by older pieces still predicting phased GAID nulling during 2026 — [Linkrunner](https://linkrunner.io/glossary/what-is-privacy-sandbox)
- ATT opt-in for gaming apps moved from 38% (Q1 2025) to 39% (Q1 2026) globally; sports 54%, action 50%, arcade 46% — [Adjust Gaming App Insights 2026 via GameDev Reports](https://gamedevreports.substack.com/p/adjust-gaming-app-insights-report)
- Median paid-to-organic install ratio for games rose from 2.07 to 3.33 (2024 to 2025), i.e. growing dependence on paid UA — [Adjust via GameDev Reports](https://gamedevreports.substack.com/p/adjust-gaming-app-insights-report)
- D2C channels including web shops generate about $17B a year, roughly 15% of the $113.3B mobile IAP market (2026 survey, secondary); 72% of top-grossing mobile games run a web store (Appcharge/Sensor Tower, secondary) — [Playio](https://blog.playio.co/mobile-game-web-shop-strategy); [GameDev.net](https://gamedev.net/news/3316-mobile-gaming-has-a-new-and-growing-measurement-problem-opinion/)
- Standard gross ROAS compares ad spend with store-reported revenue and omits web-shop revenue; the web-to-app journey break is described as an attribution "black hole" (secondary) — [AppSamurai](https://appsamurai.com/blog/web-to-app-funnels-d2c-storefronts-mobile-game-ua/)
- MMP tooling for web: tracked links with parameters matched to installs; web SDK/tracking script captures pre-install activity; Singular offers attribution forwarding and a Web Link Generator to unify UTM taxonomy across web and mobile — [Singular](https://www.singular.net/blog/web-measurement/); [Airbridge](https://www.airbridge.io/en/blog/why-data-is-gamings-new-superpower)
- Routing rule: send existing app users to the app and non-app users to mobile web — [Awin](https://resources.awin.com/tracking/app-attribution-en/)
- The main web-shop constraint is traffic, not technology or payments: players are in the game, the shop is outside it (secondary) — [Playio](https://blog.playio.co/mobile-game-web-shop-strategy)
- Through late 2025 and 2026 Google Play began permitting external payments and links for US users (secondary) — [Playio](https://blog.playio.co/mobile-game-web-shop-strategy)
- A 2025 playbook recommends blending incrementality tests, MMM sanity checks and consistent event taxonomies for UA planning (secondary) — [RocketShip HQ](https://www.rocketshiphq.com/?p=5538)
- Validate scaling decisions with holdout/lift tests and gate on 30/60/90-day retention and repeat purchase (secondary) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- Google Ads API v26 (October 2026) adds Search-lift metrics, and v24.1 adds API-created experiments, i.e. incrementality-style measurement is increasingly API-accessible (secondary) — [ppc.land](https://ppc.land/google-ads-api-v26-adds-15-search-lift-metrics-to-measure-ad-driven-searches/)

### Inferences
- Recommended stack for Carry1st: MMP (deterministic GAID on Android; SKAN/AAK only for the small iOS share) for app installs and in-app revenue; first-party server-side purchase events from the web shop sent to Google (enhanced conversions/Web to App Connect), Meta (CAPI) and TikTok (Events API); a shared player ID linking shop accounts to app users so blended ROAS = (IAP + web-shop revenue) / spend.
- The web shop sells third-party game credits and vouchers as well as top-ups for own titles, so it should be measured as an e-commerce business in its own right (new-customer CAC, repeat rate, contribution margin after payment fees), separate from game-UA ROAS.
- pLTV models should emit a predicted-value event early (D0-D3) for value bidding on all three platforms; this is common practice but no 2026 source was retrieved to cite specifics.
- Incrementality (geo holdouts by country/region) is practical in Africa because markets are discrete and budgets are small; MMM needs enough history and spend variation per country to be reliable (inference).

### Gaps
- No 2026 primary source reached on SKAdNetwork versus AdAttributionKit status (versions, re-engagement, adoption by Meta/Google/TikTok).
- No source reached comparing AppsFlyer, Adjust and Singular features for web-shop/D2C attribution specifically, or their pLTV products.
- No gaming-specific 2026 guidance found on MMM tools (Meridian, Robyn, vendor MMM) or on platform lift-study minimums in African markets.
- No source on payment-method attribution issues specific to Africa (mobile money, carrier billing, agent/offline payments) and how to post those back as conversions.

## Creative: formats, testing cadence, localisation and AI generation

### Takeaway
Video dominates game creative volume, playables and UGC outperform on install efficiency, and AI-generated variations are now a large and rising share of shipped creative, which raises the premium on conceptually distinct ideas because Meta's retrieval clusters near-duplicates. Cadence guidance converges on continuous weekly production with 2-3 week refresh cycles; evidence on African-language localisation (Pidgin, Arabic, French, Swahili) was not found.

### Cited Findings
- Video accounts for over 80% of global game ad creatives (SocialPeta, February 2026) — [SocialPeta](https://socialpeta.com/blog/Top-Mobile-Game-Ad-Creatives-and-Advertising-Trends-in-February-2026)
- Playables: 4.8 IPM versus 2.9 for video (attributed to Liftoff 2026, secondary); Liftoff's 2025 index is cited as showing playable impression-to-install rates 8x (top spenders) to 16x (others) higher than non-playables; the two figures are not consistent with each other — [Game Growth Advisor](https://gamegrowthadvisor.com/blog/2026-05-12-mobile-game-ad-creative-strategy-2026/); [Segwise](https://segwise.ai/blog/ai-game-marketing-ua-statistics-2026)
- Optimised UGC ads reportedly achieve 20% lower CPI than standard video; authentic UGC outperforms AI-faked influencer content (secondary) — [Martechvibe](https://martechvibe.com/article/ai-ugc-and-playables-reshape-mobile-ad-creative-strategies); [Game Growth Advisor](https://gamegrowthadvisor.com/blog/2026-05-12-mobile-game-ad-creative-strategy-2026/)
- AI-generated variations were roughly 20-25% of shipped creatives in 2025 and are expected to exceed 50% by end of 2026; top game advertisers ship 2,400-2,600 creative variations per quarter; AppsFlyer's framing is that AI is flooding channels and raising the cost of standing out (secondary) — [Segwise](https://segwise.ai/blog/ai-game-marketing-ua-statistics-2026)
- Average creative lifespan has dropped under 5 days in mature markets (single secondary source) — [Game Growth Advisor](https://gamegrowthadvisor.com/blog/2026-05-12-mobile-game-ad-creative-strategy-2026/)
- Meta: 8-12 distinct concepts per campaign with 2-3 variations; refresh every 2-3 weeks; near-identical creatives are clustered and compete with each other (secondary) — [Segwise](https://segwise.ai/blog/meta-andromeda-update-creative-strategy-2026)
- Google App campaigns: up to 20 images and 20 videos per ad group; show the benefit or product experience early in video; distinct messages and formats; replace assets on traffic sufficiency, not a calendar (secondary) — [Admiral Media](https://admiral.media/google-app-campaigns-best-practices/)
- TikTok Smart+: up to 50 creative assets per asset group; Symphony can generate recommended creatives and automatically resize, translate and dub assets — [TikTok Business Help Center](https://ads.tiktok.com/help/article/about-updates-to-smart-plus)
- Google Play: Gemini-assisted listing localisation from a structured file and keyword-tailored custom store listings, allowing store pages to mirror ad concepts — [Android Developers](https://developer.android.com/blog/posts/i-o-2026-what-s-new-in-google-play)

### Inferences
- A creative agent workflow should separate concept ideation (few, distinct angles) from variation production (AI-assisted resizing, dubbing, hook swaps), with a similarity check before upload to Meta and per-platform batch sizes (Google 20+20, Meta up to about 50, TikTok 50 per asset group).
- TikTok Symphony's translate/dub feature is the only platform-native localisation tool surfaced here; whether it supports Nigerian Pidgin, Swahili, Hausa or Arabic dialects is unverified, so human or creator-led localisation should be assumed for those languages.
- For the top-up shop, likely concepts are price/bonus comparisons versus in-app purchase, local payment-method proof (mobile money), speed-of-delivery demos and creator "how I top up" UGC; this is inference from general UGC findings, not sourced evidence.
- Creative lifespans in low-CPM African markets are probably longer than the "under 5 days" mature-market figure because frequency builds more slowly at small budgets (inference).

### Gaps
- No sourced evidence on performance of Pidgin, Arabic, French or Swahili localised variants, or on African creator-led creative benchmarks.
- No source on creative formats for top-up/voucher shops specifically.
- Liftoff, Sensor Tower and AppsFlyer 2026 creative reports were referenced by secondary sources but not read directly.
- Playable specifications and availability on Meta and TikTok in 2026 were not confirmed.
- Low-bandwidth/low-end-device creative constraints (file size, video length) for African audiences were not researched.

## Benchmarks: CPI, CPM, ROAS, retention and payer conversion for tier-3 / African markets

### Takeaway
No current, reliable Africa-specific paid UA benchmarks were found; the best available proxies are Adjust's 2025 regional figures (LATAM CPI $0.14 as the lowest-cost region; global CPI $0.56, CPM $4.34, D1 retention 27%) and dated 2021 Africa data (CPI around $0.04; paying-player share 32-43% by Newzoo survey). Carry1st's own account data should be treated as the benchmark source, with these numbers only as sanity bounds.

### Cited Findings
- Adjust Gaming App Insights 2026 (data January 2024 to January 2026; Africa not broken out): global gaming CPI $0.56 (+30% YoY); LATAM CPI $0.14 (+40%); Europe $0.53 (+47%); North America $1.68 (+31%); slots $4.47, idle RPG $3.19, strategy $1.03 — [Adjust via GameDev Reports](https://gamedevreports.substack.com/p/adjust-gaming-app-insights-report)
- Average gaming CPM rose from $3.63 to $4.34 (+20%); North America $15.98; LATAM and MENA CPMs each fell 3%; CPC $0.04 globally — [Adjust via GameDev Reports](https://gamedevreports.substack.com/p/adjust-gaming-app-insights-report)
- Gaming IPM 8.62 overall (racing 16.2, casino 5.13); IPM fell in Europe, LATAM, MENA and North America and grew in APAC — [Adjust via GameDev Reports](https://gamedevreports.substack.com/p/adjust-gaming-app-insights-report)
- MENA: installs +2%, sessions +7%, average session length 30.88 minutes (+3%) in 2025 — [Adjust via GameDev Reports](https://gamedevreports.substack.com/p/adjust-gaming-app-insights-report); press release: [Business Wire](https://www.businesswire.com/news/home/20260310424022/en/)
- D1 retention across all gaming apps was 27% in 2025 (Adjust) — [Adjust via GameDev Reports](https://gamedevreports.substack.com/p/adjust-gaming-app-insights-report)
- GameAnalytics 2026 benchmarks (secondary coverage): median global D1 about 22%, median D7 just under 4%; top-decile D7 about 11-12%; regional D30 medians: Oceania 1.39%, North America 1.18%, Europe 0.92%, Asia 0.53% (Asia D7 2.68%); Africa not broken out — [GameDev Reports](https://gamedevreports.substack.com/p/gameanalytics-mobile-and-pc-game); [InvestGame PDF](https://investgame.net/wp-content/uploads/2026/01/2026-01-20-Mobile_retention_benchmarks_2026.pdf)
- Conflict between sources: Playio gives median D1 about 26% and a "good" profile of 35/15/5 (D1/D7/D30), versus GameAnalytics' median D1 of about 22% — [Playio](https://blog.playio.co/d1-d7-d30-retention-benchmarks-2026); contradicted by [GameDev Reports](https://gamedevreports.substack.com/p/gameanalytics-mobile-and-pc-game)
- Mobile game CPI ranges from $0.08 to $60 depending on genre, platform and region (secondary) — [Playio](https://blog.playio.co/mobile-game-cpi-benchmarks-2026)
- Africa (2021 data): highest CPIs for sport and RPG titles around $0.04; ARPDAU roughly $0.10-$0.26 for sport, strategy and RPG; racing and sports ARPPU around $20 — [PocketGamer.biz](https://www.pocketgamer.biz/africas-gaming-market-how-to-make-a-profit-with-f2p-games)
- Share of players who pay for games (Newzoo survey, 2021): South Africa 43%, Ghana and Ethiopia 33%, Kenya and Nigeria 32% (survey-reported, not in-app payer conversion) — [PocketGamer.biz](https://www.pocketgamer.biz/95-per-cent-of-gamers-in-africa-choose-mobile-says-newzoo)
- Market size: South Africa is the largest African games market, projected to grow from $266M (2023) to $333M (2026); Nigeria's mobile revenues grew fivefold since 2019; about 90% of Nigeria's 46.5M gamers play on mobile; Egypt is reported as leading with $368M in one report (sources differ on country ranking) — [PocketGamer.biz](https://www.pocketgamer.biz/mobile-growth-drives-africas-games-industry-to-1-billion-in-revenue); [PocketGamer.biz](https://www.pocketgamer.biz/report-egypt-leads-africas-games-market-with-368m-in-revenue); [KPMG/Maliyo Africa Games Industry Report 2025](https://assets.kpmg.com/content/dam/kpmg/ng/pdf/2025/02/2025%20Africa%20Games%20Industry%20Report.pdf)
- AppsFlyer publishes Q3 2026 gaming benchmarks (paid-cohort retention by genre, platform and country) but no figures were retrievable — [AppsFlyer](https://www.appsflyer.com/?p=549948)

### Inferences
- African CPIs are probably at or below LATAM's $0.14 for casual genres, but with rising trend (global +30% YoY) and much lower ARPU, so payback depends on payer conversion and payment success more than on CPI.
- Because cheap installs make CPI a weak signal, agents should optimise to cost per first purchase / D7 ROAS including web-shop revenue, and report by country since South Africa, Nigeria, Kenya and Egypt differ sharply in monetisation.
- Survey "share who pay" (32-43%) is not comparable to in-app payer conversion, which is typically low single digits; do not use the survey figure as a conversion target.

### Gaps
- No 2025-2026 country-level CPI, CPM, ROAS or payer-conversion benchmarks for Nigeria, Kenya, South Africa, Egypt, Ghana or Morocco were found on any of the three platforms.
- No D7/D30 retention benchmarks for African cohorts; Adjust and GameAnalytics do not break out Africa in the material reached.
- No benchmarks for top-up/voucher web-shop conversion rate, AOV, CAC or repeat purchase in emerging markets.
- AppsFlyer's country-filterable benchmarks and the full Adjust PDF were not accessible; they are the best next sources. Sensor Tower, Liftoff and Moloco reports were not reached.
