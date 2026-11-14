# AI Agent Team Design for Growth Organisations (state as of November 2026)

Research date: 14 November 2026. Scope: multi-agent "AI teams" for growth, with emphasis on mobile gaming, app growth and e-commerce; ad platforms in scope are Google, Meta and TikTok only.

Reading notes for the report writer:
- Every finding carries its date where the source gave one. "Vendor claim" marks numbers published by the party selling the product; "independent" marks academic or third-party measurement.
- Most findings below were taken from search-result summaries, not from the full primary page. Only two pages were read in full: Anthropic's multi-agent research post and the Digital Applied ads-MCP playbook. Where a finding rests on a secondary summary of a primary source, it is flagged.
- One primary page (TikTok World 2026 newsroom post) returned HTTP 503 and was not read.

## 1. What multi-agent architecture patterns are used in practice, and what do Anthropic, OpenAI, Google, Microsoft and LangChain say about when to use each?

### Takeaway
All five vendors converge on the same small set of patterns (central orchestrator with workers, sequential pipeline, parallel fan-out, peer handoff, router), and the published evidence favours a central orchestrator over independent peers because it contains error propagation. Multi-agent is justified for parallelisable, high-value, context-heavy work and is a poor fit where agents need shared context or have many interdependencies.

### Cited Findings

Anthropic (read in full, published 13 June 2025)
- Architecture is an "orchestrator-worker pattern": a lead agent plans and spawns subagents that work in parallel in their own context windows and return condensed findings; a separate CitationAgent attributes claims before output — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- A Claude Opus 4 lead with Claude Sonnet 4 subagents outperformed single-agent Opus 4 by 90.2% on Anthropic's internal research eval (vendor's own internal eval, not independently replicated) — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- Token usage alone explained 80% of performance variance on BrowseComp; token usage, tool calls and model choice together explained 95% — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- Agents use about 4x the tokens of chat; multi-agent systems about 15x — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- Good fit: "valuable tasks that involve heavy parallelization", information exceeding one context window, many complex tools. Poor fit: domains needing shared context or many inter-agent dependencies — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- Effort scaling rules embedded in prompts: simple fact-finding 1 agent with 3-10 tool calls; direct comparisons 2-4 subagents with 10-15 calls each; complex research more than 10 subagents. Lead spins up 3-5 subagents in parallel; parallelism cut research time by up to 90% on complex queries — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- Synchronous execution (lead waits for each subagent batch) creates bottlenecks; asynchronous execution adds parallelism but complicates coordination, state consistency and error handling — [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)

