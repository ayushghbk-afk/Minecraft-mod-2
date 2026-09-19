# Bedrock Expansion: 200 Items — Design Specification

This is the authoritative per-entry design record. Tier 0 is foundational; tiers 1–5 are Copper/Tin through Adamantite; tier 6 is the elemental and Void endgame. Placeable entries are represented by `blocks/*.json` because Bedrock gives a block its inventory item automatically; portable entries are `items/*.json`.

## Catalog index

1. `bedrock_expansion:bedrock_dust` — Bedrock Dust (Ores & Materials, tier 6)
2. `bedrock_expansion:deepslate_crystal` — Deepslate Crystal (Ores & Materials, tier 0)
3. `bedrock_expansion:nether_quartz_shard` — Nether Quartz Shard (Ores & Materials, tier 1)
4. `bedrock_expansion:amethyst_core` — Amethyst Core (Ores & Materials, tier 2)
5. `bedrock_expansion:copper_nugget` — Copper Nugget (Ores & Materials, tier 1)
6. `bedrock_expansion:tin_ore` — Tin Ore (Ores & Materials, tier 1)
7. `bedrock_expansion:tin_ingot` — Tin Ingot (Ores & Materials, tier 1)
8. `bedrock_expansion:silver_ore` — Silver Ore (Ores & Materials, tier 2)
9. `bedrock_expansion:silver_ingot` — Silver Ingot (Ores & Materials, tier 2)
10. `bedrock_expansion:platinum_ore` — Platinum Ore (Ores & Materials, tier 3)
11. `bedrock_expansion:platinum_ingot` — Platinum Ingot (Ores & Materials, tier 3)
12. `bedrock_expansion:mythril_ore` — Mythril Ore (Ores & Materials, tier 4)
13. `bedrock_expansion:mythril_ingot` — Mythril Ingot (Ores & Materials, tier 4)
14. `bedrock_expansion:adamantite_ore` — Adamantite Ore (Ores & Materials, tier 5)
15. `bedrock_expansion:adamantite_ingot` — Adamantite Ingot (Ores & Materials, tier 5)
16. `bedrock_expansion:voidstone` — Voidstone (Ores & Materials, tier 6)
17. `bedrock_expansion:lumen_crystal` — Lumen Crystal (Ores & Materials, tier 6)
18. `bedrock_expansion:ember_dust` — Ember Dust (Ores & Materials, tier 6)
19. `bedrock_expansion:frost_shard` — Frost Shard (Ores & Materials, tier 6)
20. `bedrock_expansion:storm_fragment` — Storm Fragment (Ores & Materials, tier 6)
21. `bedrock_expansion:bedrock_pickaxe` — Bedrock Pickaxe (Tools & Weapons, tier 6)
22. `bedrock_expansion:bedrock_axe` — Bedrock Axe (Tools & Weapons, tier 6)
23. `bedrock_expansion:bedrock_shovel` — Bedrock Shovel (Tools & Weapons, tier 6)
24. `bedrock_expansion:bedrock_hoe` — Bedrock Hoe (Tools & Weapons, tier 6)
25. `bedrock_expansion:copper_sword` — Copper Sword (Tools & Weapons, tier 1)
26. `bedrock_expansion:silver_sword` — Silver Sword (Tools & Weapons, tier 2)
27. `bedrock_expansion:platinum_sword` — Platinum Sword (Tools & Weapons, tier 3)
28. `bedrock_expansion:mythril_sword` — Mythril Sword (Tools & Weapons, tier 4)
29. `bedrock_expansion:adamantite_sword` — Adamantite Sword (Tools & Weapons, tier 5)
30. `bedrock_expansion:void_blade` — Void Blade (Tools & Weapons, tier 6)
31. `bedrock_expansion:lumen_bow` — Lumen Bow (Tools & Weapons, tier 6)
32. `bedrock_expansion:ember_crossbow` — Ember Crossbow (Tools & Weapons, tier 6)
33. `bedrock_expansion:frost_trident` — Frost Trident (Tools & Weapons, tier 6)
34. `bedrock_expansion:storm_hammer` — Storm Hammer (Tools & Weapons, tier 6)
35. `bedrock_expansion:crystal_dagger` — Crystal Dagger (Tools & Weapons, tier 0)
36. `bedrock_expansion:stone_spear` — Stone Spear (Tools & Weapons, tier 0)
37. `bedrock_expansion:chainsaw` — Chainsaw (Tools & Weapons, tier 4)
38. `bedrock_expansion:drill` — Drill (Tools & Weapons, tier 5)
39. `bedrock_expansion:scythe` — Scythe (Tools & Weapons, tier 3)
40. `bedrock_expansion:war_axe` — War Axe (Tools & Weapons, tier 5)
41. `bedrock_expansion:copper_helmet` — Copper Helmet (Armor & Wearables, tier 1)
42. `bedrock_expansion:copper_chestplate` — Copper Chestplate (Armor & Wearables, tier 1)
43. `bedrock_expansion:copper_leggings` — Copper Leggings (Armor & Wearables, tier 1)
44. `bedrock_expansion:copper_boots` — Copper Boots (Armor & Wearables, tier 1)
45. `bedrock_expansion:silver_helmet` — Silver Helmet (Armor & Wearables, tier 2)
46. `bedrock_expansion:silver_chestplate` — Silver Chestplate (Armor & Wearables, tier 2)
47. `bedrock_expansion:silver_leggings` — Silver Leggings (Armor & Wearables, tier 2)
48. `bedrock_expansion:silver_boots` — Silver Boots (Armor & Wearables, tier 2)
49. `bedrock_expansion:platinum_helmet` — Platinum Helmet (Armor & Wearables, tier 3)
50. `bedrock_expansion:platinum_chestplate` — Platinum Chestplate (Armor & Wearables, tier 3)
51. `bedrock_expansion:platinum_leggings` — Platinum Leggings (Armor & Wearables, tier 3)
52. `bedrock_expansion:platinum_boots` — Platinum Boots (Armor & Wearables, tier 3)
53. `bedrock_expansion:mythril_helmet` — Mythril Helmet (Armor & Wearables, tier 4)
54. `bedrock_expansion:mythril_chestplate` — Mythril Chestplate (Armor & Wearables, tier 4)
55. `bedrock_expansion:mythril_leggings` — Mythril Leggings (Armor & Wearables, tier 4)
56. `bedrock_expansion:mythril_boots` — Mythril Boots (Armor & Wearables, tier 4)
57. `bedrock_expansion:adamantite_helmet` — Adamantite Helmet (Armor & Wearables, tier 5)
58. `bedrock_expansion:adamantite_chestplate` — Adamantite Chestplate (Armor & Wearables, tier 5)
59. `bedrock_expansion:adamantite_leggings` — Adamantite Leggings (Armor & Wearables, tier 5)
60. `bedrock_expansion:adamantite_boots` — Adamantite Boots (Armor & Wearables, tier 5)
61. `bedrock_expansion:golden_apple_pie` — Golden Apple Pie (Food & Farming, tier 0)
62. `bedrock_expansion:copper_carrot` — Copper Carrot (Food & Farming, tier 1)
63. `bedrock_expansion:silver_beetroot` — Silver Beetroot (Food & Farming, tier 2)
64. `bedrock_expansion:platinum_potato` — Platinum Potato (Food & Farming, tier 3)
65. `bedrock_expansion:mythril_bread` — Mythril Bread (Food & Farming, tier 4)
66. `bedrock_expansion:adamantite_stew` — Adamantite Stew (Food & Farming, tier 5)
67. `bedrock_expansion:lumen_berry` — Lumen Berry (Food & Farming, tier 6)
68. `bedrock_expansion:ember_pepper` — Ember Pepper (Food & Farming, tier 6)
69. `bedrock_expansion:frost_melon` — Frost Melon (Food & Farming, tier 6)
70. `bedrock_expansion:storm_corn` — Storm Corn (Food & Farming, tier 6)
71. `bedrock_expansion:void_fruit` — Void Fruit (Food & Farming, tier 6)
72. `bedrock_expansion:crystal_grapes` — Crystal Grapes (Food & Farming, tier 3)
73. `bedrock_expansion:honey_cookie` — Honey Cookie (Food & Farming, tier 0)
74. `bedrock_expansion:chocolate_bar` — Chocolate Bar (Food & Farming, tier 0)
75. `bedrock_expansion:cheese_wheel` — Cheese Wheel (Food & Farming, tier 0)
76. `bedrock_expansion:butter` — Butter (Food & Farming, tier 0)
77. `bedrock_expansion:fried_egg` — Fried Egg (Food & Farming, tier 0)
78. `bedrock_expansion:bacon_strip` — Bacon Strip (Food & Farming, tier 0)
79. `bedrock_expansion:fish_stew` — Fish Stew (Food & Farming, tier 0)
80. `bedrock_expansion:magic_cake` — Magic Cake (Food & Farming, tier 6)
81. `bedrock_expansion:copper_block` — Copper Block (Blocks & Building, tier 1)
82. `bedrock_expansion:silver_block` — Silver Block (Blocks & Building, tier 2)
83. `bedrock_expansion:platinum_block` — Platinum Block (Blocks & Building, tier 3)
84. `bedrock_expansion:mythril_block` — Mythril Block (Blocks & Building, tier 4)
85. `bedrock_expansion:adamantite_block` — Adamantite Block (Blocks & Building, tier 5)
86. `bedrock_expansion:tin_block` — Tin Block (Blocks & Building, tier 1)
87. `bedrock_expansion:lumen_block` — Lumen Block (Blocks & Building, tier 6)
88. `bedrock_expansion:ember_block` — Ember Block (Blocks & Building, tier 6)
89. `bedrock_expansion:frost_block` — Frost Block (Blocks & Building, tier 6)
90. `bedrock_expansion:storm_block` — Storm Block (Blocks & Building, tier 6)
91. `bedrock_expansion:void_block` — Void Block (Blocks & Building, tier 6)
92. `bedrock_expansion:crystal_block` — Crystal Block (Blocks & Building, tier 3)
93. `bedrock_expansion:reinforced_glass` — Reinforced Glass (Blocks & Building, tier 2)
94. `bedrock_expansion:dark_glass` — Dark Glass (Blocks & Building, tier 2)
95. `bedrock_expansion:glowing_concrete` — Glowing Concrete (Blocks & Building, tier 2)
96. `bedrock_expansion:mossy_bricks` — Mossy Bricks (Blocks & Building, tier 2)
97. `bedrock_expansion:cracked_bricks` — Cracked Bricks (Blocks & Building, tier 2)
98. `bedrock_expansion:marble` — Marble (Blocks & Building, tier 2)
99. `bedrock_expansion:polished_marble` — Polished Marble (Blocks & Building, tier 2)
100. `bedrock_expansion:limestone` — Limestone (Blocks & Building, tier 2)
101. `bedrock_expansion:copper_wire` — Copper Wire (Redstone & Tech, tier 1)
102. `bedrock_expansion:silver_wire` — Silver Wire (Redstone & Tech, tier 2)
103. `bedrock_expansion:logic_gate` — Logic Gate (Redstone & Tech, tier 2)
104. `bedrock_expansion:timer_block` — Timer Block (Redstone & Tech, tier 2)
105. `bedrock_expansion:pulse_extender` — Pulse Extender (Redstone & Tech, tier 2)
106. `bedrock_expansion:item_pipe` — Item Pipe (Redstone & Tech, tier 2)
107. `bedrock_expansion:fluid_pipe` — Fluid Pipe (Redstone & Tech, tier 2)
108. `bedrock_expansion:energy_cable` — Energy Cable (Redstone & Tech, tier 2)
109. `bedrock_expansion:solar_panel` — Solar Panel (Redstone & Tech, tier 2)
110. `bedrock_expansion:battery` — Battery (Redstone & Tech, tier 2)
111. `bedrock_expansion:generator` — Generator (Redstone & Tech, tier 2)
112. `bedrock_expansion:electric_furnace` — Electric Furnace (Redstone & Tech, tier 2)
113. `bedrock_expansion:auto_crafting_table` — Auto Crafting Table (Redstone & Tech, tier 2)
114. `bedrock_expansion:conveyor_belt` — Conveyor Belt (Redstone & Tech, tier 2)
115. `bedrock_expansion:robot_arm` — Robot Arm (Redstone & Tech, tier 2)
116. `bedrock_expansion:sensor_block` — Sensor Block (Redstone & Tech, tier 2)
117. `bedrock_expansion:speaker_block` — Speaker Block (Redstone & Tech, tier 2)
118. `bedrock_expansion:monitor_block` — Monitor Block (Redstone & Tech, tier 2)
119. `bedrock_expansion:keyboard_block` — Keyboard Block (Redstone & Tech, tier 2)
120. `bedrock_expansion:computer_block` — Computer Block (Redstone & Tech, tier 2)
121. `bedrock_expansion:mana_crystal` — Mana Crystal (Magic & Enchanting, tier 3)
122. `bedrock_expansion:spell_book` — Spell Book (Magic & Enchanting, tier 3)
123. `bedrock_expansion:fire_spell` — Fire Spell (Magic & Enchanting, tier 6)
124. `bedrock_expansion:ice_spell` — Ice Spell (Magic & Enchanting, tier 6)
125. `bedrock_expansion:lightning_spell` — Lightning Spell (Magic & Enchanting, tier 6)
126. `bedrock_expansion:healing_spell` — Healing Spell (Magic & Enchanting, tier 6)
127. `bedrock_expansion:teleport_spell` — Teleport Spell (Magic & Enchanting, tier 6)
128. `bedrock_expansion:shield_spell` — Shield Spell (Magic & Enchanting, tier 6)
129. `bedrock_expansion:summon_spell` — Summon Spell (Magic & Enchanting, tier 6)
130. `bedrock_expansion:enchantment_orb` — Enchantment Orb (Magic & Enchanting, tier 3)
131. `bedrock_expansion:rune_stone` — Rune Stone (Magic & Enchanting, tier 3)
132. `bedrock_expansion:magic_wand` — Magic Wand (Magic & Enchanting, tier 3)
133. `bedrock_expansion:staff_of_fire` — Staff of Fire (Magic & Enchanting, tier 6)
134. `bedrock_expansion:staff_of_ice` — Staff of Ice (Magic & Enchanting, tier 6)
135. `bedrock_expansion:staff_of_storms` — Staff of Storms (Magic & Enchanting, tier 6)
136. `bedrock_expansion:staff_of_life` — Staff of Life (Magic & Enchanting, tier 6)
137. `bedrock_expansion:soul_gem` — Soul Gem (Magic & Enchanting, tier 6)
138. `bedrock_expansion:void_pearl` — Void Pearl (Magic & Enchanting, tier 6)
139. `bedrock_expansion:celestial_shard` — Celestial Shard (Magic & Enchanting, tier 6)
140. `bedrock_expansion:alchemy_table` — Alchemy Table (Magic & Enchanting, tier 3)
141. `bedrock_expansion:copper_golem_spawn_egg` — Copper Golem Spawn Egg (Mobs & Drops, tier 2)
142. `bedrock_expansion:silver_golem_spawn_egg` — Silver Golem Spawn Egg (Mobs & Drops, tier 2)
143. `bedrock_expansion:crystal_golem_spawn_egg` — Crystal Golem Spawn Egg (Mobs & Drops, tier 5)
144. `bedrock_expansion:void_golem_spawn_egg` — Void Golem Spawn Egg (Mobs & Drops, tier 6)
145. `bedrock_expansion:ember_imp_spawn_egg` — Ember Imp Spawn Egg (Mobs & Drops, tier 4)
146. `bedrock_expansion:frost_wolf_spawn_egg` — Frost Wolf Spawn Egg (Mobs & Drops, tier 4)
147. `bedrock_expansion:storm_eagle_spawn_egg` — Storm Eagle Spawn Egg (Mobs & Drops, tier 5)
148. `bedrock_expansion:lumen_fairy_spawn_egg` — Lumen Fairy Spawn Egg (Mobs & Drops, tier 6)
149. `bedrock_expansion:cave_lurker_spawn_egg` — Cave Lurker Spawn Egg (Mobs & Drops, tier 2)
150. `bedrock_expansion:deep_crab_spawn_egg` — Deep Crab Spawn Egg (Mobs & Drops, tier 2)
151. `bedrock_expansion:copper_golem_core` — Copper Golem Core (Mobs & Drops, tier 2)
152. `bedrock_expansion:silver_golem_core` — Silver Golem Core (Mobs & Drops, tier 2)
153. `bedrock_expansion:crystal_golem_core` — Crystal Golem Core (Mobs & Drops, tier 5)
154. `bedrock_expansion:void_golem_core` — Void Golem Core (Mobs & Drops, tier 6)
155. `bedrock_expansion:ember_essence` — Ember Essence (Mobs & Drops, tier 4)
156. `bedrock_expansion:frost_fur` — Frost Fur (Mobs & Drops, tier 4)
157. `bedrock_expansion:storm_feather` — Storm Feather (Mobs & Drops, tier 5)
158. `bedrock_expansion:lumen_dust` — Lumen Dust (Mobs & Drops, tier 6)
159. `bedrock_expansion:lurker_eye` — Lurker Eye (Mobs & Drops, tier 2)
160. `bedrock_expansion:crab_claw` — Crab Claw (Mobs & Drops, tier 2)
161. `bedrock_expansion:wooden_chair` — Wooden Chair (Decoration & Furniture, tier 0)
162. `bedrock_expansion:wooden_table` — Wooden Table (Decoration & Furniture, tier 0)
163. `bedrock_expansion:wooden_bed` — Wooden Bed (Decoration & Furniture, tier 0)
164. `bedrock_expansion:sofa` — Sofa (Decoration & Furniture, tier 0)
165. `bedrock_expansion:bookshelf` — Bookshelf (Decoration & Furniture, tier 0)
166. `bedrock_expansion:lamp` — Lamp (Decoration & Furniture, tier 1)
167. `bedrock_expansion:ceiling_light` — Ceiling Light (Decoration & Furniture, tier 1)
168. `bedrock_expansion:wall_clock` — Wall Clock (Decoration & Furniture, tier 0)
169. `bedrock_expansion:painting_frame` — Painting Frame (Decoration & Furniture, tier 0)
170. `bedrock_expansion:vase` — Vase (Decoration & Furniture, tier 0)
171. `bedrock_expansion:large_flower_pot` — Large Flower Pot (Decoration & Furniture, tier 0)
172. `bedrock_expansion:rug` — Rug (Decoration & Furniture, tier 0)
173. `bedrock_expansion:curtain` — Curtain (Decoration & Furniture, tier 0)
174. `bedrock_expansion:fireplace` — Fireplace (Decoration & Furniture, tier 1)
175. `bedrock_expansion:kitchen_counter` — Kitchen Counter (Decoration & Furniture, tier 0)
176. `bedrock_expansion:oven` — Oven (Decoration & Furniture, tier 1)
177. `bedrock_expansion:refrigerator` — Refrigerator (Decoration & Furniture, tier 1)
178. `bedrock_expansion:toilet` — Toilet (Decoration & Furniture, tier 0)
179. `bedrock_expansion:bathtub` — Bathtub (Decoration & Furniture, tier 0)
180. `bedrock_expansion:sink` — Sink (Decoration & Furniture, tier 1)
181. `bedrock_expansion:backpack` — Backpack (Utility & Adventure, tier 2)
182. `bedrock_expansion:large_backpack` — Large Backpack (Utility & Adventure, tier 3)
183. `bedrock_expansion:ender_backpack` — Ender Backpack (Utility & Adventure, tier 6)
184. `bedrock_expansion:map_marker` — Map Marker (Utility & Adventure, tier 1)
185. `bedrock_expansion:compass_upgrade` — Compass Upgrade (Utility & Adventure, tier 1)
186. `bedrock_expansion:clock_upgrade` — Clock Upgrade (Utility & Adventure, tier 1)
187. `bedrock_expansion:lantern_helmet` — Lantern Helmet (Utility & Adventure, tier 1)
188. `bedrock_expansion:night_vision_goggles` — Night Vision Goggles (Utility & Adventure, tier 3)
189. `bedrock_expansion:scuba_helmet` — Scuba Helmet (Utility & Adventure, tier 3)
190. `bedrock_expansion:jetpack` — Jetpack (Utility & Adventure, tier 5)
191. `bedrock_expansion:parachute` — Parachute (Utility & Adventure, tier 1)
192. `bedrock_expansion:grappling_hook` — Grappling Hook (Utility & Adventure, tier 4)
193. `bedrock_expansion:lockpick` — Lockpick (Utility & Adventure, tier 1)
194. `bedrock_expansion:key` — Key (Utility & Adventure, tier 1)
195. `bedrock_expansion:treasure_map` — Treasure Map (Utility & Adventure, tier 2)
196. `bedrock_expansion:boss_key` — Boss Key (Utility & Adventure, tier 5)
197. `bedrock_expansion:dungeon_compass` — Dungeon Compass (Utility & Adventure, tier 3)
198. `bedrock_expansion:waypoint_stone` — Waypoint Stone (Utility & Adventure, tier 4)
199. `bedrock_expansion:portal_frame` — Portal Frame (Utility & Adventure, tier 6)
200. `bedrock_expansion:portal_activator` — Portal Activator (Utility & Adventure, tier 6)

