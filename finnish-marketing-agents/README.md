# Finnish marketing AI agents

Native Finnish ad copy for Google, Meta, LinkedIn and Snapchat, plus an organic + paid content calendar built from website analysis, competitor sentiment and the Meta Ad Library. English ⇄ Finnish translation included.

| Agent (`src/agents/`) | What it does |
|---|---|
| `finnish-marketing-orchestrator` | Runs the whole workflow with approval gates |
| `finnish-content-calendar` | Research, strategy, calendar |
| `finnish-ads-copywriter` | Ad copy for every campaign type + translation |

```
.
├── CLAUDE.md            project overview, loaded every session
├── CLAUDE.local.md      personal overrides (not committed)
├── .mcp.json            MCP servers (Apify, Ahrefs… optional)
├── .claude/agents/      links to src/agents (so Claude Code loads them)
├── src/agents/ workflows/ tools/ utils/ types/
├── config/              settings.json, env.example
├── prompts/             system/ rules, templates/ brief
├── data/                input/, output/, examples/
├── scripts/             setup.sh, run.sh, deploy.sh
├── docs/                architecture.md, usage.md
└── tests/               test_agents.md, test_workflows.md
```

## Install

```bash
git clone https://github.com/anishdagdu/ai-marketing-agents.git
cd ai-marketing-agents/finnish-marketing-agents
./install.sh
```

Then say **"run the Finnish workflow"** in Claude Code. To work from this folder instead (with `CLAUDE.md`, helper scripts and the character checker), run `scripts/setup.sh`. See [docs/usage.md](docs/usage.md).

**AI recommends. You approve.** The agents stop at 4 approval gates and never publish, upload or launch anything.

## JEV model router
`finnish-jev-router` picks a model for every task before the orchestrator starts it: **Fast · Haiku** for lookups, checks and formatting, **Standard · Sonnet** for plans, writing and analysis, **Deep · Opus** for high-stakes or messy problems. It scores each task 0-2 on money at stake, ambiguity, reasoning depth, blast radius and novelty (0-2 fast, 3-5 standard, 6+ deep), starts low and escalates only on evidence, reuses outputs from the last 7 days, and caps deep work at 3 tasks per run. Every decision is logged to `outputs/jev-routing-log.csv`.
