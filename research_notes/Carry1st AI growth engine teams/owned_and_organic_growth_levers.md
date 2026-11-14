# Owned and organic growth levers for Carry1st (non-paid): lifecycle, web shop, live ops, ASO, SEO/AI search, creators/community/esports, B2B, localisation

Research date: 14 November 2026. Method note: most findings come from search-result summaries plus four full-page fetches (Carry1st Pay1st page, Carry1st Discount Points press page, Appcharge January 2026 report page, PocketGamer.biz interview of 27 October 2026). Where a figure came from a search summary and I could not confirm which of the returned URLs carries it, the bullet says "URL attribution unverified". Vendor-reported numbers are flagged as such.

## 1. Lifecycle/CRM: channels, platforms and flows for player and shopper retention in Africa

### Takeaway
There is no published Africa-specific gaming CRM case study from Braze, CleverTap, MoEngage or OneSignal; the usable evidence is (a) Carry1st's own owned-account and loyalty mechanics (signed-in account, verified email, Discount Points, Gems), (b) WhatsApp per-message pricing by African country since July 2025, and (c) Indian real-money/casual gaming case studies on CleverTap and MoEngage that are the closest emerging-market analogues. Web-store data shows repeat purchase is the whole game (97% of web-store revenue from repeat buyers), so first-to-third purchase flows deserve the most automation.