## Complete item records

### 1. Bedrock Dust
- **Item ID:** `bedrock_expansion:bedrock_dust`
- **Display Name:** Bedrock Dust
- **Category:** Ores & Materials
- **Tier:** 6 — Elemental / Void
- **Purpose:** A forge catalyst that makes late-game alloys bond instead of shatter.
- **Story/Lore:** The surviving inscription for Bedrock Dust names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Grind 1 Bedrock fragment with a Voidstone catalyst at the restored Forge.
- **Recipe:** Forge process: 1 Bedrock fragment + 1 Voidstone -> 2 Bedrock Dust.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/bedrock_dust.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 2. Deepslate Crystal
- **Item ID:** `bedrock_expansion:deepslate_crystal`
- **Display Name:** Deepslate Crystal
- **Category:** Ores & Materials
- **Tier:** 0 — Foundational
- **Purpose:** A low-tier resonator used to read the first buried Forge markers.
- **Story/Lore:** The surviving inscription for Deepslate Crystal names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/deepslate_crystal.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Foundational tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 3. Nether Quartz Shard
- **Item ID:** `bedrock_expansion:nether_quartz_shard`
- **Display Name:** Nether Quartz Shard
- **Category:** Ores & Materials
- **Tier:** 1 — Copper/Tin
- **Purpose:** A heat-stable conductor for the first energy and spell circuits.
- **Story/Lore:** The surviving inscription for Nether Quartz Shard names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Nether Quartz into 4 Nether Quartz Shards.
- **Recipe:** Shapeless: 1 Minecraft Nether Quartz -> 4 Nether Quartz Shards.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/nether_quartz_shard.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 4. Amethyst Core
- **Item ID:** `bedrock_expansion:amethyst_core`
- **Display Name:** Amethyst Core
- **Category:** Ores & Materials
- **Tier:** 2 — Silver
- **Purpose:** A focused crystal lens that turns scattered enchantment into stored charge.
- **Story/Lore:** The surviving inscription for Amethyst Core names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 4 Amethyst Shards around 1 Amethyst Block.
- **Recipe:** Shaped 3x3: A A A / A B A / A A A; A=Amethyst Shard, B=Amethyst Block.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/amethyst_core.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 5. Copper Nugget
- **Item ID:** `bedrock_expansion:copper_nugget`
- **Display Name:** Copper Nugget
- **Category:** Ores & Materials
- **Tier:** 1 — Copper/Tin
- **Purpose:** A small conductive unit for wiring, alloys, and economical repairs.
- **Story/Lore:** The surviving inscription for Copper Nugget names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Copper Ingot into 9 Copper Nuggets.
- **Recipe:** Shapeless: 1 Copper Ingot -> 9 Copper Nuggets.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_nugget.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 6. Tin Ore
- **Item ID:** `bedrock_expansion:tin_ore`
- **Display Name:** Tin Ore
- **Category:** Ores & Materials
- **Tier:** 1 — Copper/Tin
- **Purpose:** A soft early ore that opens soldering, lanterns, and the first machine recipes.
- **Story/Lore:** The surviving inscription for Tin Ore names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/tin_ore.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 7. Tin Ingot
- **Item ID:** `bedrock_expansion:tin_ingot`
- **Display Name:** Tin Ingot
- **Category:** Ores & Materials
- **Tier:** 1 — Copper/Tin
- **Purpose:** A workable solder metal for stable low-voltage assemblies.
- **Story/Lore:** The surviving inscription for Tin Ingot names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Smelt 1 Tin Ore in a furnace or electric furnace.
- **Recipe:** Furnace: 1 Tin Ore -> 1 Tin Ingot.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/tin_ingot.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 8. Silver Ore
- **Item ID:** `bedrock_expansion:silver_ore`
- **Display Name:** Silver Ore
- **Category:** Ores & Materials
- **Tier:** 2 — Silver
- **Purpose:** A moon-bright ore that carries enchantment more cleanly than copper.
- **Story/Lore:** The surviving inscription for Silver Ore names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_ore.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 9. Silver Ingot
- **Item ID:** `bedrock_expansion:silver_ingot`
- **Display Name:** Silver Ingot
- **Category:** Ores & Materials
- **Tier:** 2 — Silver
- **Purpose:** A reflective conductor for precision tools and mana-safe circuitry.
- **Story/Lore:** The surviving inscription for Silver Ingot names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Smelt 1 Silver Ore in a furnace or electric furnace.
- **Recipe:** Furnace: 1 Silver Ore -> 1 Silver Ingot.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_ingot.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 10. Platinum Ore
- **Item ID:** `bedrock_expansion:platinum_ore`
- **Display Name:** Platinum Ore
- **Category:** Ores & Materials
- **Tier:** 3 — Platinum
- **Purpose:** A rare dense ore that survives pressure in deep Forge chambers.
- **Story/Lore:** The surviving inscription for Platinum Ore names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_ore.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 11. Platinum Ingot
- **Item ID:** `bedrock_expansion:platinum_ingot`
- **Display Name:** Platinum Ingot
- **Category:** Ores & Materials
- **Tier:** 3 — Platinum
- **Purpose:** A precision metal for high-efficiency tools and durable machinery.
- **Story/Lore:** The surviving inscription for Platinum Ingot names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Smelt 1 Platinum Ore in a furnace or electric furnace.
- **Recipe:** Furnace: 1 Platinum Ore -> 1 Platinum Ingot.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_ingot.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 12. Mythril Ore
- **Item ID:** `bedrock_expansion:mythril_ore`
- **Display Name:** Mythril Ore
- **Category:** Ores & Materials
- **Tier:** 4 — Mythril
- **Purpose:** A resonant ore whose light weight makes advanced mobility practical.
- **Story/Lore:** The surviving inscription for Mythril Ore names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_ore.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 13. Mythril Ingot
- **Item ID:** `bedrock_expansion:mythril_ingot`
- **Display Name:** Mythril Ingot
- **Category:** Ores & Materials
- **Tier:** 4 — Mythril
- **Purpose:** A flexible supermetal that bridges industrial engineering and magic.
- **Story/Lore:** The surviving inscription for Mythril Ingot names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Smelt 1 Mythril Ore in a furnace or electric furnace.
- **Recipe:** Furnace: 1 Mythril Ore -> 1 Mythril Ingot.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_ingot.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 14. Adamantite Ore
- **Item ID:** `bedrock_expansion:adamantite_ore`
- **Display Name:** Adamantite Ore
- **Category:** Ores & Materials
- **Tier:** 5 — Adamantite
- **Purpose:** A nearly unbreakable ore required for the final physical tier.
- **Story/Lore:** The surviving inscription for Adamantite Ore names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_ore.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 15. Adamantite Ingot
- **Item ID:** `bedrock_expansion:adamantite_ingot`
- **Display Name:** Adamantite Ingot
- **Category:** Ores & Materials
- **Tier:** 5 — Adamantite
- **Purpose:** A forge-perfect alloy that anchors structures against Void distortion.
- **Story/Lore:** The surviving inscription for Adamantite Ingot names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Smelt 1 Adamantite Ore in a furnace or electric furnace.
- **Recipe:** Furnace: 1 Adamantite Ore -> 1 Adamantite Ingot.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_ingot.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 16. Voidstone
- **Item ID:** `bedrock_expansion:voidstone`
- **Display Name:** Voidstone
- **Category:** Ores & Materials
- **Tier:** 6 — Elemental / Void
- **Purpose:** A dangerous dark anchor used to seal breaches and power controlled portals.
- **Story/Lore:** The surviving inscription for Voidstone names the last Forge architects as its maker. It was designed after the Void changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/voidstone.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 17. Lumen Crystal
- **Item ID:** `bedrock_expansion:lumen_crystal`
- **Display Name:** Lumen Crystal
- **Category:** Ores & Materials
- **Tier:** 6 — Elemental / Void
- **Purpose:** A clean light source that stores restorative energy for the Lumen path.
- **Story/Lore:** The surviving inscription for Lumen Crystal names the last Forge architects as its maker. It was designed after the Lumen Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/lumen_crystal.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 18. Ember Dust
- **Item ID:** `bedrock_expansion:ember_dust`
- **Display Name:** Ember Dust
- **Category:** Ores & Materials
- **Tier:** 6 — Elemental / Void
- **Purpose:** A hot, compact fuel that powers machines, jetpacks, and Ember spells.
- **Story/Lore:** The surviving inscription for Ember Dust names the last Forge architects as its maker. It was designed after the Ember Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/ember_dust.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 19. Frost Shard
- **Item ID:** `bedrock_expansion:frost_shard`
- **Display Name:** Frost Shard
- **Category:** Ores & Materials
- **Tier:** 6 — Elemental / Void
- **Purpose:** A cold shard that preserves food and enables slowing and protection effects.
- **Story/Lore:** The surviving inscription for Frost Shard names the last Forge architects as its maker. It was designed after the Frost Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/frost_shard.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 20. Storm Fragment
- **Item ID:** `bedrock_expansion:storm_fragment`
- **Display Name:** Storm Fragment
- **Category:** Ores & Materials
- **Tier:** 6 — Elemental / Void
- **Purpose:** A charged fragment for flight, lightning tools, and fast automation.
- **Story/Lore:** The surviving inscription for Storm Fragment names the last Forge architects as its maker. It was designed after the Storm Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** World generation or realm cache; the exact vein, chest, or realm source is listed in STORY.md.
- **Recipe:** No crafting recipe; harvest the world-gen node or realm cache.
- **Stats:** Stack 64; material hardness and smelting value are tuned to tier.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/storm_fragment.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 21. Bedrock Pickaxe
- **Item ID:** `bedrock_expansion:bedrock_pickaxe`
- **Display Name:** Bedrock Pickaxe
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A tier-six mining tool for Voidstone and the toughest Forge seams.
- **Story/Lore:** The surviving inscription for Bedrock Pickaxe names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Pickaxe.
- **Recipe:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Pickaxe.
- **Stats:** Damage 10; durability 3000; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use while sneaking to toggle the 3x3 mining intent; the script displays the mode and leaves protected blocks untouched.
- **Texture Path:** `textures/items/bedrock_pickaxe.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** scripts/tools.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 22. Bedrock Axe
- **Item ID:** `bedrock_expansion:bedrock_axe`
- **Display Name:** Bedrock Axe
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A heavy endgame axe that harvests ancient wood quickly without replacing every tool.
- **Story/Lore:** The surviving inscription for Bedrock Axe names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Axe.
- **Recipe:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Axe.
- **Stats:** Damage 10; durability 1600; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/bedrock_axe.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 23. Bedrock Shovel
- **Item ID:** `bedrock_expansion:bedrock_shovel`
- **Display Name:** Bedrock Shovel
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A high-durability excavator for clearing reinforced ash and realm soil.
- **Story/Lore:** The surviving inscription for Bedrock Shovel names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Shovel.
- **Recipe:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Shovel.
- **Stats:** Damage 10; durability 1600; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/bedrock_shovel.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 24. Bedrock Hoe
- **Item ID:** `bedrock_expansion:bedrock_hoe`
- **Display Name:** Bedrock Hoe
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A late-game cultivator that makes elemental crops viable in hostile realms.
- **Story/Lore:** The surviving inscription for Bedrock Hoe names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Hoe.
- **Recipe:** Crafting table 3x3: DDD / _M_ / _M_, where D=Bedrock Dust, M=Mythril Ingot, and _ is an empty slot -> Bedrock Hoe.
- **Stats:** Damage 10; durability 1600; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/bedrock_hoe.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 25. Copper Sword
- **Item ID:** `bedrock_expansion:copper_sword`
- **Display Name:** Copper Sword
- **Category:** Tools & Weapons
- **Tier:** 1 — Copper/Tin
- **Purpose:** The first Forge-forged blade, giving new players a modest step above stone.
- **Story/Lore:** The surviving inscription for Copper Sword names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: M / M / S, where M=Copper Ingot and S=Stick -> Copper Sword.
- **Recipe:** Crafting table 3x3: M / M / S, where M=Copper Ingot and S=Stick -> Copper Sword.
- **Stats:** Damage 5; durability 180; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_sword.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 26. Silver Sword
- **Item ID:** `bedrock_expansion:silver_sword`
- **Display Name:** Silver Sword
- **Category:** Tools & Weapons
- **Tier:** 2 — Silver
- **Purpose:** A balanced anti-spirit sword with better reach-feel but lower raw damage than platinum.
- **Story/Lore:** The surviving inscription for Silver Sword names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: M / M / S, where M=Silver Ingot and S=Stick -> Silver Sword.
- **Recipe:** Crafting table 3x3: M / M / S, where M=Silver Ingot and S=Stick -> Silver Sword.
- **Stats:** Damage 6; durability 320; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_sword.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 27. Platinum Sword
- **Item ID:** `bedrock_expansion:platinum_sword`
- **Display Name:** Platinum Sword
- **Category:** Tools & Weapons
- **Tier:** 3 — Platinum
- **Purpose:** A dependable midgame sword for deep caves and machine-guarded ruins.
- **Story/Lore:** The surviving inscription for Platinum Sword names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: M / M / S, where M=Platinum Ingot and S=Stick -> Platinum Sword.
- **Recipe:** Crafting table 3x3: M / M / S, where M=Platinum Ingot and S=Stick -> Platinum Sword.
- **Stats:** Damage 7; durability 520; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_sword.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 28. Mythril Sword
- **Item ID:** `bedrock_expansion:mythril_sword`
- **Display Name:** Mythril Sword
- **Category:** Tools & Weapons
- **Tier:** 4 — Mythril
- **Purpose:** A light, durable blade that rewards mobile combat rather than brute force.
- **Story/Lore:** The surviving inscription for Mythril Sword names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: M / M / S, where M=Mythril Ingot and S=Stick -> Mythril Sword.
- **Recipe:** Crafting table 3x3: M / M / S, where M=Mythril Ingot and S=Stick -> Mythril Sword.
- **Stats:** Damage 8; durability 780; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_sword.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 29. Adamantite Sword
- **Item ID:** `bedrock_expansion:adamantite_sword`
- **Display Name:** Adamantite Sword
- **Category:** Tools & Weapons
- **Tier:** 5 — Adamantite
- **Purpose:** A resilient end-physical-tier weapon intended for breach expeditions.
- **Story/Lore:** The surviving inscription for Adamantite Sword names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: M / M / S, where M=Adamantite Ingot and S=Stick -> Adamantite Sword.
- **Recipe:** Crafting table 3x3: M / M / S, where M=Adamantite Ingot and S=Stick -> Adamantite Sword.
- **Stats:** Damage 9; durability 1100; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_sword.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 30. Void Blade
- **Item ID:** `bedrock_expansion:void_blade`
- **Display Name:** Void Blade
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A risk-reward weapon that cuts through Void creatures while demanding careful cooldowns.
- **Story/Lore:** The surviving inscription for Void Blade names the last Forge architects as its maker. It was designed after the Void changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: V / V / S, where V=Voidstone and S=Stick -> Void Blade.
- **Recipe:** Crafting table 3x3: V / V / S, where V=Voidstone and S=Stick -> Void Blade.
- **Stats:** Damage 10; durability 1600; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/void_blade.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 31. Lumen Bow
- **Item ID:** `bedrock_expansion:lumen_bow`
- **Display Name:** Lumen Bow
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A quiet light bow that marks targets without relying on rare arrows.
- **Story/Lore:** The surviving inscription for Lumen Bow names the last Forge architects as its maker. It was designed after the Lumen Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Lumen Crystals + 3 String; pattern L S / L S / L S, L=Lumen Crystal and S=String.
- **Recipe:** 3 Lumen Crystals + 3 String; pattern L S / L S / L S, L=Lumen Crystal and S=String.
- **Stats:** Damage 10; durability 1600; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/lumen_bow.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 32. Ember Crossbow
- **Item ID:** `bedrock_expansion:ember_crossbow`
- **Display Name:** Ember Crossbow
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A charged ranged weapon that trades reload time for brief fire damage.
- **Story/Lore:** The surviving inscription for Ember Crossbow names the last Forge architects as its maker. It was designed after the Ember Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 2 Ember Dust + 2 Iron Ingots + 1 String; pattern EIE / ISI /  S , E=Ember Dust, I=Iron Ingot, S=String.
- **Recipe:** 2 Ember Dust + 2 Iron Ingots + 1 String; pattern EIE / ISI /  S , E=Ember Dust, I=Iron Ingot, S=String.
- **Stats:** Damage 10; durability 1600; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/ember_crossbow.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 33. Frost Trident
- **Item ID:** `bedrock_expansion:frost_trident`
- **Display Name:** Frost Trident
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A control weapon that slows a target so exploration remains tactical.
- **Story/Lore:** The surviving inscription for Frost Trident names the last Forge architects as its maker. It was designed after the Frost Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 2 Frost Shards + 1 Mythril Ingot; pattern F / F / M.
- **Recipe:** 2 Frost Shards + 1 Mythril Ingot; pattern F / F / M.
- **Stats:** Damage 10; durability 1600; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/frost_trident.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 34. Storm Hammer
- **Item ID:** `bedrock_expansion:storm_hammer`
- **Display Name:** Storm Hammer
- **Category:** Tools & Weapons
- **Tier:** 6 — Elemental / Void
- **Purpose:** A shockwave tool for groups, balanced by a long cooldown and heavy durability cost.
- **Story/Lore:** The surviving inscription for Storm Hammer names the last Forge architects as its maker. It was designed after the Storm Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 4 Storm Fragments + 2 Adamantite Ingots; pattern SAS / SAS /  S , S=Storm Fragment and A=Adamantite Ingot.
- **Recipe:** 4 Storm Fragments + 2 Adamantite Ingots; pattern SAS / SAS /  S , S=Storm Fragment and A=Adamantite Ingot.
- **Stats:** Damage 12; durability 700; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/storm_hammer.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** scripts/tools.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 35. Crystal Dagger
- **Item ID:** `bedrock_expansion:crystal_dagger`
- **Display Name:** Crystal Dagger
- **Category:** Tools & Weapons
- **Tier:** 0 — Foundational
- **Purpose:** A fast precision weapon for cave lurkers and weak points.
- **Story/Lore:** The surviving inscription for Crystal Dagger names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 1 Amethyst Core + 1 Copper Ingot + 1 Stick; pattern C / A / S.
- **Recipe:** 1 Amethyst Core + 1 Copper Ingot + 1 Stick; pattern C / A / S.
- **Stats:** Damage 3; durability 80; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/crystal_dagger.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Foundational tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 36. Stone Spear
- **Item ID:** `bedrock_expansion:stone_spear`
- **Display Name:** Stone Spear
- **Category:** Tools & Weapons
- **Tier:** 0 — Foundational
- **Purpose:** A reliable first hunt weapon assembled before the Forge is restored.
- **Story/Lore:** The surviving inscription for Stone Spear names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 1 Flint + 2 Sticks; pattern F / S / S.
- **Recipe:** 1 Flint + 2 Sticks; pattern F / S / S.
- **Stats:** Damage 4; durability 96; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/stone_spear.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Foundational tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 37. Chainsaw
- **Item ID:** `bedrock_expansion:chainsaw`
- **Display Name:** Chainsaw
- **Category:** Tools & Weapons
- **Tier:** 4 — Mythril
- **Purpose:** A powered wood harvester that consumes durability rapidly for speed.
- **Story/Lore:** The surviving inscription for Chainsaw names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Platinum Ingots + 2 Iron Ingots + 1 Copper Wire + 1 Stick; pattern PPI / PCW / __W, with _ empty.
- **Recipe:** 3 Platinum Ingots + 2 Iron Ingots + 1 Copper Wire + 1 Stick; pattern PPI / PCW / __W, with _ empty.
- **Stats:** Damage 8; durability 780; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/chainsaw.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** scripts/tools.js
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 38. Drill
- **Item ID:** `bedrock_expansion:drill`
- **Display Name:** Drill
- **Category:** Tools & Weapons
- **Tier:** 5 — Adamantite
- **Purpose:** A powered mining tool that clears stone quickly but needs Ember Dust fuel.
- **Story/Lore:** The surviving inscription for Drill names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Mythril Ingots + 2 Iron Ingots + 1 Copper Wire + 1 Ember Dust; pattern MIM / MCE / __M, with _ empty.
- **Recipe:** 3 Mythril Ingots + 2 Iron Ingots + 1 Copper Wire + 1 Ember Dust; pattern MIM / MCE / __M, with _ empty.
- **Stats:** Damage 9; durability 1100; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/drill.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** scripts/tools.js
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 39. Scythe
- **Item ID:** `bedrock_expansion:scythe`
- **Display Name:** Scythe
- **Category:** Tools & Weapons
- **Tier:** 3 — Platinum
- **Purpose:** A farming-and-combat hybrid that harvests a short arc of mature crops.
- **Story/Lore:** The surviving inscription for Scythe names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 2 Silver Ingots + 2 Sticks; pattern SS_ / _IS / _I_, with _ empty.
- **Recipe:** 2 Silver Ingots + 2 Sticks; pattern SS_ / _IS / _I_, with _ empty.
- **Stats:** Damage 7; durability 520; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/scythe.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 40. War Axe
- **Item ID:** `bedrock_expansion:war_axe`
- **Display Name:** War Axe
- **Category:** Tools & Weapons
- **Tier:** 5 — Adamantite
- **Purpose:** A deliberate shield-breaking weapon with high single-hit damage.
- **Story/Lore:** The surviving inscription for War Axe names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Adamantite Ingots + 2 Sticks; pattern AAA / ASA / __S, with _ empty.
- **Recipe:** 3 Adamantite Ingots + 2 Sticks; pattern AAA / ASA / __S, with _ empty.
- **Stats:** Damage 9; durability 1100; stack size 1. Tool-specific speed is granted by its script hook or vanilla-compatible component.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/war_axe.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 41. Copper Helmet
- **Item ID:** `bedrock_expansion:copper_helmet`
- **Display Name:** Copper Helmet
- **Category:** Armor & Wearables
- **Tier:** 1 — Copper/Tin
- **Purpose:** The copper helmet protects one body slot while expressing the copper/tin tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Copper Helmet names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M, with M=Copper Ingot -> Copper Helmet; 5 ingots.
- **Recipe:** Crafting table pattern MMM / M M, with M=Copper Ingot -> Copper Helmet; 5 ingots.
- **Stats:** Protection 2; durability 245; wearable slot armor.helmet; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_helmet.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 42. Copper Chestplate
- **Item ID:** `bedrock_expansion:copper_chestplate`
- **Display Name:** Copper Chestplate
- **Category:** Armor & Wearables
- **Tier:** 1 — Copper/Tin
- **Purpose:** The copper chestplate protects one body slot while expressing the copper/tin tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Copper Chestplate names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / MMM / MMM, with M=Copper Ingot -> Copper Chestplate; 8 ingots.
- **Recipe:** Crafting table pattern M M / MMM / MMM, with M=Copper Ingot -> Copper Chestplate; 8 ingots.
- **Stats:** Protection 6; durability 320; wearable slot armor.chestplate; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_chestplate.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 43. Copper Leggings
- **Item ID:** `bedrock_expansion:copper_leggings`
- **Display Name:** Copper Leggings
- **Category:** Armor & Wearables
- **Tier:** 1 — Copper/Tin
- **Purpose:** The copper leggings protects one body slot while expressing the copper/tin tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Copper Leggings names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M / M M, with M=Copper Ingot -> Copper Leggings; 7 ingots.
- **Recipe:** Crafting table pattern MMM / M M / M M, with M=Copper Ingot -> Copper Leggings; 7 ingots.
- **Stats:** Protection 5; durability 305; wearable slot armor.leggings; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_leggings.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 44. Copper Boots
- **Item ID:** `bedrock_expansion:copper_boots`
- **Display Name:** Copper Boots
- **Category:** Armor & Wearables
- **Tier:** 1 — Copper/Tin
- **Purpose:** The copper boots protects one body slot while expressing the copper/tin tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Copper Boots names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / M M, with M=Copper Ingot -> Copper Boots; 4 ingots.
- **Recipe:** Crafting table pattern M M / M M, with M=Copper Ingot -> Copper Boots; 4 ingots.
- **Stats:** Protection 2; durability 275; wearable slot armor.boots; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_boots.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 45. Silver Helmet
- **Item ID:** `bedrock_expansion:silver_helmet`
- **Display Name:** Silver Helmet
- **Category:** Armor & Wearables
- **Tier:** 2 — Silver
- **Purpose:** The silver helmet protects one body slot while expressing the silver tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Silver Helmet names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M, with M=Silver Ingot -> Silver Helmet; 5 ingots.
- **Recipe:** Crafting table pattern MMM / M M, with M=Silver Ingot -> Silver Helmet; 5 ingots.
- **Stats:** Protection 3; durability 325; wearable slot armor.helmet; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_helmet.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 46. Silver Chestplate
- **Item ID:** `bedrock_expansion:silver_chestplate`
- **Display Name:** Silver Chestplate
- **Category:** Armor & Wearables
- **Tier:** 2 — Silver
- **Purpose:** The silver chestplate protects one body slot while expressing the silver tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Silver Chestplate names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / MMM / MMM, with M=Silver Ingot -> Silver Chestplate; 8 ingots.
- **Recipe:** Crafting table pattern M M / MMM / MMM, with M=Silver Ingot -> Silver Chestplate; 8 ingots.
- **Stats:** Protection 7; durability 400; wearable slot armor.chestplate; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_chestplate.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 47. Silver Leggings
- **Item ID:** `bedrock_expansion:silver_leggings`
- **Display Name:** Silver Leggings
- **Category:** Armor & Wearables
- **Tier:** 2 — Silver
- **Purpose:** The silver leggings protects one body slot while expressing the silver tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Silver Leggings names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M / M M, with M=Silver Ingot -> Silver Leggings; 7 ingots.
- **Recipe:** Crafting table pattern MMM / M M / M M, with M=Silver Ingot -> Silver Leggings; 7 ingots.
- **Stats:** Protection 6; durability 385; wearable slot armor.leggings; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_leggings.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 48. Silver Boots
- **Item ID:** `bedrock_expansion:silver_boots`
- **Display Name:** Silver Boots
- **Category:** Armor & Wearables
- **Tier:** 2 — Silver
- **Purpose:** The silver boots protects one body slot while expressing the silver tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Silver Boots names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / M M, with M=Silver Ingot -> Silver Boots; 4 ingots.
- **Recipe:** Crafting table pattern M M / M M, with M=Silver Ingot -> Silver Boots; 4 ingots.
- **Stats:** Protection 3; durability 355; wearable slot armor.boots; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_boots.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 49. Platinum Helmet
- **Item ID:** `bedrock_expansion:platinum_helmet`
- **Display Name:** Platinum Helmet
- **Category:** Armor & Wearables
- **Tier:** 3 — Platinum
- **Purpose:** The platinum helmet protects one body slot while expressing the platinum tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Platinum Helmet names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M, with M=Platinum Ingot -> Platinum Helmet; 5 ingots.
- **Recipe:** Crafting table pattern MMM / M M, with M=Platinum Ingot -> Platinum Helmet; 5 ingots.
- **Stats:** Protection 4; durability 405; wearable slot armor.helmet; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_helmet.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 50. Platinum Chestplate
- **Item ID:** `bedrock_expansion:platinum_chestplate`
- **Display Name:** Platinum Chestplate
- **Category:** Armor & Wearables
- **Tier:** 3 — Platinum
- **Purpose:** The platinum chestplate protects one body slot while expressing the platinum tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Platinum Chestplate names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / MMM / MMM, with M=Platinum Ingot -> Platinum Chestplate; 8 ingots.
- **Recipe:** Crafting table pattern M M / MMM / MMM, with M=Platinum Ingot -> Platinum Chestplate; 8 ingots.
- **Stats:** Protection 8; durability 480; wearable slot armor.chestplate; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_chestplate.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 51. Platinum Leggings
- **Item ID:** `bedrock_expansion:platinum_leggings`
- **Display Name:** Platinum Leggings
- **Category:** Armor & Wearables
- **Tier:** 3 — Platinum
- **Purpose:** The platinum leggings protects one body slot while expressing the platinum tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Platinum Leggings names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M / M M, with M=Platinum Ingot -> Platinum Leggings; 7 ingots.
- **Recipe:** Crafting table pattern MMM / M M / M M, with M=Platinum Ingot -> Platinum Leggings; 7 ingots.
- **Stats:** Protection 7; durability 465; wearable slot armor.leggings; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_leggings.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 52. Platinum Boots
- **Item ID:** `bedrock_expansion:platinum_boots`
- **Display Name:** Platinum Boots
- **Category:** Armor & Wearables
- **Tier:** 3 — Platinum
- **Purpose:** The platinum boots protects one body slot while expressing the platinum tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Platinum Boots names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / M M, with M=Platinum Ingot -> Platinum Boots; 4 ingots.
- **Recipe:** Crafting table pattern M M / M M, with M=Platinum Ingot -> Platinum Boots; 4 ingots.
- **Stats:** Protection 4; durability 435; wearable slot armor.boots; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_boots.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 53. Mythril Helmet
- **Item ID:** `bedrock_expansion:mythril_helmet`
- **Display Name:** Mythril Helmet
- **Category:** Armor & Wearables
- **Tier:** 4 — Mythril
- **Purpose:** The mythril helmet protects one body slot while expressing the mythril tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Mythril Helmet names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M, with M=Mythril Ingot -> Mythril Helmet; 5 ingots.
- **Recipe:** Crafting table pattern MMM / M M, with M=Mythril Ingot -> Mythril Helmet; 5 ingots.
- **Stats:** Protection 5; durability 485; wearable slot armor.helmet; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_helmet.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 54. Mythril Chestplate
- **Item ID:** `bedrock_expansion:mythril_chestplate`
- **Display Name:** Mythril Chestplate
- **Category:** Armor & Wearables
- **Tier:** 4 — Mythril
- **Purpose:** The mythril chestplate protects one body slot while expressing the mythril tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Mythril Chestplate names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / MMM / MMM, with M=Mythril Ingot -> Mythril Chestplate; 8 ingots.
- **Recipe:** Crafting table pattern M M / MMM / MMM, with M=Mythril Ingot -> Mythril Chestplate; 8 ingots.
- **Stats:** Protection 9; durability 560; wearable slot armor.chestplate; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_chestplate.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 55. Mythril Leggings
- **Item ID:** `bedrock_expansion:mythril_leggings`
- **Display Name:** Mythril Leggings
- **Category:** Armor & Wearables
- **Tier:** 4 — Mythril
- **Purpose:** The mythril leggings protects one body slot while expressing the mythril tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Mythril Leggings names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M / M M, with M=Mythril Ingot -> Mythril Leggings; 7 ingots.
- **Recipe:** Crafting table pattern MMM / M M / M M, with M=Mythril Ingot -> Mythril Leggings; 7 ingots.
- **Stats:** Protection 8; durability 545; wearable slot armor.leggings; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_leggings.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 56. Mythril Boots
- **Item ID:** `bedrock_expansion:mythril_boots`
- **Display Name:** Mythril Boots
- **Category:** Armor & Wearables
- **Tier:** 4 — Mythril
- **Purpose:** The mythril boots protects one body slot while expressing the mythril tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Mythril Boots names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / M M, with M=Mythril Ingot -> Mythril Boots; 4 ingots.
- **Recipe:** Crafting table pattern M M / M M, with M=Mythril Ingot -> Mythril Boots; 4 ingots.
- **Stats:** Protection 5; durability 515; wearable slot armor.boots; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_boots.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 57. Adamantite Helmet
- **Item ID:** `bedrock_expansion:adamantite_helmet`
- **Display Name:** Adamantite Helmet
- **Category:** Armor & Wearables
- **Tier:** 5 — Adamantite
- **Purpose:** The adamantite helmet protects one body slot while expressing the adamantite tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Adamantite Helmet names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M, with M=Adamantite Ingot -> Adamantite Helmet; 5 ingots.
- **Recipe:** Crafting table pattern MMM / M M, with M=Adamantite Ingot -> Adamantite Helmet; 5 ingots.
- **Stats:** Protection 6; durability 565; wearable slot armor.helmet; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_helmet.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 58. Adamantite Chestplate
- **Item ID:** `bedrock_expansion:adamantite_chestplate`
- **Display Name:** Adamantite Chestplate
- **Category:** Armor & Wearables
- **Tier:** 5 — Adamantite
- **Purpose:** The adamantite chestplate protects one body slot while expressing the adamantite tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Adamantite Chestplate names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / MMM / MMM, with M=Adamantite Ingot -> Adamantite Chestplate; 8 ingots.
- **Recipe:** Crafting table pattern M M / MMM / MMM, with M=Adamantite Ingot -> Adamantite Chestplate; 8 ingots.
- **Stats:** Protection 10; durability 640; wearable slot armor.chestplate; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_chestplate.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 59. Adamantite Leggings
- **Item ID:** `bedrock_expansion:adamantite_leggings`
- **Display Name:** Adamantite Leggings
- **Category:** Armor & Wearables
- **Tier:** 5 — Adamantite
- **Purpose:** The adamantite leggings protects one body slot while expressing the adamantite tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Adamantite Leggings names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern MMM / M M / M M, with M=Adamantite Ingot -> Adamantite Leggings; 7 ingots.
- **Recipe:** Crafting table pattern MMM / M M / M M, with M=Adamantite Ingot -> Adamantite Leggings; 7 ingots.
- **Stats:** Protection 9; durability 625; wearable slot armor.leggings; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_leggings.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 60. Adamantite Boots
- **Item ID:** `bedrock_expansion:adamantite_boots`
- **Display Name:** Adamantite Boots
- **Category:** Armor & Wearables
- **Tier:** 5 — Adamantite
- **Purpose:** The adamantite boots protects one body slot while expressing the adamantite tier's signature trade-off.
- **Story/Lore:** The surviving inscription for Adamantite Boots names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table pattern M M / M M, with M=Adamantite Ingot -> Adamantite Boots; 4 ingots.
- **Recipe:** Crafting table pattern M M / M M, with M=Adamantite Ingot -> Adamantite Boots; 4 ingots.
- **Stats:** Protection 6; durability 595; wearable slot armor.boots; stack size 1.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_boots.png`
- **Model:** `item/handheld`
- **Sound:** item.equip.iron / random.break
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 61. Golden Apple Pie
- **Item ID:** `bedrock_expansion:golden_apple_pie`
- **Display Name:** Golden Apple Pie
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The golden apple pie is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Golden Apple Pie names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 3 Golden Apples + 3 Wheat + 1 Egg in a 3x3 pie pattern.
- **Recipe:** 3 Golden Apples + 3 Wheat + 1 Egg in a 3x3 pie pattern.
- **Stats:** Restores 5 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/golden_apple_pie.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 62. Copper Carrot
- **Item ID:** `bedrock_expansion:copper_carrot`
- **Display Name:** Copper Carrot
- **Category:** Food & Farming
- **Tier:** 1 — Copper/Tin
- **Purpose:** The copper carrot is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Copper Carrot names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Carrot + 1 Copper Nugget; roast on a campfire or craft shapeless.
- **Recipe:** 1 Carrot + 1 Copper Nugget; roast on a campfire or craft shapeless.
- **Stats:** Restores 4 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/copper_carrot.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 63. Silver Beetroot
- **Item ID:** `bedrock_expansion:silver_beetroot`
- **Display Name:** Silver Beetroot
- **Category:** Food & Farming
- **Tier:** 2 — Silver
- **Purpose:** The silver beetroot is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Silver Beetroot names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Beetroot + 1 Silver Ingot; silver-salted crop.
- **Recipe:** 1 Beetroot + 1 Silver Ingot; silver-salted crop.
- **Stats:** Restores 5 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/silver_beetroot.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 64. Platinum Potato
- **Item ID:** `bedrock_expansion:platinum_potato`
- **Display Name:** Platinum Potato
- **Category:** Food & Farming
- **Tier:** 3 — Platinum
- **Purpose:** The platinum potato is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Platinum Potato names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Potato + 1 Platinum Ingot; pressurized crop recipe.
- **Recipe:** 1 Potato + 1 Platinum Ingot; pressurized crop recipe.
- **Stats:** Restores 6 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/platinum_potato.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 65. Mythril Bread
- **Item ID:** `bedrock_expansion:mythril_bread`
- **Display Name:** Mythril Bread
- **Category:** Food & Farming
- **Tier:** 4 — Mythril
- **Purpose:** The mythril bread is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Mythril Bread names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 3 Wheat + 1 Mythril Ingot; light long-travel loaf.
- **Recipe:** 3 Wheat + 1 Mythril Ingot; light long-travel loaf.
- **Stats:** Restores 7 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/mythril_bread.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 66. Adamantite Stew
- **Item ID:** `bedrock_expansion:adamantite_stew`
- **Display Name:** Adamantite Stew
- **Category:** Food & Farming
- **Tier:** 5 — Adamantite
- **Purpose:** The adamantite stew is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Adamantite Stew names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Bowl + 1 Cooked Beef + 1 Adamantite Ingot + 1 Carrot.
- **Recipe:** 1 Bowl + 1 Cooked Beef + 1 Adamantite Ingot + 1 Carrot.
- **Stats:** Restores 10 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/adamantite_stew.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 67. Lumen Berry
- **Item ID:** `bedrock_expansion:lumen_berry`
- **Display Name:** Lumen Berry
- **Category:** Food & Farming
- **Tier:** 6 — Elemental / Void
- **Purpose:** The lumen berry is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Lumen Berry names the last Forge architects as its maker. It was designed after the Lumen Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Sweet Berry + 1 Lumen Crystal.
- **Recipe:** 1 Sweet Berry + 1 Lumen Crystal.
- **Stats:** Restores 9 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/lumen_berry.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 68. Ember Pepper
- **Item ID:** `bedrock_expansion:ember_pepper`
- **Display Name:** Ember Pepper
- **Category:** Food & Farming
- **Tier:** 6 — Elemental / Void
- **Purpose:** The ember pepper is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Ember Pepper names the last Forge architects as its maker. It was designed after the Ember Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Cocoa Bean + 1 Ember Dust.
- **Recipe:** 1 Cocoa Bean + 1 Ember Dust.
- **Stats:** Restores 9 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/ember_pepper.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 69. Frost Melon
- **Item ID:** `bedrock_expansion:frost_melon`
- **Display Name:** Frost Melon
- **Category:** Food & Farming
- **Tier:** 6 — Elemental / Void
- **Purpose:** The frost melon is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Frost Melon names the last Forge architects as its maker. It was designed after the Frost Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Melon Slice + 1 Frost Shard.
- **Recipe:** 1 Melon Slice + 1 Frost Shard.
- **Stats:** Restores 9 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/frost_melon.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 70. Storm Corn
- **Item ID:** `bedrock_expansion:storm_corn`
- **Display Name:** Storm Corn
- **Category:** Food & Farming
- **Tier:** 6 — Elemental / Void
- **Purpose:** The storm corn is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Storm Corn names the last Forge architects as its maker. It was designed after the Storm Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Wheat + 1 Storm Fragment.
- **Recipe:** 1 Wheat + 1 Storm Fragment.
- **Stats:** Restores 9 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/storm_corn.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 71. Void Fruit
- **Item ID:** `bedrock_expansion:void_fruit`
- **Display Name:** Void Fruit
- **Category:** Food & Farming
- **Tier:** 6 — Elemental / Void
- **Purpose:** The void fruit is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Void Fruit names the last Forge architects as its maker. It was designed after the Void changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Chorus Fruit + 1 Voidstone.
- **Recipe:** 1 Chorus Fruit + 1 Voidstone.
- **Stats:** Restores 9 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/void_fruit.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 72. Crystal Grapes
- **Item ID:** `bedrock_expansion:crystal_grapes`
- **Display Name:** Crystal Grapes
- **Category:** Food & Farming
- **Tier:** 3 — Platinum
- **Purpose:** The crystal grapes is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Crystal Grapes names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 3 Sweet Berries + 1 Amethyst Core.
- **Recipe:** 3 Sweet Berries + 1 Amethyst Core.
- **Stats:** Restores 6 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/crystal_grapes.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 73. Honey Cookie
- **Item ID:** `bedrock_expansion:honey_cookie`
- **Display Name:** Honey Cookie
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The honey cookie is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Honey Cookie names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 2 Wheat + 1 Honey Bottle.
- **Recipe:** 2 Wheat + 1 Honey Bottle.
- **Stats:** Restores 3 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/honey_cookie.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 74. Chocolate Bar
- **Item ID:** `bedrock_expansion:chocolate_bar`
- **Display Name:** Chocolate Bar
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The chocolate bar is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Chocolate Bar names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 2 Cocoa Beans + 1 Sugar.
- **Recipe:** 2 Cocoa Beans + 1 Sugar.
- **Stats:** Restores 3 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/chocolate_bar.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 75. Cheese Wheel
- **Item ID:** `bedrock_expansion:cheese_wheel`
- **Display Name:** Cheese Wheel
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The cheese wheel is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Cheese Wheel names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 3 Milk Buckets + 1 Salt substitute (Copper Nugget); returns 3 empty buckets.
- **Recipe:** 3 Milk Buckets + 1 Salt substitute (Copper Nugget); returns 3 empty buckets.
- **Stats:** Restores 3 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/cheese_wheel.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 76. Butter
- **Item ID:** `bedrock_expansion:butter`
- **Display Name:** Butter
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The butter is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Butter names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Milk Bucket + 1 Salt substitute (Tin Ingot); returns an empty bucket.
- **Recipe:** 1 Milk Bucket + 1 Salt substitute (Tin Ingot); returns an empty bucket.
- **Stats:** Restores 3 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/butter.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 77. Fried Egg
- **Item ID:** `bedrock_expansion:fried_egg`
- **Display Name:** Fried Egg
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The fried egg is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Fried Egg names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Egg + 1 Butter on a furnace or campfire.
- **Recipe:** 1 Egg + 1 Butter on a furnace or campfire.
- **Stats:** Restores 3 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/fried_egg.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 78. Bacon Strip
- **Item ID:** `bedrock_expansion:bacon_strip`
- **Display Name:** Bacon Strip
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The bacon strip is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Bacon Strip names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Raw Porkchop on a furnace or campfire.
- **Recipe:** 1 Raw Porkchop on a furnace or campfire.
- **Stats:** Restores 3 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/bacon_strip.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 79. Fish Stew
- **Item ID:** `bedrock_expansion:fish_stew`
- **Display Name:** Fish Stew
- **Category:** Food & Farming
- **Tier:** 0 — Foundational
- **Purpose:** The fish stew is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Fish Stew names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 1 Bowl + 1 Cooked Cod + 1 Carrot + 1 Mushroom.
- **Recipe:** 1 Bowl + 1 Cooked Cod + 1 Carrot + 1 Mushroom.
- **Stats:** Restores 3 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/fish_stew.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Nutrition is deliberately below the strongest vanilla food unless the ingredient is a rare realm drop; effects are short and low amplifier.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 80. Magic Cake
- **Item ID:** `bedrock_expansion:magic_cake`
- **Display Name:** Magic Cake
- **Category:** Food & Farming
- **Tier:** 6 — Elemental / Void
- **Purpose:** The magic cake is a purposeful ration: it restores a measured amount of hunger and supports a specific expedition condition.
- **Story/Lore:** The surviving inscription for Magic Cake names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Food crafting or cooking: 3 Wheat + 2 Lumen Crystals + 1 Egg + 1 Sugar in a cake pattern.
- **Recipe:** 3 Wheat + 2 Lumen Crystals + 1 Egg + 1 Sugar in a cake pattern.
- **Stats:** Restores 11 hunger points with measured saturation; stack size 16, except utility servings stack to 1 where a container is returned. Realm foods add a short, low-amplifier effect.
- **Interactions:** Use normally to eat; realm foods may grant one short effect and do not bypass the normal food timer.
- **Texture Path:** `textures/items/magic_cake.png`
- **Model:** `item/generated`
- **Sound:** entity.generic.eat / random.burp
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 81. Copper Block
- **Item ID:** `bedrock_expansion:copper_block`
- **Display Name:** Copper Block
- **Category:** Blocks & Building
- **Tier:** 1 — Copper/Tin
- **Purpose:** A placeable copper block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Copper Block names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Copper Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Copper Ingot in all nine slots -> 1 Copper Block.
- **Stats:** Placeable full cube; hardness 2.5; blast resistance 5; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 82. Silver Block
- **Item ID:** `bedrock_expansion:silver_block`
- **Display Name:** Silver Block
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable silver block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Silver Block names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Silver Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Silver Ingot in all nine slots -> 1 Silver Block.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 83. Platinum Block
- **Item ID:** `bedrock_expansion:platinum_block`
- **Display Name:** Platinum Block
- **Category:** Blocks & Building
- **Tier:** 3 — Platinum
- **Purpose:** A placeable platinum block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Platinum Block names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Platinum Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Platinum Ingot in all nine slots -> 1 Platinum Block.
- **Stats:** Placeable full cube; hardness 4.5; blast resistance 9; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/platinum_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 84. Mythril Block
- **Item ID:** `bedrock_expansion:mythril_block`
- **Display Name:** Mythril Block
- **Category:** Blocks & Building
- **Tier:** 4 — Mythril
- **Purpose:** A placeable mythril block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Mythril Block names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Mythril Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Mythril Ingot in all nine slots -> 1 Mythril Block.
- **Stats:** Placeable full cube; hardness 5.5; blast resistance 11; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mythril_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 85. Adamantite Block
- **Item ID:** `bedrock_expansion:adamantite_block`
- **Display Name:** Adamantite Block
- **Category:** Blocks & Building
- **Tier:** 5 — Adamantite
- **Purpose:** A placeable adamantite block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Adamantite Block names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Adamantite Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Adamantite Ingot in all nine slots -> 1 Adamantite Block.
- **Stats:** Placeable full cube; hardness 6.5; blast resistance 13; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/adamantite_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 86. Tin Block
- **Item ID:** `bedrock_expansion:tin_block`
- **Display Name:** Tin Block
- **Category:** Blocks & Building
- **Tier:** 1 — Copper/Tin
- **Purpose:** A placeable tin block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Tin Block names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Tin Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Tin Ingot in all nine slots -> 1 Tin Block.
- **Stats:** Placeable full cube; hardness 2.5; blast resistance 5; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/tin_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 87. Lumen Block
- **Item ID:** `bedrock_expansion:lumen_block`
- **Display Name:** Lumen Block
- **Category:** Blocks & Building
- **Tier:** 6 — Elemental / Void
- **Purpose:** A placeable lumen block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Lumen Block names the last Forge architects as its maker. It was designed after the Lumen Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Lumen Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Lumen Ingot in all nine slots -> 1 Lumen Block.
- **Stats:** Placeable full cube; hardness 7.5; blast resistance 15; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/lumen_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 88. Ember Block
- **Item ID:** `bedrock_expansion:ember_block`
- **Display Name:** Ember Block
- **Category:** Blocks & Building
- **Tier:** 6 — Elemental / Void
- **Purpose:** A placeable ember block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Ember Block names the last Forge architects as its maker. It was designed after the Ember Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Ember Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Ember Ingot in all nine slots -> 1 Ember Block.
- **Stats:** Placeable full cube; hardness 7.5; blast resistance 15; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/ember_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 89. Frost Block
- **Item ID:** `bedrock_expansion:frost_block`
- **Display Name:** Frost Block
- **Category:** Blocks & Building
- **Tier:** 6 — Elemental / Void
- **Purpose:** A placeable frost block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Frost Block names the last Forge architects as its maker. It was designed after the Frost Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Frost Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Frost Ingot in all nine slots -> 1 Frost Block.
- **Stats:** Placeable full cube; hardness 7.5; blast resistance 15; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/frost_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 90. Storm Block
- **Item ID:** `bedrock_expansion:storm_block`
- **Display Name:** Storm Block
- **Category:** Blocks & Building
- **Tier:** 6 — Elemental / Void
- **Purpose:** A placeable storm block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Storm Block names the last Forge architects as its maker. It was designed after the Storm Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Storm Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Storm Ingot in all nine slots -> 1 Storm Block.
- **Stats:** Placeable full cube; hardness 7.5; blast resistance 15; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/storm_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 91. Void Block
- **Item ID:** `bedrock_expansion:void_block`
- **Display Name:** Void Block
- **Category:** Blocks & Building
- **Tier:** 6 — Elemental / Void
- **Purpose:** A placeable void block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Void Block names the last Forge architects as its maker. It was designed after the Void changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Void Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Void Ingot in all nine slots -> 1 Void Block.
- **Stats:** Placeable full cube; hardness 7.5; blast resistance 15; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/void_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 92. Crystal Block
- **Item ID:** `bedrock_expansion:crystal_block`
- **Display Name:** Crystal Block
- **Category:** Blocks & Building
- **Tier:** 3 — Platinum
- **Purpose:** A placeable crystal block that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Crystal Block names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Crystal Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Crystal Ingot in all nine slots -> 1 Crystal Block.
- **Stats:** Placeable full cube; hardness 4.5; blast resistance 9; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/crystal_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 93. Reinforced Glass
- **Item ID:** `bedrock_expansion:reinforced_glass`
- **Display Name:** Reinforced Glass
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable reinforced glass that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Reinforced Glass names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Glass -> Reinforced Glass.
- **Recipe:** Pattern MMM / MCM / MMM, M=Glass and C=Copper Nugget -> Reinforced Glass.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/reinforced_glass.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 94. Dark Glass
- **Item ID:** `bedrock_expansion:dark_glass`
- **Display Name:** Dark Glass
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable dark glass that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Dark Glass names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Voidstone -> Dark Glass.
- **Recipe:** Pattern MMM / MCM / MMM, M=Voidstone and C=Copper Nugget -> Dark Glass.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/dark_glass.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 95. Glowing Concrete
- **Item ID:** `bedrock_expansion:glowing_concrete`
- **Display Name:** Glowing Concrete
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable glowing concrete that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Glowing Concrete names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Lumen Crystal -> Glowing Concrete.
- **Recipe:** Pattern MMM / MCM / MMM, M=Lumen Crystal and C=Copper Nugget -> Glowing Concrete.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/glowing_concrete.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 96. Mossy Bricks
- **Item ID:** `bedrock_expansion:mossy_bricks`
- **Display Name:** Mossy Bricks
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable mossy bricks that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Mossy Bricks names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Moss Block -> Mossy Bricks.
- **Recipe:** Pattern MMM / MCM / MMM, M=Moss Block and C=Copper Nugget -> Mossy Bricks.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/mossy_bricks.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 97. Cracked Bricks
- **Item ID:** `bedrock_expansion:cracked_bricks`
- **Display Name:** Cracked Bricks
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable cracked bricks that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Cracked Bricks names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Brick -> Cracked Bricks.
- **Recipe:** Pattern MMM / MCM / MMM, M=Brick and C=Copper Nugget -> Cracked Bricks.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/cracked_bricks.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 98. Marble
- **Item ID:** `bedrock_expansion:marble`
- **Display Name:** Marble
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable marble that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Marble names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Quartz Block -> Marble.
- **Recipe:** Pattern MMM / MCM / MMM, M=Quartz Block and C=Copper Nugget -> Marble.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/marble.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 99. Polished Marble
- **Item ID:** `bedrock_expansion:polished_marble`
- **Display Name:** Polished Marble
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable polished marble that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Polished Marble names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Marble -> Polished Marble.
- **Recipe:** Pattern MMM / MCM / MMM, M=Marble and C=Copper Nugget -> Polished Marble.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/polished_marble.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 100. Limestone
- **Item ID:** `bedrock_expansion:limestone`
- **Display Name:** Limestone
- **Category:** Blocks & Building
- **Tier:** 2 — Silver
- **Purpose:** A placeable limestone that gives the rebuilt Forge a distinct structural, lighting, or defensive function.
- **Story/Lore:** The surviving inscription for Limestone names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: 8 of the first ingredient and 1 Copper Nugget in the center; base=Calcite -> Limestone.
- **Recipe:** Pattern MMM / MCM / MMM, M=Calcite and C=Copper Nugget -> Limestone.
- **Stats:** Placeable full cube; hardness 3.5; blast resistance 7; stack size 64. Special light/transparency behavior is declared in the block JSON.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/limestone.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 101. Copper Wire
- **Item ID:** `bedrock_expansion:copper_wire`
- **Display Name:** Copper Wire
- **Category:** Redstone & Tech
- **Tier:** 1 — Copper/Tin
- **Purpose:** A placeable copper wire that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Copper Wire names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Copper Nuggets + 1 String in a line.
- **Recipe:** 3 Copper Nuggets + 1 String in a line.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/copper_wire.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 102. Silver Wire
- **Item ID:** `bedrock_expansion:silver_wire`
- **Display Name:** Silver Wire
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable silver wire that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Silver Wire names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Silver Nuggets + 1 String in a line.
- **Recipe:** 3 Silver Nuggets + 1 String in a line.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/silver_wire.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 103. Logic Gate
- **Item ID:** `bedrock_expansion:logic_gate`
- **Display Name:** Logic Gate
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable logic gate that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Logic Gate names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Copper Wire + 2 Redstone + 1 Silver Ingot.
- **Recipe:** 3 Copper Wire + 2 Redstone + 1 Silver Ingot.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/logic_gate.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 104. Timer Block
- **Item ID:** `bedrock_expansion:timer_block`
- **Display Name:** Timer Block
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable timer block that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Timer Block names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Timer Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Timer Ingot in all nine slots -> 1 Timer Block.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/timer_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 105. Pulse Extender
- **Item ID:** `bedrock_expansion:pulse_extender`
- **Display Name:** Pulse Extender
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable pulse extender that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Pulse Extender names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 2 Copper Wire + 2 Repeaters + 1 Tin Ingot.
- **Recipe:** 2 Copper Wire + 2 Repeaters + 1 Tin Ingot.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/pulse_extender.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 106. Item Pipe
- **Item ID:** `bedrock_expansion:item_pipe`
- **Display Name:** Item Pipe
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable item pipe that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Item Pipe names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 6 Copper Ingots + 1 Glass + 1 Iron Ingot.
- **Recipe:** 6 Copper Ingots + 1 Glass + 1 Iron Ingot.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/item_pipe.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 107. Fluid Pipe
- **Item ID:** `bedrock_expansion:fluid_pipe`
- **Display Name:** Fluid Pipe
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable fluid pipe that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Fluid Pipe names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 6 Tin Ingots + 1 Glass + 1 Iron Ingot.
- **Recipe:** 6 Tin Ingots + 1 Glass + 1 Iron Ingot.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/fluid_pipe.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 108. Energy Cable
- **Item ID:** `bedrock_expansion:energy_cable`
- **Display Name:** Energy Cable
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable energy cable that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Energy Cable names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 6 Silver Wire + 1 Redstone Block + 1 Copper Ingot.
- **Recipe:** 6 Silver Wire + 1 Redstone Block + 1 Copper Ingot.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/energy_cable.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 109. Solar Panel
- **Item ID:** `bedrock_expansion:solar_panel`
- **Display Name:** Solar Panel
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable solar panel that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Solar Panel names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Lumen Crystals + 3 Glass + 1 Silver Wire.
- **Recipe:** 3 Lumen Crystals + 3 Glass + 1 Silver Wire.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/solar_panel.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 110. Battery
- **Item ID:** `bedrock_expansion:battery`
- **Display Name:** Battery
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable battery that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Battery names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 2 Silver Ingots + 2 Redstone + 1 Copper Wire.
- **Recipe:** 2 Silver Ingots + 2 Redstone + 1 Copper Wire.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/battery.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 111. Generator
- **Item ID:** `bedrock_expansion:generator`
- **Display Name:** Generator
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable generator that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Generator names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Iron Ingots + 2 Ember Dust + 1 Furnace + 1 Battery.
- **Recipe:** 3 Iron Ingots + 2 Ember Dust + 1 Furnace + 1 Battery.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/generator.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 112. Electric Furnace
- **Item ID:** `bedrock_expansion:electric_furnace`
- **Display Name:** Electric Furnace
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable electric furnace that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Electric Furnace names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 5 Iron Ingots + 2 Energy Cables + 1 Furnace + 1 Silver Wire.
- **Recipe:** 5 Iron Ingots + 2 Energy Cables + 1 Furnace + 1 Silver Wire.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/electric_furnace.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 113. Auto Crafting Table
- **Item ID:** `bedrock_expansion:auto_crafting_table`
- **Display Name:** Auto Crafting Table
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable auto crafting table that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Auto Crafting Table names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 4 Platinum Ingots + 2 Logic Gates + 1 Crafting Table + 1 Computer.
- **Recipe:** 4 Platinum Ingots + 2 Logic Gates + 1 Crafting Table + 1 Computer.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/auto_crafting_table.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 114. Conveyor Belt
- **Item ID:** `bedrock_expansion:conveyor_belt`
- **Display Name:** Conveyor Belt
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable conveyor belt that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Conveyor Belt names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Leather + 2 Iron Ingots + 2 Copper Wire.
- **Recipe:** 3 Leather + 2 Iron Ingots + 2 Copper Wire.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/conveyor_belt.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 115. Robot Arm
- **Item ID:** `bedrock_expansion:robot_arm`
- **Display Name:** Robot Arm
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable robot arm that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Robot Arm names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table: 3 Platinum Ingots + 2 Energy Cables + 1 Logic Gate.
- **Recipe:** 3 Platinum Ingots + 2 Energy Cables + 1 Logic Gate.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/robot_arm.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 116. Sensor Block
- **Item ID:** `bedrock_expansion:sensor_block`
- **Display Name:** Sensor Block
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable sensor block that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Sensor Block names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Sensor Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Sensor Ingot in all nine slots -> 1 Sensor Block.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/sensor_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 117. Speaker Block
- **Item ID:** `bedrock_expansion:speaker_block`
- **Display Name:** Speaker Block
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable speaker block that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Speaker Block names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Speaker Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Speaker Ingot in all nine slots -> 1 Speaker Block.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/speaker_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 118. Monitor Block
- **Item ID:** `bedrock_expansion:monitor_block`
- **Display Name:** Monitor Block
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable monitor block that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Monitor Block names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Monitor Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Monitor Ingot in all nine slots -> 1 Monitor Block.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/monitor_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 119. Keyboard Block
- **Item ID:** `bedrock_expansion:keyboard_block`
- **Display Name:** Keyboard Block
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable keyboard block that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Keyboard Block names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Keyboard Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Keyboard Ingot in all nine slots -> 1 Keyboard Block.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/keyboard_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 120. Computer Block
- **Item ID:** `bedrock_expansion:computer_block`
- **Display Name:** Computer Block
- **Category:** Redstone & Tech
- **Tier:** 2 — Silver
- **Purpose:** A placeable computer block that contributes one readable step to the Forge automation chain.
- **Story/Lore:** The surviving inscription for Computer Block names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 9 Computer Ingot in a full 3x3 grid; the block can be reclaimed into 9 ingots.
- **Recipe:** 3x3: Computer Ingot in all nine slots -> 1 Computer Block.
- **Stats:** Placeable machine block; stack size 64; consumes or transmits one clearly documented signal/energy unit and has no autonomous item duplication.
- **Interactions:** Place, then use or power with redstone; the tech script reports the block's channel without faking item duplication.
- **Texture Path:** `textures/items/computer_block.png`
- **Model:** `block/full_cube`
- **Sound:** dig.stone / step.stone
- **Script Hooks:** scripts/tech.js
- **Balance Notes:** Automation is one-input/one-output and energy-limited; the add-on avoids free item generation and does not alter vanilla redstone rules.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 121. Mana Crystal
- **Item ID:** `bedrock_expansion:mana_crystal`
- **Display Name:** Mana Crystal
- **Category:** Magic & Enchanting
- **Tier:** 3 — Platinum
- **Purpose:** The mana crystal converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Mana Crystal names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 4 Lumen Crystals around 1 Amethyst Core.
- **Recipe:** 4 Lumen Crystals around 1 Amethyst Core.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/mana_crystal.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 122. Spell Book
- **Item ID:** `bedrock_expansion:spell_book`
- **Display Name:** Spell Book
- **Category:** Magic & Enchanting
- **Tier:** 3 — Platinum
- **Purpose:** The spell book converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Spell Book names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 3 Paper + 1 Leather + 1 Mana Crystal.
- **Recipe:** 3 Paper + 1 Leather + 1 Mana Crystal.
- **Stats:** Stack size 1; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/spell_book.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 123. Fire Spell
- **Item ID:** `bedrock_expansion:fire_spell`
- **Display Name:** Fire Spell
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The fire spell converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Fire Spell names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Spell Book + 1 Ember Dust + 1 Rune Stone.
- **Recipe:** 1 Spell Book + 1 Ember Dust + 1 Rune Stone.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/fire_spell.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 124. Ice Spell
- **Item ID:** `bedrock_expansion:ice_spell`
- **Display Name:** Ice Spell
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The ice spell converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Ice Spell names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Spell Book + 1 Frost Shard + 1 Rune Stone.
- **Recipe:** 1 Spell Book + 1 Frost Shard + 1 Rune Stone.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/ice_spell.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 125. Lightning Spell
- **Item ID:** `bedrock_expansion:lightning_spell`
- **Display Name:** Lightning Spell
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The lightning spell converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Lightning Spell names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Spell Book + 1 Storm Fragment + 1 Rune Stone.
- **Recipe:** 1 Spell Book + 1 Storm Fragment + 1 Rune Stone.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/lightning_spell.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 126. Healing Spell
- **Item ID:** `bedrock_expansion:healing_spell`
- **Display Name:** Healing Spell
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The healing spell converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Healing Spell names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Spell Book + 1 Lumen Crystal + 1 Golden Apple.
- **Recipe:** 1 Spell Book + 1 Lumen Crystal + 1 Golden Apple.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/healing_spell.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 127. Teleport Spell
- **Item ID:** `bedrock_expansion:teleport_spell`
- **Display Name:** Teleport Spell
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The teleport spell converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Teleport Spell names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Spell Book + 1 Void Pearl + 1 Ender Pearl.
- **Recipe:** 1 Spell Book + 1 Void Pearl + 1 Ender Pearl.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/teleport_spell.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 128. Shield Spell
- **Item ID:** `bedrock_expansion:shield_spell`
- **Display Name:** Shield Spell
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The shield spell converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Shield Spell names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Spell Book + 1 Adamantite Ingot + 1 Lumen Crystal.
- **Recipe:** 1 Spell Book + 1 Adamantite Ingot + 1 Lumen Crystal.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/shield_spell.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 129. Summon Spell
- **Item ID:** `bedrock_expansion:summon_spell`
- **Display Name:** Summon Spell
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The summon spell converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Summon Spell names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Spell Book + 1 Soul Gem + 1 mob core.
- **Recipe:** 1 Spell Book + 1 Soul Gem + 1 mob core.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/summon_spell.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 130. Enchantment Orb
- **Item ID:** `bedrock_expansion:enchantment_orb`
- **Display Name:** Enchantment Orb
- **Category:** Magic & Enchanting
- **Tier:** 3 — Platinum
- **Purpose:** The enchantment orb converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Enchantment Orb names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Amethyst Core + 4 Lumen Dust.
- **Recipe:** 1 Amethyst Core + 4 Lumen Dust.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/enchantment_orb.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 131. Rune Stone
- **Item ID:** `bedrock_expansion:rune_stone`
- **Display Name:** Rune Stone
- **Category:** Magic & Enchanting
- **Tier:** 3 — Platinum
- **Purpose:** The rune stone converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Rune Stone names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Stone + 1 Nether Quartz Shard + 1 Lumen Dust.
- **Recipe:** 1 Stone + 1 Nether Quartz Shard + 1 Lumen Dust.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/rune_stone.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 132. Magic Wand
- **Item ID:** `bedrock_expansion:magic_wand`
- **Display Name:** Magic Wand
- **Category:** Magic & Enchanting
- **Tier:** 3 — Platinum
- **Purpose:** The magic wand converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Magic Wand names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Stick + 1 Mana Crystal + 1 Rune Stone.
- **Recipe:** 1 Stick + 1 Mana Crystal + 1 Rune Stone.
- **Stats:** Stack size 1; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/magic_wand.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 133. Staff of Fire
- **Item ID:** `bedrock_expansion:staff_of_fire`
- **Display Name:** Staff of Fire
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The staff of fire converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Staff of Fire names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Magic Wand + 2 Ember Dust + 1 Blaze Rod.
- **Recipe:** 1 Magic Wand + 2 Ember Dust + 1 Blaze Rod.
- **Stats:** Stack size 1; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/staff_of_fire.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 134. Staff of Ice
- **Item ID:** `bedrock_expansion:staff_of_ice`
- **Display Name:** Staff of Ice
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The staff of ice converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Staff of Ice names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Magic Wand + 2 Frost Shards + 1 Packed Ice.
- **Recipe:** 1 Magic Wand + 2 Frost Shards + 1 Packed Ice.
- **Stats:** Stack size 1; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/staff_of_ice.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 135. Staff of Storms
- **Item ID:** `bedrock_expansion:staff_of_storms`
- **Display Name:** Staff of Storms
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The staff of storms converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Staff of Storms names the last Forge architects as its maker. It was designed after the Storm Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Magic Wand + 2 Storm Fragments + 1 Lightning Rod.
- **Recipe:** 1 Magic Wand + 2 Storm Fragments + 1 Lightning Rod.
- **Stats:** Stack size 1; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/staff_of_storms.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 136. Staff of Life
- **Item ID:** `bedrock_expansion:staff_of_life`
- **Display Name:** Staff of Life
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The staff of life converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Staff of Life names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Magic Wand + 2 Lumen Crystals + 1 Golden Apple.
- **Recipe:** 1 Magic Wand + 2 Lumen Crystals + 1 Golden Apple.
- **Stats:** Stack size 1; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/staff_of_life.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** scripts/magic.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 137. Soul Gem
- **Item ID:** `bedrock_expansion:soul_gem`
- **Display Name:** Soul Gem
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The soul gem converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Soul Gem names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Amethyst Core + 1 Ghast Tear + 2 Soul Sand.
- **Recipe:** 1 Amethyst Core + 1 Ghast Tear + 2 Soul Sand.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/soul_gem.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 138. Void Pearl
- **Item ID:** `bedrock_expansion:void_pearl`
- **Display Name:** Void Pearl
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The void pearl converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Void Pearl names the last Forge architects as its maker. It was designed after the Void changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Ender Pearl + 2 Voidstone.
- **Recipe:** 1 Ender Pearl + 2 Voidstone.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/void_pearl.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 139. Celestial Shard
- **Item ID:** `bedrock_expansion:celestial_shard`
- **Display Name:** Celestial Shard
- **Category:** Magic & Enchanting
- **Tier:** 6 — Elemental / Void
- **Purpose:** The celestial shard converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Celestial Shard names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 1 Lumen Crystal + 1 Storm Fragment + 1 Nether Star fragment.
- **Recipe:** 1 Lumen Crystal + 1 Storm Fragment + 1 Nether Star fragment.
- **Stats:** Stack size 16; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/celestial_shard.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 140. Alchemy Table
- **Item ID:** `bedrock_expansion:alchemy_table`
- **Display Name:** Alchemy Table
- **Category:** Magic & Enchanting
- **Tier:** 3 — Platinum
- **Purpose:** The alchemy table converts stored realm energy into one controlled magical action.
- **Story/Lore:** The surviving inscription for Alchemy Table names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Arcane crafting: 4 Platinum Ingots + 2 Rune Stones + 1 Brewing Stand + 1 Amethyst Core.
- **Recipe:** 4 Platinum Ingots + 2 Rune Stones + 1 Brewing Stand + 1 Amethyst Core.
- **Stats:** Stack size 1; effect costs 5-30 mana-equivalent charge and observes a cooldown.
- **Interactions:** Use to spend a scripted mana-equivalent charge and apply the spell effect; sneak-use is reserved for the alternate targeting mode.
- **Texture Path:** `textures/items/alchemy_table.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / block.enchantment_table.use
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 141. Copper Golem Spawn Egg
- **Item ID:** `bedrock_expansion:copper_golem_spawn_egg`
- **Display Name:** Copper Golem Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The copper golem spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Copper Golem Spawn Egg names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Copper Golem Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Copper Golem Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/copper_golem_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 142. Silver Golem Spawn Egg
- **Item ID:** `bedrock_expansion:silver_golem_spawn_egg`
- **Display Name:** Silver Golem Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The silver golem spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Silver Golem Spawn Egg names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Silver Golem Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Silver Golem Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/silver_golem_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 143. Crystal Golem Spawn Egg
- **Item ID:** `bedrock_expansion:crystal_golem_spawn_egg`
- **Display Name:** Crystal Golem Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 5 — Adamantite
- **Purpose:** The crystal golem spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Crystal Golem Spawn Egg names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Crystal Golem Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Crystal Golem Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/crystal_golem_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 144. Void Golem Spawn Egg
- **Item ID:** `bedrock_expansion:void_golem_spawn_egg`
- **Display Name:** Void Golem Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 6 — Elemental / Void
- **Purpose:** The void golem spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Void Golem Spawn Egg names the last Forge architects as its maker. It was designed after the Void changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Void Golem Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Void Golem Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/void_golem_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 145. Ember Imp Spawn Egg
- **Item ID:** `bedrock_expansion:ember_imp_spawn_egg`
- **Display Name:** Ember Imp Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 4 — Mythril
- **Purpose:** The ember imp spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Ember Imp Spawn Egg names the Mythril Wayfarers as its maker. It was designed after the Ember Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Ember Imp Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Ember Imp Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/ember_imp_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 146. Frost Wolf Spawn Egg
- **Item ID:** `bedrock_expansion:frost_wolf_spawn_egg`
- **Display Name:** Frost Wolf Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 4 — Mythril
- **Purpose:** The frost wolf spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Frost Wolf Spawn Egg names the Mythril Wayfarers as its maker. It was designed after the Frost Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Frost Wolf Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Frost Wolf Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/frost_wolf_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 147. Storm Eagle Spawn Egg
- **Item ID:** `bedrock_expansion:storm_eagle_spawn_egg`
- **Display Name:** Storm Eagle Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 5 — Adamantite
- **Purpose:** The storm eagle spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Storm Eagle Spawn Egg names the Adamantite Wardens as its maker. It was designed after the Storm Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Storm Eagle Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Storm Eagle Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/storm_eagle_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 148. Lumen Fairy Spawn Egg
- **Item ID:** `bedrock_expansion:lumen_fairy_spawn_egg`
- **Display Name:** Lumen Fairy Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 6 — Elemental / Void
- **Purpose:** The lumen fairy spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Lumen Fairy Spawn Egg names the last Forge architects as its maker. It was designed after the Lumen Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Lumen Fairy Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Lumen Fairy Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/lumen_fairy_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 149. Cave Lurker Spawn Egg
- **Item ID:** `bedrock_expansion:cave_lurker_spawn_egg`
- **Display Name:** Cave Lurker Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The cave lurker spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Cave Lurker Spawn Egg names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Cave Lurker Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Cave Lurker Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/cave_lurker_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 150. Deep Crab Spawn Egg
- **Item ID:** `bedrock_expansion:deep_crab_spawn_egg`
- **Display Name:** Deep Crab Spawn Egg
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The deep crab spawn egg is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Deep Crab Spawn Egg names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Craft 1 Egg with the matching Deep Crab Core or realm essence; alternatively find it in a Forge vault.
- **Recipe:** Shapeless: 1 Egg + 1 matching core/essence -> 1 Deep Crab Spawn Egg.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use on a block to call the matching custom entity through minecraft:entity_placer.
- **Texture Path:** `textures/items/deep_crab_spawn_egg.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 151. Copper Golem Core
- **Item ID:** `bedrock_expansion:copper_golem_core`
- **Display Name:** Copper Golem Core
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The copper golem core is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Copper Golem Core names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Copper Golem Core is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/copper_golem_core.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 152. Silver Golem Core
- **Item ID:** `bedrock_expansion:silver_golem_core`
- **Display Name:** Silver Golem Core
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The silver golem core is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Silver Golem Core names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Silver Golem Core is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/silver_golem_core.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 153. Crystal Golem Core
- **Item ID:** `bedrock_expansion:crystal_golem_core`
- **Display Name:** Crystal Golem Core
- **Category:** Mobs & Drops
- **Tier:** 5 — Adamantite
- **Purpose:** The crystal golem core is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Crystal Golem Core names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Crystal Golem Core is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/crystal_golem_core.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 154. Void Golem Core
- **Item ID:** `bedrock_expansion:void_golem_core`
- **Display Name:** Void Golem Core
- **Category:** Mobs & Drops
- **Tier:** 6 — Elemental / Void
- **Purpose:** The void golem core is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Void Golem Core names the last Forge architects as its maker. It was designed after the Void changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Void Golem Core is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/void_golem_core.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 155. Ember Essence
- **Item ID:** `bedrock_expansion:ember_essence`
- **Display Name:** Ember Essence
- **Category:** Mobs & Drops
- **Tier:** 4 — Mythril
- **Purpose:** The ember essence is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Ember Essence names the Mythril Wayfarers as its maker. It was designed after the Ember Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Ember Essence is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/ember_essence.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 156. Frost Fur
- **Item ID:** `bedrock_expansion:frost_fur`
- **Display Name:** Frost Fur
- **Category:** Mobs & Drops
- **Tier:** 4 — Mythril
- **Purpose:** The frost fur is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Frost Fur names the Mythril Wayfarers as its maker. It was designed after the Frost Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Frost Fur is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/frost_fur.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 157. Storm Feather
- **Item ID:** `bedrock_expansion:storm_feather`
- **Display Name:** Storm Feather
- **Category:** Mobs & Drops
- **Tier:** 5 — Adamantite
- **Purpose:** The storm feather is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Storm Feather names the Adamantite Wardens as its maker. It was designed after the Storm Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Storm Feather is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/storm_feather.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 158. Lumen Dust
- **Item ID:** `bedrock_expansion:lumen_dust`
- **Display Name:** Lumen Dust
- **Category:** Mobs & Drops
- **Tier:** 6 — Elemental / Void
- **Purpose:** The lumen dust is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Lumen Dust names the last Forge architects as its maker. It was designed after the Lumen Realm changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Lumen Dust is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/lumen_dust.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 159. Lurker Eye
- **Item ID:** `bedrock_expansion:lurker_eye`
- **Display Name:** Lurker Eye
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The lurker eye is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Lurker Eye names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Lurker Eye is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/lurker_eye.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 160. Crab Claw
- **Item ID:** `bedrock_expansion:crab_claw`
- **Display Name:** Crab Claw
- **Category:** Mobs & Drops
- **Tier:** 2 — Silver
- **Purpose:** The crab claw is a deliberate encounter or drop that connects a creature to the realm economy.
- **Story/Lore:** The surviving inscription for Crab Claw names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Drop from the matching Bedrock Expansion creature, chest, or realm event; Crab Claw is not craftable.
- **Recipe:** No recipe: creature drop, rare chest, or boss reward.
- **Stats:** Spawn eggs stack to 16; creature drops stack to 64. Encounter drops are chance-limited by the related loot table.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/crab_claw.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Spawn eggs consume a rare core or essence and custom creatures use modest health and drop rates so farms cannot flood progression.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 161. Wooden Chair
- **Item ID:** `bedrock_expansion:wooden_chair`
- **Display Name:** Wooden Chair
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The wooden chair makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Wooden Chair names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Wooden Chair.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Wooden Chair; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/wooden_chair.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 162. Wooden Table
- **Item ID:** `bedrock_expansion:wooden_table`
- **Display Name:** Wooden Table
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The wooden table makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Wooden Table names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Wooden Table.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Wooden Table; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/wooden_table.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 163. Wooden Bed
- **Item ID:** `bedrock_expansion:wooden_bed`
- **Display Name:** Wooden Bed
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The wooden bed makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Wooden Bed names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Wooden Bed.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Wooden Bed; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/wooden_bed.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 164. Sofa
- **Item ID:** `bedrock_expansion:sofa`
- **Display Name:** Sofa
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The sofa makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Sofa names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Sofa.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Sofa; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/sofa.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 165. Bookshelf
- **Item ID:** `bedrock_expansion:bookshelf`
- **Display Name:** Bookshelf
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The bookshelf makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Bookshelf names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Bookshelf.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Bookshelf; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/bookshelf.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 166. Lamp
- **Item ID:** `bedrock_expansion:lamp`
- **Display Name:** Lamp
- **Category:** Decoration & Furniture
- **Tier:** 1 — Copper/Tin
- **Purpose:** The lamp makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Lamp names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Lamp.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Lamp; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/lamp.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 167. Ceiling Light
- **Item ID:** `bedrock_expansion:ceiling_light`
- **Display Name:** Ceiling Light
- **Category:** Decoration & Furniture
- **Tier:** 1 — Copper/Tin
- **Purpose:** The ceiling light makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Ceiling Light names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Ceiling Light.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Ceiling Light; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/ceiling_light.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 168. Wall Clock
- **Item ID:** `bedrock_expansion:wall_clock`
- **Display Name:** Wall Clock
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The wall clock makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Wall Clock names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Wall Clock.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Wall Clock; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/wall_clock.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 169. Painting Frame
- **Item ID:** `bedrock_expansion:painting_frame`
- **Display Name:** Painting Frame
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The painting frame makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Painting Frame names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Painting Frame.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Painting Frame; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/painting_frame.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 170. Vase
- **Item ID:** `bedrock_expansion:vase`
- **Display Name:** Vase
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The vase makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Vase names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Vase.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Vase; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/vase.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 171. Large Flower Pot
- **Item ID:** `bedrock_expansion:large_flower_pot`
- **Display Name:** Large Flower Pot
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The large flower pot makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Large Flower Pot names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Large Flower Pot.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Large Flower Pot; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/large_flower_pot.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 172. Rug
- **Item ID:** `bedrock_expansion:rug`
- **Display Name:** Rug
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The rug makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Rug names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Rug.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Rug; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/rug.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 173. Curtain
- **Item ID:** `bedrock_expansion:curtain`
- **Display Name:** Curtain
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The curtain makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Curtain names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Curtain.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Curtain; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/curtain.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 174. Fireplace
- **Item ID:** `bedrock_expansion:fireplace`
- **Display Name:** Fireplace
- **Category:** Decoration & Furniture
- **Tier:** 1 — Copper/Tin
- **Purpose:** The fireplace makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Fireplace names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Fireplace.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Fireplace; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/fireplace.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 175. Kitchen Counter
- **Item ID:** `bedrock_expansion:kitchen_counter`
- **Display Name:** Kitchen Counter
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The kitchen counter makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Kitchen Counter names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Kitchen Counter.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Kitchen Counter; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/kitchen_counter.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 176. Oven
- **Item ID:** `bedrock_expansion:oven`
- **Display Name:** Oven
- **Category:** Decoration & Furniture
- **Tier:** 1 — Copper/Tin
- **Purpose:** The oven makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Oven names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Oven.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Oven; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/oven.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 177. Refrigerator
- **Item ID:** `bedrock_expansion:refrigerator`
- **Display Name:** Refrigerator
- **Category:** Decoration & Furniture
- **Tier:** 1 — Copper/Tin
- **Purpose:** The refrigerator makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Refrigerator names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Refrigerator.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Refrigerator; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/refrigerator.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 178. Toilet
- **Item ID:** `bedrock_expansion:toilet`
- **Display Name:** Toilet
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The toilet makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Toilet names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Toilet.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Toilet; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/toilet.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 179. Bathtub
- **Item ID:** `bedrock_expansion:bathtub`
- **Display Name:** Bathtub
- **Category:** Decoration & Furniture
- **Tier:** 0 — Foundational
- **Purpose:** The bathtub makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Bathtub names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Bathtub.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Bathtub; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/bathtub.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Foundational stage and points toward Copper/Tin through its material, recipe, or realm hook.

