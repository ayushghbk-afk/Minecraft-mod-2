# Realistic Sticks

A Bedrock Edition add-on that makes sticks feel like real gathered wood instead of one generic item. It adds species-specific branch sticks, a craftable sharpened stick for early survival, and tied kindling bundles for reliable camp fuel. The resource pack also gives the vanilla `minecraft:stick` a natural bark-and-cut-end texture.

## Compatibility

- **Edition:** Minecraft: Bedrock Edition
- **Target:** Bedrock 26.50 / content format `1.26.50`
- **Experiments:** None required
- **Pack version:** 1.0.0

The pack is authored against the current stable 26.50 add-on format. If a future Bedrock release changes a content schema, the `min_engine_version` and content format can be reviewed in one place by rerunning the generation scripts.

## What is included

| Item | How to obtain it | Use |
| --- | --- | --- |
| Oak, spruce, birch, jungle, acacia, dark oak, mangrove, cherry, pale oak, and bamboo sticks | Craft the matching log, stripped log, plank, or bamboo in a crafting table | Species-specific fuel; accepted by the add-on recipes |
| Sharpened stick | One Realistic Stick plus flint | Early-game hand weapon with 32 durability and +2 attack damage |
| Kindling bundle | Four Realistic Sticks plus string | 30 seconds of furnace fuel per bundle |
| Vanilla sticks | One Realistic Stick in a crafting grid | Converts the new items back to two `minecraft:stick` items for vanilla recipes |

Each wood species has its own color and grain treatment. The generated textures are deliberately pixel-art sized so they remain crisp in Bedrock's item atlas while still showing bark, grain, knots, and a cut end.

## Install

1. Download `releases/RealisticSticks-1.0.0.mcaddon` from this repository.
2. Open the file with Minecraft: Bedrock Edition. Minecraft will import both the behavior pack and resource pack.
3. Create a new world or edit an existing world.
4. Activate **Realistic Sticks | Behavior** and **Realistic Sticks | Resources**. The behavior pack already declares the resource-pack dependency, so enabling the behavior pack is normally enough.
5. Enter the world and craft sticks from the wood species you want.

For a quick smoke test, use:

```text
/give @s realstick:oak_stick 4
/give @s realstick:sharpened_stick 1
/give @s realstick:kindling_bundle 1
```

## Development

This repository keeps the two source packs unpacked so they can be edited or copied into the Bedrock development pack folders:

```text
packs/
├── realistic_sticks_bp/     # behavior pack: items and recipes
└── realistic_sticks_rp/     # resource pack: item atlas and textures
```

The project has no third-party build dependency:

```bash
python3 scripts/generate_pack_content.py
python3 scripts/generate_textures.py
python3 scripts/build_addon.py
python3 scripts/validate_addon.py
```

The build writes an importable `.mcaddon` to `releases/`. The validator checks JSON syntax, manifest UUID wiring, item-to-texture references, PNG dimensions, recipe identifiers, and the outer `.mcaddon` archive structure.

## Design notes

- Custom sticks use the `realstick:` namespace and a shared `realstick:wood_sticks` item tag, so the sharpened-stick, kindling, and vanilla-conversion recipes accept every species without duplicating those recipes.
- The add-on does not replace vanilla crafting recipes or alter world-generation loot. That keeps it compatible with other packs; use the included conversion recipe when a vanilla recipe needs `minecraft:stick`.
- The vanilla stick icon is intentionally overridden by the resource pack. Remove `textures/items/stick.png` and its `stick` entry in `textures/item_texture.json` if only the new custom items should be restyled.
- No scripts, experimental toggles, custom entities, or custom blocks are needed for the current feature set.

## References

- [Minecraft: Bedrock Edition 26.50 changelog](https://www.minecraft.net/en-us/article/minecraft--bedrock-edition-26-50-changelog)
- [Microsoft Learn: Add-On manifest reference](https://learn.microsoft.com/en-us/minecraft/creator/reference/content/addonsreference/packmanifest?view=minecraft-bedrock-stable)
- [Microsoft Learn: Custom items](https://learn.microsoft.com/en-us/minecraft/creator/documents/addcustomitems?view=minecraft-bedrock-stable)
