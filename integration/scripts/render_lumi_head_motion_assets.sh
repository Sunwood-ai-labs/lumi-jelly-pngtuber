#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$ROOT/scripts/prepare_lumi_head_motion_assets.py"
echo "Prepared Image Gen Lumi Jelly Head Motion assets"
