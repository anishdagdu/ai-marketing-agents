#!/bin/bash
# Installs the 12 Amazon Ads agents and the workflow skill into Claude Code.
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
mkdir -p ~/.claude/agents ~/.claude/skills
cp "$DIR"/agents/*.md ~/.claude/agents/
cp -R "$DIR"/workflow/amazon-ads-workflow ~/.claude/skills/
echo "Installed 12 agents + amazon-ads-workflow. Start a new Claude Code session to use them."
