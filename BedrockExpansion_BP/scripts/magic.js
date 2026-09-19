const spells = {
  'fire_spell': ['fire_resistance', 'Ember heat coils around your hands.'],
  'ice_spell': ['slowness', "Frost locks the target's footing."],
  'lightning_spell': ['speed', 'Storm current sharpens your reflexes.'],
  'healing_spell': ['regeneration', 'Lumen light closes a small wound.'],
  'shield_spell': ['resistance', 'A thin adamantine ward absorbs one mistake.'],
  'summon_spell': ['strength', 'A Forge echo answers for a moment.'],
};

export function useMagic(player, itemId) {
  const short = itemId.split(':').pop();
  if (short === 'teleport_spell') {
    const d = player.getViewDirection();
    const p = player.location;
    player.teleport({ x: p.x + d.x * 8, y: p.y + Math.max(0, d.y * 2), z: p.z + d.z * 8 }, { dimension: player.dimension });
    player.sendMessage('§dThe spell folds eight blocks of space.');
    return;
  }
  const effect = spells[short];
  if (effect) {
    player.addEffect(effect[0], 120, { amplifier: 0, showParticles: true });
    player.sendMessage(`§d${effect[1]}`);
  } else if (short === 'magic_wand' || short.startsWith('staff_') || short === 'spell_book') {
    player.sendMessage('§dThe focus hums. Select a spell item to release its realm effect.');
  }
}
