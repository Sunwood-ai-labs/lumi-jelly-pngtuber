# Lumi Jelly PNGTuber

[English](./README.md) | [日本語](./README.ja.md) | [Head-motion edition](https://github.com/Sunwood-ai-labs/lumi-jelly-head-motion-pngtuber)

Lumi Jelly is an original celestial-jellyfish PNGTuber avatar rendered as a
front-facing upper body with an ornate navy-and-gold outfit. This repository is
the general-purpose six-expression edition. The separate head-motion edition
contains the head-only five-direction runtime and its PuruPuru integration patch.

<p align="center">
  <img src="./avatar/concept.png" width="520" alt="Lumi Jelly upper-body celestial-jellyfish PNGTuber avatar">
</p>

<p align="center">
  <img alt="Upper-body edition" src="https://img.shields.io/badge/Edition-upper%20body-5865f2">
  <img alt="Six expressions" src="https://img.shields.io/badge/Expressions-6-6c63ff">
  <img alt="1024 by 1024 pixels" src="https://img.shields.io/badge/Canvas-1024%C3%971024-20a4c8">
  <img alt="Image Gen source preserved" src="https://img.shields.io/badge/Image%20Gen-source%20preserved-8b5cf6">
</p>

## Preview

![Lumi Jelly's six eye and mouth states](./avatar/expression-preview.png)

The package combines open/closed eyes with closed, half-open, and fully open
mouths. All six visible runtime frames are aligned transparent `1024 × 1024`
PNGs. `back-hair.png` and `front-hair.png` are transparent compatibility layers;
the complete generated hair and costume remain in every expression frame.

## Use the avatar

Map the files in [`avatar/`](./avatar/) to the equivalent PNGTuber states:

| State | File |
| --- | --- |
| Eyes open, mouth closed | `eyes-open-mouth-closed.png` |
| Eyes open, mouth half open | `eyes-open-mouth-half.png` |
| Eyes open, mouth open | `eyes-open-mouth-open.png` |
| Eyes closed, mouth closed | `eyes-closed-mouth-closed.png` |
| Eyes closed, mouth half open | `eyes-closed-mouth-half.png` |
| Eyes closed, mouth open | `eyes-closed-mouth-open.png` |

[`avatar/default-settings.json`](./avatar/default-settings.json) records the
settings used for PuruPuru PNGTuber. The verified PuruPuru composite is kept at
[`docs/screenshots/lumi-jelly-screenshot-proof-v2.png`](./docs/screenshots/lumi-jelly-screenshot-proof-v2.png).

## Repository contents

```text
avatar/                 Six runtime PNGs, settings, concept, expression preview
provenance/source/      Untouched Image Gen outputs on chroma background
provenance/keyed/       Background-removed intermediate PNGs
provenance/PROMPTS.md   Master and identity-preserving edit prompts
tools/                  Deterministic normalization utilities
docs/screenshots/       Real-app verification evidence
SHA256SUMS              Integrity manifest for published files
```

Head-only direction assets, motion code, and rejected legacy experiments are
intentionally excluded from this repository.

## Rebuild runtime PNGs

```bash
python3 -m pip install Pillow
./tools/render_lumi_jelly_assets.sh
```

The rebuild only removes the chroma background, normalizes size and padding,
and writes compatibility layers. It does not redraw or replace the Image Gen
character.

## Head-motion edition

For a head-only avatar with front, left, right, up, and down artwork, 30 runtime
states, and a directional PuruPuru patch, use
[`lumi-jelly-head-motion-pngtuber`](https://github.com/Sunwood-ai-labs/lumi-jelly-head-motion-pngtuber).

## Provenance

- Created on 2026-07-15 with OpenAI's built-in Image Gen tool.
- One approved master was edited with identity-preserving prompts for six states.
- Untouched outputs, keyed intermediates, and prompts are retained in-repository.
- No named artist, existing character, or third-party character asset was used
  as a prompt reference.

## License and credits

- Artwork and Image Gen sources: [LICENSE-ASSETS.md](./LICENSE-ASSETS.md)
- Code under `tools/`: [LICENSE-CODE](./LICENSE-CODE)
- Verified target app: [PuruPuru PNGTuber](https://github.com/rotejin/PuruPuruPNGTuber) by masa

OpenAI's terms govern the relationship between the user and OpenAI for the
generated output; they do not guarantee copyright availability or third-party
non-infringement in every jurisdiction.
