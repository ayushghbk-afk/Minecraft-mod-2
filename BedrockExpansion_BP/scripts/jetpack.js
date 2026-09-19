export function useMobility(player, itemId) {
  if (itemId.endsWith('grappling_hook')) return;
  if (itemId.endsWith('parachute')) {
    player.addEffect('slow_falling', 80, { amplifier: 0, showParticles: false });
    player.sendMessage('§bParachute deployed: slow falling for four seconds.');
  } else {
    player.sendMessage('§bJetpack primed. Hold jump while carrying Ember Dust fuel.');
  }
}

export function tickMobility(player, held) {
  if (!held) return;
  if (held.typeId === 'bedrock_expansion:jetpack' && player.isJumping) {
    try { player.applyImpulse({ x: 0, y: 0.08, z: 0 }); } catch (_) {}
  }
}
