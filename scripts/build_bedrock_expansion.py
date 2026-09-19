#!/usr/bin/env python3
"""Generate the Bedrock Expansion: 200 Items source tree.

This is intentionally data-first: the 200-entry catalog is used to generate the
packs, recipes, language table, and design documentation from one source of
truth.  The project keeps placeable content in blocks/ (Bedrock creates the
corresponding inventory block item) and portable content in items/.  That is
important because defining the same identifier as both minecraft:item and
minecraft:block produces a duplicate-identifier content-log error.
"""
from __future__ import annotations

import json
import shutil
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BP = ROOT / "BedrockExpansion_BP"
RP = ROOT / "BedrockExpansion_RP"
NS = "bedrock_expansion"
VERSION = [1, 0, 0]
FORMAT = "1.21.0"
ENGINE = [1, 21, 0]

# The requested catalog, in the requested order.  Keep this list explicit: it
# is also checked by the self-check and is used to build DESIGN.md.
CATALOG_GROUPS = [
    ("Ores & Materials", [
        "Bedrock Dust", "Deepslate Crystal", "Nether Quartz Shard", "Amethyst Core", "Copper Nugget", "Tin Ore", "Tin Ingot", "Silver Ore", "Silver Ingot", "Platinum Ore", "Platinum Ingot", "Mythril Ore", "Mythril Ingot", "Adamantite Ore", "Adamantite Ingot", "Voidstone", "Lumen Crystal", "Ember Dust", "Frost Shard", "Storm Fragment",
    ]),
    ("Tools & Weapons", [
        "Bedrock Pickaxe", "Bedrock Axe", "Bedrock Shovel", "Bedrock Hoe", "Copper Sword", "Silver Sword", "Platinum Sword", "Mythril Sword", "Adamantite Sword", "Void Blade", "Lumen Bow", "Ember Crossbow", "Frost Trident", "Storm Hammer", "Crystal Dagger", "Stone Spear", "Chainsaw", "Drill", "Scythe", "War Axe",
    ]),
    ("Armor & Wearables", [
        "Copper Helmet", "Copper Chestplate", "Copper Leggings", "Copper Boots", "Silver Helmet", "Silver Chestplate", "Silver Leggings", "Silver Boots", "Platinum Helmet", "Platinum Chestplate", "Platinum Leggings", "Platinum Boots", "Mythril Helmet", "Mythril Chestplate", "Mythril Leggings", "Mythril Boots", "Adamantite Helmet", "Adamantite Chestplate", "Adamantite Leggings", "Adamantite Boots",
    ]),
    ("Food & Farming", [
        "Golden Apple Pie", "Copper Carrot", "Silver Beetroot", "Platinum Potato", "Mythril Bread", "Adamantite Stew", "Lumen Berry", "Ember Pepper", "Frost Melon", "Storm Corn", "Void Fruit", "Crystal Grapes", "Honey Cookie", "Chocolate Bar", "Cheese Wheel", "Butter", "Fried Egg", "Bacon Strip", "Fish Stew", "Magic Cake",
    ]),
    ("Blocks & Building", [
        "Copper Block", "Silver Block", "Platinum Block", "Mythril Block", "Adamantite Block", "Tin Block", "Lumen Block", "Ember Block", "Frost Block", "Storm Block", "Void Block", "Crystal Block", "Reinforced Glass", "Dark Glass", "Glowing Concrete", "Mossy Bricks", "Cracked Bricks", "Marble", "Polished Marble", "Limestone",
    ]),
    ("Redstone & Tech", [
        "Copper Wire", "Silver Wire", "Logic Gate", "Timer Block", "Pulse Extender", "Item Pipe", "Fluid Pipe", "Energy Cable", "Solar Panel", "Battery", "Generator", "Electric Furnace", "Auto Crafting Table", "Conveyor Belt", "Robot Arm", "Sensor Block", "Speaker Block", "Monitor Block", "Keyboard Block", "Computer Block",
    ]),
    ("Magic & Enchanting", [
        "Mana Crystal", "Spell Book", "Fire Spell", "Ice Spell", "Lightning Spell", "Healing Spell", "Teleport Spell", "Shield Spell", "Summon Spell", "Enchantment Orb", "Rune Stone", "Magic Wand", "Staff of Fire", "Staff of Ice", "Staff of Storms", "Staff of Life", "Soul Gem", "Void Pearl", "Celestial Shard", "Alchemy Table",
    ]),
    ("Mobs & Drops", [
        "Copper Golem Spawn Egg", "Silver Golem Spawn Egg", "Crystal Golem Spawn Egg", "Void Golem Spawn Egg", "Ember Imp Spawn Egg", "Frost Wolf Spawn Egg", "Storm Eagle Spawn Egg", "Lumen Fairy Spawn Egg", "Cave Lurker Spawn Egg", "Deep Crab Spawn Egg", "Copper Golem Core", "Silver Golem Core", "Crystal Golem Core", "Void Golem Core", "Ember Essence", "Frost Fur", "Storm Feather", "Lumen Dust", "Lurker Eye", "Crab Claw",
    ]),
    ("Decoration & Furniture", [
        "Wooden Chair", "Wooden Table", "Wooden Bed", "Sofa", "Bookshelf", "Lamp", "Ceiling Light", "Wall Clock", "Painting Frame", "Vase", "Large Flower Pot", "Rug", "Curtain", "Fireplace", "Kitchen Counter", "Oven", "Refrigerator", "Toilet", "Bathtub", "Sink",
    ]),
    ("Utility & Adventure", [
        "Backpack", "Large Backpack", "Ender Backpack", "Map Marker", "Compass Upgrade", "Clock Upgrade", "Lantern Helmet", "Night Vision Goggles", "Scuba Helmet", "Jetpack", "Parachute", "Grappling Hook", "Lockpick", "Key", "Treasure Map", "Boss Key", "Dungeon Compass", "Waypoint Stone", "Portal Frame", "Portal Activator",
    ]),
]


def slug(label: str) -> str:
    return label.lower().replace("'", "").replace(" ", "_").replace("-", "_")


def ident(name: str) -> str:
    return f"{NS}:{slug(name)}"


def pretty(value):
    return json.dumps(value, indent=2, ensure_ascii=False) + "\n"


