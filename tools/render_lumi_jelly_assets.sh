#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"

python3 "$ROOT/tools/prepare_lumi_imagegen_assets.py"
echo "Prepared Image Gen Lumi Jelly assets"
