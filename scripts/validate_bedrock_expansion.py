#!/usr/bin/env python3
"""Self-check the generated Bedrock Expansion project without Minecraft installed."""
from __future__ import annotations

import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "BedrockExpansion_BP"
RP = ROOT / "BedrockExpansion_RP"
NS = "bedrock_expansion:"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def png_size(path):
    data = path.read_bytes()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", f"not PNG: {path}"
    assert data[12:16] == b"IHDR", f"missing IHDR: {path}"
    return struct.unpack(">II", data[16:24])


def main():
    catalog = load(ROOT / "BEDROCK_EXPANSION_CATALOG.json")
    entries = catalog["entries"]
    assert len(entries) == 200, len(entries)
    identifiers = [e["identifier"] for e in entries]
    assert len(set(identifiers)) == 200, "duplicate catalog identifier"
    assert [e["number"] for e in entries] == list(range(1, 201)), "catalog numbering"
    block_ids = set(catalog["block_identifiers"])
    portable = {e["identifier"] for e in entries} - block_ids
    assert len(block_ids) == 51 and len(portable) == 149, (len(block_ids), len(portable))

    for pack in (BP, RP):
        manifest = load(pack / "manifest.json")
        assert manifest["format_version"] == 2
        assert manifest["header"]["min_engine_version"][0:2] == [1, 21]
        assert len(manifest["header"]["uuid"]) == 36
    bp_manifest, rp_manifest = load(BP / "manifest.json"), load(RP / "manifest.json")
    assert any(m["type"] == "script" and m["entry"] == "scripts/main.js" for m in bp_manifest["modules"])
    assert any(d.get("uuid") == rp_manifest["header"]["uuid"] for d in bp_manifest["dependencies"])

    item_ids = set()
    for path in (BP / "items").glob("*.json"):
        data = load(path)["minecraft:item"]
        iid = data["description"]["identifier"]
        assert iid in portable, f"unexpected item {iid}"
        assert iid not in item_ids, iid
        item_ids.add(iid)
        components = data["components"]
        assert {"minecraft:icon", "minecraft:display_name", "minecraft:max_stack_size"} <= set(components), path
        assert components["minecraft:icon"]["textures"]["default"] == iid.split(":", 1)[1]
    assert item_ids == portable, f"item coverage: {len(item_ids)} / {len(portable)}"

    block_file_ids = set()
    for path in (BP / "blocks").glob("*.json"):
        data = load(path)["minecraft:block"]
        iid = data["description"]["identifier"]
        assert iid in block_ids, f"unexpected block {iid}"
        block_file_ids.add(iid)
        comps = data["components"]
        assert "minecraft:material_instances" in comps and "minecraft:loot" in comps
        loot_path = BP / comps["minecraft:loot"]
        assert loot_path.is_file(), loot_path
        assert load(loot_path)["pools"], loot_path
    assert block_file_ids == block_ids, f"block coverage: {len(block_file_ids)} / {len(block_ids)}"

    item_texture = load(RP / "textures" / "item_texture.json")["texture_data"]
    assert set(item_texture) == {e["id"] for e in entries}
    for entry in entries:
        assert png_size(RP / "textures" / "items" / f"{entry['id']}.png") == (16, 16)
    terrain = load(RP / "textures" / "terrain_texture.json")["texture_data"]
    assert set(terrain) == {x.split(":", 1)[1] for x in block_ids}
    for iid in terrain:
        assert png_size(RP / "textures" / "blocks" / f"{iid}.png") == (16, 16)
    assert png_size(BP / "pack_icon.png") == (64, 64)
    assert png_size(RP / "pack_icon.png") == (64, 64)

    recipe_ids = set()
    known = {e["identifier"] for e in entries} | {"minecraft:" + x for x in ("stick", "stone", "iron_ingot")}
    for path in (BP / "recipes").glob("*.json"):
        recipe = load(path)
        kinds = [k for k in recipe if k.startswith("minecraft:recipe_")]
        assert len(kinds) == 1, path
        body = recipe[kinds[0]]
        rid = body["description"]["identifier"]
        assert rid.startswith(NS) and rid not in recipe_ids, rid
        recipe_ids.add(rid)
        result = body.get("result", body.get("output", {}))
        if isinstance(result, dict):
            result_id = result.get("item", "")
            assert result_id.startswith(NS) or result_id.startswith("minecraft:"), (path, result_id)
        if kinds[0] == "minecraft:recipe_shaped":
            pattern = body["pattern"]
            assert len({len(x) for x in pattern}) == 1, path
            symbols = set("".join(pattern).replace(" ", ""))
            assert symbols <= set(body["key"]), (path, symbols - set(body["key"]))
    assert len(recipe_ids) >= 100, len(recipe_ids)

    entity_ids = {NS + p.stem for p in (BP / "entities").glob("*.json")}
    assert len(entity_ids) == 10
    for entity_id in entity_ids:
        stem = entity_id.split(":", 1)[1]
        entity = load(BP / "entities" / f"{stem}.json")["minecraft:entity"]
        assert entity["description"]["identifier"] == entity_id
        assert (BP / "loot_tables" / "entities" / f"{stem}.json").is_file()
        assert (BP / "spawn_rules" / f"{stem}.json").is_file()
        assert (RP / "entity" / f"{stem}.entity.json").is_file()
        assert png_size(RP / "textures" / "entity" / f"{stem}.png") == (64, 64)
    assert len(list((BP / "features").glob("*.json"))) == 8
    assert len(list((BP / "feature_rules").glob("*.json"))) == 8

    design = (ROOT / "DESIGN.md").read_text(encoding="utf-8")
    assert design.count("### ") == 200
    for entry in entries:
        assert f"`{entry['identifier']}`" in design, entry["identifier"]
    for doc in ("README.md", "STORY.md", "ITEM_PROGRESSION.md"):
        assert (ROOT / doc).is_file() and (ROOT / doc).stat().st_size > 500
    for script in ("main.js", "backpack.js", "jetpack.js", "magic.js", "tech.js", "adventure.js", "survival_gear.js", "tools.js"):
        assert (BP / "scripts" / script).is_file()
    package = ROOT / "releases" / "BedrockExpansion-1.0.0.mcaddon"
    if package.exists():
        import zipfile
        with zipfile.ZipFile(package) as addon:
            assert set(addon.namelist()) == {"BedrockExpansion_BP.mcpack", "BedrockExpansion_RP.mcpack"}
    print(f"Bedrock Expansion validated: 200 catalog entries, {len(item_ids)} portable items, {len(block_file_ids)} blocks, {len(recipe_ids)} recipes, 10 entities, 8 ore features, placeholder art, docs, and manifests OK.")


if __name__ == "__main__":
    main()
