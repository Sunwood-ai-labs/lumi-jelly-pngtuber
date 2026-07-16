# Lumi Jelly Head Motion — Image Gen production avatar

`Lumi Jelly Head Motion` is a separate head-only variant designed for strong
mouse/camera head movement. It does not replace the full-body `Lumi Jelly`.

- Every visible runtime state is an actual Image Gen output or an
  identity-preserving Image Gen edit.
- Five Image Gen directions (front/left/right/up/down) each provide six runtime
  frames covering open/closed eyes and closed/half/full mouth: 30 frames total.
- Every left/right/up/down master was generated directly from the approved
  frontal master. Direction pixels are not Canvas warps, translated crops, or
  mirrored frames.
- No neck, shoulders, torso, clothing, or bust is present.
- Mouse/camera follow, subtle roll, idle, breathing, 140 ms direction settling,
  and 70 ms mouth blending are enabled. The settling logic keeps continuous
  direction weights but renders one dominant generated frame at a time, avoiding
  double faces during rapid movement. Canvas face-mesh deformation is disabled
  for this profile so the generated directional artwork remains intact.
- Front/back hair PNGs are transparent compatibility layers because the complete
  head and tentacle hair are contained in every generated expression frame.

Rebuild without redrawing:

```bash
./scripts/render_lumi_head_motion_assets.sh
```

Untouched outputs and prompts are retained under `imagegen-v1/`. Directional
runtime assets are under `directions/<left|right|up|down>/`.
