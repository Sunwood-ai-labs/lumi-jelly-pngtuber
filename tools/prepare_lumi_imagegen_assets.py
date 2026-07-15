#!/usr/bin/env python3
"""Normalize the approved Image Gen Lumi Jelly states for PuruPuruPNGTuber."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "provenance" / "keyed"
DESTINATION = ROOT / "avatar"
STATE_NAMES = (
    "eyes-open-mouth-closed",
    "eyes-open-mouth-half",
    "eyes-open-mouth-open",
    "eyes-closed-mouth-closed",
    "eyes-closed-mouth-half",
    "eyes-closed-mouth-open",
)
CANVAS_SIZE = 1024
ART_SIZE = 922


def normalize(source: Path) -> Image.Image:
    image = Image.open(source).convert("RGBA")
    image = image.resize((ART_SIZE, ART_SIZE), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    inset = (CANVAS_SIZE - ART_SIZE) // 2
    canvas.alpha_composite(image, (inset, inset))
    return canvas


def main() -> None:
    for name in STATE_NAMES:
        source = SOURCE / f"{name}.png"
        if not source.is_file():
            raise FileNotFoundError(source)
        normalize(source).save(DESTINATION / f"{name}.png")

    transparent = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    transparent.save(DESTINATION / "back-hair.png")
    transparent.save(DESTINATION / "front-hair.png")
    normalize(SOURCE / "eyes-open-mouth-closed.png").save(DESTINATION / "concept.png")


if __name__ == "__main__":
    main()
