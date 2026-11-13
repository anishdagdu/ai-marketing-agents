#!/bin/bash
# Installs the 76 AvantStay agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/avantstay-growth-workflow ~/.claude/skills/
echo "Installed 76 agents + avantstay-growth-workflow. Start a new Claude Code session to use them."
