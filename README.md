# Realistic Sticks

A Bedrock Edition add-on that makes sticks feel like real gathered wood instead of one generic item. It adds species-specific branch sticks, fieldcraft tools and materials, a charcoal-smelting chain, and six placeable **3D blocks** for building natural camps. The resource pack also gives the vanilla `minecraft:stick` a natural bark-and-cut-end texture, livelier mob and attack animations, and water that rolls and streams like a real current.

## Compatibility

- **Edition:** Minecraft: Bedrock Edition
- **Target:** Bedrock 26.50 / content format `1.26.50`
- **Experiments:** None required
- **Pack version:** 1.2.0

The pack is authored against the current stable 26.50 add-on format. If a future Bedrock release changes a content schema, the `min_engine_version` and content format can be reviewed in one place by rerunning the generation scripts.

## What is included

**20 items, 6 3D blocks, 51 recipes, livelier vanilla mob animations, and realistic flowing water.**

### Species sticks

| Item | How to obtain it | Use |
| --- | --- | --- |
| Oak, spruce, birch, jungle, acacia, dark oak, mangrove, cherry, pale oak, and bamboo sticks | Craft the matching log, stripped log, plank, or bamboo in a crafting table | Species-specific fuel; accepted by the add-on recipes |
| Vanilla sticks | One Realistic Stick in a crafting grid | Converts the new items back to two `minecraft:stick` items for vanilla recipes |

Each wood species has its own color and grain treatment. The generated textures are deliberately pixel-art sized so they remain crisp in Bedrock's item atlas while still showing bark, grain, knots, and a cut end.

### Fieldcraft materials

| Item | How to obtain it | Use |
| --- | --- | --- |
| Bark strip | Peel 2 Realistic Sticks | Fuel (2s); crafting material |
| Bark rope | 3 bark strips in a row | String alternative; binds tools and bundles |
| Wood chips | Shave 1 Realistic Stick (gives 4) | Fuel (1s); tinder ingredient |
| Tinder bundle | 4 wood chips + bark rope (or string) | Fuel (15s); campfire and torch ingredient |
| Charcoal lump | Smelt a kindling or tinder bundle in a furnace | Strong fuel (60s); torch ingredient |

### Tools and weapons

| Item | How to obtain it | Stats |
| --- | --- | --- |
| Sharpened stick | One Realistic Stick plus flint | +2 damage, 32 durability |
| Walking staff | 2 sticks + bark rope (diagonal) | +3 damage, 96 durability |
| Hunting spear | Sharpened stick + bark rope + stick (vertical) | +5 damage, 48 durability |
| Wooden mallet | 3 kindling + 2 sticks | +6 damage, 64 durability |
| Kindling bundle | Four Realistic Sticks plus string (or bark rope) | 30 seconds of furnace fuel per bundle |
| Torches ×8 | Kindling bundle + coal (or charcoal lump) | Bulk torch crafting |

All tools are repairable with Realistic Sticks.

### 3D camp blocks (placeable)

Each block has a custom 3D model, wood sounds, and drops itself when broken:

| Block | Recipe | Notes |
| --- | --- | --- |
| Stick pile | 4 Realistic Sticks | Low decorative pile of branches |
| Kindling block | 4 Realistic Sticks + bark rope | Tied bundle block |
| Sharpened stakes | 2 sharpened sticks (vertical) | Defensive spike row on a ground beam; gives 2 |
| Campfire kit | 3 Realistic Sticks + tinder bundle | Teepee of poles over a tinder mound |
| Log stool | 6 Realistic Sticks | Stump seat with bark sides and growth-ring top |
| Trail torch | Coal + tinder bundle + stick (vertical) | Light level 14; charcoal variant also works |

### Livelier mob and attack animations

The resource pack overrides vanilla animation identifiers (no client-entity copies, so it stays compatible with Bedrock 26.50). Idle poses stay still; extra motion is driven by the same `attack_time` / walk variables vanilla already sets.

