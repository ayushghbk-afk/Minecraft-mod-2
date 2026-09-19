import { world, system, EquipmentSlot } from '@minecraft/server';
import { useBackpack } from './backpack.js';
import { useMobility, tickMobility } from './jetpack.js';
import { useMagic } from './magic.js';
import { useTech } from './tech.js';
import { useAdventure } from './adventure.js';
import { tickGear } from './survival_gear.js';
import { useTool } from './tools.js';

const NS = 'bedrock_expansion:';
const backpackIds = new Set(['backpack', 'large_backpack', 'ender_backpack']);
const magicIds = new Set(['spell_book', 'fire_spell', 'ice_spell', 'lightning_spell', 'healing_spell', 'teleport_spell', 'shield_spell', 'summon_spell', 'magic_wand', 'staff_of_fire', 'staff_of_ice', 'staff_of_storms', 'staff_of_life']);
const techIds = new Set(['copper_wire', 'silver_wire', 'logic_gate', 'timer_block', 'pulse_extender', 'item_pipe', 'fluid_pipe', 'energy_cable', 'solar_panel', 'battery', 'generator', 'electric_furnace', 'auto_crafting_table', 'conveyor_belt', 'robot_arm', 'sensor_block', 'speaker_block', 'monitor_block', 'keyboard_block', 'computer_block']);
const adventureIds = new Set(['grappling_hook', 'lockpick', 'key', 'treasure_map', 'boss_key', 'dungeon_compass', 'waypoint_stone', 'portal_activator']);
const toolIds = new Set(['bedrock_pickaxe', 'drill', 'chainsaw', 'storm_hammer']);

world.afterEvents.itemUse.subscribe((event) => {
  const player = event.source;
  const stack = event.itemStack;
  if (!player || !stack || player.typeId !== 'minecraft:player' || !stack.typeId.startsWith(NS)) return;
  const id = stack.typeId.substring(NS.length);
  if (backpackIds.has(id)) useBackpack(player, stack.typeId);
  else if (id === 'jetpack' || id === 'parachute') useMobility(player, stack.typeId);
  else if (magicIds.has(id)) useMagic(player, stack.typeId);
  else if (techIds.has(id)) useTech(player, stack.typeId);
  else if (adventureIds.has(id)) useAdventure(player, stack.typeId);
  else if (id === 'lantern_helmet' || id === 'night_vision_goggles' || id === 'scuba_helmet') player.sendMessage('§bWear this in the head slot for its survival effect.');
  else if (toolIds.has(id)) useTool(player, stack.typeId);
});

world.afterEvents.itemUseOn.subscribe((event) => {
  if (event.source?.typeId === 'minecraft:player' && event.itemStack?.typeId === `${NS}portal_activator`) event.source.sendMessage('§5Portal frame contact recorded. The five realms remain gated by the Forge core.');
});

system.runInterval(() => {
  for (const player of world.getPlayers()) {
    let equipment;
    try { equipment = player.getComponent('minecraft:equippable'); } catch (_) { equipment = undefined; }
    const head = equipment?.getEquipment(EquipmentSlot.Head);
    const held = equipment?.getEquipment(EquipmentSlot.Mainhand);
    tickGear(player, head);
    tickMobility(player, held);
  }
}, 20);

world.afterEvents.playerSpawn.subscribe((event) => {
  if (event.initialSpawn) event.player.sendMessage('§6The Bedrock Forge remembers you. Run /function bedrock_forge_help for the six-tier path.');
});
