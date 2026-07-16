# Lumi Jelly Head Motion Image Gen prompts

Renderer: OpenAI built-in Image Gen.

## Head-only master

The existing Lumi Jelly production master was supplied as the identity and
quality reference. Image Gen was asked to redesign her as a new motion-focused
floating head: complete jellyfish bell, face, fins, crescent ornament, chains,
and compact tentacle-hair silhouette, with absolutely no neck, collar,
shoulders, chest, torso, cape, clothing, or bust. The master used a perfectly
flat `#00ff00` chroma background, centered front view, generous padding, open
eyes, and closed mouth.

## Identity-preserving expression edits

Each edit repeated these invariants:

- preserve the exact head-only composition, face shape, jellyfish bell,
  tentacle silhouette, fin ears, crescent ornament, chains, jewels, colors,
  lighting, linework, framing, scale, and flat green background;
- change only the requested eyes or mouth;
- never add a neck, shoulders, torso, clothing, text, watermark, shadow,
  gradient, or extra object.

Requested states:

- eyes open, mouth closed: approved master;
- eyes open, mouth half open: small speaking mouth with dark interior, upper
  teeth, and pink tongue;
- eyes open, mouth fully open: clearly larger rounded vertical speaking mouth;
- eyes gently closed, mouth closed: symmetric happy curved lash lines;
- eyes gently closed, mouth half open: closed eyes preserved, small speaking
  mouth;
- eyes gently closed, mouth fully open: closed eyes preserved, clearly larger
  speaking mouth.

## Direct-from-front directional masters

The approved `eyes-open-mouth-closed` frontal master was attached separately to
four Image Gen edit calls. Each call preserved the complete floating-head
identity while asking for one genuine perspective change:

- `left`: about 35 degrees toward the viewer's left;
- `right`: about 35 degrees toward the viewer's right;
- `up`: about 20 degrees of upward pitch;
- `down`: about 20 degrees of downward pitch.

Every direction prompt explicitly prohibited planar warp, skew, translated
crop, mirroring, and using another direction as the reference. Head-only and
flat `#00ff00` background constraints were repeated in every call.

## Direction-specific expression edits

For each direction, the open-eyes/closed-mouth directional master was used for
the half-open mouth, open mouth, and closed-eyes/closed-mouth edits. The
direction-specific closed-eyes master was then used for the two closed-eyes
speaking states. These edits were instructed to preserve pose, perspective,
silhouette, jewelry, tentacle positions, crop, lighting, and background while
changing only the requested eyes or mouth.