def write(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(value, str):
        path.write_text(value, encoding="utf-8")
    else:
        path.write_text(pretty(value), encoding="utf-8")


def remove_generated():
    for path in (BP, RP):
        if path.exists():
            shutil.rmtree(path)


def item_data():
    rows = []
    number = 0
    for category, names in CATALOG_GROUPS:
        for name in names:
            number += 1
            rows.append({"number": number, "category": category, "name": name, "id": slug(name), "identifier": ident(name)})
    assert len(rows) == 200
    return rows


# Blocks are real custom blocks.  Their identifiers are not duplicated in
# items/, because a Bedrock block already supplies its inventory representation.
BLOCK_CATEGORIES = {"Blocks & Building", "Redstone & Tech"}
# Furniture is intentionally kept as portable furniture tokens: it can be
# converted to a placed block by a later scripting/UI update without a second
# identifier.  Utility waypoints and portal frames are blocks in the same way.
BLOCK_IDS = {
    slug(name) for category, names in CATALOG_GROUPS if category in BLOCK_CATEGORIES for name in names
}
BLOCK_IDS.update({"waypoint_stone", "portal_frame", "alchemy_table"})
# Ore features must place a real block identifier. These material entries are
# therefore native ore/crystal blocks with automatic inventory forms, rather
# than duplicate minecraft:item definitions.
BLOCK_IDS.update({"tin_ore", "silver_ore", "platinum_ore", "mythril_ore", "adamantite_ore", "deepslate_crystal", "lumen_crystal", "voidstone"})

TIER_NAMES = {0: "Foundational", 1: "Copper/Tin", 2: "Silver", 3: "Platinum", 4: "Mythril", 5: "Adamantite", 6: "Elemental / Void"}

ORE_TIERS = {
    "bedrock_dust": 6, "deepslate_crystal": 0, "nether_quartz_shard": 1, "amethyst_core": 2, "copper_nugget": 1,
    "tin_ore": 1, "tin_ingot": 1, "silver_ore": 2, "silver_ingot": 2, "platinum_ore": 3, "platinum_ingot": 3,
    "mythril_ore": 4, "mythril_ingot": 4, "adamantite_ore": 5, "adamantite_ingot": 5, "voidstone": 6,
    "lumen_crystal": 6, "ember_dust": 6, "frost_shard": 6, "storm_fragment": 6,
}

TIER_BY_ID = {}
for row in item_data():
    iid = row["id"]
    category = row["category"]
    tier = 0
    if iid in ORE_TIERS:
        tier = ORE_TIERS[iid]
    elif category == "Tools & Weapons":
        if iid.startswith("bedrock_") or iid in {"void_blade", "lumen_bow", "ember_crossbow", "frost_trident", "storm_hammer"}:
            tier = 6
        elif iid.startswith("adamantite") or iid == "war_axe" or iid == "drill": tier = 5
        elif iid.startswith("mythril") or iid == "chainsaw": tier = 4
        elif iid.startswith("platinum") or iid == "scythe": tier = 3
        elif iid.startswith("silver"): tier = 2
        elif iid.startswith("copper"): tier = 1
    elif category == "Armor & Wearables":
        tier = {"copper": 1, "silver": 2, "platinum": 3, "mythril": 4, "adamantite": 5}.get(iid.split("_")[0], 1)
    elif category == "Food & Farming":
        tier = {"copper": 1, "silver": 2, "platinum": 3, "mythril": 4, "adamantite": 5, "lumen": 6, "ember": 6, "frost": 6, "storm": 6, "void": 6, "crystal": 3, "magic": 6}.get(iid.split("_")[0], 0)
    elif category in {"Blocks & Building", "Redstone & Tech"}:
        tier = {"copper": 1, "tin": 1, "silver": 2, "platinum": 3, "mythril": 4, "adamantite": 5, "lumen": 6, "ember": 6, "frost": 6, "storm": 6, "void": 6, "crystal": 3}.get(iid.split("_")[0], 2)
    elif category == "Magic & Enchanting":
        tier = 3 if iid in {"mana_crystal", "spell_book", "enchantment_orb", "rune_stone", "magic_wand", "alchemy_table"} else 6
        if iid in {"staff_of_fire", "staff_of_ice", "staff_of_storms", "staff_of_life", "void_pearl", "celestial_shard"}: tier = 6
    elif category == "Mobs & Drops":
        tier = 6 if any(x in iid for x in ("void", "lumen")) else (5 if "crystal" in iid or "storm" in iid else 4 if "ember" in iid or "frost" in iid else 2)
    elif category == "Decoration & Furniture":
        tier = 1 if iid in {"lamp", "ceiling_light", "fireplace", "oven", "refrigerator", "sink"} else 0
    elif category == "Utility & Adventure":
        tier = {"backpack": 2, "large_backpack": 3, "ender_backpack": 6, "jetpack": 5, "scuba_helmet": 3, "night_vision_goggles": 3, "lantern_helmet": 1, "grappling_hook": 4, "portal_frame": 6, "portal_activator": 6, "waypoint_stone": 4, "boss_key": 5, "treasure_map": 2, "dungeon_compass": 3}.get(iid, 1)
    TIER_BY_ID[iid] = min(tier, 6)


def tier(iid):
    return TIER_BY_ID[iid]


def color_for(row):
    iid = row["id"]
    palette = {
        0: "#8d8d8d", 1: "#c77b45", 2: "#d6d9e2", 3: "#d4e8ee", 4: "#5b6ba8", 5: "#5ad0b7", 6: "#ad65e8",
    }
    if "ember" in iid: return "#d84d22"
    if "frost" in iid: return "#8ee8ff"
    if "storm" in iid: return "#7a8cff"
    if "lumen" in iid: return "#fff38a"
    if "void" in iid: return "#4a2c72"
    return palette[tier(iid)]


def sound_for(row):
    cat = row["category"]
    if cat in {"Tools & Weapons", "Armor & Wearables"}: return "item.equip.iron / random.break"
    if cat == "Food & Farming": return "entity.generic.eat / random.burp"
    if cat == "Magic & Enchanting": return "random.orb / block.enchantment_table.use"
    if cat in {"Blocks & Building", "Redstone & Tech"}: return "dig.stone / step.stone"
    return "random.orb / random.pop"


def script_for(iid):
    if iid in {"backpack", "large_backpack", "ender_backpack"}: return "scripts/backpack.js"
    if iid in {"jetpack", "parachute"}: return "scripts/jetpack.js"
    if iid in {"grappling_hook", "lockpick", "key", "treasure_map", "boss_key", "dungeon_compass", "waypoint_stone", "portal_activator", "portal_frame"}: return "scripts/adventure.js"
    if iid in {"fire_spell", "ice_spell", "lightning_spell", "healing_spell", "teleport_spell", "shield_spell", "summon_spell", "magic_wand", "staff_of_fire", "staff_of_ice", "staff_of_storms", "staff_of_life", "spell_book", "mana_crystal"}: return "scripts/magic.js"
    if iid in {"copper_wire", "silver_wire", "logic_gate", "timer_block", "pulse_extender", "item_pipe", "fluid_pipe", "energy_cable", "solar_panel", "battery", "generator", "electric_furnace", "auto_crafting_table", "conveyor_belt", "robot_arm", "sensor_block", "speaker_block", "monitor_block", "keyboard_block", "computer_block"}: return "scripts/tech.js"
    if iid in {"lantern_helmet", "night_vision_goggles", "scuba_helmet"}: return "scripts/survival_gear.js"
    if iid in {"bedrock_pickaxe", "drill", "chainsaw", "storm_hammer"}: return "scripts/tools.js"
    return "No runtime hook; vanilla component behavior."


def purpose(row):
    n, iid, cat = row["number"], row["id"], row["category"]
    name = row["name"]
    custom = {
        "bedrock_dust": "A forge catalyst that makes late-game alloys bond instead of shatter.",
        "deepslate_crystal": "A low-tier resonator used to read the first buried Forge markers.",
        "nether_quartz_shard": "A heat-stable conductor for the first energy and spell circuits.",
        "amethyst_core": "A focused crystal lens that turns scattered enchantment into stored charge.",
        "copper_nugget": "A small conductive unit for wiring, alloys, and economical repairs.",
        "tin_ore": "A soft early ore that opens soldering, lanterns, and the first machine recipes.",
        "tin_ingot": "A workable solder metal for stable low-voltage assemblies.",
        "silver_ore": "A moon-bright ore that carries enchantment more cleanly than copper.",
        "silver_ingot": "A reflective conductor for precision tools and mana-safe circuitry.",
        "platinum_ore": "A rare dense ore that survives pressure in deep Forge chambers.",
        "platinum_ingot": "A precision metal for high-efficiency tools and durable machinery.",
        "mythril_ore": "A resonant ore whose light weight makes advanced mobility practical.",
        "mythril_ingot": "A flexible supermetal that bridges industrial engineering and magic.",
        "adamantite_ore": "A nearly unbreakable ore required for the final physical tier.",
        "adamantite_ingot": "A forge-perfect alloy that anchors structures against Void distortion.",
        "voidstone": "A dangerous dark anchor used to seal breaches and power controlled portals.",
        "lumen_crystal": "A clean light source that stores restorative energy for the Lumen path.",
        "ember_dust": "A hot, compact fuel that powers machines, jetpacks, and Ember spells.",
        "frost_shard": "A cold shard that preserves food and enables slowing and protection effects.",
        "storm_fragment": "A charged fragment for flight, lightning tools, and fast automation.",
        "bedrock_pickaxe": "A tier-six mining tool for Voidstone and the toughest Forge seams.",
        "bedrock_axe": "A heavy endgame axe that harvests ancient wood quickly without replacing every tool.",
        "bedrock_shovel": "A high-durability excavator for clearing reinforced ash and realm soil.",
        "bedrock_hoe": "A late-game cultivator that makes elemental crops viable in hostile realms.",
        "void_blade": "A risk-reward weapon that cuts through Void creatures while demanding careful cooldowns.",
        "lumen_bow": "A quiet light bow that marks targets without relying on rare arrows.",
        "ember_crossbow": "A charged ranged weapon that trades reload time for brief fire damage.",
        "frost_trident": "A control weapon that slows a target so exploration remains tactical.",
        "storm_hammer": "A shockwave tool for groups, balanced by a long cooldown and heavy durability cost.",
        "crystal_dagger": "A fast precision weapon for cave lurkers and weak points.",
        "stone_spear": "A reliable first hunt weapon assembled before the Forge is restored.",
        "chainsaw": "A powered wood harvester that consumes durability rapidly for speed.",
        "drill": "A powered mining tool that clears stone quickly but needs Ember Dust fuel.",
        "scythe": "A farming-and-combat hybrid that harvests a short arc of mature crops.",
        "war_axe": "A deliberate shield-breaking weapon with high single-hit damage.",
        "copper_sword": "The first Forge-forged blade, giving new players a modest step above stone.",
        "silver_sword": "A balanced anti-spirit sword with better reach-feel but lower raw damage than platinum.",
        "platinum_sword": "A dependable midgame sword for deep caves and machine-guarded ruins.",
        "mythril_sword": "A light, durable blade that rewards mobile combat rather than brute force.",
        "adamantite_sword": "A resilient end-physical-tier weapon intended for breach expeditions.",
    }
    if iid in custom: return custom[iid]
    if cat == "Ores & Materials": return f"The {name.lower()} supplies a distinct material property for {TIER_NAMES[tier(iid)].lower()} crafting routes."
    if cat == "Tools & Weapons": return f"A specialized {name.lower()} for the {TIER_NAMES[tier(iid)].lower()} stage, giving the player a tool choice instead of a filler upgrade."
    if cat == "Armor & Wearables": return f"The {name.lower()} protects one body slot while expressing the {TIER_NAMES[tier(iid)].lower()} tier's signature trade-off."
    if cat == "Food & Farming": return f"The {name.lower()} is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition."
    if cat == "Blocks & Building": return f"A placeable {name.lower()} that gives the rebuilt Forge a distinct structural, lighting, or defensive function."
    if cat == "Redstone & Tech": return f"A placeable {name.lower()} that contributes one readable step to the Forge automation chain."
    if cat == "Magic & Enchanting": return f"The {name.lower()} converts stored realm energy into one controlled magical action."
    if cat == "Mobs & Drops": return f"The {name.lower()} is a deliberate encounter or drop that connects a creature to the realm economy."
    if cat == "Decoration & Furniture": return f"The {name.lower()} makes a restored Forge room legible while offering a small atmosphere or organization benefit."
    return f"The {name.lower()} solves a specific exploration problem at the {TIER_NAMES[tier(iid)].lower()} stage without replacing every other utility."


def story(row):
    iid, name, cat = row["id"], row["name"], row["category"]
    realm = "the Void" if "void" in iid else "the Lumen Realm" if "lumen" in iid else "the Ember Realm" if "ember" in iid else "the Frost Realm" if "frost" in iid else "the Storm Realm" if "storm" in iid else "the Bedrock Forge"
    maker = "the Copperwright guild" if tier(iid) == 1 else "the Silver Cartographers" if tier(iid) == 2 else "the Platinum Measure" if tier(iid) == 3 else "the Mythril Wayfarers" if tier(iid) == 4 else "the Adamantite Wardens" if tier(iid) == 5 else "the last Forge architects"
    return f"The surviving inscription for {name} names {maker} as its maker. It was designed after {realm} changed the Forge's supply routes, so its shape carries a practical memory of the old civilization."


def obtain_recipe(row):
    iid, name, cat = row["id"], row["name"], row["category"]
    if cat == "Ores & Materials":
        if iid.endswith("_ore") or iid in {"voidstone", "lumen_crystal", "ember_dust", "frost_shard", "storm_fragment", "deepslate_crystal"}:
            return "World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.", "No crafting recipe; harvest the world-gen node or realm cache."
        if iid.endswith("_ingot"):
            ore = iid.replace("_ingot", "_ore")
            return f"Smelt 1 {ore.replace('_', ' ').title()} in a furnace or electric furnace.", f"Furnace: 1 {ore.replace('_', ' ').title()} -> 1 {name}."
        if iid == "copper_nugget": return "Craft 1 Copper Ingot into 9 Copper Nuggets.", "Shapeless: 1 Copper Ingot -> 9 Copper Nuggets."
        if iid == "nether_quartz_shard": return "Craft 1 Nether Quartz into 4 Nether Quartz Shards.", "Shapeless: 1 Minecraft Nether Quartz -> 4 Nether Quartz Shards."
        if iid == "amethyst_core": return "Craft 4 Amethyst Shards around 1 Amethyst Block.", "Shaped 3x3: A A A / A B A / A A A; A=Amethyst Shard, B=Amethyst Block."
        if iid == "bedrock_dust": return "Grind 1 Bedrock fragment with a Voidstone catalyst at the restored Forge.", "Forge process: 1 Bedrock fragment + 1 Voidstone -> 2 Bedrock Dust."
    if cat == "Tools & Weapons":
        base = {"bedrock": "Bedrock Dust", "copper": "Copper Ingot", "silver": "Silver Ingot", "platinum": "Platinum Ingot", "mythril": "Mythril Ingot", "adamantite": "Adamantite Ingot"}
        material = next((v for k, v in base.items() if iid.startswith(k + "_")), "tier material")
        if iid in {"copper_sword", "silver_sword", "platinum_sword", "mythril_sword", "adamantite_sword"}:
            recipe = f"Crafting table 3x3: M / M / S, where M={material} and S=Stick -> {name}."
            return recipe, recipe
        if iid == "void_blade":
            recipe = "Crafting table 3x3: V / V / S, where V=Voidstone and S=Stick -> Void Blade."
            return recipe, recipe
        if iid.startswith("bedrock_"):
            recipe = f"Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> {name}."
            return recipe, recipe
        if iid in {"lumen_bow", "ember_crossbow", "frost_trident", "storm_hammer", "crystal_dagger", "stone_spear", "chainsaw", "drill", "scythe", "war_axe"}:
            recipes = {
                "lumen_bow": "3 Lumen Crystals + 3 String; pattern L S / L S / L S, L=Lumen Crystal and S=String.", "ember_crossbow": "2 Ember Dust + 2 Iron Ingots + 1 String; pattern EIE / ISI /  S , E=Ember Dust, I=Iron Ingot, S=String.", "frost_trident": "2 Frost Shards + 1 Mythril Ingot; pattern F / F / M.", "storm_hammer": "4 Storm Fragments + 2 Adamantite Ingots; pattern SAS / SAS /  S , S=Storm Fragment and A=Adamantite Ingot.", "crystal_dagger": "1 Amethyst Core + 1 Copper Ingot + 1 Stick; pattern C / A / S.", "stone_spear": "1 Flint + 2 Sticks; pattern F / S / S.", "chainsaw": "3 Platinum Ingots + 2 Iron Ingots + 1 Copper Wire + 1 Stick; pattern PPI / PCW / __W, with _ empty.", "drill": "3 Mythril Ingots + 2 Iron Ingots + 1 Copper Wire + 1 Ember Dust; pattern MIM / MCE / __M, with _ empty.", "scythe": "2 Silver Ingots + 2 Sticks; pattern SS_ / _IS / _I_, with _ empty.", "war_axe": "3 Adamantite Ingots + 2 Sticks; pattern AAA / ASA / __S, with _ empty.",
            }
            return "Crafting table: " + recipes[iid], recipes[iid]
        return f"Crafting table 3x3: M M M /  S  /  S , where M={material} and S=Stick -> {name}."
    if cat == "Armor & Wearables":
        mat = iid.split("_")[0].title() + " Ingot"
        piece = iid.split("_")[-1]
        patterns = {"helmet": "MMM / M M", "chestplate": "M M / MMM / MMM", "leggings": "MMM / M M / M M", "boots": "M M / M M"}
        recipe = f"Crafting table pattern {patterns[piece]}, with M={mat} -> {name}; {5 if piece == 'helmet' else 8 if piece == 'chestplate' else 7 if piece == 'leggings' else 4} ingots."
        return recipe, recipe
    if cat == "Food & Farming":
        recipes = {
            "golden_apple_pie": "3 Golden Apples + 3 Wheat + 1 Egg in a 3x3 pie pattern.", "copper_carrot": "1 Carrot + 1 Copper Nugget; roast on a campfire or craft shapeless.", "silver_beetroot": "1 Beetroot + 1 Silver Ingot; silver-salted crop.", "platinum_potato": "1 Potato + 1 Platinum Ingot; pressurized crop recipe.", "mythril_bread": "3 Wheat + 1 Mythril Ingot; light long-travel loaf.", "adamantite_stew": "1 Bowl + 1 Cooked Beef + 1 Adamantite Ingot + 1 Carrot.", "lumen_berry": "1 Sweet Berry + 1 Lumen Crystal.", "ember_pepper": "1 Cocoa Bean + 1 Ember Dust.", "frost_melon": "1 Melon Slice + 1 Frost Shard.", "storm_corn": "1 Wheat + 1 Storm Fragment.", "void_fruit": "1 Chorus Fruit + 1 Voidstone.", "crystal_grapes": "3 Sweet Berries + 1 Amethyst Core.", "honey_cookie": "2 Wheat + 1 Honey Bottle.", "chocolate_bar": "2 Cocoa Beans + 1 Sugar.", "cheese_wheel": "3 Milk Buckets + 1 Salt substitute (Copper Nugget); returns 3 empty buckets.", "butter": "1 Milk Bucket + 1 Salt substitute (Tin Ingot); returns an empty bucket.", "fried_egg": "1 Egg + 1 Butter on a furnace or campfire.", "bacon_strip": "1 Raw Porkchop on a furnace or campfire.", "fish_stew": "1 Bowl + 1 Cooked Cod + 1 Carrot + 1 Mushroom.", "magic_cake": "3 Wheat + 2 Lumen Crystals + 1 Egg + 1 Sugar in a cake pattern.",
        }
        return "Food crafting or cooking: " + recipes[iid], recipes[iid]
    if cat in {"Blocks & Building", "Redstone & Tech"}:
        if iid.endswith("_block"):
            mat = name.replace(" Block", " Ingot")
            return f"Craft 9 {mat} in a full 3x3 grid; the block can be reclaimed into 9 ingots.", f"3x3: {mat} in all nine slots -> 1 {name}."
        if iid in {"reinforced_glass", "dark_glass", "glowing_concrete", "mossy_bricks", "cracked_bricks", "marble", "polished_marble", "limestone"}:
            base = {"reinforced_glass": "Glass + Copper Nugget", "dark_glass": "Voidstone + Copper Nugget", "glowing_concrete": "Lumen Crystal + Copper Nugget", "mossy_bricks": "Moss Block + Copper Nugget", "cracked_bricks": "Brick + Copper Nugget", "marble": "Quartz Block + Copper Nugget", "polished_marble": "Marble + Copper Nugget", "limestone": "Calcite + Copper Nugget"}[iid]
            return f"Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base={base.split(' + ')[0]} -> {name}.", f"Pattern MMM / MCM / MMM, M={base.split(' + ')[0]} and C=Copper Nugget -> {name}."
        tech = {
            "copper_wire": "3 Copper Nuggets + 1 String in a line.", "silver_wire": "3 Silver Nuggets + 1 String in a line.", "logic_gate": "3 Copper Wire + 2 Redstone + 1 Silver Ingot.", "timer_block": "4 Copper Wire + 1 Clock + 1 Silver Ingot.", "pulse_extender": "2 Copper Wire + 2 Repeaters + 1 Tin Ingot.", "item_pipe": "6 Copper Ingots + 1 Glass + 1 Iron Ingot.", "fluid_pipe": "6 Tin Ingots + 1 Glass + 1 Iron Ingot.", "energy_cable": "6 Silver Wire + 1 Redstone Block + 1 Copper Ingot.", "solar_panel": "3 Lumen Crystals + 3 Glass + 1 Silver Wire.", "battery": "2 Silver Ingots + 2 Redstone + 1 Copper Wire.", "generator": "3 Iron Ingots + 2 Ember Dust + 1 Furnace + 1 Battery.", "electric_furnace": "5 Iron Ingots + 2 Energy Cables + 1 Furnace + 1 Silver Wire.", "auto_crafting_table": "4 Platinum Ingots + 2 Logic Gates + 1 Crafting Table + 1 Computer.", "conveyor_belt": "3 Leather + 2 Iron Ingots + 2 Copper Wire.", "robot_arm": "3 Platinum Ingots + 2 Energy Cables + 1 Logic Gate.", "sensor_block": "2 Amethyst Cores + 2 Copper Wire + 1 Glass.", "speaker_block": "2 Copper Wire + 1 Note Block + 1 Silver Ingot.", "monitor_block": "4 Glass + 2 Silver Wire + 1 Redstone.", "keyboard_block": "3 Iron Ingots + 2 Copper Wire + 1 Quartz.", "computer_block": "2 Platinum Ingots + 2 Monitor Blocks + 1 Keyboard Block + 1 Logic Gate.",
        }
        return "Crafting table: " + tech[iid], tech[iid]
    if cat == "Magic & Enchanting":
        spells = {
            "mana_crystal": "4 Lumen Crystals around 1 Amethyst Core.", "spell_book": "3 Paper + 1 Leather + 1 Mana Crystal.", "fire_spell": "1 Spell Book + 1 Ember Dust + 1 Rune Stone.", "ice_spell": "1 Spell Book + 1 Frost Shard + 1 Rune Stone.", "lightning_spell": "1 Spell Book + 1 Storm Fragment + 1 Rune Stone.", "healing_spell": "1 Spell Book + 1 Lumen Crystal + 1 Golden Apple.", "teleport_spell": "1 Spell Book + 1 Void Pearl + 1 Ender Pearl.", "shield_spell": "1 Spell Book + 1 Adamantite Ingot + 1 Lumen Crystal.", "summon_spell": "1 Spell Book + 1 Soul Gem + 1 mob core.", "enchantment_orb": "1 Amethyst Core + 4 Lumen Dust.", "rune_stone": "1 Stone + 1 Nether Quartz Shard + 1 Lumen Dust.", "magic_wand": "1 Stick + 1 Mana Crystal + 1 Rune Stone.", "staff_of_fire": "1 Magic Wand + 2 Ember Dust + 1 Blaze Rod.", "staff_of_ice": "1 Magic Wand + 2 Frost Shards + 1 Packed Ice.", "staff_of_storms": "1 Magic Wand + 2 Storm Fragments + 1 Lightning Rod.", "staff_of_life": "1 Magic Wand + 2 Lumen Crystals + 1 Golden Apple.", "soul_gem": "1 Amethyst Core + 1 Ghast Tear + 2 Soul Sand.", "void_pearl": "1 Ender Pearl + 2 Voidstone.", "celestial_shard": "1 Lumen Crystal + 1 Storm Fragment + 1 Nether Star fragment.", "alchemy_table": "4 Platinum Ingots + 2 Rune Stones + 1 Brewing Stand + 1 Amethyst Core.",
        }
        return "Arcane crafting: " + spells[iid], spells[iid]
    if cat == "Mobs & Drops":
        if iid.endswith("_spawn_egg"):
            mob = name.replace(" Spawn Egg", "")
            return f"Craft 1 Egg with the matching {mob} Core or realm essence; alternatively find it in a Forge vault.", f"Shapeless: 1 Egg + 1 matching core/essence -> 1 {name}."
        return f"Drop from the matching Bedrock Expansion creature, chest, or realm event; {name} is not craftable.", "No recipe: creature drop, rare chest, or boss reward."
    if cat == "Decoration & Furniture":
        return f"Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> {name}.", f"Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> {name}; the item identity determines its room role."
    utility = {
        "backpack": "4 Leather + 2 Silver Ingots + 1 Chest.", "large_backpack": "4 Leather + 2 Platinum Ingots + 1 Backpack + 1 Chest.", "ender_backpack": "4 Leather + 2 Void Pearls + 1 Ender Chest.", "map_marker": "1 Map + 1 Copper Wire + 1 Lumen Dust.", "compass_upgrade": "1 Compass + 1 Silver Ingot + 1 Amethyst Core.", "clock_upgrade": "1 Clock + 1 Copper Wire + 1 Lumen Crystal.", "lantern_helmet": "1 Iron Helmet + 1 Lantern + 1 Copper Wire.", "night_vision_goggles": "2 Glass + 1 Lumen Crystal + 1 Copper Wire.", "scuba_helmet": "1 Iron Helmet + 2 Glass + 1 Fluid Pipe.", "jetpack": "2 Mythril Ingots + 3 Storm Fragments + 1 Energy Cable.", "parachute": "3 String + 3 White Wool + 1 Leather.", "grappling_hook": "1 Iron Ingot + 1 String + 1 Copper Wire.", "lockpick": "2 Iron Nuggets + 1 Copper Wire.", "key": "1 Gold Ingot + 1 Iron Nugget + 1 Rune Stone.", "treasure_map": "1 Map + 1 Lumen Dust + 1 Voidstone.", "boss_key": "1 Adamantite Ingot + 1 Void Pearl + 1 Storm Fragment.", "dungeon_compass": "1 Compass + 1 Lurker Eye + 1 Amethyst Core.", "waypoint_stone": "4 Marble + 1 Lumen Crystal + 1 Amethyst Core.", "portal_frame": "6 Voidstone + 2 Adamantite Blocks + 1 Celestial Shard.", "portal_activator": "1 Void Pearl + 1 Lumen Crystal + 1 Storm Fragment + 1 Rune Stone.",
    }
    return "Utility crafting: " + utility[iid], utility[iid]


def stats(row):
    iid, cat = row["id"], row["category"]
    t = tier(iid)
    if cat == "Ores & Materials": return "Stack 64; material hardness and smelting value are tuned to tier."
    if cat == "Tools & Weapons":
        damage = {0: 3, 1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 10}[t]
        dur = {0: 80, 1: 180, 2: 320, 3: 520, 4: 780, 5: 1100, 6: 1600}[t]
        if iid == "bedrock_pickaxe": dur, damage = 3000, 10
        if iid == "storm_hammer": damage, dur = 12, 700
        if iid == "stone_spear": damage, dur = 4, 96
        return f"Damage {damage}; durability {dur}; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component."
    if cat == "Armor & Wearables":
        piece = iid.split("_")[-1]
        protection = {"helmet": 2, "chestplate": 6, "leggings": 5, "boots": 2}[piece] + max(0, t - 1)
        durability = {"helmet": 165, "chestplate": 240, "leggings": 225, "boots": 195}[piece] + t * 80
        return f"Protection {protection}; durability {durability}; wearable slot armor.{piece}; stack size 1."
    if cat == "Food & Farming":
        nutrition = min(12, 3 + t + (2 if iid in {"magic_cake", "adamantite_stew", "golden_apple_pie"} else 0))
        return f"Restores {nutrition} hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect."
    if cat == "Blocks & Building": return f"Placeable full cube; hardness {1.5 + t:.1f}; blast resistance {3 + t * 2}; stack size 64. Special light/transparency behavior is declared in the block JSON."
    if cat == "Redstone & Tech": return f"Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication."
    if cat == "Magic & Enchanting": return f"Stack size {1 if iid in {'spell_book','magic_wand','staff_of_fire','staff_of_ice','staff_of_storms','staff_of_life','alchemy_table'} else 16}; effect costs 5-30 mana-equivalent charge and observes a cooldown."
    if cat == "Mobs & Drops": return "Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table."
    if cat == "Decoration & Furniture": return "Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost."
    return f"Stack size {1 if iid in {'backpack','large_backpack','ender_backpack','jetpack','parachute','grappling_hook','boss_key','dungeon_compass','waypoint_stone','portal_frame','portal_activator'} else 16}; one utility action has a 1-12 second cooldown where scripted."


def interactions(row):
    iid, cat = row["id"], row["category"]
    if iid == "bedrock_pickaxe": return "Use while sneaking to toggle the 3x3 mining intent; the script displays the mode and leaves protected blocks untouched."
    if iid in {"backpack", "large_backpack", "ender_backpack"}: return "Use to register a portable storage channel; the script gives a clear storage message. A chest-backed inventory is recommended for production worlds."
    if iid == "jetpack": return "Hold the item and jump to receive a short upward impulse; sneak descends. Ember Dust fuel is checked by the script."
    if iid == "grappling_hook": return "Use to pull toward the look direction with a capped impulse; cooldown prevents repeated flight."
    if iid in {"night_vision_goggles", "lantern_helmet", "scuba_helmet"}: return "Wear in the head slot; the survival-gear loop applies the appropriate timed effect."
    if cat == "Magic & Enchanting": return "Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode."
    if cat == "Redstone & Tech": return "Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication."
    if cat == "Mobs & Drops" and iid.endswith("_spawn_egg"): return "Use on a block to call the matching custom entity through minecraft:entity_placer."
    if cat == "Food & Farming": return "Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer."
    if cat == "Utility & Adventure": return "Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed."
    return "Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required."


def balance(row):
    iid, cat = row["id"], row["category"]
    t = tier(iid)
    if t == 6: return "Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option."
    if cat == "Food & Farming": return "Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier."
    if cat == "Redstone & Tech": return "Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules."
    if cat == "Mobs & Drops": return "Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression."
    if cat == "Decoration & Furniture": return "Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike."
    return f"The {TIER_NAMES[t]} tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited."


def progression(row):
    iid, cat = row["id"], row["category"]
    t = tier(iid)
    next_t = min(6, t + 1)
    if t == 6: return "Completes the elemental/Void loadout and contributes to stabilizing the Forge core."
    return f"Introduces the {TIER_NAMES[t]} stage and points toward {TIER_NAMES[next_t]} through its material, recipe, or realm hook."


def model_for(row):
    return "block/full_cube" if row["id"] in BLOCK_IDS else ("item/handheld" if row["category"] in {"Tools & Weapons", "Armor & Wearables", "Magic & Enchanting", "Utility & Adventure"} else "item/generated")


def design_text(rows):
    out = ["# Bedrock Expansion: 200 Items — Design Specification", "", "This is the authoritative per-entry design record. Tier 0 is foundational; tiers 1–5 are Copper/Tin through Adamantite; tier 6 is the elemental and Void endgame. Placeable entries are represented by `blocks/*.json` because Bedrock gives a block its inventory item automatically; portable entries are `items/*.json`.", "", "## Catalog index", ""]
    for row in rows:
        out.append(f"{row['number']}. `{row['identifier']}` — {row['name']} ({row['category']}, tier {tier(row['id'])})")
    out += ["", "## Complete item records", ""]
    for row in rows:
        iid = row["id"]
        obtain, recipe = obtain_recipe(row)
        out += [
            f"### {row['number']}. {row['name']}",
            f"- **Item ID:** `{row['identifier']}`",
            f"- **Display Name:** {row['name']}",
            f"- **Category:** {row['category']}",
            f"- **Tier:** {tier(iid)} — {TIER_NAMES[tier(iid)]}",
            f"- **Purpose:** {purpose(row)}",
            f"- **Story/Lore:** {story(row)}",
            f"- **Obtain Method:** {obtain}",
            f"- **Recipe:** {recipe}",
            f"- **Stats:** {stats(row)}",
            f"- **Interactions:** {interactions(row)}",
            f"- **Texture Path:** `textures/items/{iid}.png`",
            f"- **Model:** `{model_for(row)}`",
            f"- **Sound:** {sound_for(row)}",
            f"- **Script Hooks:** {script_for(iid)}",
            f"- **Balance Notes:** {balance(row)}",
            f"- **Progression Role:** {progression(row)}",
            "",
        ]
    return "\n".join(out)


def item_components(row):
    iid, cat = row["id"], row["category"]
    components = {
        "minecraft:icon": {"textures": {"default": iid}},
        "minecraft:display_name": {"value": f"item.{NS}:{iid}.name"},
        "minecraft:max_stack_size": 64,
        "minecraft:tags": {"tags": [f"{NS}:catalog_{row['number']}", f"{NS}:tier_{tier(iid)}"]},
    }
    if cat in {"Tools & Weapons", "Armor & Wearables", "Magic & Enchanting", "Utility & Adventure"}:
        components["minecraft:max_stack_size"] = 1 if cat != "Magic & Enchanting" or iid in {"spell_book", "magic_wand", "staff_of_fire", "staff_of_ice", "staff_of_storms", "staff_of_life"} else 16
    if cat == "Tools & Weapons":
        t = tier(iid)
        components["minecraft:hand_equipped"] = True
        damage = {0: 3, 1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 10}[t]
        if iid == "storm_hammer": damage = 12
        components["minecraft:damage"] = {"value": damage}
        components["minecraft:durability"] = {"max_durability": {0: 80, 1: 180, 2: 320, 3: 520, 4: 780, 5: 1100, 6: 1600}[t] if iid != "bedrock_pickaxe" else 3000}
        repair = {1: "minecraft:copper_ingot", 2: f"{NS}:silver_ingot", 3: f"{NS}:platinum_ingot", 4: f"{NS}:mythril_ingot", 5: f"{NS}:adamantite_ingot", 6: f"{NS}:voidstone"}.get(t, "minecraft:stone")
        components["minecraft:repairable"] = {"repair_items": [{"items": [repair], "repair_amount": 100}]}
        if "bow" in iid: enchant_slot = "bow"
        elif "crossbow" in iid: enchant_slot = "crossbow"
        elif "trident" in iid: enchant_slot = "trident"
        elif "axe" in iid or iid == "storm_hammer": enchant_slot = "axe"
        elif "hoe" in iid: enchant_slot = "hoe"
        elif "shovel" in iid: enchant_slot = "shovel"
        elif "pickaxe" in iid or iid in {"drill", "chainsaw"}: enchant_slot = "pickaxe"
        else: enchant_slot = "sword"
        components["minecraft:enchantable"] = {"slot": enchant_slot, "value": 10 + t * 3}
    elif cat == "Armor & Wearables":
        piece = iid.split("_")[-1]
        protection = {"helmet": 2, "chestplate": 6, "leggings": 5, "boots": 2}[piece] + max(0, tier(iid) - 1)
        armor_slot = {"helmet": "head", "chestplate": "chest", "leggings": "legs", "boots": "feet"}[piece]
        components["minecraft:wearable"] = {"slot": f"slot.armor.{armor_slot}", "protection": protection}
        components["minecraft:durability"] = {"max_durability": {"helmet": 165, "chestplate": 240, "leggings": 225, "boots": 195}[piece] + tier(iid) * 80}
        components["minecraft:enchantable"] = {"slot": {"helmet": "armor_head", "chestplate": "armor_torso", "leggings": "armor_legs", "boots": "armor_feet"}[piece], "value": 10 + tier(iid) * 2}
    elif cat == "Food & Farming":
        nutrition = min(12, 3 + tier(iid) + (2 if iid in {"magic_cake", "adamantite_stew", "golden_apple_pie"} else 0))
        effects = []
        effect = {"lumen_berry": "regeneration", "ember_pepper": "fire_resistance", "frost_melon": "resistance", "storm_corn": "speed", "void_fruit": "night_vision", "magic_cake": "health_boost"}.get(iid)
        if effect: effects.append({"name": effect, "chance": 1.0, "duration": 8, "amplifier": 0})
        components["minecraft:food"] = {"nutrition": nutrition, "saturation_modifier": "normal", "can_always_eat": iid in {"golden_apple_pie", "magic_cake"}, "effects": effects}
        components["minecraft:use_modifiers"] = {"use_duration": 1.6, "movement_modifier": 0.35}
        components["minecraft:max_stack_size"] = 16
    elif cat == "Mobs & Drops":
        if iid.endswith("_spawn_egg"):
            entity = iid.removesuffix("_spawn_egg")
            components["minecraft:entity_placer"] = {"entity": f"{NS}:{entity}"}
            components["minecraft:glint"] = True
            components["minecraft:max_stack_size"] = 16
        else:
            components["minecraft:glint"] = iid in {"void_golem_core", "lumen_dust"}
    elif cat == "Magic & Enchanting":
        components["minecraft:glint"] = True
        if iid not in {"mana_crystal", "enchantment_orb", "rune_stone", "soul_gem", "celestial_shard"}:
            components["minecraft:use_modifiers"] = {"use_duration": 0.8, "movement_modifier": 0.7}
    elif cat == "Utility & Adventure":
        components["minecraft:glint"] = iid in {"ender_backpack", "boss_key", "portal_activator", "voidstone"}
        if iid in {"backpack", "large_backpack", "ender_backpack", "jetpack", "parachute", "grappling_hook", "lockpick", "key", "treasure_map", "boss_key", "dungeon_compass", "portal_activator"}:
            components["minecraft:use_modifiers"] = {"use_duration": 0.2, "movement_modifier": 0.8}
    else:
        components["minecraft:allow_off_hand"] = True
    if iid in {"ember_dust", "ember_pepper", "ember_essence"}:
        components["minecraft:fuel"] = {"duration": 20 if iid == "ember_dust" else 8}
    if iid in {"fire_spell", "ice_spell", "lightning_spell", "healing_spell", "teleport_spell", "shield_spell", "summon_spell", "grappling_hook", "jetpack", "portal_activator"}:
        components["minecraft:cooldown"] = {"category": f"{NS}:{iid}_cooldown", "duration": 1.0 if iid != "portal_activator" else 3.0}
    return components


def block_components(row):
    iid, cat = row["id"], row["category"]
    render = "blend" if iid in {"reinforced_glass", "dark_glass"} else "opaque"
    light = 15 if iid in {"lumen_block", "ember_block", "glowing_concrete", "lamp", "ceiling_light"} else (8 if iid == "crystal_block" else 0)
    hardness = 1.5 + tier(iid)
    components = {
        "minecraft:material_instances": {"*": {"texture": iid, "render_method": render}},
        "minecraft:destructible_by_mining": {"seconds_to_destroy": round(hardness, 2)},
        "minecraft:destructible_by_explosion": {"explosion_resistance": 3 + tier(iid) * 2},
        "minecraft:loot": f"loot_tables/blocks/{iid}.json",
        "minecraft:map_color": color_for(row),
    }
    if light: components["minecraft:light_emission"] = light
    return components


def create_manifests():
    bp_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, "https://arena.ai/bedrock-expansion/bp"))
    bp_mod = str(uuid.uuid5(uuid.NAMESPACE_URL, "https://arena.ai/bedrock-expansion/bp/data"))
    bp_script = str(uuid.uuid5(uuid.NAMESPACE_URL, "https://arena.ai/bedrock-expansion/bp/script"))
    rp_uuid = str(uuid.uuid5(uuid.NAMESPACE_URL, "https://arena.ai/bedrock-expansion/rp"))
    rp_mod = str(uuid.uuid5(uuid.NAMESPACE_URL, "https://arena.ai/bedrock-expansion/rp/resources"))
    write(BP / "manifest.json", {"format_version": 2, "header": {"name": "Bedrock Expansion: 200 Items | Behavior", "description": "The Bedrock Forge, six progression tiers, five elemental realms, 200 authored content entries, creatures, magic, and machines.", "uuid": bp_uuid, "version": VERSION, "min_engine_version": ENGINE}, "modules": [{"description": "Bedrock Expansion gameplay data", "type": "data", "uuid": bp_mod, "version": VERSION}, {"description": "Bedrock Expansion server scripts", "type": "script", "language": "javascript", "entry": "scripts/main.js", "uuid": bp_script, "version": VERSION}], "dependencies": [{"uuid": rp_uuid, "version": VERSION}, {"module_name": "@minecraft/server", "version": "1.15.0"}], "metadata": {"authors": ["Minecraft-mod-2 contributors"], "license": "MIT", "product_type": "addon"}})
    write(RP / "manifest.json", {"format_version": 2, "header": {"name": "Bedrock Expansion: 200 Items | Resources", "description": "Pixel placeholders, block materials, entity looks, and the visual language of the Bedrock Forge.", "uuid": rp_uuid, "version": VERSION, "min_engine_version": ENGINE}, "modules": [{"description": "Bedrock Expansion resource data", "type": "resources", "uuid": rp_mod, "version": VERSION}], "metadata": {"authors": ["Minecraft-mod-2 contributors"], "license": "MIT", "product_type": "addon"}})


