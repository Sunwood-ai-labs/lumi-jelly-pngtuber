#!/usr/bin/env python3
"""Normalize Image Gen Lumi Jelly head-motion states for PuruPuruPNGTuber."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DESTINATION = ROOT / "head-motion" / "avatar"
SOURCE = DESTINATION / "imagegen-v1" / "keyed"
IMAGEGEN_ROOT = DESTINATION / "imagegen-v1"
STATE_NAMES = (
    "eyes-open-mouth-closed",
    "eyes-open-mouth-half",
    "eyes-open-mouth-open",
    "eyes-closed-mouth-closed",
    "eyes-closed-mouth-half",
    "eyes-closed-mouth-open",
)
CANVAS_SIZE = 1024
DIRECTIONS = ("left", "right", "up", "down")


def normalize(source: Path) -> Image.Image:
    image = Image.open(source).convert("RGBA")
    return image.resize((CANVAS_SIZE, CANVAS_SIZE), Image.Resampling.LANCZOS)


def main() -> None:
    DESTINATION.mkdir(parents=True, exist_ok=True)
    for name in STATE_NAMES:
        source = SOURCE / f"{name}.png"
        if not source.is_file():
            raise FileNotFoundError(source)
        normalize(source).save(DESTINATION / f"{name}.png")

    for direction in DIRECTIONS:
        direction_source = IMAGEGEN_ROOT / "directional" / direction / "keyed"
        direction_destination = DESTINATION / "directions" / direction
        direction_destination.mkdir(parents=True, exist_ok=True)
        for name in STATE_NAMES:
            source = direction_source / f"{name}.png"
            if not source.is_file():
                raise FileNotFoundError(source)
            normalize(source).save(direction_destination / f"{name}.png")

    transparent = Image.new("RGBA", (CANVAS_SIZE, CANVAS_SIZE), (0, 0, 0, 0))
    transparent.save(DESTINATION / "back-hair.png")
    transparent.save(DESTINATION / "front-hair.png")
    normalize(SOURCE / "eyes-open-mouth-closed.png").save(DESTINATION / "concept.png")


if __name__ == "__main__":
    main()
