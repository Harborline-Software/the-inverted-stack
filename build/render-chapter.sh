#!/usr/bin/env bash
# render-chapter.sh — generate audiobook MP3 for a single chapter.
#
# Usage:
#   ./build/render-chapter.sh <chapter-slug> [--preset <name>]
#
# Examples:
#   ./build/render-chapter.sh ch01-departure
#   ./build/render-chapter.sh ch05-day-twenty-realization --preset ciufi-galeazzi
#
# What it does:
#   - Resolves the Chatterbox TTS server (Tailscale FQDN, port 8883).
#   - Disables the per-chapter preset map so --preset wins (the map otherwise
#     overrides ciufi-galeazzi to female-solo for some chapters).
#   - Runs under `caffeinate -disu` to block display, idle, and system sleep
#     while the render is in flight (typical chapter is 30-90 minutes wall
#     clock with the cloned voice).
#   - Detaches via nohup so closing the controlling shell (or the agent
#     process that launched this script) does not kill the render.
#   - Logs to build/output/audiobook/_logs/<chapter>-<timestamp>.log
#
# Requires:
#   - TTS_API_KEY set in the environment (Bearer token for the TTS server)
#   - Python 3 with the deps audiobook.py imports (openai, mutagen, ...)
#   - The Chatterbox server reachable at the URL below
#
# The script exits as soon as the background render is launched. Tail the
# log file printed at the end to follow progress.

set -euo pipefail

# ---- defaults (the flags-of-record from .wolf/cerebrum.md) ----
BASE_URL="http://desktop-umt08rn:8883/api/v1"
PRESET="ciufi-galeazzi"
ENGINE="chatterbox"

# ---- arg parsing ----
if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <chapter-slug> [--preset <name>] [--base-url <url>]" >&2
  echo "  e.g.: $0 ch01-departure" >&2
  exit 2
fi

CHAPTER="$1"; shift
while [[ $# -gt 0 ]]; do
  case "$1" in
    --preset)   PRESET="$2"; shift 2 ;;
    --base-url) BASE_URL="$2"; shift 2 ;;
    --engine)   ENGINE="$2"; shift 2 ;;
    *) echo "unknown flag: $1" >&2; exit 2 ;;
  esac
done

# ---- preflight ----
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

if [[ -z "${TTS_API_KEY:-}" ]]; then
  echo "ERROR: TTS_API_KEY is not set. Export it before running:" >&2
  echo "  export TTS_API_KEY=<bearer-token>" >&2
  exit 1
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 not found in PATH" >&2
  exit 1
fi

# Quick reachability probe — fail fast if the server is down rather than
# 30+ minutes into a render.
HTTP=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$BASE_URL" || echo "000")
if [[ "$HTTP" == "000" ]]; then
  echo "ERROR: TTS server $BASE_URL is unreachable (no HTTP response)." >&2
  echo "  Check Tailscale, the Windows GPU box, and the chatterbox-tts service." >&2
  exit 1
fi
echo "Server probe: HTTP $HTTP at $BASE_URL"

# ---- launch ----
LOG_DIR="$REPO_ROOT/build/output/audiobook/_logs"
mkdir -p "$LOG_DIR"
TS=$(date +%Y%m%d-%H%M%S)
LOG_FILE="$LOG_DIR/${CHAPTER}-${TS}.log"

echo "Rendering chapter: $CHAPTER"
echo "  engine:   $ENGINE"
echo "  preset:   $PRESET"
echo "  base-url: $BASE_URL"
echo "  log:      $LOG_FILE"
echo

# nohup + caffeinate -disu + & so the render survives:
#   - shell exit / agent process death (nohup ignores SIGHUP)
#   - laptop sleep / display sleep / idle suspend (caffeinate flags)
nohup caffeinate -disu python3 build/audiobook.py \
  --engine "$ENGINE" \
  --base-url "$BASE_URL" \
  --preset "$PRESET" \
  --no-chapter-map \
  --force \
  --per-sentence \
  --only "$CHAPTER" \
  > "$LOG_FILE" 2>&1 &

PID=$!
echo "Started PID $PID. Render is running detached."
echo
echo "Follow progress:"
echo "  tail -f $LOG_FILE"
echo
echo "Output (written incrementally):"
echo "  build/output/audiobook/vol-*/${CHAPTER}.mp3"