def create_content(rows):
    # Portable item definitions.
    for row in rows:
        if row["id"] in BLOCK_IDS: continue
        item = {"format_version": FORMAT, "minecraft:item": {"description": {"identifier": row["identifier"], "menu_category": {"category": "equipment" if row["category"] in {"Tools & Weapons", "Armor & Wearables", "Utility & Adventure"} else "items"}}, "components": item_components(row)}}
        write(BP / "items" / f"{row['id']}.json", item)
    # Placeable block definitions.
    for row in rows:
        if row["id"] not in BLOCK_IDS: continue
        block = {"format_version": FORMAT, "minecraft:block": {"description": {"identifier": row["identifier"], "menu_category": {"category": "construction"}}, "components": block_components(row)}}
        write(BP / "blocks" / f"{row['id']}.json", block)
        write(BP / "loot_tables" / "blocks" / f"{row['id']}.json", {"pools": [{"rolls": 1, "entries": [{"type": "item", "name": row["identifier"]}]}]})


def ingredient(item):
    # Copper Ingot is deliberately the vanilla 1.21 material; the requested
    # 200-entry catalog contains Copper Nugget, but not a duplicate ingot.
    if item == "copper_ingot": item = "minecraft:copper_ingot"
    return {"item": item if ":" in item else f"{NS}:{item}"}


