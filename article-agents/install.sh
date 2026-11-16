#!/bin/bash
# Installs the 6 article agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/article-creation-workflow ~/.claude/skills/
echo "Installed 6 agents + article-creation-workflow. Start a new Claude Code session to use them."
