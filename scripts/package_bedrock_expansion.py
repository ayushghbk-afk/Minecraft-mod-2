#!/usr/bin/env python3
"""Package the two generated Bedrock Expansion packs as a .mcaddon."""
from __future__ import annotations

import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASES = ROOT / "releases"


def pack_folder(folder: Path, output: Path):
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(folder.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(folder).as_posix())


def main():
    bp = ROOT / "BedrockExpansion_BP"
    rp = ROOT / "BedrockExpansion_RP"
    version = ".".join(str(x) for x in json.loads((bp / "manifest.json").read_text())["header"]["version"])
    RELEASES.mkdir(parents=True, exist_ok=True)
    bp_pack = RELEASES / "BedrockExpansion_BP.mcpack"
    rp_pack = RELEASES / "BedrockExpansion_RP.mcpack"
    addon = RELEASES / f"BedrockExpansion-{version}.mcaddon"
    pack_folder(bp, bp_pack)
    pack_folder(rp, rp_pack)
    with zipfile.ZipFile(addon, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.write(bp_pack, bp_pack.name)
        archive.write(rp_pack, rp_pack.name)
    bp_pack.unlink()
    rp_pack.unlink()
    print(f"Wrote {addon} ({addon.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
