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
VERSION = [1, 1, 0]
ENGINE = [1, 26, 50]
FORMAT = "1.26.50"
GEO_FORMAT = "1.19.0"

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

# Extra flat items: id suffix, display name, options for item_definition.
EXTRA_ITEMS = [
    ("bark_strip", "Bark strip", {"fuel": 2, "tags": ["realstick:bark"]}),
    ("bark_rope", "Bark rope", {"fuel": 3, "tags": ["realstick:rope"]}),
    ("wood_chips", "Wood chips", {"fuel": 1, "tags": ["realstick:chips"]}),
    ("tinder_bundle", "Tinder bundle", {"fuel": 15, "max_stack": 16, "tags": ["realstick:tinder"]}),
    ("charcoal_lump", "Charcoal lump", {"fuel": 60, "tags": ["realstick:charcoal"]}),
    ("walking_staff", "Walking staff", {
        "max_stack": 1, "damage": 3, "durability": 96,
        "tags": ["realstick:field_tools"], "menu_category": "equipment", "repair": True,
    }),
    ("hunting_spear", "Hunting spear", {
        "max_stack": 1, "damage": 5, "durability": 48,
        "tags": ["realstick:field_tools"], "menu_category": "equipment", "repair": True,
    }),
    ("wooden_mallet", "Wooden mallet", {
        "max_stack": 1, "damage": 6, "durability": 64, "repair_amount": 12,
        "tags": ["realstick:field_tools"], "menu_category": "equipment", "repair": True,
    }),
]

# 3D blocks: id suffix, display name, creative category, box, extras.
BLOCKS = [
    ("stick_pile", "Stick pile", "nature",
     {"origin": [-8, 0, -8], "size": [16, 6, 16]}, {}),
    ("kindling_block", "Kindling block", "nature",
     {"origin": [-8, 0, -8], "size": [16, 6, 16]}, {}),
    ("sharpened_stakes", "Sharpened stakes", "construction",
     {"origin": [-8, 0, -8], "size": [16, 15, 16]}, {}),
    ("campfire_kit", "Campfire kit", "nature",
     {"origin": [-8, 0, -8], "size": [16, 12, 16]}, {}),
    ("log_stool", "Log stool", "construction",
     {"origin": [-6, 0, -6], "size": [12, 10, 12]}, {"materials": "stool"}),
    ("trail_torch", "Trail torch", "construction",
     {"origin": [-4, 0, -4], "size": [8, 16, 8]},
     {"light": 14, "flammable": False, "map_color": "#c98a3a"}),
]