### 180. Sink
- **Item ID:** `bedrock_expansion:sink`
- **Display Name:** Sink
- **Category:** Decoration & Furniture
- **Tier:** 1 — Copper/Tin
- **Purpose:** The sink makes a restored Forge room legible while offering a small atmosphere or organization benefit.
- **Story/Lore:** The surviving inscription for Sink names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Crafting table 3x3: P P P / S W S / _ S _, where P=Oak Planks, S=Stick, W=White Wool, and _ is empty -> Sink.
- **Recipe:** Exact furniture recipe: 3 Oak Planks + 3 Sticks + 1 White Wool in the stated grid -> Sink; the item identity determines its room role.
- **Stats:** Stack size 64; decorative tokens use no combat damage and are intentionally light on resource cost.
- **Interactions:** Use, place, mine, equip, or craft according to its vanilla-compatible component set; no hidden alternate action is required.
- **Texture Path:** `textures/items/sink.png`
- **Model:** `item/generated`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** Decoration is inexpensive and non-combat so building style is a reward rather than a hidden power spike.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 181. Backpack
- **Item ID:** `bedrock_expansion:backpack`
- **Display Name:** Backpack
- **Category:** Utility & Adventure
- **Tier:** 2 — Silver
- **Purpose:** The backpack solves a specific exploration problem at the silver stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Backpack names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 4 Leather + 2 Silver Ingots + 1 Chest.
- **Recipe:** 4 Leather + 2 Silver Ingots + 1 Chest.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use to register a portable storage channel; the script gives a clear storage message. A chest-backed inventory is recommended for production worlds.
- **Texture Path:** `textures/items/backpack.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/backpack.js
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 182. Large Backpack
- **Item ID:** `bedrock_expansion:large_backpack`
- **Display Name:** Large Backpack
- **Category:** Utility & Adventure
- **Tier:** 3 — Platinum
- **Purpose:** The large backpack solves a specific exploration problem at the platinum stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Large Backpack names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 4 Leather + 2 Platinum Ingots + 1 Backpack + 1 Chest.
- **Recipe:** 4 Leather + 2 Platinum Ingots + 1 Backpack + 1 Chest.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use to register a portable storage channel; the script gives a clear storage message. A chest-backed inventory is recommended for production worlds.
- **Texture Path:** `textures/items/large_backpack.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/backpack.js
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 183. Ender Backpack
- **Item ID:** `bedrock_expansion:ender_backpack`
- **Display Name:** Ender Backpack
- **Category:** Utility & Adventure
- **Tier:** 6 — Elemental / Void
- **Purpose:** The ender backpack solves a specific exploration problem at the elemental / void stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Ender Backpack names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 4 Leather + 2 Void Pearls + 1 Ender Chest.
- **Recipe:** 4 Leather + 2 Void Pearls + 1 Ender Chest.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use to register a portable storage channel; the script gives a clear storage message. A chest-backed inventory is recommended for production worlds.
- **Texture Path:** `textures/items/ender_backpack.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/backpack.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 184. Map Marker
- **Item ID:** `bedrock_expansion:map_marker`
- **Display Name:** Map Marker
- **Category:** Utility & Adventure
- **Tier:** 1 — Copper/Tin
- **Purpose:** The map marker solves a specific exploration problem at the copper/tin stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Map Marker names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Map + 1 Copper Wire + 1 Lumen Dust.
- **Recipe:** 1 Map + 1 Copper Wire + 1 Lumen Dust.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/map_marker.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 185. Compass Upgrade
- **Item ID:** `bedrock_expansion:compass_upgrade`
- **Display Name:** Compass Upgrade
- **Category:** Utility & Adventure
- **Tier:** 1 — Copper/Tin
- **Purpose:** The compass upgrade solves a specific exploration problem at the copper/tin stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Compass Upgrade names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Compass + 1 Silver Ingot + 1 Amethyst Core.
- **Recipe:** 1 Compass + 1 Silver Ingot + 1 Amethyst Core.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/compass_upgrade.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 186. Clock Upgrade
- **Item ID:** `bedrock_expansion:clock_upgrade`
- **Display Name:** Clock Upgrade
- **Category:** Utility & Adventure
- **Tier:** 1 — Copper/Tin
- **Purpose:** The clock upgrade solves a specific exploration problem at the copper/tin stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Clock Upgrade names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Clock + 1 Copper Wire + 1 Lumen Crystal.
- **Recipe:** 1 Clock + 1 Copper Wire + 1 Lumen Crystal.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/clock_upgrade.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** No runtime hook; vanilla component behavior.
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 187. Lantern Helmet
- **Item ID:** `bedrock_expansion:lantern_helmet`
- **Display Name:** Lantern Helmet
- **Category:** Utility & Adventure
- **Tier:** 1 — Copper/Tin
- **Purpose:** The lantern helmet solves a specific exploration problem at the copper/tin stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Lantern Helmet names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Iron Helmet + 1 Lantern + 1 Copper Wire.
- **Recipe:** 1 Iron Helmet + 1 Lantern + 1 Copper Wire.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Wear in the head slot; the survival-gear loop applies the appropriate timed effect.
- **Texture Path:** `textures/items/lantern_helmet.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/survival_gear.js
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 188. Night Vision Goggles
- **Item ID:** `bedrock_expansion:night_vision_goggles`
- **Display Name:** Night Vision Goggles
- **Category:** Utility & Adventure
- **Tier:** 3 — Platinum
- **Purpose:** The night vision goggles solves a specific exploration problem at the platinum stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Night Vision Goggles names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 2 Glass + 1 Lumen Crystal + 1 Copper Wire.
- **Recipe:** 2 Glass + 1 Lumen Crystal + 1 Copper Wire.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Wear in the head slot; the survival-gear loop applies the appropriate timed effect.
- **Texture Path:** `textures/items/night_vision_goggles.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/survival_gear.js
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 189. Scuba Helmet
- **Item ID:** `bedrock_expansion:scuba_helmet`
- **Display Name:** Scuba Helmet
- **Category:** Utility & Adventure
- **Tier:** 3 — Platinum
- **Purpose:** The scuba helmet solves a specific exploration problem at the platinum stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Scuba Helmet names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Iron Helmet + 2 Glass + 1 Fluid Pipe.
- **Recipe:** 1 Iron Helmet + 2 Glass + 1 Fluid Pipe.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Wear in the head slot; the survival-gear loop applies the appropriate timed effect.
- **Texture Path:** `textures/items/scuba_helmet.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/survival_gear.js
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 190. Jetpack
- **Item ID:** `bedrock_expansion:jetpack`
- **Display Name:** Jetpack
- **Category:** Utility & Adventure
- **Tier:** 5 — Adamantite
- **Purpose:** The jetpack solves a specific exploration problem at the adamantite stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Jetpack names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 2 Mythril Ingots + 3 Storm Fragments + 1 Energy Cable.
- **Recipe:** 2 Mythril Ingots + 3 Storm Fragments + 1 Energy Cable.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Hold the item and jump to receive a short upward impulse; sneak descends. Ember Dust fuel is checked by the script.
- **Texture Path:** `textures/items/jetpack.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/jetpack.js
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 191. Parachute
- **Item ID:** `bedrock_expansion:parachute`
- **Display Name:** Parachute
- **Category:** Utility & Adventure
- **Tier:** 1 — Copper/Tin
- **Purpose:** The parachute solves a specific exploration problem at the copper/tin stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Parachute names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 3 String + 3 White Wool + 1 Leather.
- **Recipe:** 3 String + 3 White Wool + 1 Leather.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/parachute.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/jetpack.js
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 192. Grappling Hook
- **Item ID:** `bedrock_expansion:grappling_hook`
- **Display Name:** Grappling Hook
- **Category:** Utility & Adventure
- **Tier:** 4 — Mythril
- **Purpose:** The grappling hook solves a specific exploration problem at the mythril stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Grappling Hook names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Iron Ingot + 1 String + 1 Copper Wire.
- **Recipe:** 1 Iron Ingot + 1 String + 1 Copper Wire.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use to pull toward the look direction with a capped impulse; cooldown prevents repeated flight.
- **Texture Path:** `textures/items/grappling_hook.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 193. Lockpick
- **Item ID:** `bedrock_expansion:lockpick`
- **Display Name:** Lockpick
- **Category:** Utility & Adventure
- **Tier:** 1 — Copper/Tin
- **Purpose:** The lockpick solves a specific exploration problem at the copper/tin stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Lockpick names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 2 Iron Nuggets + 1 Copper Wire.
- **Recipe:** 2 Iron Nuggets + 1 Copper Wire.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/lockpick.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 194. Key
- **Item ID:** `bedrock_expansion:key`
- **Display Name:** Key
- **Category:** Utility & Adventure
- **Tier:** 1 — Copper/Tin
- **Purpose:** The key solves a specific exploration problem at the copper/tin stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Key names the Copperwright guild as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Gold Ingot + 1 Iron Nugget + 1 Rune Stone.
- **Recipe:** 1 Gold Ingot + 1 Iron Nugget + 1 Rune Stone.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/key.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** The Copper/Tin tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Copper/Tin stage and points toward Silver through its material, recipe, or realm hook.

