#!/bin/bash
# Installs the 139 Carry1st agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/carry1st-growth-workflow ~/.claude/skills/
echo "Installed 139 agents + carry1st-growth-workflow. Start a new Claude Code session to use them."