def dump(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def item_definition(identifier: str, display_name: str, icon: str, *, max_stack: int = 64,
                    fuel: float | None = None, damage: int | None = None,
                    durability: int | None = None, tags: list[str] | None = None,
                    menu_category: str = "items", repair_items: list[str] | None = None,
                    repair_amount: int = 8):
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
            "repair_items": [{"items": repair_items, "repair_amount": repair_amount}]
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


def shaped_recipe_multi(identifier: str, pattern: list[str], key: dict, result: str,
                        count: int, group: str, unlock: str | None = None):
    recipe = {
        "format_version": FORMAT,
        "minecraft:recipe_shaped": {
            "description": {"identifier": identifier},
            "group": group,
            "tags": ["crafting_table"],
            "pattern": pattern,
            "key": key,
            "result": {"item": result, "count": count},
        },
    }
    if unlock:
        recipe["minecraft:recipe_shaped"]["unlock"] = [{"item": unlock}]
    return recipe


def shapeless_recipe(identifier: str, ingredients: list[dict], result: str,
                     count: int, group: str, unlock: str | None = None):
    recipe = {
        "format_version": FORMAT,
        "minecraft:recipe_shapeless": {
            "description": {"identifier": identifier},
            "group": group,
            "tags": ["crafting_table"],
            "ingredients": ingredients,
            "result": {"item": result, "count": count},
        },
    }
    if unlock:
        recipe["minecraft:recipe_shapeless"]["unlock"] = [{"item": unlock}]
    return recipe


def furnace_recipe(identifier: str, input_item: str, result: str):
    return {
        "format_version": FORMAT,
        "minecraft:recipe_furnace": {
            "description": {"identifier": identifier},
            "tags": ["furnace"],
            "input": {"item": input_item},
            "output": {"item": result, "count": 1},
        },
    }


# ---------------------------------------------------------------------------
# 3D block geometry helpers. Every cube uses explicit per-face UVs so faces
# always sample inside the 16x16 block texture, whatever the cube size is.
# ---------------------------------------------------------------------------

def face_uv(size, origin=(0, 0)):
    w, h, d = size
    ox, oy = origin
    return {
        "north": {"uv": [ox, oy], "uv_size": [w, h]},
        "south": {"uv": [ox, oy], "uv_size": [w, h]},
        "east": {"uv": [ox, oy], "uv_size": [d, h]},
        "west": {"uv": [ox, oy], "uv_size": [d, h]},
        "up": {"uv": [ox, oy], "uv_size": [w, d]},
        "down": {"uv": [ox, oy], "uv_size": [w, d]},
    }


def cube(origin, size, uv_origin=(0, 0), rotation=None, pivot=None):
    entry = {"origin": list(origin), "size": list(size), "uv": face_uv(size, uv_origin)}
    if rotation is not None:
        entry["rotation"] = list(rotation)
        entry["pivot"] = list(pivot if pivot is not None else [0, 0, 0])
    return entry


def block_geo(identifier: str, cubes: list[dict]):
    return {
        "format_version": GEO_FORMAT,
        "minecraft:geometry": [
            {
                "description": {
                    "identifier": identifier,
                    "texture_width": 16,
                    "texture_height": 16,
                    "visible_bounds_width": 2,
                    "visible_bounds_height": 2.5,
                    "visible_bounds_offset": [0, 0.75, 0],
                },
                "bones": [{"name": "root", "pivot": [0, 0, 0], "cubes": cubes}],
            }
        ],
    }


def stick_pile_cubes():
    return [
        cube([-7, 0, -1], [14, 2, 2], rotation=[0, 12, 0], pivot=[0, 1, 0]),
        cube([-6, 2, -1], [12, 2, 2], rotation=[0, -18, 0], pivot=[0, 3, 0]),
        cube([-5, 0, -1], [10, 2, 2], rotation=[0, 55, 0], pivot=[0, 1, 0]),
        cube([-4, 4, -1], [8, 2, 2], rotation=[0, -45, 0], pivot=[0, 5, 0]),
        cube([-3, 2, -2], [6, 1, 1], rotation=[0, 70, 0], pivot=[0, 2, 0]),
    ]


def kindling_block_cubes():
    cubes = []
    # Six parallel sticks stacked 2 high, 3 wide.
    for y0 in (1, 3):
        for z0 in (-3, -1, 1):
            cubes.append(cube([-7, y0, z0], [14, 2, 2]))
    # Two twine wraps around the bundle.
    for x0 in (-4, 3):
        cubes.append(cube([x0, 5, -3], [1, 1, 6]))     # top band
        cubes.append(cube([x0, 1, -3], [1, 1, 6]))     # bottom band
        cubes.append(cube([x0, 1, -3.5], [1, 4, 1]))   # side bands
        cubes.append(cube([x0, 1, 2.5], [1, 4, 1]))
    return cubes


def sharpened_stakes_cubes():
    cubes = [cube([-8, 0, -3], [16, 2, 6])]  # ground beam
    for x0 in (-7, -2, 3):
        cubes.append(cube([x0, 2, -2], [4, 5, 4]))            # base
        cubes.append(cube([x0 + 0.5, 7, -1.5], [3, 5, 3]))    # mid
        cubes.append(cube([x0 + 1.5, 12, -0.5], [1, 3, 1]))   # point
    return cubes


def campfire_kit_cubes():
    return [
        cube([-7, 0, -1], [14, 1, 2]),                        # ground sticks
        cube([-1, 0, -7], [2, 1, 14]),
        cube([-2, 1, -2], [4, 2, 4]),                          # tinder mound
        cube([-1, 0, -6], [2, 12, 2], rotation=[18, 0, 0], pivot=[0, 0, -5]),
        cube([-1, 0, 4], [2, 12, 2], rotation=[-18, 0, 0], pivot=[0, 0, 5]),
        cube([-6, 0, -1], [2, 12, 2], rotation=[0, 0, -18], pivot=[-5, 0, 0]),
        cube([4, 0, -1], [2, 12, 2], rotation=[0, 0, 18], pivot=[5, 0, 0]),
    ]


def log_stool_cubes():
    return [
        cube([-5, 0, -5], [10, 8, 10]),   # stump body
        cube([-6, 8, -6], [12, 2, 12]),   # seat slab
    ]


def trail_torch_cubes():
    return [
        cube([-1, 0, -1], [2, 13, 2]),                 # post
        cube([-3, 9, -1], [6, 2, 2]),                  # peg handle
        cube([-3, 13, -3], [6, 2, 6]),                 # coal tray
        cube([-2, 15, -2], [4, 1, 4], uv_origin=(12, 0)),  # glowing coals
    ]


GEOMETRY_BUILDERS = {
    "stick_pile": stick_pile_cubes,
    "kindling_block": kindling_block_cubes,
    "sharpened_stakes": sharpened_stakes_cubes,
    "campfire_kit": campfire_kit_cubes,
    "log_stool": log_stool_cubes,
    "trail_torch": trail_torch_cubes,
}

MAP_COLORS = {
    "stick_pile": "#8a5a33",
    "kindling_block": "#6e4526",
    "sharpened_stakes": "#b09268",
    "campfire_kit": "#5a3a22",
    "log_stool": "#7a5230",
    "trail_torch": "#c98a3a",
}


def block_definition(name: str, category: str, box: dict, extras: dict):
    if extras.get("materials") == "stool":
        materials = {
            "up": {"texture": "realstick_log_top", "render_method": "opaque"},
            "*": {"texture": "realstick_log_side", "render_method": "opaque"},
        }
    else:
        materials = {
            "*": {"texture": f"realstick_{name}", "render_method": "opaque"},
        }
    components = {
        "minecraft:collision_box": box,
        "minecraft:selection_box": box,
        "minecraft:destructible_by_mining": {"seconds_to_destroy": 0.4},
        "minecraft:destructible_by_explosion": {"explosion_resistance": 2.0},
        "minecraft:geometry": f"geometry.realstick_{name}",
        "minecraft:material_instances": materials,
        "minecraft:map_color": extras.get("map_color", MAP_COLORS[name]),
        "minecraft:loot": f"loot_tables/blocks/{name}.json",
    }
    if extras.get("flammable", True):
        components["minecraft:flammable"] = {
            "catch_chance_modifier": 5,
            "destroy_chance_modifier": 20,
        }
    if extras.get("light"):
        components["minecraft:light_emission"] = extras["light"]
    return {
        "format_version": FORMAT,
        "minecraft:block": {
            "description": {
                "identifier": f"realstick:{name}",
                "menu_category": {"category": category},
            },
            "components": components,
        },
    }


def main() -> None:
    # Manifests use format_version 2 even though content files target 1.26.50.
    dump(BP / "manifest.json", {
        "format_version": 2,
        "header": {
            "name": "Realistic Sticks | Behavior",
            "description": "Species sticks, fieldcraft tools, tinder, charcoal, and 3D camp blocks.",
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
            "description": "Pixel textures and 3D models for natural wood sticks.",
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

    for name, display, options in EXTRA_ITEMS:
        kwargs = dict(options)
        if kwargs.pop("repair", False):
            kwargs["repair_items"] = wood_ids
        dump(BP / "items" / f"{name}.json", item_definition(
            f"realstick:{name}", display, f"realstick:{name}", **kwargs))

    # Custom 3D blocks, their models, and their loot tables.
    for name, _display, category, box, extras in BLOCKS:
        dump(BP / "blocks" / f"{name}.json",
             block_definition(name, category, box, extras))
        dump(RP / "models" / "blocks" / f"{name}.geo.json",
             block_geo(f"geometry.realstick_{name}", GEOMETRY_BUILDERS[name]()))
        dump(BP / "loot_tables" / "blocks" / f"{name}.json", {
            "pools": [{
                "rolls": 1,
                "entries": [{"type": "item", "name": f"realstick:{name}", "weight": 1}],
            }],
        })

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

    sticks = {"tag": "realstick:wood_sticks"}
    new_recipes = [
        ("bark_strip_from_sticks", shapeless_recipe(
            "realstick:bark_strip_from_sticks",
            [{**sticks, "count": 2}], "realstick:bark_strip", 3,
            "realstick:fieldcraft", "realstick:oak_stick")),
        ("bark_rope", shaped_recipe_multi(
            "realstick:bark_rope", ["BBB"], {"B": {"item": "realstick:bark_strip"}},
            "realstick:bark_rope", 1, "realstick:fieldcraft", "realstick:bark_strip")),
        ("wood_chips_from_stick", shapeless_recipe(
            "realstick:wood_chips_from_stick",
            [sticks], "realstick:wood_chips", 4,
            "realstick:fieldcraft")),
        ("tinder_bundle", shapeless_recipe(
            "realstick:tinder_bundle",
            [{"item": "realstick:wood_chips", "count": 4},
             {"item": "realstick:bark_rope"}],
            "realstick:tinder_bundle", 1, "realstick:fieldcraft", "realstick:bark_rope")),
        ("tinder_bundle_from_string", shapeless_recipe(
            "realstick:tinder_bundle_from_string",
            [{"item": "realstick:wood_chips", "count": 4},
             {"item": "minecraft:string"}],
            "realstick:tinder_bundle", 1, "realstick:fieldcraft", "minecraft:string")),
        ("kindling_bundle_from_rope", shapeless_recipe(
            "realstick:kindling_bundle_from_rope",
            [{**sticks, "count": 4}, {"item": "realstick:bark_rope"}],
            "realstick:kindling_bundle", 1, "realstick:fieldcraft", "realstick:bark_rope")),
        ("charcoal_from_kindling", furnace_recipe(
            "realstick:charcoal_from_kindling",
            "realstick:kindling_bundle", "realstick:charcoal_lump")),
        ("charcoal_from_tinder", furnace_recipe(
            "realstick:charcoal_from_tinder",
            "realstick:tinder_bundle", "realstick:charcoal_lump")),
        ("walking_staff", shaped_recipe_multi(
            "realstick:walking_staff", ["  R", " S ", "S  "],
            {"R": {"item": "realstick:bark_rope"}, "S": sticks},
            "realstick:walking_staff", 1, "realstick:fieldcraft", "realstick:bark_rope")),
        ("hunting_spear", shaped_recipe_multi(
            "realstick:hunting_spear", ["P", "R", "S"],
            {"P": {"tag": "realstick:sharpened_sticks"},
             "R": {"item": "realstick:bark_rope"}, "S": sticks},
            "realstick:hunting_spear", 1, "realstick:fieldcraft",
            "realstick:sharpened_stick")),
        ("wooden_mallet", shaped_recipe_multi(
            "realstick:wooden_mallet", ["KK", "KS", " S"],
            {"K": {"tag": "realstick:kindling"}, "S": sticks},
            "realstick:wooden_mallet", 1, "realstick:fieldcraft",
            "realstick:kindling_bundle")),
        ("torches_from_kindling", shapeless_recipe(
            "realstick:torches_from_kindling",
            [{"item": "realstick:kindling_bundle"}, {"item": "minecraft:coal"}],
            "minecraft:torch", 8, "realstick:fieldcraft", "minecraft:coal")),
        ("torches_from_charcoal", shapeless_recipe(
            "realstick:torches_from_charcoal",
            [{"item": "realstick:kindling_bundle"},
             {"item": "realstick:charcoal_lump"}],
            "minecraft:torch", 8, "realstick:fieldcraft", "realstick:charcoal_lump")),
        ("stick_pile", shapeless_recipe(
            "realstick:stick_pile", [{**sticks, "count": 4}],
            "realstick:stick_pile", 1, "realstick:camp")),
        ("kindling_block", shapeless_recipe(
            "realstick:kindling_block",
            [{**sticks, "count": 4}, {"item": "realstick:bark_rope"}],
            "realstick:kindling_block", 1, "realstick:camp", "realstick:bark_rope")),
        ("sharpened_stakes", shaped_recipe_multi(
            "realstick:sharpened_stakes", ["P", "P"],
            {"P": {"tag": "realstick:sharpened_sticks"}},
            "realstick:sharpened_stakes", 2, "realstick:camp",
            "realstick:sharpened_stick")),
        ("campfire_kit", shapeless_recipe(
            "realstick:campfire_kit",
            [{**sticks, "count": 3}, {"item": "realstick:tinder_bundle"}],
            "realstick:campfire_kit", 1, "realstick:camp", "realstick:tinder_bundle")),
        ("log_stool", shapeless_recipe(
            "realstick:log_stool", [{**sticks, "count": 6}],
            "realstick:log_stool", 1, "realstick:camp")),
        ("trail_torch", shaped_recipe_multi(
            "realstick:trail_torch", ["C", "T", "S"],
            {"C": {"item": "minecraft:coal"},
             "T": {"item": "realstick:tinder_bundle"}, "S": sticks},
            "realstick:trail_torch", 1, "realstick:camp", "minecraft:coal")),
        ("trail_torch_from_charcoal", shaped_recipe_multi(
            "realstick:trail_torch_from_charcoal", ["C", "T", "S"],
            {"C": {"item": "realstick:charcoal_lump"},
             "T": {"item": "realstick:tinder_bundle"}, "S": sticks},
            "realstick:trail_torch", 1, "realstick:camp", "realstick:charcoal_lump")),
    ]
    for filename, recipe in new_recipes:
        dump(BP / "recipes" / f"{filename}.json", recipe)

    texture_data = {"stick": {"textures": "textures/items/stick"}}
    for name, _display, _source, _kind in SPECIES:
        texture_data[f"realstick:{name}_stick"] = {"textures": f"textures/items/{name}_stick"}
    texture_data["realstick:sharpened_stick"] = {"textures": "textures/items/sharpened_stick"}
    texture_data["realstick:kindling_bundle"] = {"textures": "textures/items/kindling_bundle"}
    for name, _display, _options in EXTRA_ITEMS:
        texture_data[f"realstick:{name}"] = {"textures": f"textures/items/{name}"}
    dump(RP / "textures" / "item_texture.json", {
        "resource_pack_name": "realistic_sticks",
        "texture_name": "atlas.items",
        "texture_data": texture_data,
    })

    # Terrain atlas entries for the 3D blocks (the stool reuses log side/top).
    terrain_data = {}
    for name, *_ in BLOCKS:
        if name == "log_stool":
            continue
        terrain_data[f"realstick_{name}"] = {"textures": f"textures/blocks/{name}"}
    terrain_data["realstick_log_side"] = {"textures": "textures/blocks/log_side"}
    terrain_data["realstick_log_top"] = {"textures": "textures/blocks/log_top"}
    dump(RP / "textures" / "terrain_texture.json", {
        "resource_pack_name": "realistic_sticks",
        "texture_name": "atlas.terrain",
        "padding": 8,
        "num_mip_levels": 4,
        "texture_data": terrain_data,
    })

    dump(RP / "blocks.json", {
        "format_version": [1, 1, 0],
        **{f"realstick:{name}": {"sound": "wood"} for name, *_ in BLOCKS},
    })

    (RP / "texts" / "languages.json").parent.mkdir(parents=True, exist_ok=True)
    (RP / "texts" / "languages.json").write_text('["en_US"]\n', encoding="utf-8")
    names = [f"item.realstick:{name}_stick={display} stick" for name, display, *_ in SPECIES]
    names += [
        "item.realstick:sharpened_stick=Sharpened stick",
        "item.realstick:kindling_bundle=Kindling bundle",
    ]
    names += [f"item.realstick:{name}={display}" for name, display, _ in EXTRA_ITEMS]
    names += [f"tile.realstick:{name}.name={display}" for name, display, *_ in BLOCKS]
    (RP / "texts" / "en_US.lang").write_text(
        "# Realistic Sticks English localization\n" + "\n".join(names) + "\n",
        encoding="utf-8",
    )
    (BP / "texts").mkdir(parents=True, exist_ok=True)
    (BP / "texts" / "languages.json").write_text('["en_US"]\n', encoding="utf-8")
    print(f"Generated pack JSON for {len(SPECIES)} wood species, "
          f"{len(EXTRA_ITEMS)} extra items, and {len(BLOCKS)} 3D blocks.")


if __name__ == "__main__":
    main()