LangChain (January 2026 blog and docs; search summary)
- Four core patterns: subagents (main agent calls subagents as tools; strong context isolation, one extra model call per delegation, centralised control), skills (single agent loads packaged instructions/scripts on demand; fewer calls, higher token use from context accumulation), handoffs (control passes between agents via tool calls; suits sequential stateful workflows; cannot parallelise), router (classify input, dispatch to one or more specialists; suits multi-domain tasks) — [LangChain blog](https://www.langchain.com/blog/choosing-the-right-multi-agent-architecture); [LangChain docs](https://docs.langchain.com/oss/python/langchain/multi-agent/index)
- Stateful patterns (handoffs, skills) save 40-50% of calls on repeat requests; for multi-domain tasks the parallel patterns (subagents, router) are most efficient; patterns can be mixed — [LangChain docs](https://docs.langchain.com/oss/python/langchain/multi-agent/index)

OpenAI ("A practical guide to building agents", 2025; search summary of third-party write-ups)
- Two orchestration patterns: manager (a central agent coordinates specialists via tool calls; orchestration agents can themselves be tools for other agents) and decentralised (peers transfer control through one-way handoffs). Handoffs reduce bottlenecks but increase coordination complexity. In the Agents SDK a handoff is a type of tool — [OpenAI guide PDF](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf); [summary](https://agentic-ai.readthedocs.io/en/latest/DesignPatterns/openai-patterns/)
- The guide has a dedicated guardrails section; summaries describe guardrails as mission-critical — [OpenAI guide PDF](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)

Microsoft Agent Framework (docs; search summary)
- Five built-in orchestrations: sequential (each step consumes the previous output), concurrent (same input to all, results gathered), handoff (decentralised routing, agents pick targets), group chat (a manager picks the next speaker and can pause for human input), Magentic (manager with planning and persistent task state; the most elaborate) — [Microsoft Learn](https://learn.microsoft.com/agent-framework/workflows/orchestrations)

Google (A2A, ADK; search summary)
- Google donated the A2A protocol to the Linux Foundation in June 2025; at its one-year mark (April 2026) the project reported more than 150 supporting organisations and describes A2A as complementary to MCP — [Linux Foundation](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year?hs_amp=true)
- Agent Cards are JSON discovery documents declaring an agent's identity, skills and capabilities; newer versions add signed Agent Cards. One framing: an agent uses A2A to delegate to a specialist, which uses MCP to call its tools — [Galileo guide](https://galileo.ai/blog/google-agent2agent-a2a-protocol-guide)

Independent evidence on pattern choice
- Google Research study (arXiv 2512.08296, blog January 2026) across 180 configurations, five architectures and three LLM families: independent multi-agent systems amplified errors about 17.2x versus single-agent baselines, while centralised (orchestrator) systems contained this to about 4.4x; the orchestrator acts as a "validation bottleneck". Centralised coordination gained about 80.9% on a financial-reasoning task (figure varies 80.8-80.9% across summaries) — [Google Research](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/); [arXiv](https://arxiv.org/html/2512.08296v2)

### Inferences
- For a 10-12 team engine, the defensible shape is a two-level supervisor hierarchy: one engine-level orchestrator routing to team leads, each team lead running an orchestrator-worker or sequential pipeline internally. Peer-to-peer handoffs between teams should be avoided for anything that writes to an ad account, given the 17.2x versus 4.4x result.
- Map patterns to growth work: router for intake (classify a request to a team); sequential pipeline with a critic for creative production (brief, generate, review, policy check, publish); orchestrator-worker with parallel fan-out for analysis and research (per-channel, per-geo, per-title); event-driven triggers for monitoring (spend anomaly, creative fatigue); group-chat or manager-with-human-pause for budget reallocation.
- "10-12 agents per team" is better implemented in many cases as skills loaded by fewer agents (LangChain's skills pattern) than as 10-12 separately running agents, because each additional running agent adds token cost and a coordination surface. The 15x token multiplier is the cost of real multi-agent fan-out.
- Evaluator/critic agents are a pipeline stage, not a separate architecture: Anthropic's CitationAgent and LLM judge are the published precedent.

### Gaps
- Anthropic's "Building effective agents" post (workflows versus agents, "start with the simplest solution") was not retrieved in this session; no finding is cited from it.
- Google ADK's specific workflow agent types (sequential, parallel, loop, coordinator) did not surface in search; not verified against ADK docs.
- OpenAI Agents SDK tracing and guardrail specifics were not retrieved; only the orchestration patterns are sourced.
- No vendor source on shared-memory or blackboard architectures was found; the only sourced memory guidance is Anthropic's external-store-plus-references approach (section 2).

## 2. How should agents be scoped, and how do teams avoid duplicated work and conflicting actions?

### Takeaway
Published guidance says each delegated agent needs four things: an objective, an output format, tool and source guidance, and explicit task boundaries; without them agents duplicate work or leave gaps. No source found describes a published mechanism for preventing two agents from changing the same budget, so conflict control has to be designed from first principles.

### Cited Findings
- Each subagent should receive an objective, an output format, guidance on tools and sources, and clear task boundaries. Without this, subagents duplicated work or left gaps; Anthropic's example: one subagent researched the 2021 chip crisis while two others duplicated 2025 supply-chain research — [Anthropic, June 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- Subagents can write outputs to external storage and pass lightweight references back to the lead, reducing information loss and token overhead — [Anthropic, June 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- The lead agent saves its plan to memory because context beyond 200,000 tokens gets truncated; agents summarise completed phases, store essentials externally and can spawn fresh subagents with clean contexts — [Anthropic, June 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- MAST taxonomy (Cemri et al., UC Berkeley; NeurIPS 2025): 14 failure modes in 3 categories: specification issues, inter-agent misalignment and task verification, from 1,600+ annotated traces across 7 frameworks. Failures stem mainly from system design, not only from model limitations — [arXiv 2503.13657](https://arxiv.org/html/2503.13657v2)
- Subagents-as-tools gives centralised control at the price of one extra call because results flow back through the main agent — [LangChain docs](https://docs.langchain.com/oss/python/langchain/multi-agent/index)
- Practitioner guidance for ad-account queries: include date range, metric, campaign ID and attribution window in every query to reduce hallucinated figures, and verify key numbers against the platform UI — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)
- Editing Meta budgets or audiences more than roughly once per day can reset the learning phase (practitioner report, not published Meta policy) — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)

### Inferences
- Agent contract template implied by the sources: name; single responsibility; trigger; inputs (with schema and source of truth); outputs (schema plus storage location, passed by reference); tools and permission scope (read, draft, write); boundaries (what it must not touch); escalation rule; evaluation criteria.
- Conflict avoidance design that follows from the centralisation evidence: (a) exactly one agent per platform holds write scope for budgets and bids, and all other agents submit proposals to it; (b) a shared change ledger in the warehouse records every proposed and applied mutation with entity ID, old value, new value, proposer and approver; (c) per-entity locks or cool-down windows (for Meta, at most one budget or audience edit per entity per day, per the learning-phase caution); (d) the orchestrator resolves competing proposals before anything is written.
- Shared data layer: analysis agents should read from one modelled warehouse layer (cost, MMP-attributed installs and revenue, LTV predictions) so all agents reason from the same numbers; hand-offs should be stored artifacts with references, not long messages, following Anthropic's artifact pattern.
- MAST's three categories map to three design controls: written specifications per agent, typed hand-off formats between agents, and a verification stage at the end of each workflow.

### Gaps
- No published case study found of a growth team's agent-to-agent conflict resolution (for example budget locking); the mechanisms above are inferred.
- No source found on feature stores or knowledge bases specifically as shared memory for marketing agents.
- The failure-rate range of 41% to 86.7% for multi-agent frameworks appears in a secondary summary of MAST and was not confirmed in the paper text; treat as unverified.

## 3. What tools and connectors exist for agents to act on growth systems, and which are official?

### Takeaway
By mid-2026 Google, Meta and TikTok each had an official ads MCP server, with very different write permissions: Google's is read-only, Meta's is read/write with new entities paused by default, and TikTok's is described as full-lifecycle read/write but its availability status is disputed. AppsFlyer and Braze have official MCP servers; no official Adjust server was found.

### Cited Findings

Ad platforms (official)
- Google Ads MCP: launched 28 April 2026, open source, maintained by the Google Ads API team at GitHub `googleads/google-ads-mcp`. Read-only by design; mutations remain in the REST/gRPC API. Three tools (`list_accessible_customers`, `search` for GAQL, `get_resource_metadata`) and four resources. Self-hosted; requires a developer token with at least Explorer access — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)
- Meta Ads AI Connectors: official MCP server plus CLI, open beta from 29 April 2026, hosted at `mcp.facebook.com/ads`, free during beta. 29 tools: product catalog (10), insights and benchmarks (7), campaign management (5), dataset and tracking diagnostics (4), accounts/pages/assets (3). Read/write. Entities created via MCP start paused and need human activation in Ads Manager; the CLI creates entities active by default unless `--status PAUSED` is passed. Business OAuth with three scope tiers (read-only, read/write, read/write/financial). No vision or creative analysis, no Ad Library access — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)
- TikTok Ads MCP: announced 13 May 2026 at TikTok World; described as read/write across planning, launch, bid and budget adjustment, targeting and optimisation, with a companion TikTok Ads Skills SDK. No public tool inventory, auth details or status at time of the article — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook). Sources conflict on status: one says announced but not generally available, another says shipped on 13 May 2026 — [ContentGrip](https://www.contentgrip.com/ad-platform-mcp-rollout/); [Adspirer guide](https://www.adspirer.com/docs/guides/best-ad-mcp-servers-2026)
- MCP spec version 2025-11-25; remote servers must use OAuth 2.1 with PKCE. Third-party registries tracked roughly 10,000+ MCP servers by April 2026 — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)

Ad platforms (third-party)
- Cross-platform hosted servers exist from vendors such as Adspirer, Ryze AI and Synter; their coverage and pricing claims are vendor marketing — [Blue Alpha comparison](https://bluealpha.ai/mcp/comparison); [Adspirer guide](https://www.adspirer.com/docs/guides/best-ad-mcp-servers-2026)

Measurement and lifecycle
- AppsFlyer MCP: official, in beta, "provided for evaluation purposes", remote server at `https://mcp.appsflyer.com/auth/mcp` — [AppsFlyer support](https://support.appsflyer.com/hc/en-us/articles/36349070304785--Beta-AppsFlyer-MCP); [AppsFlyer product news](https://www.appsflyer.com/product-news/agentic-ai-suite/appsflyer-mcp-model-context-protocol-beta-server-is-launched/). A community server (`ysntony/appsflyer-mcp`) also exists and is not an AppsFlyer product — [Glama](https://glama.ai/mcp/servers/@ysntony/appsflyer-mcp)
- Adjust: only third-party servers found (for example `bitscorp-mcp/mcp-adjust`, which queries reports and metrics); no official Adjust server confirmed — [Playbooks](https://playbooks.com/mcp/bitscorp-mcp/mcp-adjust)
- Braze MCP: official remote server with US (`https://mcp.braze.com/mcp`) and EU (`https://mcp.braze.eu/mcp`) endpoints. Braze docs say the remote server is in Early Access, while a Braze blog post describes it as generally available. The older local server (August 2025) is deprecated. Customers using IP allowlisting cannot use it — [Braze docs](https://www.braze.com/docs/user_guide/brazeai/mcp_server/); [Braze blog](https://www.braze.com/resources/articles/introducing-braze-mcp-server). A non-official write-enabled fork (fireMCP) exists — [Glama](https://glama.ai/mcp/servers/@saarkia/fireMCP)

Standards
- IAB Tech Lab published "Agentic Mobile" on 22 June 2026, an open standard giving AI agents an interface to mobile in-app inventory, pricing and reporting over MCP and A2A; supply-side only in v1 (from a search summary; primary page not read) — [Mobile Dev Memo index](https://mobiledevmemo.com/category/original-content/page/5/)

### Inferences
- Official/community matrix for the engine: Google Ads (official, read-only; writes need the Google Ads API directly or a third-party server), Meta (official, read/write, paused-by-default), TikTok (official, write-capable, status to verify), AppsFlyer (official beta), Braze (official, early access or GA depending on source, and the write-enabled fork implies the official one is read-oriented), Adjust (community only).
- Because Google's official server cannot write, a Google budget/bid agent needs a custom tool wrapping the Google Ads API, which is also the natural place to enforce spend caps in code.
- Meta's paused-by-default behaviour is a ready-made human approval gate; the CLI's active-by-default behaviour is a trap for scripted agents.

### Gaps
- Not researched in this session: MCP or API connectors for BigQuery, Snowflake, CleverTap, Slack, ticketing systems, and creative generation tools (image, video, playable). No findings are cited for them.
- Adjust's own position on MCP was not checked on adjust.com.
- TikTok Ads MCP's current availability, tool list and auth model were not verified against TikTok documentation (newsroom page returned 503).
- Whether Braze's official server supports writes was not confirmed.

## 4. What documented case studies exist, with measured results and failures?

### Takeaway
Independently verified results for agentic growth operations in gaming, apps and e-commerce are scarce; almost every performance number found is vendor-reported. The best-documented cautionary cases are Klarna's partial return to human support (May 2025) and Duolingo's "AI-first" backlash (2025).

### Cited Findings

Gaming and app user acquisition (all vendor-reported unless stated)
- Sett raised a US$30M Series B for an AI platform automating UA creative production for mobile games; reported customers include Zynga, Playtika, Scopely, Tripledot, Rovio and Papaya — [ContentGrip](https://www.contentgrip.com/sett-series-b-ua-automation/)
- Playco is reported by a vendor to have achieved 5.7x creative throughput and a 31% CPI reduction using an AI marketing product; no Playco-published source was found (vendor claim) — [Hellyeah AI](https://www.hellyeahai.com/blog/ai-marketing-for-gaming)
- WGT cut its concept-to-test cycle from 2-3 weeks to 2-3 days (vendor case study) — [Segwise](https://segwise.ai/blog/ai-tools-create-ua-ads-mobile-games-apps)
- An anonymous mid-core casual game's acquisition cost was reportedly reduced by 45% using AI avatars and text-to-video variants (vendor claim, unnamed client) — [Kreado AI](https://www.kreadoai.com/article/ai-mobile-game-ad-creative-tools)
- A first-person AppsFlyer blog account describes an AI agent running acquisition for a game built in 14 days: 5,563 installs at $0.39 eCPI (single anecdote, not a controlled study) — [AppsFlyer blog](https://www.appsflyer.com/blog/measurement-analytics/ai-mobile-game/)
- Several 2026 vendor posts repeat that 70-80% of mobile game campaign performance variance comes from creative rather than bid strategy (widely repeated, origin not verified) — [Hellyeah AI](https://www.hellyeahai.com/blog/ai-user-acquisition-for-mobile-games)

Platform automation
- Advantage+ Shopping campaigns reportedly delivered about 22% higher ROAS than manual campaigns (third-party blog citing Enrich Labs, 2025; not verified) — [Digital Applied](https://www.digitalapplied.com/blog/meta-ai-automated-ads-2026-marketing-guide)

Customer support and "AI-first" operating models
- Klarna began rehiring human support agents in May 2025 on a freelance, shift-based model; the hybrid setup has AI handle routine queries and humans handle complex cases. Klarna framed this as not a full reversal on AI; a secondary source reports the CEO told Bloomberg cost-cutting had "gone too far" — [Tech.co](https://tech.co/news/klarna-reverses-ai-overhaul); [Maginative](https://www.maginative.com/article/klarna-dials-back-its-ai-customer-service-strategy-now-its-hiring-humans-again/)
- Duolingo's spring 2025 "AI-first" announcement (phasing out contractors for AI-capable work) drew public backlash; the CEO later said AI would not replace employees. TechCrunch reported in August 2025 that Duolingo beat quarterly revenue estimates despite the backlash, with the stock up almost 30% on the news — [TechCrunch, 7 August 2025](https://www.techcrunch.com/2025/08/07/the-backlash-against-duolingo-going-ai-first-didnt-even-matter/); [Influencer Marketing Hub](https://influencermarketinghub.com/duolingo-ceo-clarifies-ai-strategy-after-backlash-we-wont-replace-jobs-with-ai/)

Consultancy and analyst data
- McKinsey's Technology Trends Outlook 2026, as quoted by CIO.com: only 37% of companies attribute any positive EBIT impact to their AI programmes — [CIO.com](https://www.cio.com/article/4226418/ai-agents-a-lot-of-effort-but-still-little-return.html)
- A June 2026 McKinsey report, as covered by trade press, says AI could unlock up to $90 billion in improved marketing returns in the US (projection, not a measured result) — [Advanced Television, 23 June 2026](https://www.advanced-television.com/2026/06/23/research-ai-could-unlock-90bn-in-marketing-returns-in-us/)
- Secondary outlets report McKinsey projecting that agentic AI could automate 60% or 66% of marketing tasks (the two write-ups disagree) and link adoption to 10-30% revenue growth; not confirmed against the McKinsey original — [Pulse](https://www.pulse.bot/marketing/news/mckinsey-forecasts-agentic-ai-could-run-twothirds-of-marketing-tasks-lift-revenue-1030-2ec4c6f9-06dd-4241-8db3-46f947de9d75/)

### Inferences
- The consistent, plausible gain in the evidence is creative throughput and iteration speed (days instead of weeks). CPI reductions of 30-45% appear only in vendor material and should not be used as planning targets.
- Klarna's outcome supports a hybrid design for any customer-facing agent team: AI for routine volume, a defined human path for complex cases, with quality measured separately for each.
- Duolingo shows the communication risk of an "AI-first" label is separate from the commercial result; internal and public framing of an agent programme needs care.

### Gaps
- No case studies were found from Zynga, Supercell, Shopify, Deconstructor of Fun, a16z, Sequoia or BCG on agentic growth operations; these suggested sources were not reached.
- No documented case found for automated bid/budget management by custom agents, AI-driven LTV prediction, or AI live ops with measured results.
- No independently audited or peer-reviewed study of AI creative automation in mobile gaming was found.
- Mobile Dev Memo: no dedicated essay on agent team design surfaced; only podcast listings, including an April 2026 episode described as moving agentic commerce "from the initial hype" to "AI-assisted shopping" — [Mobile Dev Memo](https://mobiledevmemo.com/podcast-re-evaluating-agentic-commerce-with-andrew-lipsman/)
- Claims that Klarna's stock fell about 52% since IPO and that Duolingo's stock was down 80% from peak by April 2026 each rest on a single weak source and were not verified.

## 5. What governance is needed?

### Takeaway
The sourced baseline is: narrowest OAuth scope per phase, a human approving all spend changes, new entities created paused, every agent action logged, and LLM-judge plus human evaluation of agent quality. For Nigeria and South Africa, electronic direct marketing requires prior express consent, and solely automated decisions with significant effects need express consent and bias safeguards under Nigeria's GAID 2025.

### Cited Findings

Spend and action guardrails
- Recommended practice: use the narrowest OAuth scope each phase needs and avoid the financial tier by default; put a human in charge of spend changes; rate-limit and batch agent mutations; log every agent action; live budget and bid changes only behind explicit approval gates and change caps — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)
- Meta's MCP creates entities paused by default, requiring human activation — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)

Evaluation and monitoring
- Anthropic started evaluation with about 20 queries from real usage; used an LLM judge with a single prompt scoring 0.0-1.0 plus pass/fail on factual accuracy, citation accuracy, completeness, source quality and tool efficiency; human testing caught issues automation missed (agents favouring SEO content farms); for stateful workflows they evaluated end state rather than process — [Anthropic, June 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- Production practices: full tracing for debugging, resume-from-checkpoint with retry logic rather than restart, and rainbow deployments that shift traffic gradually so running agents are not disrupted — [Anthropic, June 2025](https://www.anthropic.com/engineering/multi-agent-research-system)

Brand safety
- TikTok says Symphony Agent ships with AI labels, invisible watermarks and content moderation filters (vendor claim) — [Communicate Online](https://communicateonline.me/news/tiktok-launches-ai-powered-symphony-agent-expands-creative-tools-across-mena/)
- Commentators flag that fully automated ad creation challenges brand oversight, compliance and design standards — [ContentGrip](https://www.contentgrip.com/meta-ai-ad-generation-2026-plan/)

Data privacy: Nigeria
- The NDPA General Application and Implementation Directive (GAID) was issued 20 March 2025 and took effect in September 2025 (one source: 19 September 2025), replacing the 2019 NDPR as the operative instrument — [Mondaq](https://www.mondaq.com/nigeria/data-protection/1624030/highlights-of-the-nigeria-data-protection-act-general-application-and-implementation-directive-2025)
- Explicit consent is required for direct marketing, alongside children's data, sensitive data and cross-border transfers; one law-firm summary says express consent is required when a controller contacts its customers to promote products or services — [Mondaq, GAID Unpacked II](https://www.mondaq.com/nigeria/privacy-protection/1700306/gaid-2025-unpacked-series-ii-data-protection-officers-mandatory-consents-and-emerging-technologies)
- Controllers relying solely on automated processing with legal or similarly significant effects must obtain express consent and show bias safeguards; profiling and automated decision-making trigger a DPIA requirement — [Mondaq, GAID Unpacked II](https://www.mondaq.com/nigeria/privacy-protection/1700306/gaid-2025-unpacked-series-ii-data-protection-officers-mandatory-consents-and-emerging-technologies)

Data privacy: South Africa
- Amended POPIA Regulations took effect 17 April 2025. Amended regulation 6 states that opt-out does not amount to consent under section 69(2). Consent must be written but may be obtained on a form "substantially similar to" Form 4 by any reasonably accessible method, including email, SMS, WhatsApp or telephone — [Michalsons](https://www.michalsons.com/blog/popia-amendment-regulations-commence/77824); [Cliffe Dekker Hofmeyr, 21 May 2025](https://www.cliffedekkerhofmeyr.com/en/news/publications/2025/Sectors/Technology-Communications/Technology-and-Communications-Alert-21-May-Important-POPIA-amendments-to-note)
- Section 69 generally requires prior consent for electronic direct marketing unless the limited "existing customer" exception applies; a prospect may be approached for consent only once and only if consent was not previously withheld — [MJK Inc](https://mjkinc.co.za/popia/electronic-marketing-section-69)
- A separate Consumer Protection Act amendment introduces an opt-out registry (Consumer Protection Act Amendment Regulations, 2026) — [Webber Wentzel](https://webberwentzel.com/News/Pages/opting-out-the-amendment-to-the-consumer-protection-act-regulations.aspx)

### Inferences
- Lifecycle agents (push, email, SMS, WhatsApp) must check a consent record before any send to Nigerian or South African users; consent state belongs in the shared data layer as a hard gate, enforced in code rather than in a prompt.
- Agents that personalise offers or pricing per user in Nigeria may fall under the automated decision-making rule; a DPIA for the agent system as a whole is the prudent default.
- Approval thresholds should be tiered by reversibility and money at risk: read and draft actions autonomous; creation of paused entities autonomous; activation, budget increases above a set percentage or absolute amount, and any audience upload require human approval.
- Cost control is a governance item in its own right given the 4x and 15x token multipliers: per-team token budgets, cheaper models for worker agents (Anthropic's Opus lead with Sonnet subagents is the precedent), and effort-scaling rules in prompts.
- Evaluation should start small (about 20 real cases per team), combine an LLM judge with human review, and judge end state (for example, "was the correct paused campaign created with the right budget?").

### Gaps
- GDPR was not researched in this session; no findings are cited for it.
- Ad-policy compliance tooling (automated pre-checks against Google, Meta and TikTok ad policies) was not researched.
- The privacy findings come from law-firm commentary, not the statutory text; exact wording should be checked against GAID and Government Gazette notice GN 6126. Sources differ on whether GAID accepts implied consent generally.
- No published numeric benchmarks for spend approval thresholds were found.
- No source was found on audit-log standards specific to marketing agents.

## 6. What does a realistic rollout look like, and what are the failure modes of large agent counts?

### Takeaway
The one sourced rollout template is a 90-day, three-phase ramp from read-only reporting to gated live changes on a single account. Independent research shows large, loosely coordinated agent counts amplify errors and cost, and Gartner predicts over 40% of agentic AI projects will be cancelled by the end of 2027.

### Cited Findings

Phasing
- Phase 1 (days 1-30): read-only reporting only. Phase 2 (days 31-60): write access on paused campaigns and test ad sets, with human review before activation. Phase 3 (days 61-90): live budget and bid changes only behind explicit approval gates and change caps, starting with one account, with every action logged — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)

Failure modes
- Independent agents amplified errors about 17.2x versus about 4.4x for centralised coordination — [Google Research, January 2026](https://research.google/blog/towards-a-science-of-scaling-agent-systems-when-and-why-agent-systems-work/)
- Errors compound in long-running stateful agents; restarting from scratch is expensive, so systems need checkpoints and retries — [Anthropic, June 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- Multi-agent systems use about 15x the tokens of chat, so they suit only tasks whose value justifies the cost — [Anthropic, June 2025](https://www.anthropic.com/engineering/multi-agent-research-system)
- MAST: failures cluster in specification issues, inter-agent misalignment and task verification; one benchmarked framework (ChatDev) achieved only 33.33% correctness on the paper's ProgramDev benchmark — [arXiv 2503.13657](https://arxiv.org/html/2503.13657v2)
- Gartner (June 2025): more than 40% of agentic AI projects will be cancelled by end of 2027 due to escalating costs and unclear business value; it estimates only about 130 of thousands of "agentic" vendors are genuine ("agent washing") and notes many use cases positioned as agentic do not require agentic implementations — [Reuters via The Star, 25 June 2025](https://www.thestar.com.my/tech/tech-news/2025/06/25/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-gartner-says)

Human roles
- Coverage of McKinsey's marketing work describes "orchestrators", marketers who connect teams and AI-enabled workflows; a secondary summary says marketing teams move from platform operators to strategy designers overseeing autonomous systems — [Fullcast](https://www.fullcast.com/content/only-10-of-teams-scale-ai-agents-despite-exploding-investment)
- Klarna's hybrid model keeps humans on complex customer cases — [Tech.co](https://tech.co/news/klarna-reverses-ai-overhaul)

### Inferences
- A design of roughly 100-140 agents is at the high-risk end of what the evidence supports. The plan should state that agent count is a ceiling for role definitions, with most roles implemented as skills or sequential steps and only a minority as concurrently running agents.
- Suggested team order, from lowest to highest risk and following the read-then-draft-then-write ramp: (1) analytics and reporting (read-only); (2) creative research and production (drafts, human-reviewed); (3) measurement and tracking QA; (4) lifecycle drafting; (5) paid media on Meta (paused-by-default gate exists); (6) TikTok; (7) Google writes (needs custom API tooling); (8) budget allocation across channels last.
- KPIs for the agent system itself, derived from the sources: task success rate by end-state check; LLM-judge score and human-review pass rate; human override and rollback rate; share of actions needing approval; duplicate or conflicting action count; cost per completed task (tokens); time from brief to live test; incidents (spend cap breaches, policy rejections).
- Human roles that remain: an engine owner (Head of Growth), one human lead per team acting as approver and evaluator, a platform/automation engineer for tools and guardrails, a data owner for the shared layer, and creative direction and brand sign-off.

### Gaps
- No published rollout case study for a growth organisation operating 100+ agents was found; the phasing source is a practitioner playbook, not an audited case.
- Whether the "only 10% of teams scale AI agents" figure in the Fullcast headline is sourced to McKinsey was not verified.
- No sourced data on realistic team sizes or agent-to-human ratios.

## 7. What are the ad platforms' own agentic features in 2026, and how should custom agents complement them?

### Takeaway
All three platforms now ship their own agents: Google's Ask Advisor (announced 20 May 2026), TikTok's Symphony Agent and Smart+ upgrades (May-June 2026), and Meta's Advantage+ with a reported but unconfirmed end-2026 target for fully automated ads. Platform agents optimise inside one walled garden, so custom agents add most value across platforms and on first-party data.

### Cited Findings

Google
- Google Marketing Live was held 20 May 2026. Ask Advisor is a Gemini-powered agent spanning Google Ads, Google Analytics, Merchant Center and Google Marketing Platform; it follows Ads Advisor, which launched May 2025, reached 50% of eligible users in September 2025 and full English availability in December 2025 — [PPC Land](https://ppc.land/googles-ask-advisor-unifies-ads-analytics-and-commerce-in-one-ai-agent/)
- Ask Advisor is reported to be in English beta with full rollout by late 2026; the underlying Gemini variant is not disclosed (single secondary source) — [TechWyse](https://www.techwyse.com/news/business/google-marketing-live-2026-ask-advisor-ai-mode-ads-ucp)
- Other announcements covered: an "AI Brief" advertiser control, AI Mode ad formats in testing, Business Agent for Leads, Asset Studio, Meridian in Analytics 360, and an expanded Universal Cart with the Universal Commerce Protocol — [Brainlabs](https://www.brainlabsdigital.com/google-marketing-live-2026/); [Google blog collection](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/)

Meta
- The Wall Street Journal reported in 2025 that Meta aims to let brands fully create and target ads with AI by the end of 2026, with advertisers supplying little more than a product image and budget; sources differ on whether this was an official announcement or a report — [Campaign Asia](https://www.campaignasia.com/article/meta-aims-to-fully-automate-ad-creation-with-ai-by-2026/502831)
- Current Advantage+ automates targeting and budgets but requires uploaded assets; the planned system would generate creatives from a URL — [Dataslayer](https://www.dataslayer.ai/blog/meta-plans-full-ai-advertising-automation-by-2026-what-this-actually-means)
- A third-party guide says the URL-to-campaign system is being tested with select advertisers (undated, unverified) — [Digital Applied](https://www.digitalapplied.com/blog/meta-ai-automated-ads-2026-marketing-guide)
- Meta's official MCP server (open beta 29 April 2026) lets external agents such as Claude, ChatGPT and Perplexity manage campaigns — [Digital Applied, 7 June 2026](https://www.digitalapplied.com/blog/official-ads-mcp-servers-meta-google-tiktok-2026-playbook)

TikTok
- TikTok World, 13 May 2026: Smart+ gained Auto Selection, which pools advertiser assets, creator content and Symphony creatives and picks the best performers; Music Autofix was added for Smart+ App campaigns — [TechWyse](https://www.techwyse.com/news/platform-updates/tiktok-world-2026-new-ad-tools-ai-mcp-travel-booking)
- Cannes Lions, June 2026: TikTok launched Symphony Agent, which combines campaign goals with trend and top-video insights to build campaigns inside Symphony Creative Studio, Content Suite and TikTok One; ByteDance's Seedance 2.0 video model was integrated into Symphony; Dentsu is integrating Symphony into its Zoyumi platform — [Communicate Online](https://communicateonline.me/news/tiktok-launches-ai-powered-symphony-agent-expands-creative-tools-across-mena/); [Shopifreaks](https://www.shopifreaks.com/tiktok-unveils-symphony-ai-ad-agent-at-cannes-integrates-with-dentsus-zoyumi-platform-and-launches-custom-creator-networks-with-starbucks/)
- October 2026: TikTok's newsroom announced further updates including a Smart+ workflow consolidating creative sources into one approval flow — [TikTok Newsroom](https://newsroom.tiktok.com/?lang=en&tag=safety)

Industry direction
- Axios (13 January 2026) reports AI agents buying and selling ads on behalf of marketers are driving a new growth era for advertising — [Axios](https://www.axios.com/media-trends-membership/2026/01/13/ai-agents-advertising-automation)

### Inferences
- Division of labour: leave in-platform bidding, targeting, creative selection and within-campaign budget distribution to Smart+, Advantage+ and Performance Max/App campaigns. Custom agents should own what platforms cannot see or will not do impartially: cross-platform budget allocation, MMP- and warehouse-based truth (incrementality, LTV-based ROAS), creative strategy and supply into the platforms' selection systems, policy and brand pre-checks, anomaly detection, and lifecycle and commerce actions.
- Platform agents grade their own performance; an independent analytics team reading MMP and warehouse data is the check on platform-reported results.
- Since platforms increasingly select creative automatically (Smart+ Auto Selection), the custom creative team's output is volume and diversity of on-brand concepts, not manual ad-level optimisation.
- Platform MCP servers mean custom agents can call platform capabilities as tools instead of rebuilding them; the engine should treat platform agents as specialists it delegates to.

### Gaps
- No confirmation was found, as of 14 November 2026, of whether Meta has launched or delayed its fully automated ads system; Meta's newsroom was not checked directly.
- Meta's "Business AI" product was not specifically researched; no findings are cited for it.
- TikTok's primary TikTok World announcement could not be read (HTTP 503); TikTok details rest on trade press.
- Google's primary Marketing Live post was not read in full; Ask Advisor's current rollout status in November 2026 is unverified.
- No source was found comparing platform-native agents with custom agents on measured performance.
