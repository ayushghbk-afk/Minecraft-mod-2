#!/usr/bin/env python3
"""Generate replaceable placeholder PNG art for Bedrock Expansion.

Pillow is the preferred renderer (``python3 -m pip install Pillow``).  A
small dependency-free PNG writer is included so CI and offline Bedrock pack
workflows can still produce valid files when Pillow is unavailable.  All item
and block icons are deliberately 16x16 pixel art; entity swatches are 64x64.
"""
from __future__ import annotations

import hashlib
import json
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RP = ROOT / "BedrockExpansion_RP"
CATALOG = ROOT / "BEDROCK_EXPANSION_CATALOG.json"

try:  # Pillow is the intended implementation.
    from PIL import Image, ImageDraw
    HAVE_PILLOW = True
except ImportError:  # pragma: no cover - exercised on minimal build images.
    Image = ImageDraw = None
    HAVE_PILLOW = False


def hex_rgb(value: str):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


def palette(identifier: str):
    digest = hashlib.sha256(identifier.encode("utf-8")).digest()
    anchors = {
        "ember": (214, 73, 31), "frost": (119, 210, 238), "storm": (99, 110, 224),
        "lumen": (247, 220, 96), "void": (79, 40, 112), "copper": (184, 105, 54),
        "silver": (202, 211, 224), "platinum": (170, 224, 225), "mythril": (75, 110, 173),
        "adamantite": (49, 171, 139), "tin": (151, 164, 169), "crystal": (100, 202, 230),
    }
    base = next((color for word, color in anchors.items() if word in identifier), (112 + digest[0] % 60, 82 + digest[1] % 60, 60 + digest[2] % 70))
    dark = tuple(max(0, c - 55) for c in base)
    light = tuple(min(255, c + 48) for c in base)
    return base, dark, light


def fallback_png(path: Path, width: int, height: int, pixels):
    """Write RGBA pixels as a valid non-interlaced PNG using stdlib only."""
    raw = bytearray()
    for y in range(height):
        raw.append(0)
        for x in range(width): raw.extend(bytes(pixels[y][x]))
    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xffffffff)
    data = b"\x89PNG\r\n\x1a\n"
    data += chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
    data += chunk(b"IDAT", zlib.compress(bytes(raw), 9))
    data += chunk(b"IEND", b"")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


def fallback_art(identifier: str, width: int, height: int, block=False):
    base, dark, light = palette(identifier)
    pixels = [[(*dark, 255) for _ in range(width)] for _ in range(height)]
    # Border, inset, shine, and a deterministic stripe make each placeholder
    # readable even in a packed atlas.
    for y in range(1, height - 1):
        for x in range(1, width - 1): pixels[y][x] = (*base, 255)
    for y in range(2, max(3, height // 3)):
        for x in range(2, max(3, width - 2)): pixels[y][x] = (*light, 255)
    step = max(3, (sum(identifier.encode()) % 6) + 3)
    for y in range(2, height - 2):
        x = (y * step + len(identifier)) % max(1, width - 4) + 2
        pixels[y][x] = (*dark, 255)
    if block:
        for x in range(width):
            pixels[height // 2][x] = (*dark, 255)
    return pixels


def pillow_art(identifier: str, width: int, height: int, block=False):
    base, dark, light = palette(identifier)
    image = Image.new("RGBA", (width, height), dark + (255,))
    draw = ImageDraw.Draw(image)
    draw.rectangle((1, 1, width - 2, height - 2), fill=base + (255,))
    draw.rectangle((2, 2, width - 3, max(2, height // 3)), fill=light + (255,))
    step = max(3, (sum(identifier.encode()) % 6) + 3)
    for y in range(2, height - 2):
        x = (y * step + len(identifier)) % max(1, width - 4) + 2
        draw.point((x, y), fill=dark + (255,))
    if block:
        draw.line((0, height // 2, width - 1, height // 2), fill=dark + (255,))
    return image


def save_art(path: Path, identifier: str, width: int, height: int, block=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    if HAVE_PILLOW:
        pillow_art(identifier, width, height, block=block).save(path, "PNG", optimize=False)
    else:
        fallback_png(path, width, height, fallback_art(identifier, width, height, block=block))


def main():
    catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    entries = catalog["entries"]
    blocks = set(catalog["block_identifiers"])
    for entry in entries:
        iid = entry["id"]
        save_art(RP / "textures" / "items" / f"{iid}.png", iid, 16, 16, block=entry["identifier"] in blocks)
        if entry["identifier"] in blocks:
            save_art(RP / "textures" / "blocks" / f"{iid}.png", iid, 16, 16, block=True)
    for entity_file in sorted((ROOT / "BedrockExpansion_RP" / "entity").glob("*.entity.json")):
        iid = entity_file.name.removesuffix(".entity.json")
        save_art(RP / "textures" / "entity" / f"{iid}.png", iid, 64, 64)
    save_art(RP / "pack_icon.png", "bedrock_expansion_pack_icon", 64, 64, block=True)
    save_art(ROOT / "BedrockExpansion_BP" / "pack_icon.png", "bedrock_expansion_behavior_icon", 64, 64, block=True)
    renderer = "Pillow" if HAVE_PILLOW else "stdlib PNG fallback"
    print(f"Generated {len(entries)} item placeholders, {len(blocks)} block textures, entity swatches, and pack icons with {renderer}.")


if __name__ == "__main__":
    main()