| Who | What changes |
| --- | --- |
| Players | Bigger third-person swing with torso twist and a forward lunge; first-person punch and item swing travel farther |
| Zombies, husks, drowned | Two-arm clawing lunge with body lean and head snap |
| Skeletons and other humanoids | Heavier walk (arm swing, hip sway, foot plant) and a committed melee swing |
| Vindicators | Overhead chop with follow-through |
| Iron golems | Two-handed slam that folds the body into the hit, plus a heavier stomp |
| Creepers | Waddling walk with body roll |
| Spiders | Larger alternating leg waves and a crawling bob |
| Cows, pigs, sheep, and other quadrupeds | Diagonal gait with body bounce and head nod |
| Chickens | Head-bobbing strut |

### Realistic flowing water

Vanilla liquid spread is engine-side and is not replaced (oceans, buckets, boats, and drowning keep working). The pack restyles the water flipbooks so the surface behaves more like real water:

- Still water uses overlapping wave trains and caustic glints that roll across ponds and oceans.
- Flowing water is a downhill current: meandering streamlines, foam where filaments converge, and whitewater on the fast layer.
- Cauldrons use the same still-water sheet.

The grey sheets (`water_still_grey`, `water_flow_grey`) stay greyscale so biome tint still paints jungle, swamp, and ocean water correctly.

## Install

1. Download `releases/RealisticSticks-1.2.0.mcaddon` from this repository.
2. Open the file with Minecraft: Bedrock Edition. Minecraft will import both the behavior pack and resource pack.
3. Create a new world or edit an existing world.
4. Activate **Realistic Sticks | Behavior** and **Realistic Sticks | Resources**. The behavior pack already declares the resource-pack dependency, so enabling the behavior pack is normally enough.
5. Enter the world and craft sticks from the wood species you want.

For a quick smoke test, use:

```text
/give @s realstick:oak_stick 16
/give @s realstick:hunting_spear 1
/give @s realstick:wooden_mallet 1
/give @s realstick:charcoal_lump 4
/give @s realstick:stick_pile 4
/give @s realstick:campfire_kit 1
/give @s realstick:trail_torch 2
```

## Development

This repository keeps the two source packs unpacked so they can be edited or copied into the Bedrock development pack folders:

```text
packs/
├── realistic_sticks_bp/     # behavior pack: items, blocks, loot, and recipes
└── realistic_sticks_rp/     # resource pack: textures, models, mob animations, water flipbooks
```

The project has no third-party build dependency:

```bash
python3 scripts/generate_pack_content.py
python3 scripts/generate_textures.py
python3 scripts/generate_animations.py
python3 scripts/build_addon.py
python3 scripts/validate_addon.py
```

The build writes an importable `.mcaddon` to `releases/`. The validator checks JSON syntax, manifest UUID wiring, item-to-texture references, block-to-geometry and block-to-loot references, PNG dimensions, water flipbook size (16×512), animation identifier overrides, recipe identifiers, and the outer `.mcaddon` archive structure.

## Design notes

- Custom sticks use the `realstick:` namespace and a shared `realstick:wood_sticks` item tag, so the tool, bundle, and vanilla-conversion recipes accept every species without duplicating those recipes.
- Custom 3D blocks use plain cube geometry with explicit per-face UVs and a single 16×16 texture each (the stool uses separate bark-side and ring-top textures), keeping them stable with no experiments required.
- The add-on does not replace vanilla crafting recipes or alter world-generation loot. That keeps it compatible with other packs; use the included conversion recipe when a vanilla recipe needs `minecraft:stick`.
- The vanilla stick icon is intentionally overridden by the resource pack. Remove `textures/items/stick.png` and its `stick` entry in `textures/item_texture.json` if only the new custom items should be restyled.
- No scripts, experimental toggles, or custom entities are needed for the current feature set.

## References

- [Minecraft: Bedrock Edition 26.50 changelog](https://www.minecraft.net/en-us/article/minecraft--bedrock-edition-26-50-changelog)
- [Microsoft Learn: Add-On manifest reference](https://learn.microsoft.com/en-us/minecraft/creator/reference/content/addonsreference/packmanifest?view=minecraft-bedrock-stable)
- [Microsoft Learn: Custom items](https://learn.microsoft.com/en-us/minecraft/creator/documents/addcustomitems?view=minecraft-bedrock-stable)
- [Microsoft Learn: Advanced custom blocks](https://learn.microsoft.com/en-us/minecraft/creator/documents/advancedcustomblocks?view=minecraft-bedrock-stable)
