export function tickGear(player, head) {
  if (!head) return;
  const id = head.typeId;
  if (id === 'bedrock_expansion:night_vision_goggles' || id === 'bedrock_expansion:lantern_helmet') player.addEffect('night_vision', 220, { amplifier: 0, showParticles: false });
  if (id === 'bedrock_expansion:scuba_helmet') player.addEffect('water_breathing', 220, { amplifier: 0, showParticles: false });
}
