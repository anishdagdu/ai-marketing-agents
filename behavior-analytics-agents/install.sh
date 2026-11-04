#!/bin/bash
# Installs the 12 behaviour analytics agents (incl. the JEV model router) and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/behavior-insights-workflow ~/.claude/skills/
echo "Installed 12 agents + behavior-insights-workflow. Start a new Claude Code session to use them."
