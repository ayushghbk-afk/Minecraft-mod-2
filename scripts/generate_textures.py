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
BLOCK_DIR = ROOT / "packs" / "realistic_sticks_rp" / "textures" / "blocks"
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

ROPE_DARK = (52, 35, 25, 255)
ROPE_BASE = (178, 127, 78, 255)
ROPE_LIGHT = (226, 178, 118, 255)
FLINT_DARK = (90, 90, 95, 255)
FLINT_BASE = (200, 200, 205, 255)
FLINT_LIGHT = (245, 245, 250, 255)


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


def band_across(canvas, start, end, t: float, half_width: float, color, width: float = 1.0):
    """Paint a binding band across a diagonal shaft at fraction t."""
    cx = start[0] + (end[0] - start[0]) * t
    cy = start[1] + (end[1] - start[1]) * t
    nx, ny = -(end[1] - start[1]), end[0] - start[0]
    length = math.hypot(nx, ny) or 1
    nx, ny = nx / length, ny / length
    stroke(canvas, (cx - nx * half_width, cy - ny * half_width),
           (cx + nx * half_width, cy + ny * half_width), width, color)


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


# ---------------------------------------------------------------------------
# New item textures (32x32).
# ---------------------------------------------------------------------------

def bark_strip_texture(size: int = 32):
    rng = random.Random("realistic-sticks:bark_strip")
    canvas = new_canvas(size)
    base, dark, light, bark = PALETTES["oak"]
    for y in range(2, 30):
        wobble = math.sin(y * 0.4) * 1.5
        cx = 16 + wobble
        half = 4 + math.sin(y * 0.9) * 0.8
        for x in range(int(cx - half - 1), int(cx + half + 2)):
            dist = abs(x - cx)
            if dist > half + 0.6:
                continue
            if dist > half - 0.6:
                put(canvas, x, y, dark)
            elif dist < 1.4:
                put(canvas, x, y, light)
            else:
                put(canvas, x, y, rng.choice((base, base, bark)))
    for _ in range(4):  # cracks across the strip
        y = rng.randrange(4, 28)
        for x in range(12, 21):
            if rng.random() < 0.8:
                put(canvas, x, y, dark)
    for _ in range(30):  # pale flecks
        put(canvas, rng.randrange(12, 21), rng.randrange(3, 29), light)
    return canvas


def bark_rope_texture(size: int = 32):
    rng = random.Random("realistic-sticks:bark_rope")
    canvas = new_canvas(size)
    circle(canvas, 15, 15, 11, ROPE_DARK)
    circle(canvas, 15, 15, 10, ROPE_BASE)
    circle(canvas, 15, 15, 7, ROPE_DARK)
    circle(canvas, 15, 15, 6, ROPE_BASE)
    circle(canvas, 15, 15, 3.4, ROPE_DARK)
    circle(canvas, 15, 15, 2, (0, 0, 0, 0))
    for step in range(12):  # twist marks around the coil
        angle = step * math.pi / 6
        for radius in (8.5, 4.8):
            x = int(15 + math.cos(angle) * radius)
            y = int(15 + math.sin(angle) * radius)
            put(canvas, x, y, ROPE_LIGHT)
            put(canvas, x + 1, y, ROPE_DARK)
    stroke(canvas, (23, 21), (30, 28), 3, ROPE_DARK)
    stroke(canvas, (23, 21), (30, 28), 1.6, ROPE_BASE)
    for _ in range(12):
        put(canvas, rng.randrange(6, 25), rng.randrange(6, 25), ROPE_LIGHT)
    return canvas


def wood_chips_texture(size: int = 32):
    rng = random.Random("realistic-sticks:wood_chips")
    canvas = new_canvas(size)
    colors = [
        ((236, 218, 174, 255), (137, 111, 76, 255)),
        ((190, 126, 70, 255), (104, 61, 33, 255)),
        ((211, 133, 71, 255), (123, 63, 37, 255)),
    ]
    for _ in range(7):
        cx, cy = rng.randrange(7, 25), rng.randrange(7, 25)
        angle = rng.uniform(0, math.pi)
        dx, dy = math.cos(angle) * 4, math.sin(angle) * 4
        light, dark = rng.choice(colors)
        stroke(canvas, (cx - dx, cy - dy), (cx + dx, cy + dy), 4.4, dark)
        stroke(canvas, (cx - dx, cy - dy), (cx + dx, cy + dy), 2.6, light)
        put(canvas, int(cx + dx), int(cy + dy), dark)
    return canvas


