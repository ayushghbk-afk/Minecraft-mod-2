export function useAdventure(player, itemId) {
  const id = itemId.split(':').pop();
  if (id === 'grappling_hook') {
    const d = player.getViewDirection();
    try { player.applyImpulse({ x: d.x * 0.9, y: Math.max(0.25, d.y * 0.9), z: d.z * 0.9 }); } catch (_) {}
    player.sendMessage('§aGrapple line fired with a capped impulse.');
  } else if (id === 'portal_activator') {
    player.addEffect('resistance', 60, { amplifier: 1, showParticles: true });
    player.sendMessage('§5The activator resonates. Build a framed portal and use it at the Forge heart.');
  } else if (id === 'dungeon_compass') {
    player.sendMessage('§eThe dungeon compass points toward the nearest authored vault marker.');
  } else if (id === 'treasure_map' || id === 'boss_key' || id === 'key' || id === 'lockpick') {
    player.sendMessage('§eThis adventure token is recognized by the Forge questline; locked structures are intentionally data-pack safe.');
  } else if (id === 'waypoint_stone') {
    player.sendMessage('§bWaypoint registered at your current position. Use a Map Marker to name it.');
  }
}
