#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$ROOT/tools/prepare_lumi_head_motion_assets.py"
python3 "$ROOT/tools/build_lumi_head_motion_contact_sheet.py"
echo "Prepared Image Gen Lumi Jelly Head Motion assets"