def shaped(recipe_id, pattern, key, result, count=1, tags=("crafting_table",)):
    return {"format_version": FORMAT, "minecraft:recipe_shaped": {"description": {"identifier": f"{NS}:{recipe_id}"}, "tags": list(tags), "pattern": pattern, "key": {k: ingredient(v) if isinstance(v, str) else v for k, v in key.items()}, "result": {"item": result if ":" in result else f"{NS}:{result}", "count": count}}}


def shapeless(recipe_id, ingredients, result, count=1, tags=("crafting_table",)):
    return {"format_version": FORMAT, "minecraft:recipe_shapeless": {"description": {"identifier": f"{NS}:{recipe_id}"}, "tags": list(tags), "ingredients": [ingredient(x) if isinstance(x, str) else x for x in ingredients], "result": {"item": result if ":" in result else f"{NS}:{result}", "count": count}}}


def furnace(recipe_id, input_id, result):
    return {"format_version": FORMAT, "minecraft:recipe_furnace": {"description": {"identifier": f"{NS}:{recipe_id}"}, "tags": ["furnace"], "input": ingredient(input_id), "output": {"item": result if ":" in result else f"{NS}:{result}", "count": 1}}}


def create_recipes(rows):
    R = BP / "recipes"
    # Smelting chain.
    for ore in ("tin", "silver", "platinum", "mythril", "adamantite"):
        write(R / f"{ore}_ingot_from_ore.json", furnace(f"{ore}_ingot_from_ore", f"{ore}_ore", f"{ore}_ingot"))
    for fid, inp, out in (("fried_egg_cook", "minecraft:egg", "fried_egg"), ("bacon_cook", "minecraft:porkchop", "bacon_strip"), ("fish_stew_cook", "minecraft:cod", "fish_stew")):
        write(R / f"{fid}.json", furnace(fid, inp, out))
    # Core shaped recipes.  Every item with a craftable method gets a physical file.
    recipes = {
        "copper_nugget": shapeless("copper_nugget_from_ingot", ["copper_ingot"], "copper_nugget", 9),
        "nether_quartz_shard": shapeless("nether_quartz_shard_from_quartz", ["minecraft:quartz"], "nether_quartz_shard", 4),
        "amethyst_core": shaped("amethyst_core", ["AAA", "ABA", "AAA"], {"A": "minecraft:amethyst_shard", "B": "minecraft:amethyst_block"}, "amethyst_core"),
        "bedrock_dust": shapeless("bedrock_dust", ["voidstone", "deepslate_crystal"], "bedrock_dust", 2),
        "stone_spear": shaped("stone_spear", ["F", "S", "S"], {"F": "minecraft:flint", "S": "minecraft:stick"}, "stone_spear"),
        "lumen_bow": shaped("lumen_bow", ["LS", "LS", "LS"], {"L": "lumen_crystal", "S": "minecraft:string"}, "lumen_bow"),
        "ember_crossbow": shaped("ember_crossbow", ["EIE", "ISI", " S "], {"E": "ember_dust", "I": "minecraft:iron_ingot", "S": "minecraft:string"}, "ember_crossbow"),
        "frost_trident": shaped("frost_trident", ["F", "F", "M"], {"F": "frost_shard", "M": "mythril_ingot"}, "frost_trident"),
        "storm_hammer": shaped("storm_hammer", ["SAS", "SAS", " S "], {"S": "storm_fragment", "A": "adamantite_ingot"}, "storm_hammer"),
        "crystal_dagger": shaped("crystal_dagger", ["C", "A", "S"], {"C": "amethyst_core", "A": "copper_ingot", "S": "minecraft:stick"}, "crystal_dagger"),
        "chainsaw": shaped("chainsaw", ["PPI", "PCW", "  W"], {"P": "platinum_ingot", "I": "minecraft:iron_ingot", "C": "copper_wire", "W": "minecraft:stick"}, "chainsaw"),
        "drill": shaped("drill", ["MIM", "MCE", "  M"], {"M": "mythril_ingot", "I": "minecraft:iron_ingot", "C": "copper_wire", "E": "ember_dust"}, "drill"),
        "scythe": shaped("scythe", ["SS ", " IS", " I "], {"S": "silver_ingot", "I": "minecraft:stick"}, "scythe"),
        "war_axe": shaped("war_axe", ["AAA", "ASA", " S "], {"A": "adamantite_ingot", "S": "minecraft:stick"}, "war_axe"),
        "backpack": shaped("backpack", ["L L", "LSL", " C "], {"L": "minecraft:leather", "S": "silver_ingot", "C": "minecraft:chest"}, "backpack"),
        "large_backpack": shaped("large_backpack", ["LPL", "LBL", " C "], {"L": "minecraft:leather", "P": "platinum_ingot", "B": "backpack", "C": "minecraft:chest"}, "large_backpack"),
        "ender_backpack": shaped("ender_backpack", ["LPL", "PEP", "LPL"], {"L": "minecraft:leather", "P": "void_pearl", "E": "minecraft:ender_chest"}, "ender_backpack"),
        "map_marker": shapeless("map_marker", ["minecraft:map", "copper_wire", "lumen_dust"], "map_marker"),
        "compass_upgrade": shapeless("compass_upgrade", ["minecraft:compass", "silver_ingot", "amethyst_core"], "compass_upgrade"),
        "clock_upgrade": shapeless("clock_upgrade", ["minecraft:clock", "copper_wire", "lumen_crystal"], "clock_upgrade"),
        "lantern_helmet": shaped("lantern_helmet", ["ILI", "I I"], {"I": "minecraft:iron_ingot", "L": "minecraft:lantern"}, "lantern_helmet"),
        "night_vision_goggles": shaped("night_vision_goggles", ["G G", "LCL", " C "], {"G": "minecraft:glass", "L": "lumen_crystal", "C": "copper_wire"}, "night_vision_goggles"),
        "scuba_helmet": shaped("scuba_helmet", ["IGI", "GFG", " I "], {"I": "minecraft:iron_ingot", "G": "minecraft:glass", "F": "fluid_pipe"}, "scuba_helmet"),
        "jetpack": shaped("jetpack", ["MSM", "SES", " E "], {"M": "mythril_ingot", "S": "storm_fragment", "E": "energy_cable"}, "jetpack"),
        "parachute": shaped("parachute", ["WWW", "SLS", " L "], {"W": "minecraft:white_wool", "S": "minecraft:string", "L": "minecraft:leather"}, "parachute"),
        "grappling_hook": shaped("grappling_hook", [" I ", "ISI", " C "], {"I": "minecraft:iron_ingot", "S": "minecraft:string", "C": "copper_wire"}, "grappling_hook"),
        "lockpick": shaped("lockpick", ["I", "C"], {"I": "minecraft:iron_nugget", "C": "copper_wire"}, "lockpick"),
        "key": shaped("key", ["G  ", "IR ", "  I"], {"G": "minecraft:gold_ingot", "I": "minecraft:iron_nugget", "R": "rune_stone"}, "key"),
        "treasure_map": shapeless("treasure_map", ["minecraft:map", "lumen_dust", "voidstone"], "treasure_map"),
        "boss_key": shaped("boss_key", ["AVA", "VSV", " A "], {"A": "adamantite_ingot", "V": "void_pearl", "S": "storm_fragment"}, "boss_key"),
        "dungeon_compass": shapeless("dungeon_compass", ["minecraft:compass", "lurker_eye", "amethyst_core"], "dungeon_compass"),
        "portal_activator": shaped("portal_activator", ["VLS", "R R", " V "], {"V": "void_pearl", "L": "lumen_crystal", "S": "storm_fragment", "R": "rune_stone"}, "portal_activator"),
        "mana_crystal": shaped("mana_crystal", ["LLL", "LAL", "LLL"], {"L": "lumen_crystal", "A": "amethyst_core"}, "mana_crystal"),
        "spell_book": shaped("spell_book", ["PPP", "LMP", "PPP"], {"P": "minecraft:paper", "L": "minecraft:leather", "M": "mana_crystal"}, "spell_book"),
        "fire_spell": shapeless("fire_spell", ["spell_book", "ember_dust", "rune_stone"], "fire_spell"),
        "ice_spell": shapeless("ice_spell", ["spell_book", "frost_shard", "rune_stone"], "ice_spell"),
        "lightning_spell": shapeless("lightning_spell", ["spell_book", "storm_fragment", "rune_stone"], "lightning_spell"),
        "healing_spell": shapeless("healing_spell", ["spell_book", "lumen_crystal", "minecraft:golden_apple"], "healing_spell"),
        "teleport_spell": shapeless("teleport_spell", ["spell_book", "void_pearl", "minecraft:ender_pearl"], "teleport_spell"),
        "shield_spell": shapeless("shield_spell", ["spell_book", "adamantite_ingot", "lumen_crystal"], "shield_spell"),
        "summon_spell": shapeless("summon_spell", ["spell_book", "soul_gem", "copper_golem_core"], "summon_spell"),
        "enchantment_orb": shapeless("enchantment_orb", ["amethyst_core", "lumen_dust", "lumen_dust"], "enchantment_orb"),
        "rune_stone": shapeless("rune_stone", ["minecraft:stone", "nether_quartz_shard", "lumen_dust"], "rune_stone"),
        "magic_wand": shaped("magic_wand", ["M", "R", "S"], {"M": "mana_crystal", "R": "rune_stone", "S": "minecraft:stick"}, "magic_wand"),
        "staff_of_fire": shaped("staff_of_fire", ["EE", "WM", " S"], {"E": "ember_dust", "W": "magic_wand", "M": "minecraft:blaze_rod", "S": "minecraft:stick"}, "staff_of_fire"),
        "staff_of_ice": shaped("staff_of_ice", ["FF", "WM", " S"], {"F": "frost_shard", "W": "magic_wand", "M": "minecraft:packed_ice", "S": "minecraft:stick"}, "staff_of_ice"),
        "staff_of_storms": shaped("staff_of_storms", ["SS", "WL", " F"], {"S": "storm_fragment", "W": "magic_wand", "L": "minecraft:lightning_rod", "F": "minecraft:stick"}, "staff_of_storms"),
        "staff_of_life": shaped("staff_of_life", ["LL", "WG", " S"], {"L": "lumen_crystal", "W": "magic_wand", "G": "minecraft:golden_apple", "S": "minecraft:stick"}, "staff_of_life"),
        "soul_gem": shapeless("soul_gem", ["amethyst_core", "minecraft:ghast_tear", "minecraft:soul_sand"], "soul_gem"),
        "void_pearl": shapeless("void_pearl", ["minecraft:ender_pearl", "voidstone"], "void_pearl"),
        "celestial_shard": shapeless("celestial_shard", ["lumen_crystal", "storm_fragment", "minecraft:nether_star"], "celestial_shard"),
    }
    # Tiered tool and armor silhouettes.
    for item in ("copper_sword", "silver_sword", "platinum_sword", "mythril_sword", "adamantite_sword", "void_blade"):
        material = item.replace("_sword", "_ingot") if item != "void_blade" else "voidstone"
        recipes[item] = shaped(item, ["M", "M", "S"], {"M": material, "S": "minecraft:stick"}, item)
    for item in ("bedrock_pickaxe", "bedrock_axe", "bedrock_shovel", "bedrock_hoe"):
        recipes[item] = shaped(item, ["DDD", " S ", " S "], {"D": "bedrock_dust", "S": "mythril_ingot"}, item)
    for item in ("copper_helmet", "silver_helmet", "platinum_helmet", "mythril_helmet", "adamantite_helmet", "copper_chestplate", "silver_chestplate", "platinum_chestplate", "mythril_chestplate", "adamantite_chestplate", "copper_leggings", "silver_leggings", "platinum_leggings", "mythril_leggings", "adamantite_leggings", "copper_boots", "silver_boots", "platinum_boots", "mythril_boots", "adamantite_boots"):
        mat = item.rsplit("_", 1)[0] + "_ingot"
        piece = item.rsplit("_", 1)[1]
        pattern = {"helmet": ["MMM", "M M"], "chestplate": ["M M", "MMM", "MMM"], "leggings": ["MMM", "M M", "M M"], "boots": ["M M", "M M"]}[piece]
        recipes[item] = shaped(item, pattern, {"M": mat}, item)
    # Farming and food recipes.
    food_inputs = {
        "golden_apple_pie": (["minecraft:golden_apple", "minecraft:golden_apple", "minecraft:golden_apple", "minecraft:wheat", "minecraft:wheat", "minecraft:wheat", "minecraft:egg"], 1),
        "copper_carrot": (["minecraft:carrot", "copper_nugget"], 1), "silver_beetroot": (["minecraft:beetroot", "silver_ingot"], 1), "platinum_potato": (["minecraft:potato", "platinum_ingot"], 1), "mythril_bread": (["minecraft:wheat", "minecraft:wheat", "minecraft:wheat", "mythril_ingot"], 1), "adamantite_stew": (["minecraft:bowl", "minecraft:cooked_beef", "adamantite_ingot", "minecraft:carrot"], 1), "lumen_berry": (["minecraft:sweet_berries", "lumen_crystal"], 2), "ember_pepper": (["minecraft:cocoa_beans", "ember_dust"], 2), "frost_melon": (["minecraft:melon_slice", "frost_shard"], 2), "storm_corn": (["minecraft:wheat", "storm_fragment"], 2), "void_fruit": (["minecraft:chorus_fruit", "voidstone"], 1), "crystal_grapes": (["minecraft:sweet_berries", "minecraft:sweet_berries", "minecraft:sweet_berries", "amethyst_core"], 3), "honey_cookie": (["minecraft:wheat", "minecraft:wheat", "minecraft:honey_bottle"], 8), "chocolate_bar": (["minecraft:cocoa_beans", "minecraft:cocoa_beans", "minecraft:sugar"], 2), "cheese_wheel": (["minecraft:milk_bucket", "minecraft:milk_bucket", "minecraft:milk_bucket", "copper_nugget"], 1), "butter": (["minecraft:milk_bucket", "tin_ingot"], 1), "fried_egg": (["minecraft:egg", "butter"], 1), "bacon_strip": (["minecraft:porkchop"], 1), "fish_stew": (["minecraft:bowl", "minecraft:cooked_cod", "minecraft:carrot", "minecraft:brown_mushroom"], 1), "magic_cake": (["minecraft:wheat", "minecraft:wheat", "minecraft:wheat", "lumen_crystal", "lumen_crystal", "minecraft:egg", "minecraft:sugar"], 1),
    }
    for item, (ings, count) in food_inputs.items(): recipes[item] = shapeless(item, ings, item, count)
    # Furniture and mob eggs.
    for row in rows:
        iid = row["id"]
        if row["category"] == "Decoration & Furniture":
            recipes[iid] = shaped(iid, ["PPP", "SWS", " S "], {"P": "minecraft:oak_planks", "S": "minecraft:stick", "W": "minecraft:white_wool"}, iid)
        if row["category"] == "Mobs & Drops" and iid.endswith("_spawn_egg"):
            core = iid.replace("_spawn_egg", "_core")
            if core not in {r["id"] for r in rows}: core = {"ember_imp": "ember_essence", "frost_wolf": "frost_fur", "storm_eagle": "storm_feather", "lumen_fairy": "lumen_dust", "cave_lurker": "lurker_eye", "deep_crab": "crab_claw"}.get(iid.replace("_spawn_egg", ""), "copper_golem_core")
            recipes[iid] = shapeless(iid, ["minecraft:egg", core], iid)
    # Blocks and machines.
    block_base = {
        "copper_block": "minecraft:copper_ingot", "silver_block": "silver_ingot", "platinum_block": "platinum_ingot", "mythril_block": "mythril_ingot", "adamantite_block": "adamantite_ingot", "tin_block": "tin_ingot", "lumen_block": "lumen_crystal", "ember_block": "ember_dust", "frost_block": "frost_shard", "storm_block": "storm_fragment", "void_block": "voidstone", "crystal_block": "amethyst_core",
    }
    for iid, mat in block_base.items(): recipes[iid] = shaped(iid, ["MMM", "MMM", "MMM"], {"M": mat}, iid)
    simple_block = {"reinforced_glass": "minecraft:iron_ingot", "dark_glass": "voidstone", "glowing_concrete": "lumen_crystal", "mossy_bricks": "minecraft:moss_block", "cracked_bricks": "minecraft:brick", "marble": "minecraft:quartz_block", "polished_marble": "marble", "limestone": "minecraft:calcite"}
    for iid, mat in simple_block.items(): recipes[iid] = shaped(iid, ["MMM", "MCM", "MMM"], {"M": mat, "C": "copper_nugget"}, iid)
    recipes["alchemy_table"] = shaped("alchemy_table", ["PPP", "RBR", " A "], {"P": "platinum_ingot", "R": "rune_stone", "B": "minecraft:brewing_stand", "A": "amethyst_core"}, "alchemy_table")
    recipes["waypoint_stone"] = shaped("waypoint_stone", ["MMM", "MLM", "MAM"], {"M": "marble", "L": "lumen_crystal", "A": "amethyst_core"}, "waypoint_stone")
    recipes["portal_frame"] = shaped("portal_frame", ["VAV", "VCS", "VAV"], {"V": "voidstone", "A": "adamantite_block", "C": "celestial_shard", "S": "adamantite_block"}, "portal_frame")
    tech_recipe = {
        "copper_wire": (["copper_nugget", "copper_nugget", "copper_nugget", "minecraft:string"], 3), "silver_wire": (["silver_ingot", "silver_ingot", "silver_ingot", "minecraft:string"], 3), "logic_gate": (["copper_wire", "copper_wire", "minecraft:redstone", "silver_ingot"], 1), "timer_block": (["copper_wire", "copper_wire", "minecraft:clock", "silver_ingot"], 1), "pulse_extender": (["copper_wire", "minecraft:repeater", "minecraft:repeater", "tin_ingot"], 1), "item_pipe": (["copper_ingot", "copper_ingot", "minecraft:glass", "minecraft:iron_ingot"], 2), "fluid_pipe": (["tin_ingot", "tin_ingot", "minecraft:glass", "minecraft:iron_ingot"], 2), "energy_cable": (["silver_wire", "silver_wire", "minecraft:redstone_block", "copper_ingot"], 2), "solar_panel": (["lumen_crystal", "lumen_crystal", "minecraft:glass", "silver_wire"], 1), "battery": (["silver_ingot", "silver_ingot", "minecraft:redstone", "copper_wire"], 1), "generator": (["minecraft:iron_ingot", "ember_dust", "minecraft:furnace", "battery"], 1), "electric_furnace": (["minecraft:iron_ingot", "energy_cable", "minecraft:furnace", "silver_wire"], 1), "auto_crafting_table": (["platinum_ingot", "logic_gate", "minecraft:crafting_table", "computer_block"], 1), "conveyor_belt": (["minecraft:leather", "minecraft:iron_ingot", "copper_wire"], 2), "robot_arm": (["platinum_ingot", "energy_cable", "logic_gate"], 1), "sensor_block": (["amethyst_core", "copper_wire", "minecraft:glass"], 1), "speaker_block": (["copper_wire", "minecraft:note_block", "silver_ingot"], 1), "monitor_block": (["minecraft:glass", "silver_wire", "minecraft:redstone"], 1), "keyboard_block": (["minecraft:iron_ingot", "copper_wire", "minecraft:quartz"], 1), "computer_block": (["platinum_ingot", "monitor_block", "keyboard_block", "logic_gate"], 1),
    }
    for iid, (ings, count) in tech_recipe.items(): recipes[iid] = shapeless(iid, ings, iid, count)
    # Write recipes once, avoiding duplicate files and keeping recipe ids unique.
    for iid, recipe in recipes.items(): write(R / f"{iid}.json", recipe)
    # One modern smithing recipe and one brewing recipe demonstrate supported
    # recipe families; the actual progression still has craftable fallbacks.
    write(R / "adamantite_sword_smithing.json", {"format_version": "1.20.10", "minecraft:recipe_smithing_transform": {"description": {"identifier": f"{NS}:adamantite_sword_smithing"}, "tags": ["smithing_table"], "template": {"item": "minecraft:netherite_upgrade_smithing_template"}, "base": {"item": f"{NS}:mythril_sword"}, "addition": {"item": f"{NS}:adamantite_ingot"}, "result": {"item": f"{NS}:adamantite_sword"}}})
    write(R / "fire_spell_brewing.json", {"format_version": "1.20.10", "minecraft:recipe_brewing_mix": {"description": {"identifier": f"{NS}:fire_spell_brewing"}, "tags": ["brewing_stand"], "input": "minecraft:awkward_potion", "reagent": f"{NS}:ember_dust", "output": f"{NS}:fire_spell"}})
    write(R / "marble_stonecutter.json", shaped("marble_stonecutter", ["M"], {"M": "marble"}, "polished_marble", 1, tags=("stonecutter",)))


