#!/usr/bin/env bash
# HyperFrames Overview — local HTTP server with live edit saving
#
# file://로 overview.html을 열면 이미지·폰트·캔버스 작업에서 CORS 에러가 날 수 있다.
# 이 스크립트는 topic 폴더를 루트로 삼아 정적 HTTP 서버를 띄워 http:// 컨텍스트에서
# overview.html을 열 수 있게 한다.
#
# 최신 overview.html 의 Edit 버튼은 Done 시 POST /save 로 변경사항을 저장한다.
# 그래서 기본 서버도 hyperframes-overview-edit/serve-live.sh 로 위임한다.
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

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIVE_SERVE="$SCRIPT_DIR/../hyperframes-overview-edit/serve-live.sh"

if [ ! -x "$LIVE_SERVE" ]; then
  echo "Live overview server not found: $LIVE_SERVE" >&2
  exit 1
fi

exec "$LIVE_SERVE" "$TOPIC" "$PORT"
