#!/usr/bin/env python3
"""Verify the standalone upper-body Lumi Jelly release."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
STATES = (
    "eyes-open-mouth-closed",
    "eyes-open-mouth-half",
    "eyes-open-mouth-open",
    "eyes-closed-mouth-closed",
    "eyes-closed-mouth-half",
    "eyes-closed-mouth-open",
)


def assert_png(path: Path, expected_size: tuple[int, int]) -> None:
    if not path.is_file():
        raise AssertionError(f"missing: {path.relative_to(ROOT)}")
    with Image.open(path) as image:
        if image.format != "PNG" or image.size != expected_size:
            raise AssertionError(
                f"invalid PNG: {path.relative_to(ROOT)} format={image.format} size={image.size}"
            )


def main() -> None:
    for state in STATES:
        assert_png(ROOT / "avatar" / f"{state}.png", (1024, 1024))
        assert_png(ROOT / "provenance" / "keyed" / f"{state}.png", (1254, 1254))
        assert_png(ROOT / "provenance" / "source" / f"{state}-chroma.png", (1254, 1254))

    assert_png(ROOT / "avatar" / "concept.png", (1024, 1024))
    assert_png(ROOT / "avatar" / "expression-preview.png", (1800, 660))
    if (ROOT / "head-motion").exists() or (ROOT / "integration").exists():
        raise AssertionError("head-motion or integration content leaked into upper-body release")
    if (ROOT / "avatar" / "directions").exists():
        raise AssertionError("direction states leaked into upper-body release")

    print("upper-body release verified: 6 frontal runtime states")


if __name__ == "__main__":
    main()
