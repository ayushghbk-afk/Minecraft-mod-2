#!/usr/bin/env python3
"""Write the JSON source files for the Realistic Sticks add-on."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "packs" / "realistic_sticks_bp"
RP = ROOT / "packs" / "realistic_sticks_rp"

BP_UUID = "0f6a5f6e-8db3-4df0-b8f7-fab9d9e7c901"
BP_MODULE_UUID = "9d1cde2a-9c41-4fdb-b28d-f44c818c5c01"
RP_UUID = "74e20c0d-8f94-4d65-9821-4131be457401"
RP_MODULE_UUID = "b8410363-f43b-429f-9b36-3d51d8dc8d01"
VERSION = [1, 0, 0]
ENGINE = [1, 26, 50]
FORMAT = "1.26.50"

# name, display name, source item, source kind
SPECIES = [
    ("oak", "Oak", "oak_log", "log"),
    ("spruce", "Spruce", "spruce_log", "log"),
    ("birch", "Birch", "birch_log", "log"),
    ("jungle", "Jungle", "jungle_log", "log"),
    ("acacia", "Acacia", "acacia_log", "log"),
    ("dark_oak", "Dark Oak", "dark_oak_log", "log"),
    ("mangrove", "Mangrove", "mangrove_log", "log"),
    ("cherry", "Cherry", "cherry_log", "log"),
    ("pale_oak", "Pale Oak", "pale_oak_log", "log"),
    ("bamboo", "Bamboo", "bamboo", "bamboo"),
]


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def item_definition(identifier: str, display_name: str, icon: str, *, max_stack: int = 64,
                    fuel: float | None = None, damage: int | None = None,
                    durability: int | None = None, tags: list[str] | None = None,
                    menu_category: str = "items", repair_items: list[str] | None = None):
    components = {
        "minecraft:icon": {"textures": {"default": icon}},
        "minecraft:display_name": {"value": display_name},
        "minecraft:max_stack_size": max_stack,
    }
    if fuel is not None:
        components["minecraft:fuel"] = {"duration": fuel}
    if damage is not None:
        components["minecraft:damage"] = {"value": damage}
        components["minecraft:hand_equipped"] = True
    if durability is not None:
        components["minecraft:durability"] = {"max_durability": durability}
    if repair_items:
        components["minecraft:repairable"] = {
            "repair_items": [{"items": repair_items, "repair_amount": 8}]
        }
    if tags:
        components["minecraft:tags"] = {"tags": tags}
    return {
        "format_version": FORMAT,
        "minecraft:item": {
            "description": {
                "identifier": identifier,
                "menu_category": {"category": menu_category},
            },
            "components": components,
        },
    }


def shaped_recipe(identifier: str, source: str, result: str, count: int, unlock: str, group: str):
    return {
        "format_version": FORMAT,
        "minecraft:recipe_shaped": {
            "description": {"identifier": identifier},
            "group": group,
            "tags": ["crafting_table"],
            "pattern": ["L"],
            "key": {"L": {"item": source}},
            "unlock": [{"item": unlock}],
            "result": {"item": result, "count": count},
        },
    }


def main() -> None:
    # Manifests use format_version 2 even though content files target 1.26.50.
    dump(BP / "manifest.json", {
        "format_version": 2,
        "header": {
            "name": "Realistic Sticks | Behavior",
            "description": "Species-specific sticks, a sharpened stick, and camp kindling.",
            "uuid": BP_UUID,
            "version": VERSION,
            "min_engine_version": ENGINE,
        },
        "modules": [{
            "description": "Realistic Sticks gameplay data",
            "type": "data",
            "uuid": BP_MODULE_UUID,
            "version": VERSION,
        }],
        "dependencies": [{"uuid": RP_UUID, "version": VERSION}],
        "metadata": {
            "authors": ["Minecraft-mod-2 contributors"],
            "license": "MIT",
            "product_type": "addon",
        },
    })
    dump(RP / "manifest.json", {
        "format_version": 2,
        "header": {
            "name": "Realistic Sticks | Resources",
            "description": "Hand-authored pixel textures for natural wood sticks.",
            "uuid": RP_UUID,
            "version": VERSION,
            "min_engine_version": ENGINE,
        },
        "modules": [{
            "description": "Realistic Sticks resource textures",
            "type": "resources",
            "uuid": RP_MODULE_UUID,
            "version": VERSION,
        }],
        "metadata": {
            "authors": ["Minecraft-mod-2 contributors"],
            "license": "MIT",
            "product_type": "addon",
        },
    })

    wood_ids = [f"realstick:{name}_stick" for name, *_ in SPECIES]
    for name, display, _source, _kind in SPECIES:
        dump(BP / "items" / f"{name}_stick.json", item_definition(
            f"realstick:{name}_stick",
            f"{display} stick",
            f"realstick:{name}_stick",
            fuel=5,
            tags=["realstick:wood_sticks"],
        ))

    dump(BP / "items" / "sharpened_stick.json", item_definition(
        "realstick:sharpened_stick",
        "Sharpened stick",
        "realstick:sharpened_stick",
        max_stack=1,
        damage=2,
        durability=32,
        tags=["realstick:sharpened_sticks"],
        repair_items=wood_ids,
        menu_category="equipment",
    ))
    dump(BP / "items" / "kindling_bundle.json", item_definition(
        "realstick:kindling_bundle",
        "Kindling bundle",
        "realstick:kindling_bundle",
        max_stack=16,
        fuel=30,
        tags=["realstick:kindling"],
    ))

    for name, _display, source, kind in SPECIES:
        result = f"realstick:{name}_stick"
        if kind == "log":
            log = f"minecraft:{source}"
            stripped_log = f"minecraft:stripped_{source}"
            planks = f"minecraft:{name}_planks"
            dump(BP / "recipes" / f"{name}_stick_from_log.json", shaped_recipe(
                f"realstick:{name}_stick_from_{name}_log", log, result, 4, log, "realstick:wood_sticks"))
            dump(BP / "recipes" / f"{name}_stick_from_stripped_log.json", shaped_recipe(
                f"realstick:{name}_stick_from_stripped_{name}_log", stripped_log, result, 4,
                stripped_log, "realstick:wood_sticks"))
            dump(BP / "recipes" / f"{name}_stick_from_planks.json", shaped_recipe(
                f"realstick:{name}_stick_from_{name}_planks", planks, result, 2,
                planks, "realstick:wood_sticks"))
        else:
            bamboo = f"minecraft:{source}"
            dump(BP / "recipes" / "bamboo_stick_from_bamboo.json", shaped_recipe(
                "realstick:bamboo_stick_from_bamboo", bamboo, result, 2, bamboo, "realstick:wood_sticks"))

    dump(BP / "recipes" / "sharpened_stick.json", {
        "format_version": FORMAT,
        "minecraft:recipe_shapeless": {
            "description": {"identifier": "realstick:sharpened_stick"},
            "group": "realstick:fieldcraft",
            "tags": ["crafting_table"],
            "ingredients": [
                {"tag": "realstick:wood_sticks"},
                {"item": "minecraft:flint"},
            ],
            "unlock": [{"item": "minecraft:flint"}],
            "result": {"item": "realstick:sharpened_stick", "count": 1},
        },
    })
    dump(BP / "recipes" / "kindling_bundle.json", {
        "format_version": FORMAT,
        "minecraft:recipe_shapeless": {
            "description": {"identifier": "realstick:kindling_bundle"},
            "group": "realstick:fieldcraft",
            "tags": ["crafting_table"],
            "ingredients": [
                {"tag": "realstick:wood_sticks", "count": 4},
                {"item": "minecraft:string"},
            ],
            "unlock": [{"item": "minecraft:string"}],
            "result": {"item": "realstick:kindling_bundle", "count": 1},
        },
    })
    dump(BP / "recipes" / "convert_to_vanilla_sticks.json", {
        "format_version": FORMAT,
        "minecraft:recipe_shapeless": {
            "description": {"identifier": "realstick:convert_to_vanilla_sticks"},
            "group": "realstick:fieldcraft",
            "tags": ["crafting_table"],
            "ingredients": [{"tag": "realstick:wood_sticks"}],
            "result": {"item": "minecraft:stick", "count": 2},
        },
    })

    texture_data = {"stick": {"textures": "textures/items/stick"}}
    for name, _display, _source, _kind in SPECIES:
        texture_data[f"realstick:{name}_stick"] = {"textures": f"textures/items/{name}_stick"}
    texture_data["realstick:sharpened_stick"] = {"textures": "textures/items/sharpened_stick"}
    texture_data["realstick:kindling_bundle"] = {"textures": "textures/items/kindling_bundle"}
    dump(RP / "textures" / "item_texture.json", {
        "resource_pack_name": "realistic_sticks",
        "texture_name": "atlas.items",
        "texture_data": texture_data,
    })

    (RP / "texts" / "languages.json").parent.mkdir(parents=True, exist_ok=True)
    (RP / "texts" / "languages.json").write_text('["en_US"]\n', encoding="utf-8")
    names = [f"item.realstick:{name}_stick={display} stick" for name, display, *_ in SPECIES]
    names += [
        "item.realstick:sharpened_stick=Sharpened stick",
        "item.realstick:kindling_bundle=Kindling bundle",
    ]
    (RP / "texts" / "en_US.lang").write_text(
        "# Realistic Sticks English localization\n" + "\n".join(names) + "\n",
        encoding="utf-8",
    )
    (BP / "texts").mkdir(parents=True, exist_ok=True)
    (BP / "texts" / "languages.json").write_text('["en_US"]\n', encoding="utf-8")
    print(f"Generated pack JSON for {len(SPECIES)} wood species.")


if __name__ == "__main__":
    main()
