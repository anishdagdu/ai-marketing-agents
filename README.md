# AI Marketing Agents

Three sets of Claude Code agents for marketing teams, in one repo: **paid ads**, **search visibility** and **tracking health**.

> **AI recommends. You approve.** None of these agents launch campaigns, change budgets, edit pages or publish GTM changes. They write plans and reports; a human makes every change.

| Project | What it does | Agents |
|---|---|---|
| [AI Paid Traffic](ai-paid-traffic-agents/) | Runs paid ads end to end on Meta, Google and TikTok: research, strategy, creative, platform builds, tracking and scaling | 8 agents + 1 workflow |
| [AI Search Everywhere](ai-search-everywhere-agents/) | Visibility on Google and AI answer engines: SEO, AEO, GEO, AIO and SXO, with ranking targets and a weekly report | 7 agents + 8 skills |
| [GTM Health Agent](gtm-health-agent/) | Audits Google Tag Manager every Monday: flags tags that won't fire, explains why and recommends fixes | 1 weekly agent |

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

## How they fit together

- **Tracking first:** the GTM Health Agent keeps conversion data correct, which the paid-traffic scale agent and the search weekly report both rely on.
- **Paid + organic:** keyword research from AI Search Everywhere feeds Google Search campaigns in AI Paid Traffic, and paid search terms show which organic pages to build.
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

## License

Each project keeps its own license and notices. AI Search Everywhere is MIT; see its [LICENSE](ai-search-everywhere-agents/LICENSE) and [THIRD_PARTY_NOTICES](ai-search-everywhere-agents/THIRD_PARTY_NOTICES.md).
