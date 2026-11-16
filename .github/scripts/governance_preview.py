#!/usr/bin/env python3
"""Repository-only, symlink-safe Engineering Governance preview packager.

This script never imports or packages standalone-skills. It performs no release.
"""
from __future__ import annotations

import argparse
import json
import re
import stat
import subprocess
from pathlib import Path
import zipfile

ROOTS = ("skills", "references")


def preview_entries(repo: Path) -> list[Path]:
    """Enumerate source files, rejecting links/special files before filtering."""
    repo = repo.resolve(strict=True)
    selected = []
    for root_name in ROOTS:
        root = repo / root_name
        if root.is_symlink() or not root.is_dir():
            raise ValueError("Invalid preview source root: " + root_name)
        trusted_root = root.resolve(strict=True)
        for path in root.rglob("*"):
            # Reject *all* symlinks, even excluded files and directory links.
            if path.is_symlink():
                raise ValueError("Symlink in preview input: " + str(path))
            if path.is_dir():
                continue
            # Check lstat before is_file so FIFOs/special files are never read.
            if not stat.S_ISREG(path.lstat().st_mode):
                raise ValueError("Non-regular preview input: " + str(path))
            real = path.resolve(strict=True)
            if not real.is_relative_to(trusted_root):
                raise ValueError("Preview source escapes root: " + str(path))
            relative = path.relative_to(repo)
            if relative.parts[0] != root_name:
                raise ValueError("Wrong preview source owner: " + str(path))
            if ("__pycache__" in path.parts or path.suffix == ".pyc"
                    or path.name.endswith("_ACCEPTANCE.md")):
                continue
            selected.append(relative)
    return sorted(selected)


def build_preview(repo: Path, output_dir: Path, head: str) -> Path:
    """Create and inspect the actual ZIP; do not install or publish anything."""
    repo = repo.resolve(strict=True)
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise ValueError("Invalid source SHA")
    manifest = json.loads((repo / "plugin.json").read_text(encoding="utf-8"))
    if manifest.get("name") != "engineering-governance":
        raise ValueError("Not the Governance plugin manifest")
    version = manifest.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError("Missing Governance version")
    entries = preview_entries(repo)
    codex = {
        "interface": {
            "displayName": "Engineering Governance",
            "shortDescription": manifest["extensions"]["com.openai"]["interface"]["shortDescription"],
            "longDescription": manifest["description"],
            "developerName": "Workspace upload",
            "category": "Other",
            "capabilities": [],
            "defaultPrompt": None,
        },
        "name": manifest["name"],
        "version": version,
        "description": manifest["description"],
        "author": {"name": "Workspace upload"},
        "keywords": [],
        "skills": "./skills",
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    dest = output_dir / f"engineering-governance-web-preview-{version}-{head[:12]}.zip"
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("plugin.json", json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
        archive.writestr(".codex-plugin/plugin.json", json.dumps(codex, indent=2, ensure_ascii=False) + "\n")
        for rel in entries:
            path = repo / rel
            # Recheck the path before reading, avoiding stale selection.
            if path.is_symlink() or not stat.S_ISREG(path.lstat().st_mode):
                raise ValueError("Unsafe preview source changed: " + str(rel))
            if not path.resolve(strict=True).is_relative_to((repo / rel.parts[0]).resolve(strict=True)):
                raise ValueError("Preview source changed owner: " + str(rel))
            archive.write(path, rel.as_posix())
        archive.writestr("PREVIEW_SOURCE_SHA.txt", head + "\n")
    with zipfile.ZipFile(dest) as archive:
        expected = {"plugin.json", ".codex-plugin/plugin.json", "PREVIEW_SOURCE_SHA.txt"}
        expected.update(rel.as_posix() for rel in entries)
        if set(archive.namelist()) != expected:
            raise ValueError("Preview ZIP manifest mismatch")
        if any(name.startswith("standalone-skills/") for name in archive.namelist()):
            raise ValueError("Standalone Skill leaked into Governance ZIP")
        if archive.read("PREVIEW_SOURCE_SHA.txt").decode("utf-8") != head + "\n":
            raise ValueError("Preview source identity mismatch")
    return dest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    parser.add_argument("--verify-only", action="store_true")
    args = parser.parse_args()
    repo = args.repo_root.resolve()
    if args.verify_only:
        entries = preview_entries(repo)
        print(f"GOVERNANCE_PREVIEW_SOURCE_CHECK_PASS={len(entries)}")
        return 0
    head = subprocess.check_output(
        ["git", "-C", str(repo), "rev-parse", "HEAD"], text=True, timeout=30).strip()
    out = build_preview(repo, args.output_dir, head)
    print(f"WEB_PREVIEW_PACKAGE={out}")
    print(f"WEB_PREVIEW_SOURCE_SHA={head}")
    with zipfile.ZipFile(out) as archive:
        print(f"WEB_PREVIEW_FILE_COUNT={len(archive.namelist())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
