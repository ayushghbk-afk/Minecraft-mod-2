#!/usr/bin/env python3
"""Generate the small pixel-art textures used by Realistic Sticks.

The generator deliberately uses only the Python standard library so a fresh
checkout can rebuild the pack without installing an image-processing package.
"""

from __future__ import annotations

import math
import random
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEM_DIR = ROOT / "packs" / "realistic_sticks_rp" / "textures" / "items"
PACK_ICON_PATHS = [
    ROOT / "packs" / "realistic_sticks_bp" / "pack_icon.png",
    ROOT / "packs" / "realistic_sticks_rp" / "pack_icon.png",
]

PALETTES = {
    "oak": ((129, 81, 43, 255), (72, 43, 26, 255), (190, 126, 70, 255), (104, 61, 33, 255)),
    "spruce": ((91, 62, 42, 255), (43, 31, 25, 255), (143, 96, 59, 255), (68, 46, 33, 255)),
    "birch": ((203, 180, 132, 255), (78, 57, 40, 255), (236, 218, 174, 255), (137, 111, 76, 255)),
    "jungle": ((145, 91, 49, 255), (65, 39, 25, 255), (198, 129, 69, 255), (113, 65, 35, 255)),
    "acacia": ((160, 91, 48, 255), (69, 40, 28, 255), (211, 133, 71, 255), (123, 63, 37, 255)),
    "dark_oak": ((75, 48, 31, 255), (30, 22, 19, 255), (118, 75, 44, 255), (54, 34, 25, 255)),
    "mangrove": ((112, 55, 42, 255), (49, 27, 26, 255), (169, 83, 56, 255), (87, 39, 34, 255)),
    "cherry": ((173, 104, 89, 255), (73, 40, 45, 255), (221, 150, 130, 255), (129, 67, 67, 255)),
    "pale_oak": ((178, 157, 122, 255), (80, 67, 54, 255), (218, 199, 160, 255), (130, 111, 87, 255)),
    "bamboo": ((153, 157, 67, 255), (62, 74, 31, 255), (207, 196, 95, 255), (105, 116, 45, 255)),
}


def new_canvas(size: int) -> list[list[tuple[int, int, int, int]]]:
    return [[(0, 0, 0, 0) for _ in range(size)] for _ in range(size)]


def put(canvas, x: int, y: int, color) -> None:
    if 0 <= y < len(canvas) and 0 <= x < len(canvas[y]):
        canvas[y][x] = color


def circle(canvas, cx: float, cy: float, radius: float, color) -> None:
    min_x = max(0, int(math.floor(cx - radius)))
    max_x = min(len(canvas[0]) - 1, int(math.ceil(cx + radius)))
    min_y = max(0, int(math.floor(cy - radius)))
    max_y = min(len(canvas) - 1, int(math.ceil(cy + radius)))
    r2 = radius * radius
    for y in range(min_y, max_y + 1):
        for x in range(min_x, max_x + 1):
            if (x - cx) ** 2 + (y - cy) ** 2 <= r2:
                put(canvas, x, y, color)


def stroke(canvas, start, end, width: float, color, taper: bool = False) -> None:
    x1, y1 = start
    x2, y2 = end
    distance = math.hypot(x2 - x1, y2 - y1)
    steps = max(1, int(distance * 3))
    for i in range(steps + 1):
        t = i / steps
        radius = width / 2
        if taper:
            radius *= 1.0 - 0.82 * t
        circle(canvas, x1 + (x2 - x1) * t, y1 + (y2 - y1) * t, radius, color)


def distance_to_segment(px, py, ax, ay, bx, by) -> float:
    dx, dy = bx - ax, by - ay
    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)
    t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)))
    return math.hypot(px - (ax + t * dx), py - (ay + t * dy))