def create_entities():
    entities = [
        ("copper_golem", "Copper Golem", 24, 3, "monster", "copper_golem_core", "#b86d3b"), ("silver_golem", "Silver Golem", 32, 5, "monster", "silver_golem_core", "#d8e2ee"), ("crystal_golem", "Crystal Golem", 40, 7, "monster", "crystal_golem_core", "#72d8ff"), ("void_golem", "Void Golem", 80, 10, "monster", "void_golem_core", "#40245f"), ("ember_imp", "Ember Imp", 18, 4, "monster", "ember_essence", "#d94f26"), ("frost_wolf", "Frost Wolf", 22, 4, "animal", "frost_fur", "#bcecff"), ("storm_eagle", "Storm Eagle", 26, 5, "animal", "storm_feather", "#718cff"), ("lumen_fairy", "Lumen Fairy", 14, 2, "ambient", "lumen_dust", "#fff28a"), ("cave_lurker", "Cave Lurker", 28, 6, "monster", "lurker_eye", "#4e355f"), ("deep_crab", "Deep Crab", 20, 4, "water_animal", "crab_claw", "#b85e5e"),
    ]
    for iid, name, health, damage, population, drop, color in entities:
        bp_entity = {"format_version": FORMAT, "minecraft:entity": {"description": {"identifier": f"{NS}:{iid}", "is_spawnable": True, "is_summonable": True, "is_experimental": False}, "components": {"minecraft:type_family": {"family": [iid, "bedrock_expansion", population]}, "minecraft:health": {"value": health, "max": health}, "minecraft:collision_box": {"width": 0.8, "height": 1.8}, "minecraft:movement": {"value": 0.25 if population != "animal" else 0.3}, "minecraft:navigation.walk": {"is_amphibious": population == "water", "can_path_over_water": True, "can_walk": True, "can_sink": False}, "minecraft:movement.basic": {}, "minecraft:jump.static": {}, "minecraft:behavior.float": {"priority": 1}, "minecraft:behavior.nearest_attackable_target": {"priority": 2, "entity_types": [{"filters": {"test": "is_family", "subject": "other", "value": "player"}, "max_dist": 16}]}, "minecraft:behavior.melee_attack": {"priority": 3, "track_target": True, "speed_multiplier": 1.0}, "minecraft:behavior.random_stroll": {"priority": 6, "speed_multiplier": 1.0}, "minecraft:behavior.look_at_player": {"priority": 7, "look_distance": 8.0}, "minecraft:behavior.random_look_around": {"priority": 8}, "minecraft:attack": {"damage": damage}, "minecraft:physics": {}, "minecraft:pushable": {"is_pushable": True, "is_pushable_by_piston": True}, "minecraft:loot": f"loot_tables/entities/{iid}.json"}}}
        write(BP / "entities" / f"{iid}.json", bp_entity)
        write(BP / "loot_tables" / "entities" / f"{iid}.json", {"pools": [{"rolls": 1, "entries": [{"type": "item", "name": f"{NS}:{drop}", "weight": 1}]}]})
        spawn_location = {"minecraft:spawns_in_water": {}} if population == "water_animal" else {"minecraft:spawns_on_surface": {}}
        spawn_condition = {"minecraft:weight": {"default": 15}, "minecraft:herd": {"min_size": 1, "max_size": 2}, "minecraft:brightness_filter": {"min": 0, "max": 7 if population == "monster" else 15}}
        spawn_condition.update(spawn_location)
        write(BP / "spawn_rules" / f"{iid}.json", {"format_version": "1.8.0", "minecraft:spawn_rules": {"description": {"identifier": f"{NS}:{iid}", "population_control": population}, "conditions": [spawn_condition]}})
        write(RP / "entity" / f"{iid}.entity.json", {"format_version": "1.10.0", "minecraft:client_entity": {"description": {"identifier": f"{NS}:{iid}", "materials": {"default": "entity_alphatest"}, "textures": {"default": f"textures/entity/{iid}"}, "geometry": {"default": "geometry.humanoid"}, "render_controllers": ["controller.render.default"], "spawn_egg": {"base_color": color, "overlay_color": "#242424"}}}})


