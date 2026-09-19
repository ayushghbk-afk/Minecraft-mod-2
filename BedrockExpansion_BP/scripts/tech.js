export function useTech(player, itemId) {
  const id = itemId.split(':').pop();
  const messages = {
    'logic_gate': 'Logic gate ready: redstone input is read on the next pulse.',
    'timer_block': 'Timer block armed: its channel is intentionally one-shot.',
    'pulse_extender': 'Pulse extender is configured for a short Forge tick window.',
    'item_pipe': 'Item pipe routes one stack at a time; it never duplicates output.',
    'fluid_pipe': 'Fluid pipe awaits a source and preserves vanilla container rules.',
    'energy_cable': 'Energy cable reports a capped 100-unit channel.',
    'battery': 'Battery status: 0/100 until a generator or solar panel is connected.',
    'computer_block': 'Computer console: use the Forge ledger functions for diagnostics.',
  };
  player.sendMessage(`§3${messages[id] || 'Forge machine channel selected.'}`);
}