def tinder_bundle_texture(size: int = 32):
    rng = random.Random("realistic-sticks:tinder_bundle")
    canvas = new_canvas(size)
    base, dark, light, _ = PALETTES["pale_oak"]
    branches = [((7, 22), (24, 12)), ((8, 12), (25, 22)), ((7, 17), (25, 17))]
    for start, end in branches:
        stroke(canvas, start, end, 4.2, dark)
        stroke(canvas, start, end, 2.6, base)
        stroke(canvas, (start[0] + 0.4, start[1] - 0.4),
               (end[0] - 0.4, end[1] + 0.4), 0.8, light)
    grass = (220, 200, 130, 255)
    for _ in range(8):  # dry grass wisps poking out of the top
        x = rng.randrange(9, 23)
        stroke(canvas, (x, 13), (x + rng.uniform(-3, 3), rng.uniform(3, 8)), 0.8, grass)
    stroke(canvas, (16, 10), (16, 24), 1.5, ROPE_DARK)
    stroke(canvas, (17, 10), (17, 24), 0.55, ROPE_BASE)
    return canvas


def charcoal_lump_texture(size: int = 32):
    rng = random.Random("realistic-sticks:charcoal_lump")
    canvas = new_canvas(size)
    circle(canvas, 12, 19, 7, (30, 30, 34, 255))
    circle(canvas, 20, 14, 6, (38, 38, 44, 255))
    circle(canvas, 17, 22, 5, (22, 22, 26, 255))
    for _ in range(40):  # ashen variation
        x, y = rng.randrange(5, 27), rng.randrange(7, 27)
        if canvas[y][x][3]:
            put(canvas, x, y, rng.choice(((30, 30, 34, 255), (48, 48, 56, 255),
                                          (90, 90, 100, 255), (22, 22, 26, 255))))
    for _ in range(6):  # glowing cracks
        x, y = rng.randrange(8, 24), rng.randrange(10, 24)
        if canvas[y][x][3]:
            color = rng.choice(((255, 110, 20, 255), (255, 190, 80, 255), (180, 40, 10, 255)))
            stroke(canvas, (x, y), (x + rng.uniform(-4, 4), y + rng.uniform(-2, 2)), 0.8, color)
    circle(canvas, 10, 15, 1.2, (120, 120, 130, 255))
    circle(canvas, 19, 10, 1.0, (120, 120, 130, 255))
    return canvas


def walking_staff_texture(size: int = 32):
    canvas = branch_texture("oak")
    start, end = (5, 27), (27, 5)
    _, dark, light, _ = PALETTES["oak"]
    circle(canvas, end[0], end[1], 2.6, dark)   # rounded knob head
    circle(canvas, end[0] - 0.5, end[1] - 0.5, 1.4, light)
    for t in (0.68, 0.75, 0.82):  # rope grip wraps below the knob
        band_across(canvas, start, end, t, 3.4, ROPE_DARK, 1.2)
        band_across(canvas, start, end, t + 0.015, 3.4, ROPE_BASE, 0.5)
    circle(canvas, start[0], start[1], 2.0, dark)  # worn foot cap
    return canvas


def hunting_spear_texture(size: int = 32):
    canvas = branch_texture("spruce")
    start, end = (5, 27), (27, 5)
    # Flint head as a small diamond at the tip.
    for dx, dy in [(0, -2), (-1, -1), (0, -1), (1, -1),
                   (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0),
                   (-1, 1), (0, 1), (1, 1), (0, 2)]:
        edge = abs(dx) + abs(dy) >= 3
        put(canvas, 28 + dx, 4 + dy, FLINT_DARK if edge else FLINT_BASE)
    put(canvas, 27, 3, FLINT_LIGHT)
    put(canvas, 28, 3, FLINT_LIGHT)
    for t in (0.74, 0.80, 0.86):  # sinew binding under the head
        band_across(canvas, start, end, t, 3.2, ROPE_DARK, 1.2)
        band_across(canvas, start, end, t + 0.015, 3.2, ROPE_LIGHT, 0.5)
    return canvas


def wooden_mallet_texture(size: int = 32):
    rng = random.Random("realistic-sticks:wooden_mallet")
    canvas = new_canvas(size)
    base, dark, light, _ = PALETTES["oak"]
    stroke(canvas, (5, 27), (19, 13), 7, dark)   # handle
    stroke(canvas, (5, 27), (19, 13), 5, base)
    stroke(canvas, (6, 25.5), (18, 13.5), 1.3, light)
    for y in (5, 9, 13):  # stacked-log head
        stroke(canvas, (15, y), (29, y), 5.2, dark)
        stroke(canvas, (15, y), (29, y), 3.6, base)
    stroke(canvas, (16.5, 3.5), (27.5, 3.5), 0.9, light)
    for x in (19, 25):  # rope bands around the head
        stroke(canvas, (x, 2), (x, 16), 1.6, ROPE_DARK)
        stroke(canvas, (x + 1, 2), (x + 1, 16), 0.6, ROPE_BASE)
    circle(canvas, 5, 27, 2.0, light)  # pommel cut end
    for _ in range(20):
        put(canvas, rng.randrange(15, 29), rng.randrange(3, 15),
            rng.choice((base, dark, light)))
    return canvas