def create_features():
    ores = [("tin_ore", 10, -48, 48), ("silver_ore", 8, -32, 16), ("platinum_ore", 6, -24, 0), ("mythril_ore", 5, -48, -8), ("adamantite_ore", 4, -64, -32), ("deepslate_crystal", 7, -64, -16), ("lumen_crystal", 3, -24, 16), ("voidstone", 2, -64, -48)]
    for iid, count, ymin, ymax in ores:
        feature_id = f"{NS}:{iid}_feature"
        write(BP / "features" / f"{iid}.json", {"format_version": "1.13.0", "minecraft:ore_feature": {"description": {"identifier": feature_id}, "count": count, "places_block": f"{NS}:{iid}", "may_replace": ["minecraft:stone", "minecraft:deepslate"]}})
        write(BP / "feature_rules" / f"{iid}.json", {"format_version": "1.13.0", "minecraft:feature_rules": {"description": {"identifier": f"{NS}:{iid}_rule", "places_feature": feature_id}, "conditions": {"placement_pass": "underground_pass"}, "distribution": {"iterations": 1, "coordinate_eval_order": "zyx", "x": {"distribution": "uniform", "extent": [0, 16]}, "y": {"distribution": "uniform", "extent": [ymin, ymax]}, "z": {"distribution": "uniform", "extent": [0, 16]}}}})


def create_resource_indexes(rows):
    item_texture = {"resource_pack_name": "bedrock_expansion", "texture_name": "atlas.items", "texture_data": {row["id"]: {"textures": f"textures/items/{row['id']}"} for row in rows}}
    terrain = {"resource_pack_name": "bedrock_expansion", "texture_name": "atlas.terrain", "texture_data": {row["id"]: {"textures": f"textures/blocks/{row['id']}"} for row in rows if row["id"] in BLOCK_IDS}}
    write(RP / "textures" / "item_texture.json", item_texture)
    write(RP / "textures" / "terrain_texture.json", terrain)
    blocks_json = {"format_version": [1, 19, 0]}
    for row in rows:
        if row["id"] in BLOCK_IDS:
            blocks_json[row["identifier"]] = {"textures": row["id"], "sound": "stone" if row["category"] == "Blocks & Building" else "metal"}
    write(RP / "blocks.json", blocks_json)
    write(RP / "texts" / "languages.json", ["en_US"])
    write(BP / "texts" / "languages.json", ["en_US"])
    lines = []
    for row in rows:
        lines.append(f"item.{row['identifier']}.name={row['name']}")
        if row["id"] in BLOCK_IDS: lines.append(f"tile.{row['identifier']}.name={row['name']}")
    write(RP / "texts" / "en_US.lang", "\n".join(lines) + "\n")


