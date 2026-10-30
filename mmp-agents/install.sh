#!/bin/bash
# Installs the 21 MMP agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/mmp-growth-workflow ~/.claude/skills/
echo "Installed 21 agents + mmp-growth-workflow. Start a new Claude Code session to use them."
