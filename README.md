# Lumi Jelly for PuruPuru PNGTuber

[English](./README.md) | [日本語](./README.ja.md)

An original celestial jellyfish PNGTuber character with two production-ready
variants: the original avatar and a head-only five-direction motion avatar.
Image Gen sources are preserved and both variants are verified in PuruPuru
PNGTuber.

<p align="center">
  <img src="./avatar/concept.png" width="520" alt="Lumi Jelly, an aqua-and-lavender celestial jellyfish PNGTuber avatar">
</p>

<p align="center">
  <img alt="Six expression PNGs" src="https://img.shields.io/badge/Expressions-6-6c63ff">
  <img alt="Five generated directions" src="https://img.shields.io/badge/Head%20Motion-5%20directions-5865f2">
  <img alt="Thirty head motion states" src="https://img.shields.io/badge/Head%20States-30-8b5cf6">
  <img alt="1024 by 1024 pixels" src="https://img.shields.io/badge/Canvas-1024%C3%971024-20a4c8">
  <img alt="Image Gen source preserved" src="https://img.shields.io/badge/Image%20Gen-source%20preserved-8b5cf6">
  <img alt="PuruPuru ready" src="https://img.shields.io/badge/PuruPuru-ready-f06b47">
</p>

## Head-only directional motion variant

`Lumi Jelly Head Motion` contains no neck, shoulders, torso, clothing, or bust.
Its left, right, up, and down masters were each generated directly from the
approved frontal Image Gen master—never mirrored, warped, or derived from a
different direction. Every direction has six eye/mouth states, for 30 generated
runtime frames total.

![All 30 head-only direction and expression states](./docs/screenshots/head-motion/all-30-runtime-states.png)

The app renders one dominant generated direction at a time. A 140 ms continuous
direction-weight settle prevents input chatter without crossfading whole faces,
so rapid movement does not create double eyes or double mouths.

![Rapid left, right, up, down, and front movement in the real app](./docs/screenshots/head-motion/rapid-direction-cycle.gif)

Verified real-app states are also preserved individually under
[`docs/screenshots/head-motion/`](./docs/screenshots/head-motion/), including
left/right/up/down, speaking, and blinking screenshots. The original-size
`6144 × 5290` QA sheet keeps every runtime state at its native `1024 × 1024`
resolution.

## Preview

![Lumi Jelly shown with closed, half-open, and fully open mouth states](./avatar/expression-preview.png)

Closed, half-open, and fully open mouth states are supplied for both open and
closed eyes. All runtime PNG files share the same transparent `1024 × 1024`
canvas and alignment.

## Verified in the app

![Lumi Jelly shown in three verified PuruPuru PNGTuber states](./docs/screenshots/lumi-jelly-screenshot-proof-v2.png)

The final build was checked in the real app UI:

- character profile: `Lumi Jelly / 保存済み`;
- closed mouth: `口: とじ`;
- half-open mouth: `口: はんびらき`;
- fully open mouth: `口: ぜんかい`;
- 52 upstream integration tests passed; and
- an independent full-resolution visual audit passed.

## Use with PuruPuru PNGTuber

1. Clone [PuruPuru PNGTuber](https://github.com/rotejin/PuruPuruPNGTuber).
2. Run the installer with the absolute path to that checkout:

   ```bash
   ./tools/install_into_purupuru.sh /absolute/path/to/PuruPuruPNGTuber
   ```

3. Start PuruPuru PNGTuber with `./run_local_server.sh` and select
   **Lumi Jelly** or **Lumi Jelly Head Motion** from the character switcher.

The patch adds automatic profile registration and the corresponding static
tests. It was produced against upstream tag `v0.1.0` (`9dc1e73`). If upstream
changes make the patch fail, use the files in `avatar/` as the authoritative
character package and port the small registration block manually.

## Repository contents

```text
avatar/                 Runtime PNGs, settings, concept, expression preview
head-motion/avatar/     Head-only runtime PNGs plus preserved Image Gen sources
provenance/source/      Untouched Image Gen outputs on chroma background
provenance/keyed/       Background-removed intermediate PNGs
provenance/PROMPTS.md   Master and identity-preserving edit prompts
tools/                  Normalization and installation utilities
integration/            Context-checked PuruPuru patch (`.patch.gz`) and target scripts
docs/screenshots/       Final full-app verification evidence
SHA256SUMS              Integrity manifest for published files
```

The rejected low-quality SVG experiment and obsolete Canvas-warp diagnostic
screenshots are intentionally excluded from this public repository.

## Rebuild runtime PNGs

The keyed intermediates can be normalized back into the aligned runtime files:

```bash
python3 -m pip install Pillow
./tools/render_lumi_jelly_assets.sh
./tools/render_lumi_head_motion_assets.sh
```

This step performs resizing, transparent padding, and compatibility-layer
generation only. It does not redraw or replace the Image Gen character.

## Provenance

- Created on 2026-07-15 with OpenAI's built-in Image Gen tool.
- One approved master was edited with identity-preserving prompts to create six
  eye/mouth states.
- Untouched outputs and prompt records are retained under `provenance/`.
- Head-motion sources, keyed intermediates, direction lineage, and prompt
  records are retained under `head-motion/avatar/imagegen-v1/`.
- Runtime processing is limited to chroma-key removal, padding, and resizing.
- No named artist, existing character, or third-party character asset was used
  as a prompt reference.

## License and credits

- Lumi Jelly artwork and image sources: see [LICENSE-ASSETS.md](./LICENSE-ASSETS.md).
- Code under `tools/` and `integration/`: Apache License 2.0, see
  [LICENSE-CODE](./LICENSE-CODE). Upstream-derived patch context retains its
  upstream attribution.
- Target app: [PuruPuru PNGTuber](https://github.com/rotejin/PuruPuruPNGTuber)
  by masa. The app is not bundled here.

OpenAI's terms govern the relationship between the user and OpenAI for the
generated output; they do not guarantee copyright availability or third-party
non-infringement in every jurisdiction.
