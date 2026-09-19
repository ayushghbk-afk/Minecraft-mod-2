# Script hooks

`main.js` routes item-use events to focused modules. The modules use only stable `@minecraft/server` primitives: item-use events, effects, impulses, teleport, equipment, and messages. Backpacks intentionally expose a safe storage-channel preview because arbitrary-size item containers are not available as a portable custom-item component in stable Bedrock.
