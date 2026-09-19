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


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"{path} is not a PNG")
    if len(data) < 24 or data[12:16] != b"IHDR":
        raise AssertionError(f"{path} has no PNG IHDR")
    width, height, bit_depth, color_type = struct.unpack(">IIBB", data[16:26])
    if (bit_depth, color_type) != (8, 6):
        raise AssertionError(f"{path} must be 8-bit RGBA, got bit depth {bit_depth}, color type {color_type}")
    return width, height


def assert_png(path: Path, expected_size: tuple[int, int] | None = None) -> None:
    width, height = png_size(path)
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


def validate_sources() -> tuple[int, int, int]:
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

    lang = (RP / "texts" / "en_US.lang").read_text(encoding="utf-8")

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
        assert f"item.{identifier}=" in lang, f"{path}: missing lang entry for {identifier}"
        for component in ("minecraft:icon", "minecraft:display_name", "minecraft:max_stack_size"):
            assert component in item["components"], f"{path}: missing {component}"

    # 3D block models and their terrain textures.
    geometry_ids: set[str] = set()
    for path in sorted((RP / "models" / "blocks").glob("*.geo.json")):
        geo = load_json(path)
        for entry in geo["minecraft:geometry"]:
            identifier = entry["description"]["identifier"]
            assert identifier not in geometry_ids, identifier
            geometry_ids.add(identifier)
            assert entry["description"]["texture_width"] == 16, path
            assert entry["description"]["texture_height"] == 16, path
            bones = entry["bones"]
            assert bones, f"{path}: no bones"
            assert any(bone.get("cubes") for bone in bones), f"{path}: no cubes"
            for bone in bones:
                for cube_def in bone.get("cubes", []):
                    assert len(cube_def["origin"]) == 3, f"{path}: bad cube origin"
                    assert len(cube_def["size"]) == 3, f"{path}: bad cube size"
                    assert all(s > 0 for s in cube_def["size"]), f"{path}: bad cube size"
                    uv = cube_def["uv"]
                    if isinstance(uv, dict):
                        for face in ("north", "south", "east", "west", "up", "down"):
                            assert face in uv, f"{path}: missing {face} UV"
                    if "rotation" in cube_def:
                        assert "pivot" in cube_def, f"{path}: rotated cube without pivot"

    terrain_data = load_json(RP / "textures" / "terrain_texture.json")["texture_data"]
    for key, definition in terrain_data.items():
        texture_path = ROOT / "packs" / "realistic_sticks_rp" / (definition["textures"] + ".png")
        assert_png(texture_path, (16, 16))

    blocks_json = load_json(RP / "blocks.json")
    assert blocks_json["format_version"] == [1, 1, 0]

    block_files = sorted((BP / "blocks").glob("*.json"))
    block_ids: set[str] = set()
    for path in block_files:
        block = load_json(path)["minecraft:block"]
        identifier = block["description"]["identifier"]
        assert identifier.startswith("realstick:")
        assert identifier not in block_ids, identifier
        block_ids.add(identifier)
        assert identifier not in item_ids, f"{path}: block id collides with item id"
        components = block["components"]
        geometry = components["minecraft:geometry"]
        geometry_id = geometry["identifier"] if isinstance(geometry, dict) else geometry
        assert geometry_id in geometry_ids, f"{path}: missing geometry {geometry_id}"
        materials = components["minecraft:material_instances"]
        assert materials, f"{path}: no material instances"
        for face, instance in materials.items():
            target = materials[instance] if isinstance(instance, str) else instance
            assert target["texture"] in terrain_data, f"{path}: missing terrain key {target['texture']}"
        loot_path = BP / components["minecraft:loot"]
        assert loot_path.is_file(), f"{path}: missing loot table {loot_path}"
        loot = load_json(loot_path)
        assert loot["pools"], f"{loot_path}: no loot pools"
        assert f"tile.{identifier}.name=" in lang, f"{path}: missing lang entry for {identifier}"
        assert identifier in blocks_json, f"{path}: missing RP blocks.json entry"
        for box_key in ("minecraft:collision_box", "minecraft:selection_box"):
            box = components[box_key]
            if isinstance(box, dict):
                assert len(box["origin"]) == 3 and len(box["size"]) == 3, f"{path}: bad {box_key}"

    animation_files = sorted((RP / "animations").glob("*.json"))
    animation_ids: set[str] = set()
    assert animation_files, "missing resource-pack animation overrides"
    for path in animation_files:
        data = load_json(path)
        assert data.get("format_version") == "1.8.0", f"{path}: bad animation format_version"
        animations = data.get("animations")
        assert isinstance(animations, dict) and animations, f"{path}: no animations"
        for anim_id, anim in animations.items():
            assert anim_id.startswith("animation."), f"{path}: bad animation id {anim_id}"
            assert anim_id not in animation_ids, anim_id
            animation_ids.add(anim_id)
            assert anim.get("loop") is True, f"{path}: {anim_id} must loop"
            bones = anim.get("bones")
            assert isinstance(bones, dict) and bones, f"{path}: {anim_id} has no bones"
            for bone_name, bone in bones.items():
                assert bone_name, f"{path}: empty bone name"
                assert any(key in bone for key in ("rotation", "position", "scale")), (
                    f"{path}: {anim_id}.{bone_name} has no transform"
                )

    required_anims = {
        "animation.humanoid.attack.rotations",
        "animation.player.attack.rotations",
        "animation.player.first_person.attack_rotation",
        "animation.zombie.attack_bare_hand",
        "animation.quadruped.walk",
        "animation.creeper.legs",
        "animation.spider.walk",
        "animation.iron_golem.attack",
        "animation.vindicator.attack",
        "animation.chicken.move",
    }
    missing_anims = required_anims - animation_ids
    assert not missing_anims, f"missing animation overrides: {sorted(missing_anims)}"

    water_files = {
        "water_still_grey.png": (16, 512),
        "water_flow_grey.png": (16, 512),
        "water_still.png": (16, 512),
        "water_flow.png": (16, 512),
        "cauldron_water.png": (16, 512),
    }
    for name, size in water_files.items():
        assert_png(RP / "textures" / "blocks" / name, size)

    recipe_files = sorted((BP / "recipes").glob("*.json"))
    recipe_ids: set[str] = set()
    known_results = item_ids | block_ids
    for path in recipe_files:
        recipe = load_json(path)
        kinds = [key for key in recipe if key.startswith("minecraft:recipe_")]
        assert len(kinds) == 1, f"{path}: expected one recipe body"
        container = recipe[kinds[0]]
        identifier = container["description"]["identifier"]
        assert identifier.startswith("realstick:")
        assert identifier not in recipe_ids, identifier
        recipe_ids.add(identifier)
        if kinds[0] == "minecraft:recipe_shaped":
            pattern = container["pattern"]
            assert pattern and len({len(row) for row in pattern}) == 1, f"{path}: ragged pattern"
            key = container["key"]
            assert set("".join(pattern).replace(" ", "")) <= set(key), f"{path}:pattern/key mismatch"
            for slot in key.values():
                assert "item" in slot or "tag" in slot, f"{path}: bad key slot"
        elif kinds[0] == "minecraft:recipe_shapeless":
            for ingredient in container["ingredients"]:
                assert "item" in ingredient or "tag" in ingredient, f"{path}: bad ingredient"
        elif kinds[0] == "minecraft:recipe_furnace":
            assert "item" in container["input"] or "tag" in container["input"], f"{path}: bad input"
            assert "item" in container["output"], f"{path}: bad output"
        result = container.get("result", container.get("output", {})).get("item", "")
        assert result.startswith("realstick:") or result.startswith("minecraft:"), f"{path}: bad result"
        if result.startswith("realstick:"):
            assert result in known_results, f"{path}: unknown result {result}"

    return len(item_files), len(block_files), len(recipe_files), len(animation_ids)


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
    item_count, block_count, recipe_count, animation_count = validate_sources()
    validate_package()
    print(f"Validated Realistic Sticks: {item_count} items, {block_count} 3D blocks, "
          f"{recipe_count} recipes, {animation_count} animation overrides, "
          f"5 water flipbooks, 2 packs, package OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
