#!/bin/bash
# serve-live.sh — static file server + POST /save endpoint for overview edits.
#
# Usage:
#   serve-live.sh <topic-dir> [port]
#
# Falls back to python3 → python. Requires Python 3.

set -e

TOPIC="${1:-}"
PORT="${2:-8765}"

if [ -z "$TOPIC" ]; then
  echo "Usage: serve-live.sh <topic-dir> [port]"
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY_SCRIPT="$SCRIPT_DIR/serve-live.py"

if [ ! -f "$PY_SCRIPT" ]; then
  echo "serve-live.py not found at $PY_SCRIPT"
  exit 1
fi

if command -v python3 > /dev/null 2>&1; then
  exec python3 "$PY_SCRIPT" "$TOPIC" "$PORT"
elif command -v python > /dev/null 2>&1; then
  exec python "$PY_SCRIPT" "$TOPIC" "$PORT"
else
  echo "Python 3 is required to run serve-live.py"
  exit 1
fi
