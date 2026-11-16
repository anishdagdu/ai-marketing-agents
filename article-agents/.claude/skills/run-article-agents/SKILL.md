---
name: run-article-agents
description: Test, validate, install or smoke-test the article-agents pack (6 ar-* agents + article-creation-workflow skill). Use when asked to run, check, verify, install or test the article agents, or after editing any file under article-agents/.
---

# Run article-agents

This unit is a **prompt pack**, not an app: 6 Claude Code subagents (`agents/ar-*.md`) and one orchestrator skill (`workflow/article-creation-workflow/SKILL.md`). "Running" it means validating the pack and installing it. The driver is `smoke.sh`. Paths below are relative to `article-agents/`.

## Run (agent path): the smoke driver

```bash
bash .claude/skills/run-article-agents/smoke.sh
```

It exits 0 and prints `SMOKE PASS` when all of these hold:
- 6 agent files; each has frontmatter where `name` matches the filename, a `description` of 60+ chars with a "Use when" trigger, a valid `model`, and an `outputs/articles/<slug>/` path
- the workflow skill invokes all 6 agents by name, and every numbered output (`01-brief.md` … `06-seo.md`) is written by an agent and mentioned in the skill
- the handoff chain holds: each agent reads the file the previous step writes
- `install.sh` runs into a **throwaway `HOME`** (your real `~/.claude` is untouched), installs 6 agents plus the skill, and a second run doesn't nest the skill directory

Each failure prints a `FAIL <file>: <reason>` line and the script exits 1.

## Install for real

```bash
./install.sh
```

This copies into `~/.claude/agents/` and `~/.claude/skills/`. Start a new Claude Code session, then say "run the article workflow on <topic>".

## Gotchas
- **Run it from `article-agents/`** or by full path. The script `cd`s to the unit itself, so either works; the relative paths in this file assume `article-agents/`.
- **The `claude` CLI wasn't on PATH** in the session that built this, so the smoke test checks structure only. It doesn't call a model. To exercise an agent for real, install the pack, open a new session, and ask for one step (e.g. "write a brief for <keyword>").
- **Frontmatter parsing is strict**: the file must start with `---` on line 1 and use `key: value` on a single line. A multi-line `description:` reads as empty and fails the length check.
- **Renaming an output file** (e.g. `05-final.md`) has to happen in both the producing agent, the consuming agent and the workflow skill, or the chain check fails. That's on purpose.
- **In zsh**, `${PIPESTATUS[0]}` is empty; use `$pipestatus[1]` or just read the `SMOKE PASS/FAIL` line.

## Troubleshooting
- `FAIL agents/X.md: name 'Y' != filename` → fix the `name:` line or rename the file. The installed agent is invoked by `name`.
- `FAIL publisher doesn't read 05-final` → an output filename drifted between agents; grep for the old name and align it.
