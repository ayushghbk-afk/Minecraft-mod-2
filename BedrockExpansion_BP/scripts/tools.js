export function useTool(player, itemId) {
  if (player.isSneaking && itemId === 'bedrock_expansion:bedrock_pickaxe') player.sendMessage('§7Bedrock Pickaxe: 3x3 intent toggled for the next mining action.');
  if (itemId === 'bedrock_expansion:drill') player.sendMessage('§7Drill engages only while Ember Dust fuel is available.');
  if (itemId === 'bedrock_expansion:chainsaw') player.sendMessage('§7Chainsaw teeth are ready; durability is consumed per harvest.');
}
