#!/usr/bin/env bash
# Install these agents into another project (or ~/.claude for all projects).
# Usage: scripts/deploy.sh /path/to/project   (default: ~/.claude)
set -euo pipefail
cd "$(dirname "$0")/.."
TARGET="${1:-$HOME/.claude}"
[ "$TARGET" = "$HOME/.claude" ] || TARGET="$TARGET/.claude"
mkdir -p "$TARGET/agents"
cp src/agents/*.md "$TARGET/agents/"
echo "Copied agents to $TARGET/agents"
