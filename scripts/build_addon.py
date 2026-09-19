#!/usr/bin/env python3
"""Build the two source packs into an importable Bedrock .mcaddon file."""

from __future__ import annotations

import io
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKS = [
    (ROOT / "packs" / "realistic_sticks_bp", "RealisticSticks_BP.mcpack"),
    (ROOT / "packs" / "realistic_sticks_rp", "RealisticSticks_RP.mcpack"),
]
OUTPUT_DIR = ROOT / "releases"


def version_from_behavior_pack() -> str:
    manifest = json.loads((PACKS[0][0] / "manifest.json").read_text(encoding="utf-8"))
    version = manifest["header"]["version"]
    return ".".join(str(part) for part in version)


def files_in(directory: Path):
    return sorted(path for path in directory.rglob("*") if path.is_file())


def zip_directory(directory: Path) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in files_in(directory):
            relative = path.relative_to(directory).as_posix()
            info = zipfile.ZipInfo(relative, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    return buffer.getvalue()


def main() -> None:
    version = version_from_behavior_pack()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output = OUTPUT_DIR / f"RealisticSticks-{version}.mcaddon"
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as addon:
        for directory, filename in PACKS:
            if not directory.is_dir():
                raise SystemExit(f"Missing pack directory: {directory}")
            content = zip_directory(directory)
            info = zipfile.ZipInfo(filename, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            addon.writestr(info, content)
    print(f"Built {output.relative_to(ROOT)} ({output.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
