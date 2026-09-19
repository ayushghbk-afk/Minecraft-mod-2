#!/usr/bin/env python3
"""Validate the source packs and the generated .mcaddon without Minecraft installed."""

from __future__ import annotations

import json
import struct
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "packs" / "realistic_sticks_bp"
RP = ROOT / "packs" / "realistic_sticks_rp"
EXPECTED_ENGINE = [1, 26, 50]


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid JSON in {path}: {exc}") from exc


def assert_png(path: Path, expected_size: tuple[int, int] | None = None) -> None:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"{path} is not a PNG")
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise AssertionError(f"{path} has no PNG IHDR")
    width, height, bit_depth, color_type = struct.unpack(">IIBB", data[16:26])
    if (bit_depth, color_type) != (8, 6):
        raise AssertionError(f"{path} must be 8-bit RGBA, got bit depth {bit_depth}, color type {color_type}")
    if expected_size and (width, height) != expected_size:
        raise AssertionError(f"{path} must be {expected_size[0]}x{expected_size[1]}, got {width}x{height}")


def validate_manifest(pack: Path, expected_module_type: str):
    manifest = load_json(pack / "manifest.json")
    assert manifest["format_version"] == 2
    header = manifest["header"]
    assert header["min_engine_version"] == EXPECTED_ENGINE, header["min_engine_version"]
    assert len(header["uuid"]) == 36
    modules = manifest["modules"]
    assert len(modules) == 1
    assert modules[0]["type"] == expected_module_type
    assert len(modules[0]["uuid"]) == 36
    assert modules[0]["uuid"] != header["uuid"]
    return manifest


def validate_sources() -> tuple[int, int]:
    bp_manifest = validate_manifest(BP, "data")
    rp_manifest = validate_manifest(RP, "resources")
    dependency = bp_manifest["dependencies"][0]
    assert dependency["uuid"] == rp_manifest["header"]["uuid"]
    assert dependency["version"] == rp_manifest["header"]["version"]

    texture_data = load_json(RP / "textures" / "item_texture.json")["texture_data"]
    for key, definition in texture_data.items():
        texture_path = ROOT / "packs" / "realistic_sticks_rp" / (definition["textures"] + ".png")
        assert_png(texture_path, (32, 32))
    assert_png(BP / "pack_icon.png", (64, 64))
    assert_png(RP / "pack_icon.png", (64, 64))

    item_files = sorted((BP / "items").glob("*.json"))
    item_ids: set[str] = set()
    for path in item_files:
        item = load_json(path)["minecraft:item"]
        identifier = item["description"]["identifier"]
        assert identifier.startswith("realstick:")
        assert identifier not in item_ids, identifier
        item_ids.add(identifier)
        icon = item["components"]["minecraft:icon"]["textures"]["default"]
        assert icon in texture_data, f"{path}: missing texture key {icon}"

    recipe_files = sorted((BP / "recipes").glob("*.json"))
    recipe_ids: set[str] = set()
    for path in recipe_files:
        recipe = load_json(path)
        container = next(value for key, value in recipe.items() if key.startswith("minecraft:recipe_"))
        identifier = container["description"]["identifier"]
        assert identifier.startswith("realstick:")
        assert identifier not in recipe_ids, identifier
        recipe_ids.add(identifier)

    return len(item_files), len(recipe_files)


def validate_package() -> None:
    manifests = [load_json(BP / "manifest.json"), load_json(RP / "manifest.json")]
    version = ".".join(str(part) for part in manifests[0]["header"]["version"])
    package = ROOT / "releases" / f"RealisticSticks-{version}.mcaddon"
    if not package.exists():
        raise AssertionError(f"Missing package {package}; run scripts/build_addon.py first")
    with zipfile.ZipFile(package) as addon:
        names = set(addon.namelist())
        expected = {"RealisticSticks_BP.mcpack", "RealisticSticks_RP.mcpack"}
        assert names == expected, names
        for filename in sorted(expected):
            with zipfile.ZipFile(addon.open(filename)) as pack:
                assert "manifest.json" in pack.namelist()
                assert all(not name.startswith("/") for name in pack.namelist())


def main() -> int:
    item_count, recipe_count = validate_sources()
    validate_package()
    print(f"Validated Realistic Sticks: {item_count} items, {recipe_count} recipes, 2 packs, package OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