### 195. Treasure Map
- **Item ID:** `bedrock_expansion:treasure_map`
- **Display Name:** Treasure Map
- **Category:** Utility & Adventure
- **Tier:** 2 — Silver
- **Purpose:** The treasure map solves a specific exploration problem at the silver stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Treasure Map names the Silver Cartographers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Map + 1 Lumen Dust + 1 Voidstone.
- **Recipe:** 1 Map + 1 Lumen Dust + 1 Voidstone.
- **Stats:** Stack size 16; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/treasure_map.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** The Silver tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Silver stage and points toward Platinum through its material, recipe, or realm hook.

### 196. Boss Key
- **Item ID:** `bedrock_expansion:boss_key`
- **Display Name:** Boss Key
- **Category:** Utility & Adventure
- **Tier:** 5 — Adamantite
- **Purpose:** The boss key solves a specific exploration problem at the adamantite stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Boss Key names the Adamantite Wardens as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Adamantite Ingot + 1 Void Pearl + 1 Storm Fragment.
- **Recipe:** 1 Adamantite Ingot + 1 Void Pearl + 1 Storm Fragment.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/boss_key.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** The Adamantite tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Adamantite stage and points toward Elemental / Void through its material, recipe, or realm hook.

### 197. Dungeon Compass
- **Item ID:** `bedrock_expansion:dungeon_compass`
- **Display Name:** Dungeon Compass
- **Category:** Utility & Adventure
- **Tier:** 3 — Platinum
- **Purpose:** The dungeon compass solves a specific exploration problem at the platinum stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Dungeon Compass names the Platinum Measure as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Compass + 1 Lurker Eye + 1 Amethyst Core.
- **Recipe:** 1 Compass + 1 Lurker Eye + 1 Amethyst Core.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/dungeon_compass.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** The Platinum tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Platinum stage and points toward Mythril through its material, recipe, or realm hook.

