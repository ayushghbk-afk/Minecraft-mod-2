const PREFIX = '§6[Forge Pack]§r';

export function useBackpack(player, itemId) {
  const slots = itemId === 'bedrock_expansion:large_backpack' ? 18 : itemId === 'bedrock_expansion:ender_backpack' ? 27 : 9;
  const channel = itemId.endsWith('ender_backpack') ? 'linked Ender channel' : 'local pack';
  player.sendMessage(`${PREFIX} ${channel} selected: ${slots} planned slots. Store important items in a chest while using the documented preview build.`);
}