### Cited Findings
- Carry1st Shop loyalty is "Carry1st Discount Points", a cashback-style scheme: points are earned on Shop purchases made with a registered payment method (e-wallets, bank transfers, cards, direct carrier billing, cash-based methods), "at least 100 points for any purchase", the cart shows maximum points before purchase, points have local-currency value, can part-pay or fully pay, and cannot be transferred. Claiming requires sign-in and a verified email. Launch markets: Nigeria, South Africa, Kenya, Egypt, Morocco, Ivory Coast. Page is undated. — [Carry1st press](https://carry1st.com/press/introducing-carry1st-discount-points-your-new-loyalty-system)
- Carry1st distinguishes Gems (a purchasable, transferable payment method) from Points (non-transferable loyalty); Points can be combined with any other payment method including Gems; earning rates are shown at checkout. Undated. — [Carry1st Terms and Conditions](https://carry1st.com/terms-and-conditions); [Carry1st Discount Points page](https://shop.carry1st.com/carry1st-discount-points)
- WhatsApp Business Platform moved from conversation-based to per-message pricing on 1 July 2025; businesses pay per delivered template message by category, and marketing templates cost considerably more than utility templates. — [Meta developer docs](https://developers.facebook.com/docs/whatsapp/pricing)
- Reported marketing-message rates: Nigeria about $0.062 (N84), Kenya about $0.0248 (KSh 3.3), South Africa reported as $0.62 (R10.0, looks anomalous and should be checked against Meta's rate card) per Techpoint (2025); another table gives $0.0516 Nigeria and $0.0225 Kenya, and Business Daily Africa cites $0.0225 for Kenya. Sources conflict; rates vary by date and tier. — [Techpoint Africa](https://techpoint.africa/?p=358292); contradicted in part by [Business Daily Africa](https://www.businessdailyafrica.com/bd/markets/market-news/meta-sets-whatsapp-messaging-charges-5573670)
- CleverTap gaming cases (India, vendor-reported, undated in results): WinZO reports roughly 40% higher retention from real-time personalisation; Mobile Premier League uses CleverTap for onboarding journeys in the first-seven-day retention window and fast push. — [WinZO case](https://www.casestudies.com/company/clevertap/case-study/how-winzo-acts-on-real-time-data-insights-to-revolutionize-mobile-gaming); [MPL case](https://clevertap.com/case-study/how-mobile-premier-league-boosts-engagement-through-ultra-fast-push-notifications-and-more/)
- MoEngage gaming case (India, vendor-reported): Classic Rummy reports 24% retention improvement and a 3x increase in total payment value within six months. — [MoEngage/casestudies.com](https://www.casestudies.com/company/moengage/case-study/classic-rummy-boosts-player-retention-by-24-with-moengage)
- CleverTap and MoEngage both send WhatsApp through WhatsApp Business API providers; CleverTap also offers its own BSP function (per a WhatsApp API vendor blog, 2025). — [Heltar](https://www.heltar.com/blogs/clevertap-vs-moengage-which-is-better-for-you-in-2025-cmi5wzlt6001ui9tuupk30ijo)
- Pushwoosh markets "WhatsApp for gaming" with claimed 60-90% open rates; this is vendor marketing, not independent evidence. — [Pushwoosh](https://www.pushwoosh.com/ar/products/whatsapp-for-gaming/)
- Appcharge (15 January 2026, about $700M annual DTC volume, US/Europe/Asia, not Africa): 97% of web-store revenue came from repeat buyers; repeat rates exceed roughly 84% after a player's third web-store purchase; recommendation is to plan lifecycle around the third purchase and to build owned distribution outside the app. — [Appcharge](https://appcharge.com/blog/inside-700-m-of-mobile-game-dtc-transactions-2026-report)
- Appcharge coverage lists email, community platforms and VIP programmes as web-store engagement channels, without quantified results. — [PocketGamer.biz](https://www.pocketgamer.biz/appcharge-us-web-store-purchases-are-3x-higher-on-average-than-payment-links)
- Braze: no gaming-specific case study with measured uplift was found. Forrester TEI figures commissioned by Braze are composite (for example $76.7M cross-sell gains) and the AI decisioning spotlight interviewed media, financial services, travel and CPG, not games. — [Forrester TEI for Braze](https://tei.forrester.com/go/braze/aidecisioningspotlight/); [BrazeAI Decisioning Studio](https://braze.com/product/brazeai-decisioning-studio)

### Inferences
- Flow priority for the Shop, derived from the repeat-buyer data: (1) account creation and email verification at first purchase (already required to claim Points), (2) second- and third-purchase nudges using Points balance, (3) top-up reminders timed to CODM season and battle-pass resets, (4) payment-failure recovery (bank transfer and mobile-money timeouts), (5) win-back with points-expiry or bonus offers.
- Channel economics differ sharply by country: WhatsApp marketing templates are cheap in Kenya relative to Nigeria, so a per-country channel-mix rule (WhatsApp utility templates for order status and payment recovery everywhere; marketing templates only for high-value segments in Nigeria) is a natural agent decision.
- Utility-category WhatsApp templates (delivery confirmation, failed payment) are the low-cost, high-relevance entry point; marketing templates should be reserved for segments with proven repeat value.
- Braze, CleverTap and MoEngage are functionally interchangeable for these flows; the Indian RMG cases suggest CleverTap/MoEngage have more emerging-market gaming references. Klaviyo is e-commerce oriented and fits the Shop email/SMS side rather than in-game messaging.

### Gaps
- Which CRM/engagement platform Carry1st actually uses: not found.
- No Africa-specific benchmarks for push opt-in, email deliverability, SMS or Telegram/Discord CRM performance in gaming were found.
- No published data on payment-failure recovery rates for mobile money or bank transfer in top-up stores.
- Whether Carry1st runs a referral programme: no evidence found; treat as unverified.
- Points expiry rules and exact earn rates are not published on the pages read.

## 2. Web shop / D2C best practices (Xsolla, Appcharge, Stash, Codashop models), checkout, fraud, and post-ruling deep links

### Takeaway
By 2025-2026 the web shop is a mainstream, LiveOps-run product: D2C is estimated at about $17bn (roughly 15% of mobile IAP), 72% of top-grossing games run one, and revenue is almost entirely repeat. The consistent playbook is web-exclusive value (bonus currency, exclusive items, loyalty), browsing without login, personalised offers, and full local-payment coverage. US steering rulings against Apple (April 2025) and Google (October 2025) legalised in-app links to web stores in the US only; they do not directly change rules in African markets.

### Cited Findings
- Appcharge and GDC survey estimate mobile-game D2C at $17bn in 2025, about 15% of a $113.3bn IAP market (survey median applied to Newzoo's estimate, not a direct measurement). — [PocketGamer.biz](https://www.pocketgamer.biz/report-mobile-game-d2c-revenues-reach-17bn-as-publishers-push-beyond-app-stores/); critique in [PocketGamer.biz](https://www.pocketgamer.biz/the-truth-behind-mobile-gamings-17bn-d2c-market/)
- 72% of top-grossing mobile games run a web store (Appcharge/Sensor Tower data cited in coverage; URL attribution unverified). — [PocketGamer.biz D2C tag](https://www.pocketgamer.biz/tags/direct-to-consumer)
- A top-performing web store reaches about 30% of a game's revenue; Stash projects 50% of in-app revenue moving to owned channels over the next few years (vendor opinion, January 2025). — [Stash](https://www.stash.gg/blog/singular-growth-materminds-podcast-jan-2025)
- Appcharge (15 January 2026): US web-store average purchase value is 3x that of payment links; 56% of US payment-link users were new to D2C; about 25% of payment-link buyers later make a first web-store purchase; adding payment links raised total D2C revenue over 30 days without web-store decline. Recommended model: payment links as acquisition layer, web store as repeat-value layer, run like LiveOps. — [Appcharge](https://appcharge.com/blog/inside-700-m-of-mobile-game-dtc-transactions-2026-report)
- Payment-method lesson from the same report: in the US, cards plus Apple Pay and Google Pay drive about 75% of web-store revenue; in Europe no method exceeds 30% and missing local methods can effectively close a market. — [Appcharge](https://appcharge.com/blog/inside-700-m-of-mobile-game-dtc-transactions-2026-report)
- Omdia/FastSpring survey: 75% of companies with a web shop say D2C's revenue share grew in the last 12 months. — [GameDev Reports](https://gamedevreports.substack.com/p/omdia-and-fastspring-d2c-game-monetization)
- Xsolla guidance (drawn from 600+ web-shop launches): the shop must offer unique value unavailable in-game (deals, rewards, mechanics); promote via compliant in-game and out-of-game channels and LiveOps retention mechanics; do not move game news to the shop just to force traffic. — [Xsolla](https://xsolla.com/blog/build-a-better-path-to-direct-to-player-profit); [Xsolla tips](https://xsolla.com/blog/ecommerce-best-practices-for-gamers)
- Xsolla-sponsored claim: offerwall integration for non-payers drove 5% web-shop revenue growth and a 37% lift in payment transactions (vendor figure). — [GamesBeat](https://gamesbeat.com/?p=309580)
- Appcharge design playbook: differentiate web offers from the in-game store and surface personalised deals based on play habits, progress and profile. — [Appcharge](https://appcharge.com/blog/the-mobile-game-web-store-designers-playbook)
- Stash: communicate clearly the extra value of web versus in-game and let users browse offers before logging in. — [Stash](https://www.stash.gg/blog/how-to-analyze-and-optimize-your-games-web-shop); seamless login and offer visibility also stressed by [Neon](https://www.neonpay.com/blog/optimize-your-game-s-webshop-to-boost-conversion-seamless-login-offer-visibility)
- Carry1st Shop model (Codashop-like direct top-up): player selects product, enters in-game UID, pays, and receives COD Points or Battle Pass directly with no voucher or PIN. — [Carry1st press](https://carry1st.com/press/carry1st-teams-up-with-call-of-duty-r-mobile-to-enable-local-payments-across-africa)
- Pay1st bundles "120+ local payment methods" across South Africa, Nigeria, Kenya, Egypt, Morocco and Ghana ("and more"); Carry1st acts as Merchant of Record handling compliance, tax, FX and risk so partners collect in USD. — [Carry1st Pay1st](https://www.carry1st.com/pay1st)
- Local method examples: bank transfer in Nigeria, M-Pesa in Kenya, mobile money in Ghana; mobile money, crypto and bank transfers on the Shop. — [The Fintech Times](https://thefintechtimes.com/carry1st-becomes-one-stop-digital-essentials-shop-for-consumers-across-africa/)
- Fewer than 10% of African consumers have access to international credit cards, per Carry1st's Guillaume Noe (27 October 2026); he argues payment access, not willingness to pay, constrains spend. — [PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)
- Epic v. Apple, 30 April 2025: Judge Gonzalez Rogers found Apple in wilful violation of the 2021 anti-steering injunction, including over its 27% commission on linked-out purchases; Apple updated US App Store guidelines in May 2025 to allow external links. — [MacRumors](https://www.macrumors.com/2025/04/30/apple-app-store-anti-steering-injunction-violation); [Neon explainer](https://www.neonpay.com/blog/making-sense-of-the-april-30th-2025-epic-v-apple-ruling)
- December 2025: Apple won back the right in principle to charge some commission on linked-out purchases, though the court regarded 27% as prohibitive (secondary report; verify against the ruling). — [9to5Mac](https://9to5mac.com/2025/12/11/apple-defeats-ban-on-charging-commission-on-linked-out-purchases-from-ios-apps/)
- Epic v. Google: after the US Supreme Court declined to pause the injunction, Google announced on 29 October 2025 that US developers may use alternative payments and external links and may price lower off Play Billing; changes are US-only, and Google may still apply UX and safety review. Later dates and the fee regime conflict across sources (a December 2025 programme launch, a pending settlement hearing in 2026, and fee reporting tied to a July 2026 notice). — [Google Play Console Help](https://support.google.com/googleplay/android-developer/answer/15582165?hl=en); [PocketGamer.biz](https://www.pocketgamer.biz/google-play-opens-up-third-party-payments-in-the-us-marking-a-turning-point-for-developer-revenue); [Stash](https://www.stash.gg/blog/a-new-era-for-android-monetization-how-to-launch-compliant-link-out-payments)

### Inferences
- For Africa the binding constraint is payment reach rather than store commission; Carry1st's edge is local methods plus Merchant-of-Record, so checkout optimisation should focus on method ordering by country, timeout/abandonment handling for bank transfer and mobile-money push prompts, and UID validation before payment.
- The steering rulings are US-specific; in-game deep links to the Shop in African markets remain governed by each publisher's store agreements. Out-of-game traffic (search, creators, esports, CRM, community) is therefore the dependable acquisition path for the Shop.
- Offer design that maps to existing Carry1st mechanics: web-only bonus (Points multipliers), first-purchase bonus, third-purchase milestone reward, season-start bundles, and Gems gifting as a social loop.
- Appcharge's "third purchase" habit threshold is a ready-made KPI for an agent team (share of buyers reaching purchase three within N days).

### Gaps
- No Africa-specific web-shop benchmarks (conversion rate, AOV, repeat rate) were found.
- No published fraud-control detail for Pay1st or top-up stores (UID fraud, mobile-money reversal, voucher resale); the Pay1st page only says Carry1st manages "risk".
- No quantified loyalty-programme results from any vendor.
- Current status and fee level of Google's and Apple's US link-out regimes is unsettled; needs legal confirmation.
- Bonus-versus-in-app price differentials actually offered on Carry1st Shop were not captured.

## 3. Live ops and monetisation: calendars, regional pricing, localised offers, battle passes, segmentation, coordination with marketing

### Takeaway
LiveOps intensity keeps rising (top games averaged 89 events a month in 2025) and 2026 commentary points to templatised events, finer personalisation and AI replacing static segments. Carry1st states that localised live ops and community experiences are a planned growth pillar, but as a regional publisher it mostly layers local beats (esports, creator moments, Shop promotions) on top of partners' global calendars.

### Cited Findings
- The top 130 mobile games increased average monthly LiveOps events by 18% to 89 in 2025 (AppMagic data cited by Google). — [Google Think: Bravestars](https://business.google.com/us/think/ai-excellence/bravestars-games-app-marketing-liveops/)
- 2026 LiveOps trends per PocketGamer.biz: templatisation, personalisation and AI; Balancy's CEO expects static segmentation to give way to more personalised approaches. — [PocketGamer.biz](https://www.pocketgamer.biz/2026-live-ops-trends-templatisation-personalisation-and-ai)
- Appcharge (January 2026): D2C behaviour "mirrors LiveOps, not traditional e-commerce"; web stores should combine merchandising mechanics with go-to-market playbooks. — [Appcharge](https://appcharge.com/blog/inside-700-m-of-mobile-game-dtc-transactions-2026-report)
- Carry1st strategy (27 October 2026): two parts, growing the player base via on-the-ground esports, communities, creators and brand partnerships, and growing revenue via commerce and payments; it plans localised live ops and community experiences that give players more meaningful ways to spend. — [PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)
- Africa market context cited in the same interview: $1.77bn revenue and 369.66m players in 2025; Newzoo forecast of 406m players and $1.98bn in 2026; revenue growth (+11.9%) outpacing player growth (+9.9%). — [PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)
- Battle Passes and COD Points are sold directly on Carry1st Shop, so season resets are natural Shop beats. — [Carry1st press](https://carry1st.com/press/carry1st-teams-up-with-call-of-duty-r-mobile-to-enable-local-payments-across-africa)
- Older evidence of personalised offers: Hill Climb Racing 2 reported +52% true LTV uplift from personalised LiveOps offers (2019 deck, dated). — [SlideShare](https://de.slideshare.net/GameCamp/live-ops-in-mobile-gaming-how-to-do-it-right)
- CleverTap positions LiveOps tooling for gaming (Big Fish, MobilityWare) but the results returned no metrics. — [CleverTap](https://clevertap.com/blog/liveops-capabilities-gaming-big-fish/)

### Inferences
- A workable coordination model for a regional publisher: a single beat calendar merging (a) partner global seasons and battle-pass resets, (b) Africa Cup qualifier and finals dates, (c) creator programme moments, (d) local paydays and holidays, with Shop offers, CRM sends, store promotional content and community posts keyed to each beat.
- Payer segmentation for the Shop can be built from purchase count (0, 1, 2, 3+), given the third-purchase habit finding, rather than from in-game telemetry Carry1st may not own.
- Regional pricing in practice means local-currency price points and payment-method-specific bundles; FX volatility (for example naira) makes price refresh a recurring automation task.

### Gaps
- No public detail on Carry1st's regional pricing policy, localised in-game events, or how much LiveOps control it has under Activision/Tencent/Riot agreements.
- No Deconstructor of Fun, Naavik or GameRefinery material specific to Africa surfaced in the searches run.
- No recent measured results for AI-driven offer personalisation in a named mobile game beyond vendor claims.

## 4. ASO and store presence

### Takeaway
Google Play (the dominant store in African markets) gives publishers country-level custom store listings (up to 50), localised listing experiments, pre-registration listings, churned-user targeting and promotional content surfaces; review reply automation has the best-documented uplift. Evidence on African-language listing localisation and APK-size effects is thin and mostly from low-quality sources.

### Cited Findings
- Custom store listings can be tailored by country, for pre-registration, or to win back inactive users; up to 50 custom listings; a country can be targeted by only one at a time. — [Google Play Console](https://play.google.com/console/about/customstorelistings/)
- Custom listings can be linked to Google Ads App Campaign ad groups and can now target inactive/churned users; they carry no special ranking boost, their value is conversion. — [MobileAction](https://www.mobileaction.co/blog/custom-store-listings-on-google-play/); [ASOMobile](https://asomobile.net/en/blog/custom-store-listing-v-google-play)
- Store listing experiments can test icon, feature graphic, screenshots, promo video and descriptions in up to five languages per localised experiment; pre-registration campaigns are terminated in all countries if the title has not launched within 90 days. — [Google Play Academy](https://playacademy.exceedlms.com/student/activity/454856?sid_i=19)
- Google PlayTime 2025 recap: promotional content likely powers new hero spotlights; a "You" tab for gamers shows active promotional content and leagues for installed games; changes to store listing experiments are on the roadmap without a date. — [AppTweak](https://www.apptweak.com/en/aso-blog/google-playtime-2025)
- Google Play supports roughly 77-80+ locales and indexes the full listing text; screenshots and video should be localised, since text-only translation yields a fraction of the uplift. — [AppTweak](https://www.apptweak.com/en/aso-blog/beginner-s-guide-to-app-localization-on-google-play); [MobileAction](https://www.mobileaction.co/guide/localization-guide/)
- Vendor ASO guides recommend Swahili for Kenya and Tanzania and considering Yoruba, Hausa and Igbo for Nigeria (low-authority vendor pages, no measured results). — [AppDrift Kenya](https://appdrift.co/app-store-optimization/kenya); [AppDrift Nigeria](https://appdrift.co/app-store-optimization/nigeria)
- Reviews: AppFollow's 2026 gaming benchmark (22,800+ gaming apps, 51.5M reviews, vendor research) says the average mobile game replies to 24.8% of reviews versus 52.4% for its clients, and associates engagement with a +0.42 star lift. — [AppFollow benchmark](https://appfollow.io/blog/gaming-reply-rate-benchmarks-2026)
- Review automation cases (vendor-reported): Toca Boca +109% reply rate and 26.7K stars added after replies; Kakao Games Europe reply effect +1.52 with ratings moving 4.17 to 4.6 on Android; BitMango 2.3x response rate; Easybrain's Art Puzzle 4.17 (December 2024) to 4.47 (September 2025), with game fixes also credited. — [Toca Boca](https://appfollow.io/toca-boca-review-automation-reply-effect); [Kakao](https://www.casestudies.com/company/appfollow/case-study/kakao-games-europe-gets-152-in-rating-for-reviews-responded-with-appfollow); [BitMango](https://www.casestudies.com/company/appfollow/case-study/bitmango-increased-the-response-rate-by-23-times-in-3-days-with-appfollows-auto-replies); [Easybrain](https://appfollow.io/easybrain-app-ratings-management)

### Inferences
- For Carry1st the ASO surface splits in two: titles it publishes (where it may control listings per country) and the Carry1st Shop app. Country custom listings for Nigeria, Kenya, South Africa, Egypt, Morocco and Ghana showing local payment methods and local esports imagery are the obvious first tests.
- Promotional content submissions should be scheduled off the same beat calendar as LiveOps and Africa Cup dates.
- Payment and top-up delivery complaints are likely a major review theme for a shop app; review tagging can double as a support and fraud signal.

### Gaps
- No data found on APK/app size, Android Go or low-end-device effects on install conversion in Africa (2025-2026).
- No measured results for Swahili, Hausa, Yoruba, Amharic, Arabic or French listing localisation in African markets.
- Unknown how much store-listing control Carry1st has for partner titles such as CODM.
- Play Console limits quoted come partly from third-party blogs; verify in current Help Center.

## 5. SEO and AI-search visibility for top-up shops

### Takeaway
Top-up leaders win transactional queries with game x country landing pages and near-total coverage of brand-plus-game terms (Codashop claims 90%+ impression share on key terms and 90 localised pages in 25 countries). AI answer engines still send small traffic to top-up stores, and the evidence on what earns citations is mixed: front-loaded answers, statistics and in-body FAQs help, third-party mentions matter more than owned pages, and schema evidence conflicts.

### Cited Findings
- Coda (Codashop) describes localised reach for intent-driven users, reports 90 localised pages in 25 countries for campaigns, and claims 90%+ average impression share on key monetisation search terms (self-reported). — [Coda](https://www.coda.co/codashop); [Coda blog](https://www.coda.co/blog/app-monetization-and-marketing/)
- Semrush estimates for codashop.com show high-volume brand-plus-game terms such as "codashop ml" and "top up ml" in Indonesia (third-party estimate, updated November 2025). — [Semrush](https://www.semrush.com/website/codashop.com/overview)
- The same Semrush snapshot lists about 8K visits from ChatGPT and 130 from Perplexity for codashop.com, small relative to total traffic. — [Semrush](https://www.semrush.com/website/codashop.com/overview)
- Princeton GEO study (KDD 2024, peer-reviewed) is the base evidence: GEO techniques raised citation rate by up to 40%, with adding statistics among the stronger tactics (about 37%), as summarised in 2026 evidence round-ups. — [Everything PR round-up](https://everything-pr.com/how-ai-engines-cite-the-web-the-six-studies-that-define-the-2026-evidence-base); [Radiant Elephant](https://www.radiantelephant.com/?p=47908)
- Secondary summaries (vendor studies; URL attribution unverified among the round-ups): Kevin Indig's analysis of 1.2M ChatGPT citations found citations concentrate on content near the top of a page; SE Ranking found in-body FAQ sections nearly double citation odds; domains with profiles on review platforms such as Trustpilot were about 3x more likely to be cited by ChatGPT; AirOps found brands 6.5x more likely to be cited via third-party sources than their own domain. — [Everything PR round-up](https://everything-pr.com/how-ai-engines-cite-the-web-the-six-studies-that-define-the-2026-evidence-base); [Elite Content Marketer stats](https://www.elitecontentmarketer.com/geo-aeo-statistics)
- Schema evidence conflicts: one study summary says markup did nothing for citations, another claims about +22%. — [Radiant Elephant](https://www.radiantelephant.com/?p=47908); contradicted by [Elite Content Marketer stats](https://www.elitecontentmarketer.com/geo-aeo-statistics)
- A six-week study of 1,127 URLs across five AI engines found the highest domain overlap between any two engines was 17%; Copilot cited Reddit zero times while AI Overviews and ChatGPT did cite it. — [Digital Authority](https://www.digitalauthority.me/?p=88331)
- Carry1st already publishes SEO-friendly esports content on its blog (Africa Cup guides and regional qualifier recaps). — [Carry1st blog](https://carry1st.com/blog/everything-you-need-to-know-about-the-carry1st-africa-cup-2025)

### Inferences
- Programmatic page matrix for Carry1st Shop: game x country x payment method (for example "buy CODM CP Nigeria bank transfer", "Free Fire diamonds Kenya M-Pesa"), each with live local-currency price table, delivery time, UID how-to, payment steps and an in-body FAQ placed near the top. This matches both the Codashop pattern and the citation findings.
- Because AI engines favour third-party sources, Trustpilot-style review profiles, creator videos, esports press and community threads are part of AI-search visibility, which ties SEO to the creator and esports teams.
- Engine overlap is low, so AI visibility tracking must be per engine (ChatGPT, AI Overviews, Perplexity, Copilot, Gemini) with a prompt set per country and game.
- "Cheap" queries invite grey-market resellers; official-partner status (Activision, Riot, Supercell, EA) is the trust differentiator to state plainly on pages.

### Gaps
- No keyword-volume or ranking data for African top-up queries ("buy CODM CP Nigeria", "cheap Free Fire diamonds") was retrieved; Semrush/Ahrefs lookups were not run.
- No evidence on llms.txt effect, and no e-commerce or top-up-specific AI citation study.
- Carry1st Shop's current organic traffic, page architecture and AI-referral share are unknown.

## 6. Creators, community and esports

### Takeaway
Carry1st's esports flagship is the Carry1st Africa Cup: a $15,000 CODM event in 2025 recognised by Activision as the World Championship qualifier, growing in 2026 to $30,000, two titles (CODM and Mobile Legends: Bang Bang), 38 countries and Esports World Cup qualification. It is run at a loss as a brand and player-base investment that feeds Shop, Pay1st and Flow1st. Creator development is formalised via the CODM Creators College (2026, with Infinix); African gaming audiences are heavy daily YouTube and TikTok users.

### Cited Findings
- Africa Cup 2025: $15,000 prize pool, qualifiers May to July, over 200 teams and 1,000 players expected, first CODM event in Africa recognised by Activision as a qualifier for the CODM World Championship 2025 ($1M global pool). — [PocketGamer.biz](https://www.pocketgamer.biz/carry1st-africa-cup-2025-returns-with-15000-call-of-duty-mobile-prize-pool); [GamesBeat](https://gamesbeat.com/carry1st-brings-call-of-duty-mobile-tournament-to-africa-as-championship-qualifier); [esports.gg](https://esports.gg/news/codm/carry1st-africa-cup-journey-to-call-of-duty-mobile-world-championship-2025)
- LAN Grand Finals were held 30-31 August 2025 in Ikeja, Lagos; Spotify was Official Music Sponsor and Mentos also partnered. — [Carry1st press: Spotify](https://carry1st.com/press/carry1st-and-spotify-partner-to-unite-music-and-gaming-at-africa-cup-grand-finals---officially-the-qualifier-for-call-of-duty-r-mobile-world-championship-2025); [Carry1st press: Mentos](https://www.carry1st.com/press/carry1st-mentos-partner-africa-cup-codm-2025-grand-finals)
- Regional qualifiers (South Africa, Uganda, North Africa) each got recap posts on the Carry1st blog; a recap headline reports Bear Clan as 2025 champion (headline only, details unverified). — [South Africa recap](https://carry1st.com/blog/carry1st-africa-cup-2025-south-africa-qualifiers-recap); [Uganda recap](https://carry1st.com/blog/carry1st-africa-cup-2025-uganda-qualifiers-recap); [Champions post](https://carry1st.com/blog/bear-clan-crowned-champions-carry1st-africa-cup-2025)
- Africa Cup 2026 (interview dated 27 October 2026): prize pool doubled to $30,000, described by Carry1st as the largest for an African-only tournament to its knowledge; similar participation (200+ teams, 1,000+ players, seven regions); CODM open to 38 countries with five regional qualifiers; added Mobile Legends: Bang Bang, with the MLBB Women's Invitational qualifying for the Esports World Cup; Carry1st does not profit from the event and investment rises yearly; no aggressive game expansion planned for 2027. — [PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)
- Noe frames esports as "the flagship" (the Formula 1 analogy) feeding Shop, Pay1st and Flow1st (an API letting digital platforms sell in-game items and currencies). — [PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)
- CODM Creators College: an in-person training programme in Lagos for emerging African gaming creators; in 2026 Call of Duty: Mobile with Carry1st and Infinix unveiled the "Chosen 10", with creators from Nigeria, South Africa, Ghana and Kenya; described as an extension of Carry1st's creator ecosystem. Source is trade press only; no official announcement found. — [Esports Africa News: Chosen 10](https://esportsafricanews.com/meet-the-chosen-10-africas-next-wave-of-codm-creators-2/); [Esports Africa News: Creators College](https://esportsafricanews.com/codm-creators-college-empowering-africas-next-generation-of-gaming-creators/?amp=1)
- Creator economics (Nigeria, Techpoint; URL attribution unverified): creator KingPlays reported earning over N4 million in a year from a TikTok page of 222,000 followers; MalayYT, with about 68,800 TikTok followers, is described as one of Nigeria's biggest CODM creators. This implies the CODM creator tier is mostly micro to mid-size. — [Techpoint Africa](https://techpoint.africa/?p=290435)
- Survey of 2,588 gamers in Egypt, Kenya, Nigeria and South Africa: about 87% watch YouTube daily and 74% use TikTok daily (URL attribution unverified between the two market reports returned). — [PocketGamer.biz](https://www.pocketgamer.biz/report-egypt-leads-africas-games-market-with-368m-in-revenue); [Outlook Respawn](https://respawn.outlookindia.com/gaming/gaming-news/africas-gaming-revenue-surges-egypt-claims-the-top-spot)
- Twitch, YouTube and TikTok Live are the main stages for African streamers, who localise humour and language; creators in Nigeria, Kenya and South Africa monetise via TikTok and local payment systems, coaching and community building. — [allAfrica](https://allafrica.com/stories/202509040104.html); [The African Mirror](https://theafricanmirror.africa/news/e-sports-is-booming-in-africa/)
- Africa esports market size estimates conflict: about $40M rising past $60M (Maliyo-attributed) versus $66M for 2025 (Statista-attributed); South Africa cited at $7-10M. — [Focus Gaming News](https://focusgn.com/africa/africa-emerges-as-a-major-hub-for-esports-and-igaming); [News Central](https://newscentraltv.com/?p=355916)

### Inferences
- Because the CODM creator pool is dominated by sub-250K accounts, an always-on micro-creator programme (affiliate codes tied to Shop Points or Gems, monthly content briefs keyed to season beats, tournament co-streams) fits better than a few large sponsorships; Gems being transferable makes them a natural creator giveaway currency.
- Each Africa Cup stage produces reusable owned content (recaps, VODs, player stories) that serves SEO, AI-search citations, CRM and store promotional content; a content-repurposing agent has clear inputs.
- Sponsors (Spotify, Mentos, Infinix) show a brand-partnership revenue line that offsets event cost and needs its own pipeline.
- The 38-country CODM footprint is wider than Pay1st's six core payment markets, so esports registration data is a lead list for payment-method expansion.

### Gaps
- No evidence found on Carry1st affiliate, referral or campus ambassador programmes, nor on its Discord/WhatsApp/Telegram community sizes.
- Africa Games Week involvement by Carry1st was not confirmed in the sources retrieved.
- No viewership figures for Africa Cup broadcasts.
- No reliable ranked list of African gaming creators by platform; ranking-tool pages found were commercial and not used.

## 7. B2B growth for Pay1st (publisher and merchant partner acquisition)

### Takeaway
Pay1st sells one integration giving 120+ local methods with Carry1st as Merchant of Record, in two modes (Gateway inside the partner's checkout, or listing on Carry1st Shop), and has added a third product, Flow1st, for third-party distribution of in-game items. Reference logos (Activision, Riot, Supercell, EA, Garena, MPL, Tinder, Nanobit, Audiomack) and outcome proof (six-fold annual CODM volume growth) are the visible pipeline assets; the documented motion is partnership-led, with esports, creators and consumer reach as the bundled differentiator.

### Cited Findings
- Pay1st value proposition: "120+ local payment methods", six named geographies, Merchant of Record covering compliance, tax, FX and risk with USD settlement, API docs and dedicated engineering support. Notable partners shown: Riot, Supercell, MPL, Activision, Tinder, Nanobit, Garena; testimonials from Riot (Hasan Colakoglu) and Call of Duty (Jeff Gullett). The page has no conversion or revenue-lift statistics. — [Carry1st Pay1st](https://www.carry1st.com/pay1st)
- Two integration styles: Shop integration (products listed on Carry1st Shop) and Gateway integration (Pay1st methods in the partner's native checkout, web store, game client or APK). — [Pay1st docs](https://pay1st-docs.carry1st.com)
- EA joined for FC Mobile; Carry1st described EA as another Pay1st partner alongside Activision and Supercell. — [PocketGamer.biz](https://www.pocketgamer.biz/asia/news/83523/carry1st-partners-with-electronic-arts-to-expand-fc-mobile-growth-in-africa/)
- Press coverage states CODM transaction volumes grew six-fold annually since Pay1st launched two years earlier (URL attribution unverified; reported in Nigerian business press on the CODM payments partnership). — [BusinessDay](https://businessday.ng/life-arts/article/africas-350m-gamers-get-in-app-payment-platforms/)
- Non-gaming merchants: Audiomack partnered with Carry1st for music-subscription payments across Africa (October 2024); Tinder appears among partner logos. — [TechEconomy](https://techeconomy.ng/carry1st-partners-with-audiomack-to-streamline-music-subscription-payments-across-africa/); [Carry1st Pay1st](https://www.carry1st.com/pay1st)
- Flow1st: a distribution API (v1.0 reference, integration checklist, changelog, distributor-balance endpoint) letting digital platforms sell in-game items and currencies. — [Flow1st docs](https://distribution-docs.carry1st.com/); [PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)
- As of October 2026 publishing partners include Activision, Tencent and Riot Games; a Stellar Gate Games deal covers third-party distribution and rights for Iraq; an Entrepreneur in Residence programme gives leaders P&L responsibility across Shop, Pay1st and Flow1st in specific markets; Carry1st attends Pocket Gamer Connects Jordan (7-8 November 2026). — [PocketGamer.biz](https://www.pocketgamer.biz/carry1sts-guillaume-noe-esports-is-to-gaming-what-formula-1-is-to-the-car-industry/)

### Inferences
- The B2B funnel implied by these assets: target account list (top-grossing titles in Pay1st markets and subscription apps with card-dependent checkout) to outreach with a country-level "payment gap" model (the under-10% card access statistic) to pilot via Shop integration (low engineering) to upgrade to Gateway, then expansion into co-marketing (esports, creators) and Flow1st distribution.
- Events (PG Connects, Africa Games Week, Gamescom, GDC) and trade press (PocketGamer.biz, GamesBeat) are the visible demand channels; a B2B agent team would handle account research, payment-gap sizing per title, case-study production and conference meeting pipelines.
- Flow1st adds a second B2B audience (telcos, wallets, super-apps and resellers that want to sell game credits), with a different pitch from the publisher side.
- The lack of public conversion-uplift numbers on the Pay1st page is a content gap; anonymised uplift benchmarks would strengthen outbound.

### Gaps
- No public information on Pay1st pricing, take rate, sales team structure, sales cycle length or CRM tooling.
- No 2026 new-partner announcements were found in the single search run; Riot partnership scope (titles, countries) not detailed.
- No description of what "Marketing" support for partner titles (shown for CODM and Free Fire on the Pay1st page) includes.

## 8. Documented AI and automation use cases with measured results

### Takeaway
The best-documented automation with numbers is app-review reply automation (reply rates doubling, rating lifts of about 0.3 to 0.4 stars, hours saved), all vendor-reported. AI decisioning in CRM, AI-personalised offers and GEO have published uplift claims but little gaming-specific or Africa-specific measurement; for most other functions (creator ops, esports ops, B2B pipeline, localisation) no measured cases were found.

### Cited Findings
- Review management: Joyteractive reached a 91% reply rate, about 55-minute typical reply time and roughly 35 hours a month of manual work removed (vendor-reported). — [AppFollow](https://appfollow.io/blog/scaling-player-connection-with-the-help-of-ai-and-the-human-touch)
- Review management: AppFollow says AI replies arrive about 12x faster and associates engagement with a +0.42 star lift across its 2026 gaming benchmark; causation is not isolated from product fixes. — [AppFollow reply time benchmark](https://appfollow.io/blog/gaming-reply-time-benchmarks-2026); [AppFollow reply rate benchmark](https://appfollow.io/blog/gaming-reply-rate-benchmarks-2026)
- Review management: Toca Boca +109% reply rate and 498% more reviews replied year over year; BitMango 2.3x response rate with response time cut by at least 60%. — [Toca Boca](https://appfollow.io/toca-boca-review-automation-reply-effect); [BitMango](https://www.casestudies.com/company/appfollow/case-study/bitmango-increased-the-response-rate-by-23-times-in-3-days-with-appfollows-auto-replies)
- ASO tooling: AppTweak offers a GPT-powered reply assistant and bulk replies; its published rating example is non-gaming (The North Face, 3.68 to 4.23 on iOS after a post-checkout prompt). — [AppTweak](https://www.apptweak.com/en/aso-blog/tips-to-manage-app-store-reviews)
- CRM personalisation: WinZO about 40% retention improvement with real-time personalisation (CleverTap); Classic Rummy 24% retention and 3x payment value (MoEngage). Vendor-reported, India. — [WinZO](https://www.casestudies.com/company/clevertap/case-study/how-winzo-acts-on-real-time-data-insights-to-revolutionize-mobile-gaming); [Classic Rummy](https://www.casestudies.com/company/moengage/case-study/classic-rummy-boosts-player-retention-by-24-with-moengage)
- AI decisioning: Braze cites a 105% cross-sell increase on its product page (customer unnamed) and Forrester composite models; no gaming customers in the TEI spotlight. — [BrazeAI](https://www.braze.com/product/brazeai); [Forrester TEI spotlight](https://tei.forrester.com/go/braze/aidecisioningspotlight/)
- LiveOps: Google's Bravestars piece documents AI use in app marketing and LiveOps for a Vietnamese studio (results not captured in the snippet); industry commentary expects AI-driven personalisation to replace static segments in 2026. — [Google Think](https://business.google.com/us/think/ai-excellence/bravestars-games-app-marketing-liveops/); [PocketGamer.biz](https://www.pocketgamer.biz/2026-live-ops-trends-templatisation-personalisation-and-ai)
- Web shop: Xsolla-reported offerwall result of +5% web-shop revenue and +37% payment transactions is automation of non-payer engagement, not AI as such. — [GamesBeat](https://gamesbeat.com/?p=309580)
- AI search: GEO techniques lifted citation rates by up to 40% in the Princeton study, the only peer-reviewed measurement found. — [Everything PR round-up](https://everything-pr.com/how-ai-engines-cite-the-web-the-six-studies-that-define-the-2026-evidence-base)

### Inferences
- Ranking of functions by automation readiness for agent teams (evidence strength in brackets): review replies and review-theme mining (strong, vendor); programmatic SEO page generation and AI-visibility monitoring (moderate); CRM journey drafting, segment and send-time decisions (moderate, non-African); Shop offer and price-refresh by country (logical, unmeasured); creator sourcing, briefing and content repurposing from esports (unmeasured); B2B account research and payment-gap modelling (unmeasured).
- Human approval is warranted for anything that sends messages with per-message cost (WhatsApp marketing templates), changes prices, or replies publicly on payment disputes.

### Gaps
- No measured AI results specific to African gaming or to Carry1st.
- No measured cases for AI in creator management, esports operations, localisation into African languages, or B2B payments sales.
- Braze, OneSignal and Klaviyo gaming-specific AI case studies were not found; Metica and Deconstructor of Fun sources did not surface.
- Localisation as a standalone function (in-game text, voice, culturalisation for African markets) returned no dated, sourced findings beyond store-listing guidance.