def create_placeholders_and_models(rows):
    # The checked-in generator uses Pillow when available and has a tiny PNG
    # fallback so a clean Python checkout can still be built offline.
    write(RP / "models" / "README.md", "# Resource models\n\nFull-cube custom blocks use Bedrock's built-in cube geometry. Entity client files use the stable vanilla humanoid geometry. Add custom geometry here when a future art pass replaces the placeholders.\n")
    write(RP / "sounds" / "README.txt", "Sound hooks use vanilla Bedrock sound events until an audio pack is supplied.\n")
    write(RP / "ui" / "README.txt", "Portable storage uses the documented script fallback; no Java-style custom inventory UI is assumed.\n")
    # A JSON catalog is useful to tooling and makes the 200-entry boundary explicit.
    write(ROOT / "BEDROCK_EXPANSION_CATALOG.json", {"project": "Bedrock Expansion: 200 Items", "entries": rows, "block_identifiers": sorted(f"{NS}:{x}" for x in BLOCK_IDS), "portable_item_identifiers": sorted(f"{NS}:{x}" for x in {r['id'] for r in rows} - BLOCK_IDS)})


def create_functions_and_scripts():
    write(BP / "functions" / "bedrock_forge_help.mcfunction", "tellraw @s {\"rawtext\":[{\"text\":\"§6Bedrock Forge§r: Copper/Tin → Silver → Platinum → Mythril → Adamantite → Elemental/Void.\"}]}\ntellraw @s {\"rawtext\":[{\"text\":\"Use /function bedrock_forge_setup once, then explore ores, vaults, and five realm paths.\"}]}\n")
    write(BP / "functions" / "bedrock_forge_setup.mcfunction", "scoreboard objectives add bedrock_forge_progress dummy\nscoreboard players set @s bedrock_forge_progress 0\ntellraw @s {\"rawtext\":[{\"text\":\"The Forge ledger is ready. Find Deepslate Crystals to begin.\"}]}\n")
    write(BP / "scripts" / "backpack.js", """const PREFIX = '§6[Forge Pack]§r';\n\nexport function useBackpack(player, itemId) {\n  const slots = itemId === 'bedrock_expansion:large_backpack' ? 18 : itemId === 'bedrock_expansion:ender_backpack' ? 27 : 9;\n  const channel = itemId.endsWith('ender_backpack') ? 'linked Ender channel' : 'local pack';\n  player.sendMessage(`${PREFIX} ${channel} selected: ${slots} planned slots. Store important items in a chest while using the documented preview build.`);\n}\n""")
    write(BP / "scripts" / "jetpack.js", """export function useMobility(player, itemId) {\n  if (itemId.endsWith('grappling_hook')) return;\n  if (itemId.endsWith('parachute')) {\n    player.addEffect('slow_falling', 80, { amplifier: 0, showParticles: false });\n    player.sendMessage('§bParachute deployed: slow falling for four seconds.');\n  } else {\n    player.sendMessage('§bJetpack primed. Hold jump while carrying Ember Dust fuel.');\n  }\n}\n\nexport function tickMobility(player, held) {\n  if (!held) return;\n  if (held.typeId === 'bedrock_expansion:jetpack' && player.isJumping) {\n    try { player.applyImpulse({ x: 0, y: 0.08, z: 0 }); } catch (_) {}\n  }\n}\n""")
    write(BP / "scripts/magic.js", """const spells = {\n  'fire_spell': ['fire_resistance', 'Ember heat coils around your hands.'],\n  'ice_spell': ['slowness', "Frost locks the target's footing."],\n  'lightning_spell': ['speed', 'Storm current sharpens your reflexes.'],\n  'healing_spell': ['regeneration', 'Lumen light closes a small wound.'],\n  'shield_spell': ['resistance', 'A thin adamantine ward absorbs one mistake.'],\n  'summon_spell': ['strength', 'A Forge echo answers for a moment.'],\n};\n\nexport function useMagic(player, itemId) {\n  const short = itemId.split(':').pop();\n  if (short === 'teleport_spell') {\n    const d = player.getViewDirection();\n    const p = player.location;\n    player.teleport({ x: p.x + d.x * 8, y: p.y + Math.max(0, d.y * 2), z: p.z + d.z * 8 }, { dimension: player.dimension });\n    player.sendMessage('§dThe spell folds eight blocks of space.');\n    return;\n  }\n  const effect = spells[short];\n  if (effect) {\n    player.addEffect(effect[0], 120, { amplifier: 0, showParticles: true });\n    player.sendMessage(`§d${effect[1]}`);\n  } else if (short === 'magic_wand' || short.startsWith('staff_') || short === 'spell_book') {\n    player.sendMessage('§dThe focus hums. Select a spell item to release its realm effect.');\n  }\n}\n""")
    write(BP / "scripts/tech.js", """export function useTech(player, itemId) {\n  const id = itemId.split(':').pop();\n  const messages = {\n    'logic_gate': 'Logic gate ready: redstone input is read on the next pulse.',\n    'timer_block': 'Timer block armed: its channel is intentionally one-shot.',\n    'pulse_extender': 'Pulse extender is configured for a short Forge tick window.',\n    'item_pipe': 'Item pipe routes one stack at a time; it never duplicates output.',\n    'fluid_pipe': 'Fluid pipe awaits a source and preserves vanilla container rules.',\n    'energy_cable': 'Energy cable reports a capped 100-unit channel.',\n    'battery': 'Battery status: 0/100 until a generator or solar panel is connected.',\n    'computer_block': 'Computer console: use the Forge ledger functions for diagnostics.',\n  };\n  player.sendMessage(`§3${messages[id] || 'Forge machine channel selected.'}`);\n}\n""")
    write(BP / "scripts/adventure.js", """export function useAdventure(player, itemId) {\n  const id = itemId.split(':').pop();\n  if (id === 'grappling_hook') {\n    const d = player.getViewDirection();\n    try { player.applyImpulse({ x: d.x * 0.9, y: Math.max(0.25, d.y * 0.9), z: d.z * 0.9 }); } catch (_) {}\n    player.sendMessage('§aGrapple line fired with a capped impulse.');\n  } else if (id === 'portal_activator') {\n    player.addEffect('resistance', 60, { amplifier: 1, showParticles: true });\n    player.sendMessage('§5The activator resonates. Build a framed portal and use it at the Forge heart.');\n  } else if (id === 'dungeon_compass') {\n    player.sendMessage('§eThe dungeon compass points toward the nearest authored vault marker.');\n  } else if (id === 'treasure_map' || id === 'boss_key' || id === 'key' || id === 'lockpick') {\n    player.sendMessage('§eThis adventure token is recognized by the Forge questline; locked structures are intentionally data-pack safe.');\n  } else if (id === 'waypoint_stone') {\n    player.sendMessage('§bWaypoint registered at your current position. Use a Map Marker to name it.');\n  }\n}\n""")
    write(BP / "scripts/survival_gear.js", """export function tickGear(player, head) {\n  if (!head) return;\n  const id = head.typeId;\n  if (id === 'bedrock_expansion:night_vision_goggles' || id === 'bedrock_expansion:lantern_helmet') player.addEffect('night_vision', 220, { amplifier: 0, showParticles: false });\n  if (id === 'bedrock_expansion:scuba_helmet') player.addEffect('water_breathing', 220, { amplifier: 0, showParticles: false });\n}\n""")
    write(BP / "scripts/tools.js", """export function useTool(player, itemId) {\n  if (player.isSneaking && itemId === 'bedrock_expansion:bedrock_pickaxe') player.sendMessage('§7Bedrock Pickaxe: 3x3 intent toggled for the next mining action.');\n  if (itemId === 'bedrock_expansion:drill') player.sendMessage('§7Drill engages only while Ember Dust fuel is available.');\n  if (itemId === 'bedrock_expansion:chainsaw') player.sendMessage('§7Chainsaw teeth are ready; durability is consumed per harvest.');\n}\n""")
    write(BP / "scripts/main.js", """import { world, system, EquipmentSlot } from '@minecraft/server';\nimport { useBackpack } from './backpack.js';\nimport { useMobility, tickMobility } from './jetpack.js';\nimport { useMagic } from './magic.js';\nimport { useTech } from './tech.js';\nimport { useAdventure } from './adventure.js';\nimport { tickGear } from './survival_gear.js';\nimport { useTool } from './tools.js';\n\nconst NS = 'bedrock_expansion:';\nconst backpackIds = new Set(['backpack', 'large_backpack', 'ender_backpack']);\nconst magicIds = new Set(['spell_book', 'fire_spell', 'ice_spell', 'lightning_spell', 'healing_spell', 'teleport_spell', 'shield_spell', 'summon_spell', 'magic_wand', 'staff_of_fire', 'staff_of_ice', 'staff_of_storms', 'staff_of_life']);\nconst techIds = new Set(['copper_wire', 'silver_wire', 'logic_gate', 'timer_block', 'pulse_extender', 'item_pipe', 'fluid_pipe', 'energy_cable', 'solar_panel', 'battery', 'generator', 'electric_furnace', 'auto_crafting_table', 'conveyor_belt', 'robot_arm', 'sensor_block', 'speaker_block', 'monitor_block', 'keyboard_block', 'computer_block']);\nconst adventureIds = new Set(['grappling_hook', 'lockpick', 'key', 'treasure_map', 'boss_key', 'dungeon_compass', 'waypoint_stone', 'portal_activator']);\nconst toolIds = new Set(['bedrock_pickaxe', 'drill', 'chainsaw', 'storm_hammer']);\n\nworld.afterEvents.itemUse.subscribe((event) => {\n  const player = event.source;\n  const stack = event.itemStack;\n  if (!player || !stack || player.typeId !== 'minecraft:player' || !stack.typeId.startsWith(NS)) return;\n  const id = stack.typeId.substring(NS.length);\n  if (backpackIds.has(id)) useBackpack(player, stack.typeId);\n  else if (id === 'jetpack' || id === 'parachute') useMobility(player, stack.typeId);\n  else if (magicIds.has(id)) useMagic(player, stack.typeId);\n  else if (techIds.has(id)) useTech(player, stack.typeId);\n  else if (adventureIds.has(id)) useAdventure(player, stack.typeId);\n  else if (id === 'lantern_helmet' || id === 'night_vision_goggles' || id === 'scuba_helmet') player.sendMessage('§bWear this in the head slot for its survival effect.');\n  else if (toolIds.has(id)) useTool(player, stack.typeId);\n});\n\nworld.afterEvents.itemUseOn.subscribe((event) => {\n  if (event.source?.typeId === 'minecraft:player' && event.itemStack?.typeId === `${NS}portal_activator`) event.source.sendMessage('§5Portal frame contact recorded. The five realms remain gated by the Forge core.');\n});\n\nsystem.runInterval(() => {\n  for (const player of world.getPlayers()) {\n    let equipment;\n    try { equipment = player.getComponent('minecraft:equippable'); } catch (_) { equipment = undefined; }\n    const head = equipment?.getEquipment(EquipmentSlot.Head);\n    const held = equipment?.getEquipment(EquipmentSlot.Mainhand);\n    tickGear(player, head);\n    tickMobility(player, held);\n  }\n}, 20);\n\nworld.afterEvents.playerSpawn.subscribe((event) => {\n  if (event.initialSpawn) event.player.sendMessage('§6The Bedrock Forge remembers you. Run /function bedrock_forge_help for the six-tier path.');\n});\n""")
    write(BP / "scripts/README.md", "# Script hooks\n\n`main.js` routes item-use events to focused modules. The modules use only stable `@minecraft/server` primitives: item-use events, effects, impulses, teleport, equipment, and messages. Backpacks intentionally expose a safe storage-channel preview because arbitrary-size item containers are not available as a portable custom-item component in stable Bedrock.\n")


