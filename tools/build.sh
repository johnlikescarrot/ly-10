#!/usr/bin/env bash
# Build the review-outline PDF from the markdown-ish content in tools/content/.
#
#   ./tools/build.sh [output.pdf]
#
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(dirname "$HERE")"
OUT="${1:-$ROOT/DeCuongOnTap-KTGK1-VatLi10-2026-2027.pdf}"
VENV="$ROOT/.pdfenv"

if [ ! -d "$VENV" ]; then
  echo "==> Creating build virtualenv"
  python3 -m venv "$VENV"
fi

echo "==> Installing dependencies"
"$VENV/bin/pip" install --quiet --upgrade pip
"$VENV/bin/pip" install --quiet -r "$HERE/requirements.txt"

echo "==> Rendering PDF"
"$VENV/bin/python" "$HERE/render.py" "$HERE/content" "$OUT"

echo "==> Done: $OUT"