def branch_texture(name: str, sharp: bool = False, size: int = 32):
    rng = random.Random(f"realistic-sticks:{name}:{sharp}:{size}")
    base, dark, light, bark = PALETTES[name]
    canvas = new_canvas(size)
    scale = size / 32
    # The diagonal keeps the silhouette readable in the tiny inventory atlas.
    start = (5 * scale, 27 * scale)
    end = ((27 if not sharp else 24) * scale, (5 if not sharp else 8) * scale)
    stroke(canvas, start, end, 8 * scale, dark)
    stroke(canvas, start, end, 6 * scale, base)
    # A broken highlight follows the grain rather than looking like a flat bar.
    stroke(canvas, (6.0 * scale, 25.5 * scale), (25.0 * scale, 6.5 * scale), 1.4 * scale, light)
    for i in range(11):
        t = rng.uniform(0.06, 0.94)
        cx = start[0] + (end[0] - start[0]) * t
        cy = start[1] + (end[1] - start[1]) * t
        # Bark bands run across the branch.
        nx, ny = -(end[1] - start[1]), end[0] - start[0]
        length = math.hypot(nx, ny) or 1
        nx, ny = nx / length, ny / length
        stroke(canvas, (cx - nx * 2.1 * scale, cy - ny * 2.1 * scale),
               (cx + nx * 2.1 * scale, cy + ny * 2.1 * scale), 0.75 * scale, bark)
    # Small, deterministic bark variation makes each species feel different.
    for _ in range(95 if size == 32 else 380):
        x = rng.randrange(size)
        y = rng.randrange(size)
        if distance_to_segment(x, y, start[0], start[1], end[0], end[1]) < 2.7 * scale:
            put(canvas, x, y, rng.choice((base, base, bark, light, dark)))
    # A visible cut end at the thick end reinforces that this is a branch, not a rod.
    circle(canvas, start[0], start[1], 2.2 * scale, light)
    circle(canvas, start[0] + 0.2 * scale, start[1] - 0.2 * scale, 1.1 * scale, bark)
    # A pointed, freshly sharpened tip for the early-game weapon.
    if sharp:
        stroke(canvas, (23.5 * scale, 8.5 * scale), (30 * scale, 1.8 * scale), 1.6 * scale, dark, taper=True)
        stroke(canvas, (23.8 * scale, 8.2 * scale), (29.8 * scale, 2.0 * scale), 0.8 * scale, light, taper=True)
    return canvas


def kindling_texture(size: int = 32):
    canvas = new_canvas(size)
    branches = [
        ("oak", (4, 24), (26, 8)),
        ("spruce", (5, 10), (27, 25)),
        ("birch", (5, 18), (26, 18)),
    ]
    for name, start, end in branches:
        base, dark, light, _ = PALETTES[name]
        start = tuple(v * size / 32 for v in start)
        end = tuple(v * size / 32 for v in end)
        stroke(canvas, start, end, 4.7 * size / 32, dark)
        stroke(canvas, start, end, 3.0 * size / 32, base)
        stroke(canvas,
               (start[0] + 0.4 * size / 32, start[1] - 0.4 * size / 32),
               (end[0] - 0.4 * size / 32, end[1] + 0.4 * size / 32),
               0.8 * size / 32,
               light)
    # Two dark twine wraps hold the bundle together.
    for x in (11, 20):
        stroke(canvas, (x * size / 32, 10 * size / 32), (x * size / 32, 24 * size / 32),
               1.5 * size / 32, (52, 35, 25, 255))
        stroke(canvas, ((x + 1) * size / 32, 10 * size / 32), ((x + 1) * size / 32, 24 * size / 32),
               0.55 * size / 32, (178, 127, 78, 255))
    return canvas


def upscale(canvas, factor: int):
    return [
        [canvas[y // factor][x // factor] for x in range(len(canvas[0]) * factor)]
        for y in range(len(canvas) * factor)
    ]


def png_chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def write_png(path: Path, canvas) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    height, width = len(canvas), len(canvas[0])
    raw = bytearray()
    for row in canvas:
        raw.append(0)  # no filter; stable and easy to inspect
        for red, green, blue, alpha in row:
            raw.extend((red, green, blue, alpha))
    payload = b"\x89PNG\r\n\x1a\n"
    payload += png_chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
    payload += png_chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    payload += png_chunk(b"IEND", b"")
    path.write_bytes(payload)


def main() -> None:
    ITEM_DIR.mkdir(parents=True, exist_ok=True)
    # The vanilla stick is intentionally overridden so the base game item also
    # gets the same natural branch silhouette when this resource pack is active.
    write_png(ITEM_DIR / "stick.png", branch_texture("oak"))
    for species in PALETTES:
        write_png(ITEM_DIR / f"{species}_stick.png", branch_texture(species))
    write_png(ITEM_DIR / "sharpened_stick.png", branch_texture("oak", sharp=True))
    write_png(ITEM_DIR / "kindling_bundle.png", kindling_texture())
    pack_icon = upscale(kindling_texture(32), 2)
    for path in PACK_ICON_PATHS:
        write_png(path, pack_icon)
    print(f"Generated {len(PALETTES) + 2} item textures and {len(PACK_ICON_PATHS)} pack icons.")


if __name__ == "__main__":
    main()