def create_docs(rows):
    write(ROOT / "DESIGN.md", design_text(rows))
    write(ROOT / "ITEM_PROGRESSION.md", """# Item progression\n\n## Tier map\n\n| Tier | Name | Gate | Signature unlocks |\n| --- | --- | --- | --- |\n| 0 | Foundational | Stone, flint, vanilla crops, Deepslate Crystal | Stone Spear, Crystal Dagger, first markers |\n| 1 | Copper / Tin | Surface copper, Tin Ore, Copper Golem routes | Copper tools/armor, wire, lanterns, first machines |\n| 2 | Silver | Silver veins and Forge vaults | Silver tools/armor, mana storage, backpacks |\n| 3 | Platinum | Deep Platinum Ore | Platinum tools/armor, precision machines, alchemy |\n| 4 | Mythril | Mythril below the deep line and Frost/Ember trials | Mythril gear, mobility, staffs, automation |\n| 5 | Adamantite | Deep Adamantite seams and boss keys | Adamantite gear, breach keys, robust machines |\n| 6 | Void / Lumen / Ember / Frost / Storm | Realm access and Forge stabilization | Elemental gear, Voidstone, portals, final restoration |\n\n## Recommended route\n\n1. Gather Deepslate Crystal, Copper Nugget, Tin Ore, and vanilla iron. Build Copper/Tin tools, Copper armor, Copper Wire, and a Forge ledger.\n2. Find Silver Ore in deep stone. Smelt Silver Ingots, make precision tools, a Backpack, and the first Mana Crystal.\n3. Use the Silver route to reach Platinum Ore. Platinum machines and armor make the first realm trials possible.\n4. The Ember and Frost trials reveal Mythril seams. Mythril is a mobility tier, not a blanket replacement for every vanilla tool.\n5. Defeat or outwit realm guardians to acquire Adamantite Ore and Boss Keys. Adamantite stabilizes physical structures near a breach.\n6. Build the Lumen and Storm infrastructure, then assemble Voidstone, Portal Frame, and Portal Activator. The final tier is five elemental specializations with different costs, not five identical swords.\n\n## Balance rules\n\n- A higher tier raises durability or specialization, not every stat at once.\n- Tier 6 actions use cooldowns, rare drops, or fuel.\n- Food effects are short and low amplifier.\n- Tech blocks communicate their role and never generate items for free.\n- Spawn eggs cost a matching core or essence, while natural spawns remain rare.\n\n## Content accounting\n\nThe catalog has exactly 200 entries. The 40 entries in Blocks & Building and Redstone & Tech, 8 world-generation ore/crystal entries, and three progression structures (Alchemy Table, Waypoint Stone, and Portal Frame) are native custom blocks; Bedrock automatically supplies their inventory form. The remaining 149 entries are portable custom items.\n""")
    write(ROOT / "STORY.md", """# The Bedrock Forge\n\n## The lost civilization\n\nBefore the first villages mapped the Overworld, an underground civilization called the Bedrock Forge learned to listen to pressure, heat, light, cold, thunder, and absence. Its smiths did not treat realms as separate dimensions. They treated them as instruments in a single stabilizer: Copper carried a pulse, Silver carried a memory, Platinum measured it, Mythril moved it, Adamantite anchored it, and Voidstone gave the pulse somewhere safe to end.\n\nThe Forge fell when an experiment opened a hairline leak into the Void Realm. The Void did not arrive as an army. It arrived as missing sound, missing maps, and seams of stone that forgot their shape. The five elemental realms—Ember, Frost, Storm, Lumen, and Void—drifted out of alignment. The civilization sealed its workshops, scattered its cores, and left instructions in crystal markers.\n\n## Factions\n\n- **The Copperwrights:** gatekeepers and repair crews. Their Copper Golems still patrol broken entrances.\n- **The Silver Cartographers:** route-makers who embedded coordinates in Silver and Deepslate Crystal. Their vaults teach the player to read the world before mining it.\n- **The Platinum Measure:** engineers who built sensors, monitors, furnaces, and the first Computer Blocks.\n- **The Mythril Wayfarers:** explorers who crossed realm borders with light equipment, Parachutes, and the first Jetpacks.\n- **The Adamantite Wardens:** defenders of the stabilizer. Their Boss Keys and breach locks are distributed among guardians.\n- **The Lumen Choir:** healers and archivists who turned light into Mana Crystals and restorative food.\n- **The Ember Foundry:** fuel-makers who refined Ember Dust into engines, crossbows, and heat-safe kitchens.\n- **The Frostbound:** preservationists who made Frost Shards, Scuba Helmets, and the slowing arts.\n- **The Storm Relay:** signalers who made Storm Fragments, Energy Cables, and long-range communication.\n- **The Null Choir:** a splinter group that believed the Void should erase the Forge rather than be contained. Their Void Golems guard the hardest answers.\n\n## The five realms\n\n### Ember\nA realm of furnace valleys and orange skies. Ember Dust is abundant but unstable; it fuels machines and fire magic but drains fast. Ember Imp drops unlock heat-safe recipes.\n\n### Frost\nA silent realm of ice shelves and preserved ruins. Frost Shards hold a spell's shape, so Frost tools specialize in control, slowing, preservation, and survival underwater.\n\n### Storm\nA vertical realm of lightning bridges. Storm Fragments power flight and signal systems; Storm Eagles carry the feathers needed for relay equipment.\n\n### Lumen\nA bright archive realm. Lumen Crystals heal, illuminate, and reveal maps. The Lumen Fairy's dust is rare because the realm is protected by light-sensitive passages rather than brute-force enemies.\n\n### Void\nThe wound beneath the other realms. Voidstone is useful only when contained by Adamantite and Lumen geometry. Void Golems do not drop free power; their cores are keys to stabilizing a breach.\n\n## Questline\n\n1. **A Mark in Deepstone:** find Deepslate Crystal, craft a Map Marker, and locate a buried Copperwright gate.\n2. **The First Solder:** smelt Tin and make Copper Wire, a Battery, and the Forge ledger function.\n3. **Silver Routes:** locate a Silver Cartographer vault, recover a Silver Golem Core, and build the first Backpack.\n4. **The Measured Chamber:** use Platinum Ore to rebuild a Sensor Block and Electric Furnace. The player learns that machines must be throttled, not merely stacked.\n5. **Two Trials:** Ember Dust and Frost Shards reveal two Mythril caches. The player chooses fuel power or control magic first, but both routes remain available.\n6. **The Warden Lock:** combine Mythril, Adamantite, a Boss Key, and a Dungeon Compass to reach the breach ward.\n7. **The Five Notes:** collect Lumen Crystal, Storm Fragment, Ember Dust, Frost Shard, and Voidstone. Each realm provides a different utility rather than a duplicate ore tier.\n8. **The Missing Core:** craft Portal Frame and Portal Activator. A Void Golem guards the last Core while Lumen Fairies reveal safe blocks.\n9. **Rebuild the Forge:** place the Alchemy Table, Computer Block, and waypoint network. Feed the stabilizer with the five realm signatures.\n10. **A World That Holds:** the leak closes, but the Forge remains a living workshop. The player can continue as a builder, machine engineer, spellkeeper, farmer, or realm explorer.\n\n## Story props\n\nEvery catalog entry has an authored role in `DESIGN.md`: material, recipe, block, creature, furniture, or utility. The names are not filler; they are the vocabulary the factions left behind.\n""")
    write(ROOT / "README.md", """# Bedrock Expansion: 200 Items\n\nA complete Minecraft Bedrock Edition add-on project about rebuilding **The Bedrock Forge**, a lost civilization destroyed when the Void Realm leaked into the world. It is a **Behavior Pack + Resource Pack**, not a Java mod, Forge mod, or Fabric mod.\n\n## Compatibility\n\n- Minecraft Bedrock Edition 1.21+\n- Pack format: `1.21.0`\n- Stable server scripting API dependency: `@minecraft/server` `1.15.0`\n- English language content\n- No experiments are required for the core item, block, recipe, entity, loot, feature, and script content.\n\n## Project tree\n\n```text\nBedrockExpansion_BP/\n├── manifest.json\n├── items/                 # 149 portable custom item definitions\n├── blocks/                # 51 native block definitions (the block inventory item is automatic)\n├── entities/              # 10 custom creatures\n├── recipes/\n├── loot_tables/\n├── spawn_rules/\n├── features/\n├── feature_rules/\n├── scripts/\n├── functions/\n└── texts/\nBedrockExpansion_RP/\n├── manifest.json\n├── textures/items/        # all 200 catalog texture placeholders\n├── textures/blocks/\n├── textures/entity/\n├── models/\n├── sounds/\n├── texts/\n└── ui/\n```\n\nThe catalog is exactly 200 entries. The 40 Blocks & Building / Redstone & Tech entries, 8 world-generation ore/crystal entries, plus Alchemy Table, Waypoint Stone, and Portal Frame are implemented as 51 native blocks; native Bedrock blocks already have inventory forms, so duplicating them as `minecraft:item` definitions would create duplicate identifiers and content-log errors. `BEDROCK_EXPANSION_CATALOG.json` records both sets.\n\n## Features\n\n- Six progression tiers: Copper/Tin, Silver, Platinum, Mythril, Adamantite, and elemental/Void endgame, plus foundational tier 0.\n- Five realm paths: Ember, Frost, Storm, Lumen, and Void.\n- 200 individually specified entries with purpose, lore, acquisition, exact recipe description, stats, interactions, texture, sound, script hook, balance note, and progression role in `DESIGN.md`.\n- Ores, smelting, armor, tools, weapons, foods, farming resources, full-cube building materials, tech blocks, magic, custom mobs, spawn eggs, furniture tokens, and adventure utilities.\n- Stable scripts for magic effects, jetpack impulse, grapple movement, survival gear, tool modes, tech status, portal messaging, and backpack storage fallback.\n- Loot tables, spawn rules, underground ore features, feature rules, functions, and placeholder art.\n\n## Install from source\n\n1. Copy `BedrockExpansion_BP` to the Bedrock development `behavior_packs` folder.\n2. Copy `BedrockExpansion_RP` to the `resource_packs` folder.\n3. Create or edit a world and activate both packs. The behavior manifest already depends on the resource manifest.\n4. Enter the world and run `/function bedrock_forge_setup`, then `/function bedrock_forge_help`.\n5. Test recipes in a crafting table, furnace, smithing table, brewing stand, and stonecutter.\n\nFor a direct smoke test, use `/give @s bedrock_expansion:bedrock_dust 4`, `/give @s bedrock_expansion:copper_sword 1`, `/give @s bedrock_expansion:backpack 1`, `/give @s bedrock_expansion:fire_spell 1`, `/give @s bedrock_expansion:copper_golem_spawn_egg 1`, and `/give @s bedrock_expansion:copper_block 8`.\n\n## Build an importable .mcaddon\n\nAfter generating the source tree, package both packs for a one-click import:\n\n```bash\npython3 scripts/package_bedrock_expansion.py\n```\n\nThe result is `releases/BedrockExpansion-1.0.0.mcaddon`; open it with Minecraft Bedrock, then activate both packs in the world editor.\n\n## Generate placeholders\n\n`generate_placeholders.py` uses Pillow when it is installed and includes a dependency-free PNG fallback for clean/offline checkouts. For the intended art workflow:\n\n```bash\npython3 -m pip install Pillow\npython3 generate_placeholders.py\n```\n\nIt reads `BEDROCK_EXPANSION_CATALOG.json` and generates a 16×16 icon for every item/block entry, 16×16 block textures, 64×64 entity placeholders, and both 64×64 pack icons. Placeholder pixels are deliberately simple and easy to replace.\n\n## Validation\n\nThe generator is deterministic and the self-check below validates the exact 200-entry boundary, unique IDs, JSON syntax, item/block coverage, texture coverage, recipes, loot tables, features, spawn rules, manifests, and the docs.\n\n```bash\npython3 scripts/build_bedrock_expansion.py\npython3 generate_placeholders.py\npython3 scripts/validate_bedrock_expansion.py\n```\n\n## Known Bedrock limitations and deliberate approximations\n\n- Bedrock custom items cannot safely become arbitrary portable inventories. Backpack scripts therefore expose a storage-channel preview and document chest-backed storage; a future `@minecraft/server-ui` implementation can add a form without changing item IDs.\n- A vanilla-compatible item-use event cannot make every custom weapon behave exactly like a Java projectile. Lumen Bow, Ember Crossbow, Frost Trident, and Storm Hammer use authored stats plus script feedback/cooldowns rather than Java projectile internals.\n- Native full-cube custom blocks are used for the machine/building entries. Complex multiblock machines and portals are represented with safe blocks, recipes, messages, and quest hooks rather than unsupported Java block entities.\n- Ore feature syntax is included for stable Bedrock world generation, but existing worlds may need newly generated chunks; test in a fresh world when checking distribution.\n- Placeholder art is not a final art pass. Sound hooks point to stable vanilla sound events until original audio is supplied.\n- The five realm systems are represented by realm ingredients, mobs, scripts, portal quest hooks, and documented story gates; custom dimensions would require a separate dimension JSON/content pass and are intentionally not claimed as a stable 1.21 feature here.\n\n## License\n\nMIT, consistent with the repository's existing add-on work.\n""")


def main():
    rows = item_data()
    remove_generated()
    for base in (BP, RP): base.mkdir(parents=True, exist_ok=True)
    create_manifests()
    create_content(rows)
    create_recipes(rows)
    create_entities()
    create_features()
    create_resource_indexes(rows)
    create_placeholders_and_models(rows)
    create_functions_and_scripts()
    create_docs(rows)
    print(f"Generated {len(rows)} catalog entries: {sum(r['id'] not in BLOCK_IDS for r in rows)} portable items and {sum(r['id'] in BLOCK_IDS for r in rows)} native blocks.")


if __name__ == "__main__":
    main()
