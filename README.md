# Bedrock Expansion: 200 Items

A complete Minecraft Bedrock Edition add-on project about rebuilding **The Bedrock Forge**, a lost civilization destroyed when the Void Realm leaked into the world. It is a **Behavior Pack + Resource Pack**, not a Java mod, Forge mod, or Fabric mod.

## Compatibility

- Minecraft Bedrock Edition 1.21+
- Pack format: `1.21.0`
- Stable server scripting API dependency: `@minecraft/server` `1.15.0`
- English language content
- No experiments are required for the core item, block, recipe, entity, loot, feature, and script content.

## Project tree

```text
BedrockExpansion_BP/
├── manifest.json
├── items/                 # 149 portable custom item definitions
├── blocks/                # 51 native block definitions (the block inventory item is automatic)
├── entities/              # 10 custom creatures
├── recipes/
├── loot_tables/
├── spawn_rules/
├── features/
├── feature_rules/
├── scripts/
├── functions/
└── texts/
BedrockExpansion_RP/
├── manifest.json
├── textures/items/        # all 200 catalog texture placeholders
├── textures/blocks/
├── textures/entity/
├── models/
├── sounds/
├── texts/
└── ui/
```

The catalog is exactly 200 entries. The 40 Blocks & Building / Redstone & Tech entries, 8 world-generation ore/crystal entries, plus Alchemy Table, Waypoint Stone, and Portal Frame are implemented as 51 native blocks; native Bedrock blocks already have inventory forms, so duplicating them as `minecraft:item` definitions would create duplicate identifiers and content-log errors. `BEDROCK_EXPANSION_CATALOG.json` records both sets.

## Features

- Six progression tiers: Copper/Tin, Silver, Platinum, Mythril, Adamantite, and elemental/Void endgame, plus foundational tier 0.
- Five realm paths: Ember, Frost, Storm, Lumen, and Void.
- 200 individually specified entries with purpose, lore, acquisition, exact recipe description, stats, interactions, texture, sound, script hook, balance note, and progression role in `DESIGN.md`.
- Ores, smelting, armor, tools, weapons, foods, farming resources, full-cube building materials, tech blocks, magic, custom mobs, spawn eggs, furniture tokens, and adventure utilities.
- Stable scripts for magic effects, jetpack impulse, grapple movement, survival gear, tool modes, tech status, portal messaging, and backpack storage fallback.
- Loot tables, spawn rules, underground ore features, feature rules, functions, and placeholder art.

## Install from source

1. Copy `BedrockExpansion_BP` to the Bedrock development `behavior_packs` folder.
2. Copy `BedrockExpansion_RP` to the `resource_packs` folder.
3. Create or edit a world and activate both packs. The behavior manifest already depends on the resource manifest.
4. Enter the world and run `/function bedrock_forge_setup`, then `/function bedrock_forge_help`.
5. Test recipes in a crafting table, furnace, smithing table, brewing stand, and stonecutter.

For a direct smoke test, use `/give @s bedrock_expansion:bedrock_dust 4`, `/give @s bedrock_expansion:copper_sword 1`, `/give @s bedrock_expansion:backpack 1`, `/give @s bedrock_expansion:fire_spell 1`, `/give @s bedrock_expansion:copper_golem_spawn_egg 1`, and `/give @s bedrock_expansion:copper_block 8`.

## Build an importable .mcaddon

After generating the source tree, package both packs for a one-click import:

```bash
python3 scripts/package_bedrock_expansion.py
```

The result is `releases/BedrockExpansion-1.0.0.mcaddon`; open it with Minecraft Bedrock, then activate both packs in the world editor.

## Generate placeholders

`generate_placeholders.py` uses Pillow when it is installed and includes a dependency-free PNG fallback for clean/offline checkouts. For the intended art workflow:

```bash
python3 -m pip install Pillow
python3 generate_placeholders.py
```

It reads `BEDROCK_EXPANSION_CATALOG.json` and generates a 16×16 icon for every item/block entry, 16×16 block textures, 64×64 entity placeholders, and both 64×64 pack icons. Placeholder pixels are deliberately simple and easy to replace.

## Validation

The generator is deterministic and the self-check below validates the exact 200-entry boundary, unique IDs, JSON syntax, item/block coverage, texture coverage, recipes, loot tables, features, spawn rules, manifests, and the docs.

```bash
python3 scripts/build_bedrock_expansion.py
python3 generate_placeholders.py
python3 scripts/validate_bedrock_expansion.py
```

## Known Bedrock limitations and deliberate approximations

- Bedrock custom items cannot safely become arbitrary portable inventories. Backpack scripts therefore expose a storage-channel preview and document chest-backed storage; a future `@minecraft/server-ui` implementation can add a form without changing item IDs.
- A vanilla-compatible item-use event cannot make every custom weapon behave exactly like a Java projectile. Lumen Bow, Ember Crossbow, Frost Trident, and Storm Hammer use authored stats plus script feedback/cooldowns rather than Java projectile internals.
- Native full-cube custom blocks are used for the machine/building entries. Complex multiblock machines and portals are represented with safe blocks, recipes, messages, and quest hooks rather than unsupported Java block entities.
- Ore feature syntax is included for stable Bedrock world generation, but existing worlds may need newly generated chunks; test in a fresh world when checking distribution.
- Placeholder art is not a final art pass. Sound hooks point to stable vanilla sound events until original audio is supplied.
- The five realm systems are represented by realm ingredients, mobs, scripts, portal quest hooks, and documented story gates; custom dimensions would require a separate dimension JSON/content pass and are intentionally not claimed as a stable 1.21 feature here.

## License

MIT, consistent with the repository's existing add-on work.