### 198. Waypoint Stone
- **Item ID:** `bedrock_expansion:waypoint_stone`
- **Display Name:** Waypoint Stone
- **Category:** Utility & Adventure
- **Tier:** 4 — Mythril
- **Purpose:** The waypoint stone solves a specific exploration problem at the mythril stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Waypoint Stone names the Mythril Wayfarers as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 4 Marble + 1 Lumen Crystal + 1 Amethyst Core.
- **Recipe:** 4 Marble + 1 Lumen Crystal + 1 Amethyst Core.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/waypoint_stone.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** The Mythril tier costs its matching material, has a finite durability budget, and remains a sidegrade where a vanilla tool is better suited.
- **Progression Role:** Introduces the Mythril stage and points toward Adamantite through its material, recipe, or realm hook.

### 199. Portal Frame
- **Item ID:** `bedrock_expansion:portal_frame`
- **Display Name:** Portal Frame
- **Category:** Utility & Adventure
- **Tier:** 6 — Elemental / Void
- **Purpose:** The portal frame solves a specific exploration problem at the elemental / void stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Portal Frame names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 6 Voidstone + 2 Adamantite Blocks + 1 Celestial Shard.
- **Recipe:** 6 Voidstone + 2 Adamantite Blocks + 1 Celestial Shard.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/portal_frame.png`
- **Model:** `block/full_cube`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.

### 200. Portal Activator
- **Item ID:** `bedrock_expansion:portal_activator`
- **Display Name:** Portal Activator
- **Category:** Utility & Adventure
- **Tier:** 6 — Elemental / Void
- **Purpose:** The portal activator solves a specific exploration problem at the elemental / void stage without replacing every other utility.
- **Story/Lore:** The surviving inscription for Portal Activator names the last Forge architects as its maker. It was designed after the Bedrock Forge changed the Forge's supply routes, so its shape carries a practical memory of the old civilization.
- **Obtain Method:** Utility crafting: 1 Void Pearl + 1 Lumen Crystal + 1 Storm Fragment + 1 Rune Stone.
- **Recipe:** 1 Void Pearl + 1 Lumen Crystal + 1 Storm Fragment + 1 Rune Stone.
- **Stats:** Stack size 1; one utility action has a 1-12 second cooldown where scripted.
- **Interactions:** Use in the world to receive a context message or the documented movement/waypoint action; no Java-only GUI is assumed.
- **Texture Path:** `textures/items/portal_activator.png`
- **Model:** `item/handheld`
- **Sound:** random.orb / random.pop
- **Script Hooks:** scripts/adventure.js
- **Balance Notes:** Endgame access is gated behind a realm ingredient, a cooldown or durability cost, and the Forge stabilization quest; it does not replace every earlier option.
- **Progression Role:** Completes the elemental/Void loadout and contributes to stabilizing the Forge core.
