# CRM Agents: Lottery & Gaming CRM with Responsible-Gaming Guardrails

![CRM Agents architecture](docs/crm-agents-architecture.gif)

Ten Claude Code agents, five skills and one workflow skill for Optimove-style CRM. They share one data layer (gaming platform, retail loyalty card, app/web events, payments and RG limits) and follow one rule: **the Responsible Gaming Guardian can stop any message before it is sent.**

> **AI recommends. You approve.** The agents write journeys, triggers, copy and send lists as **drafts**. People approve new journeys and any change to RG thresholds or caps. The agents never send messages themselves: the final send list goes to your CRM or ESP platform. Every decision is logged with a reason, for the gambling regulator and GDPR.

## How it works

| # | Agent | What it does | Key rule |
|---|---|---|---|
| 1 | [`crm-player-360`](agents/crm-player-360.md) | Merges identities into one profile and builds micro-segments | Keeps RG fields on every profile |
| 2 | [`crm-predictive-scoring`](agents/crm-predictive-scoring.md) | 30-day churn risk, 12-month LTV, next best action | High RG risk → care message, never an offer |
| 3 | [`crm-journey-orchestrator`](agents/crm-journey-orchestrator.md) | Turns a goal in plain language into a multi-step journey | Draft only, 5–10% control group |
| 4 | [`crm-realtime-trigger`](agents/crm-realtime-trigger.md) | First deposit, win, ticket, jackpot threshold, limit reached | No promotion for 7 days after "limit reached" |
| 5 | [`crm-uplift-analyst`](agents/crm-uplift-analyst.md) | Uplift against control and a global holdout, with confidence intervals | No uplift for 2 cycles → flag to stop |
| 6 | [`crm-test-optimiser`](agents/crm-test-optimiser.md) | Bandit tests on channel, timing, subject line and creative | Optimises uplift, never spend |
| 7 | [`crm-personalisation`](agents/crm-personalisation.md) | Ranks games and content, writes copy in fi/sv/en | RG-flagged players get non-promotional content |
| 8 | [`crm-rg-guardian`](agents/crm-rg-guardian.md) | **Scores RG risk live, vetoes promotions, escalates to player care** | Target: 0% of at-risk players sent a promotion |
| 9 | [`crm-contact-policy`](agents/crm-contact-policy.md) | Max 3 promotions a week, quiet hours, channel priority | Highest predicted uplift wins |
| 10 | [`crm-insights-calendar`](agents/crm-insights-calendar.md) | Campaign calendar, weekly summary, "why did X drop?" | — |

### Skills

| Skill | Used by | What it does |
|---|---|---|
| [`rg-risk-check`](skills/rg-risk-check/SKILL.md) | RG Guardian, Scoring, Triggers | Five-signal RG score, band and reason |
| [`contact-policy-check`](skills/contact-policy-check/SKILL.md) | Contact Policy, Triggers | Caps, quiet hours, uplift tie-break |
| [`uplift-readout`](skills/uplift-readout/SKILL.md) | Uplift Analyst | Runs `uplift.py`: uplift, 95% CI, incremental revenue, sample size |
| [`journey-design`](skills/journey-design/SKILL.md) | Journey Orchestrator | Journey spec template and ready-made patterns |
| [`crm-copywriter`](skills/crm-copywriter/SKILL.md) | Personalisation | Responsible copy in fi/sv/en within channel limits |

The [`crm-agents-workflow`](workflow/crm-agents-workflow/SKILL.md) skill runs everything in order: Player 360 → scoring → journeys and triggers (you approve) → RG Guardian → contact policy → personalisation → hand-off → uplift, tests and weekly insights. It stops at step 1 if RG-limit data is missing, because nothing can be sent safely without it.

## Example: player at risk of churning

1. **Scoring:** churn risk jumps from 0.30 to 0.75 after 3 missed weekly draws
2. **RG Guardian:** low risk, so the flow continues (high risk → care message, stop)
3. **Contact Policy:** 1 message this week, so a send is allowed
4. **Orchestrator:** starts a win-back journey with 10% held back as control
5. **Personalisation:** their usual game (Lotto) plus the next jackpot as the hook
6. **Test Optimiser:** push against email, evening against morning
7. **Uplift Analyst:** after 14 days, reports the lift in reactivation against control
8. **Insights:** adds the result to the weekly summary and suggests making it always-on

## Requirements

- [Claude Code](https://claude.com/claude-code)
- Data exports in a `data/` folder (or warehouse access): transactions, gameplay, retail card, app/web events, payments, RG limits, consents
- Python 3.9+ for the uplift script and the demo simulator

## Install

```bash
bash install.sh
```

Then, in a new Claude Code session, say **"run the CRM workflow"**. Or ask for one step, for example "who is about to churn", "build a shop-to-app journey" or "is this campaign safe to send".

## Try it without data

`simulator/crm_agents.py` runs all 10 agents in Python on 400 simulated players. It prints a weekly summary, checks that no at-risk player got a promotion, and writes `audit_log.json`.

```bash
python3 simulator/crm_agents.py
```

## Files

- `agents/`: the 10 agent definitions
- `skills/`: the 5 shared skills (`uplift-readout` includes `scripts/uplift.py`)
- `workflow/crm-agents-workflow/SKILL.md`: the orchestrator skill
- `simulator/crm_agents.py`: runnable demo of the whole system
- `docs/crm-agents-architecture.gif`: architecture animation
- `docs/make_gif.py`: regenerates the GIF (needs Pillow)
