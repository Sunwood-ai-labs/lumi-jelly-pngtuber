#!/usr/bin/env python3
"""Build a five-direction runtime QA sheet for Lumi Jelly Head Motion."""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
ASSET_ROOT = ROOT / "assets" / "lumi-jelly-head-motion"
OUTPUT_DIRECTORY = ROOT / "artifacts" / "lumi-head-directional-final"
DIRECTIONS = ("front", "left", "right", "up", "down")
STATES = (
    "eyes-open-mouth-closed",
    "eyes-open-mouth-half",
    "eyes-open-mouth-open",
    "eyes-closed-mouth-closed",
    "eyes-closed-mouth-half",
    "eyes-closed-mouth-open",
)
LABEL_HEIGHT = 34


def checker(size: int) -> Image.Image:
    image = Image.new("RGBA", (size, size), "white")
    draw = ImageDraw.Draw(image)
    block = 32
    for y in range(0, size, block):
        for x in range(0, size, block):
            if (x // block + y // block) % 2:
                draw.rectangle((x, y, x + block - 1, y + block - 1), fill="#e8edf4")
    return image


def runtime_path(direction: str, state: str) -> Path:
    if direction == "front":
        return ASSET_ROOT / f"{state}.png"
    return ASSET_ROOT / "directions" / direction / f"{state}.png"


def build_sheet(tile_size: int, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet = Image.new("RGB", (len(STATES) * tile_size, len(DIRECTIONS) * (tile_size + LABEL_HEIGHT)), "#f7f2eb")
    draw = ImageDraw.Draw(sheet)
    for row, direction in enumerate(DIRECTIONS):
        for column, state in enumerate(STATES):
            source = Image.open(runtime_path(direction, state)).convert("RGBA")
            if tile_size != source.width:
                source = source.resize((tile_size, tile_size), Image.Resampling.LANCZOS)
            tile = checker(tile_size)
            tile.alpha_composite(source, ((tile_size - source.width) // 2, (tile_size - source.height) // 2))
            x = column * tile_size
            y = row * (tile_size + LABEL_HEIGHT)
            sheet.paste(tile.convert("RGB"), (x, y))
            draw.text((x + 8, y + tile_size + 9), f"{direction} / {state}", fill="#18202a")
    sheet.save(output)
    print(output)


def main() -> None:
    build_sheet(320, OUTPUT_DIRECTORY / "all-30-runtime-states.png")
    build_sheet(1024, OUTPUT_DIRECTORY / "all-30-runtime-states-original.png")


if __name__ == "__main__":
    main()
