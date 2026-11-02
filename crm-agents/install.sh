#!/bin/bash
# Installs the 12 CRM agents, 5 skills and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/skills/* ~/.claude/skills/
cp -R "$DIR"/workflow/crm-agents-workflow ~/.claude/skills/
echo "Installed 12 agents, 5 skills + crm-agents-workflow. Start a new Claude Code session to use them."