# ---------------------------------------------------------------------------
# Block textures (16x16). Kept as uniform grain so every model face samples
# clean wood wherever its UVs land.
# ---------------------------------------------------------------------------

def wood_grain_16(seed: str, base, dark, light, stripes: int = 5):
    rng = random.Random(seed)
    size = 16
    canvas = new_canvas(size)
    for y in range(size):
        for x in range(size):
            canvas[y][x] = base
    for _ in range(stripes):  # long vertical grain stripes
        x = rng.randrange(size)
        color = rng.choice((dark, dark, light))
        y0 = rng.randrange(0, 6)
        for y in range(y0, size):
            if rng.random() < 0.9:
                put(canvas, x, y, color)
    for _ in range(28):  # speckle
        put(canvas, rng.randrange(size), rng.randrange(size),
            rng.choice((base, base, dark, light)))
    kx, ky = rng.randrange(3, 13), rng.randrange(3, 13)  # a small knot
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            put(canvas, kx + dx, ky + dy, dark)
    put(canvas, kx, ky, light)
    return canvas


def log_side_texture():
    return wood_grain_16("realistic-sticks:log_side",
                         (96, 60, 36, 255), (52, 32, 20, 255),
                         (150, 100, 60, 255), stripes=8)


def log_top_texture():
    canvas = new_canvas(16)
    light = (210, 170, 120, 255)
    mid = (160, 120, 80, 255)
    bark = (90, 55, 32, 255)
    for y in range(16):
        for x in range(16):
            dist = math.hypot(x - 7.5, y - 7.5)
            if dist > 7.4:
                canvas[y][x] = bark
            elif int(dist) % 2 == 0:
                canvas[y][x] = light
            else:
                canvas[y][x] = mid
    put(canvas, 7, 7, bark)
    put(canvas, 8, 8, bark)
    return canvas


def trail_torch_texture():
    canvas = wood_grain_16("realistic-sticks:trail_torch",
                           (91, 62, 42, 255), (43, 31, 25, 255),
                           (143, 96, 59, 255), stripes=4)
    rng = random.Random("realistic-sticks:trail_torch:ember")
    embers = [(25, 22, 24, 255), (255, 120, 20, 255),
              (255, 200, 60, 255), (180, 40, 10, 255)]
    for y in range(16):  # ember strip sampled by the coal cube faces
        for x in range(12, 16):
            put(canvas, x, y, embers[0] if rng.random() < 0.55 else rng.choice(embers[1:]))
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
    BLOCK_DIR.mkdir(parents=True, exist_ok=True)
    # The vanilla stick is intentionally overridden so the base game item also
    # gets the same natural branch silhouette when this resource pack is active.
    write_png(ITEM_DIR / "stick.png", branch_texture("oak"))
    for species in PALETTES:
        write_png(ITEM_DIR / f"{species}_stick.png", branch_texture(species))
    write_png(ITEM_DIR / "sharpened_stick.png", branch_texture("oak", sharp=True))
    write_png(ITEM_DIR / "kindling_bundle.png", kindling_texture())
    new_items = {
        "bark_strip": bark_strip_texture(),
        "bark_rope": bark_rope_texture(),
        "wood_chips": wood_chips_texture(),
        "tinder_bundle": tinder_bundle_texture(),
        "charcoal_lump": charcoal_lump_texture(),
        "walking_staff": walking_staff_texture(),
        "hunting_spear": hunting_spear_texture(),
        "wooden_mallet": wooden_mallet_texture(),
    }
    for name, canvas in new_items.items():
        write_png(ITEM_DIR / f"{name}.png", canvas)

    blocks = {
        "stick_pile": wood_grain_16("realistic-sticks:stick_pile", *PALETTES["oak"][:3]),
        "kindling_block": wood_grain_16("realistic-sticks:kindling_block", *PALETTES["dark_oak"][:3]),
        "sharpened_stakes": wood_grain_16("realistic-sticks:sharpened_stakes", *PALETTES["pale_oak"][:3]),
        "campfire_kit": wood_grain_16("realistic-sticks:campfire_kit", *PALETTES["spruce"][:3]),
        "log_side": log_side_texture(),
        "log_top": log_top_texture(),
        "trail_torch": trail_torch_texture(),
    }
    for name, canvas in blocks.items():
        write_png(BLOCK_DIR / f"{name}.png", canvas)

    pack_icon = upscale(kindling_texture(32), 2)
    for path in PACK_ICON_PATHS:
        write_png(path, pack_icon)
    print(f"Generated {len(PALETTES) + 2 + len(new_items)} item textures, "
          f"{len(blocks)} block textures, and {len(PACK_ICON_PATHS)} pack icons.")


if __name__ == "__main__":
    main()
