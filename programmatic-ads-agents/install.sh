#!/bin/bash
# Installs the 20 programmatic agents (incl. the JEV model router) and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/programmatic-growth-workflow ~/.claude/skills/
echo "Installed 20 agents + programmatic-growth-workflow. Start a new Claude Code session to use them."
