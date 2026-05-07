#!/usr/bin/env bash
# HyperFrames Overview — local HTTP server
#
# file://로 overview.html을 열면 이미지·폰트·캔버스 작업에서 CORS 에러가 날 수 있다.
# 이 스크립트는 topic 폴더를 루트로 삼아 정적 HTTP 서버를 띄워 http:// 컨텍스트에서
# overview.html을 열 수 있게 한다.
#
# Usage:
#   bash .codex/skills/hyperframes-overview/serve.sh <topic-path> [port]
#
# Examples:
#   bash .codex/skills/hyperframes-overview/serve.sh topics/apple-history
#   bash .codex/skills/hyperframes-overview/serve.sh topics/apple-history 8765

set -euo pipefail

TOPIC="${1:-}"
PORT="${2:-8765}"

if [ -z "$TOPIC" ]; then
  echo "Usage: bash serve.sh <topic-path> [port]" >&2
  exit 1
fi
if [ ! -d "$TOPIC" ]; then
  echo "Topic directory not found: $TOPIC" >&2
  exit 1
fi
if [ ! -f "$TOPIC/overview.html" ]; then
  echo "overview.html not found in $TOPIC — hyperframes-overview 스킬로 먼저 생성하세요." >&2
  exit 1
fi

echo "Serving $TOPIC on http://localhost:$PORT/overview.html"
echo "Press Ctrl+C to stop."

cd "$TOPIC"
if command -v python3 >/dev/null 2>&1; then
  exec python3 -m http.server "$PORT"
elif command -v python >/dev/null 2>&1; then
  exec python -m http.server "$PORT"
elif command -v npx >/dev/null 2>&1; then
  exec npx --yes serve -p "$PORT" -l "$PORT" .
else
  echo "python3 / python / npx 중 아무것도 없어 서버를 띄울 수 없습니다." >&2
  exit 1
fi
