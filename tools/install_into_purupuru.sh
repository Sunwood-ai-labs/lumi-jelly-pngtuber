#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TARGET="${1:-}"
PATCH_FILE="$(mktemp "${TMPDIR:-/tmp}/lumi-jelly-patch.XXXXXX")"
trap 'rm -f "$PATCH_FILE"' EXIT

gzip -dc "$ROOT/integration/purupuru-lumi-jelly.patch.gz" > "$PATCH_FILE"

if [[ -z "$TARGET" || ! -f "$TARGET/app.js" || ! -d "$TARGET/tests" ]]; then
  echo "Usage: $0 /absolute/path/to/PuruPuruPNGTuber" >&2
  exit 2
fi

if [[ -e "$TARGET/assets/lumi-jelly" ]]; then
  echo "Refusing to overwrite existing $TARGET/assets/lumi-jelly" >&2
  exit 3
fi

for path in \
  "$TARGET/scripts/prepare_lumi_imagegen_assets.py" \
  "$TARGET/scripts/render_lumi_jelly_assets.sh"; do
  if [[ -e "$path" ]]; then
    echo "Refusing to overwrite existing $path" >&2
    exit 3
  fi
done

git -C "$TARGET" apply --check "$PATCH_FILE"

mkdir -p "$TARGET/assets/lumi-jelly/imagegen-v2/source"
mkdir -p "$TARGET/assets/lumi-jelly/imagegen-v2/keyed"

cp "$ROOT"/avatar/*.png "$TARGET/assets/lumi-jelly/"
cp "$ROOT/avatar/default-settings.json" "$TARGET/assets/lumi-jelly/"
cp "$ROOT/avatar/ASSET_NOTICE.md" "$TARGET/assets/lumi-jelly/"
cp "$ROOT/LICENSE-ASSETS.md" "$TARGET/assets/lumi-jelly/ASSET_LICENSE.md"
cp "$ROOT/provenance/PROMPTS.md" "$TARGET/assets/lumi-jelly/imagegen-v2/"
cp "$ROOT"/provenance/source/*.png "$TARGET/assets/lumi-jelly/imagegen-v2/source/"
cp "$ROOT"/provenance/keyed/*.png "$TARGET/assets/lumi-jelly/imagegen-v2/keyed/"
cp "$ROOT/integration/scripts/prepare_lumi_imagegen_assets.py" "$TARGET/scripts/"
cp "$ROOT/integration/scripts/render_lumi_jelly_assets.sh" "$TARGET/scripts/"
chmod +x "$TARGET/scripts/render_lumi_jelly_assets.sh"

git -C "$TARGET" apply "$PATCH_FILE"

echo "Installed Lumi Jelly into $TARGET"
echo "Run: python3 -m unittest discover -s tests -q"
