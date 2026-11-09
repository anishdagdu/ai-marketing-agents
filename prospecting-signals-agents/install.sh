#!/bin/bash
# Installs the 14 prospecting and signals agents (incl. the JEV router) and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/prospecting-signals-workflow ~/.claude/skills/
echo "Installed 14 agents + prospecting-signals-workflow. Start a new Claude Code session to use them."
