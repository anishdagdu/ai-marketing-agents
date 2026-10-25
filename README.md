# AI Marketing Agents

Five sets of Claude Code agents for marketing teams, in one repo: **paid ads**, **search visibility**, **tracking health**, **social content** and **email/SMS from first-party data**.

> **AI recommends. You approve.** None of these agents launch campaigns, change budgets, edit pages, publish GTM changes or send emails. The content agents schedule posts only after you approve, and the Klaviyo agents save flows and campaigns as drafts. They write plans and reports; a human signs off on every change.

| Project | What it does | Agents |
|---|---|---|
| [AI Paid Traffic](ai-paid-traffic-agents/) | Runs paid ads end to end on Meta, Google and TikTok: research, strategy, creative, platform builds, tracking and scaling | 8 agents + 1 workflow |
| [AI Search Everywhere](ai-search-everywhere-agents/) | Visibility on Google and AI answer engines: SEO, AEO, GEO, AIO and SXO, with ranking targets and a weekly report | 7 agents + 8 skills |
| [GTM Health Agent](gtm-health-agent/) | Audits Google Tag Manager every Monday: flags tags that won't fire, explains why and recommends fixes | 1 weekly agent |
| [Content Agents](content-agents/) | Social media content calendar built from your own and your competitors' sentiment, scheduled through Postiz | 5 agents |
| [Klaviyo 1PD Agents](klaviyo-1pd-agents/) | High-converting email and SMS from first-party data: data audit, segments, revenue flows, campaigns and a weekly performance loop | 5 agents + 1 workflow |

## AI Paid Traffic

![AI Paid Traffic workflow](ai-paid-traffic-agents/ai-paid-traffic-workflow.png)

Research → Strategy (you approve) → Creative → Meta / Google / TikTok in parallel → Tracking → Scale.
[Read more and install →](ai-paid-traffic-agents/)

## AI Search Everywhere

![AI Search Everywhere workflow](ai-search-everywhere-agents/docs/ai-search-workflow-infographic.png)

SEO + AIO → AEO + GEO → SXO → Rankings → weekly report every Monday.
[Read more and install →](ai-search-everywhere-agents/)

## GTM Health Agent

![GTM Health Agent workflow](gtm-health-agent/gtm-agent-workflow.gif)

Weekly read-only GTM audit: 30+ checks, P0–P3 severity, health score per container, likely cause and fix, week-over-week comparison.
[Read more and set up →](gtm-health-agent/)

## Content Agents

![Content Agents workflow](content-agents/content-agents-workflow.png)

Website + competitor sentiment → content calendar (you approve) → schedule in Postiz.
[Read more and install →](content-agents/)

## Klaviyo 1PD Agents

![Klaviyo 1PD agents workflow](klaviyo-1pd-agents/klaviyo-agents-workflow.gif)

First-party data audit → segments (you approve) → revenue flows (drafts) → campaigns (drafts, you send) → weekly performance loop.
[Read more and install →](klaviyo-1pd-agents/)

## How they fit together

- **Tracking first:** the GTM Health Agent keeps conversion data correct, which the paid-traffic scale agent and the search weekly report both rely on.
- **Paid + organic:** keyword research from AI Search Everywhere feeds Google Search campaigns in AI Paid Traffic, and paid search terms show which organic pages to build.
- **Organic social:** the content agents' competitor research shares angles with the paid-traffic research agent; winning organic posts make good Spark Ads and creative tests.
- **First-party data:** the Klaviyo segment agent builds consented VIP and buyer seed audiences for paid-traffic lookalikes and exclusions, and GTM health keeps the onsite events Klaviyo flows trigger on firing.
- **One Monday routine:** GTM health report, search weekly report and paid-traffic Optimize mode can all run at the start of the week.

## Get everything

```bash
git clone https://github.com/anishdagdu/ai-marketing-agents.git
```

Then follow the install steps in each project's README.

## Requirements

- [Claude Code](https://claude.com/claude-code)
- AI Paid Traffic uses the 40 **AI for Paid Traffic** skills by HeyOz (not included)
- GTM Health Agent needs the Google Tag Manager MCP connector
- Content Agents can schedule through a [Postiz](https://github.com/gitroomhq/postiz-app) account (optional)

## License

Each project keeps its own license and notices. AI Search Everywhere is MIT; see its [LICENSE](ai-search-everywhere-agents/LICENSE) and [THIRD_PARTY_NOTICES](ai-search-everywhere-agents/THIRD_PARTY_NOTICES.md).
