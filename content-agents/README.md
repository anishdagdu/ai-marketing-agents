# Content Agents

Five Claude Code agents that build a social media content calendar from real sentiment research, then schedule it in [Postiz](https://github.com/gitroomhq/postiz-app), the open-source social media scheduler.

![Content agents workflow](content-agents-workflow.png)

> **AI recommends. You approve.** Nothing is scheduled until you say yes, and the publisher always does a dry run first.

## The agents

| Agent | What it does | Output |
|---|---|---|
| `content-orchestrator` | Runs the workflow, stops at 2 approval checkpoints, and reports what needs a human | Summary |
| `website-sentiment-analyst` | Covers your website's promise and tone plus 10+ reviews and mentions. Gives a sentiment score (−1 to +1) and shows where what you promise differs from what customers say | `output/website_sentiment.md/.json` |
| `competitor-sentiment-analyst` | Covers each competitor's positioning, content, what customers love and complain about, and topics no competitor covers | `output/competitor_sentiment.md/.json` |
| `content-calendar-planner` | Writes the strategy, weekly themes and ready-to-post copy for each platform, with a visual brief for each post | `output/content_calendar.json/.csv/.md` |
| `postiz-publisher` | Matches posts to Postiz channels, does a dry run, then schedules once you approve | `output/postiz_schedule_log.json` |

**Workflow:** config → website and competitor research (run at the same time) → checkpoint 1: review the insights → calendar plan → checkpoint 2: approve before posting → publish to Postiz.

## Install

```bash
./install.sh
```

1. Copy `config.yaml` into your project and fill in your brand, website pages, competitors, social handles, posts per week, content themes and key dates.
2. *(Optional, for scheduling)* Set your Postiz API key. You'll find it in Postiz under Settings → Public API.
   ```bash
   export POSTIZ_API_KEY=...
   # self-hosted Postiz only:
   export POSTIZ_API_URL=https://your-postiz-domain/api/public/v1
   ```
3. In Claude Code, ask: **"Run the content orchestrator for 4 weeks."**

You can also run a single agent, for example *"use the competitor-sentiment-analyst"*.

## Quality rules built into the agents

- Uses evidence only: no invented stats, reviews or quotes, and every finding cites its source.
- Shows a confidence level and flags thin evidence (fewer than 5 mentions).
- Writes copy natively for each platform and never reuses the same text across platforms.
- Uses a set content mix: 40% value, 20% proof, 15% objections, 15% behind the scenes, 10% offer.
- Links every post to a real research insight.

## Files

```
content-agents/
├── agents/                        # 5 agent files
├── config.yaml                    # your brand, competitors, handles
├── install.sh
└── content-agents-workflow.png
```

## Requirements

- [Claude Code](https://claude.com/claude-code) with web search and web fetch
- A [Postiz](https://postiz.com) account (cloud or self-hosted), only needed for scheduling
