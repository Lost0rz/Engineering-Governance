#!/usr/bin/env python3
"""Build and verify isolated Wiki Knowledge Builder archives from a pinned Git checkout.

No release, install, or upload. Output files are created only in --output-dir.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import stat
import subprocess
import zipfile

REPO = Path(__file__).resolve().parents[2]
REL = Path("standalone-skills/wiki-knowledge-builder")
SKILL_NAME = "wiki-knowledge-builder"
VERSION = "0.2.0"
DESCRIPTION = ("Independent context-aware knowledge distillation Skill with deep source audits, "
               "actionable technical detail, and canonical Wiki Markdown. No automatic Wiki writes.")


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args],
                                   stderr=subprocess.PIPE, timeout=30)


def source_files(repo: Path) -> dict[str, bytes]:
    """Require real regular source files. Never follow symlinks or package caches."""
    root = repo / REL
    if root.is_symlink() or not root.is_dir():
        raise ValueError("Invalid independent Skill source directory")
    found = {}
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError("Unexpected symlink in Skill package: " + str(path))
        mode = path.lstat().st_mode
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise ValueError("Non-regular Skill source: " + str(path))
        rel = path.relative_to(root).as_posix()
        if "__pycache__" in path.relative_to(root).parts or path.suffix == ".pyc":
            continue
        if rel.startswith("/") or ".." in Path(rel).parts or rel in found:
            raise ValueError("Unsafe or duplicate Skill path: " + rel)
        found[rel] = path.read_bytes()
    if "SKILL.md" not in found or "scripts/validate_note.py" not in found:
        raise ValueError("Required independent Skill files absent")
    if f"# Wiki Knowledge Builder v{VERSION}" not in found["SKILL.md"].decode("utf-8"):
        raise ValueError("Source Skill version does not match archive version")
    return found


def pinned_checkout_files(repo: Path, head: str, found: dict[str, bytes]) -> None:
    """Each packaged file must exist at HEAD with the identical Git blob SHA."""
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise ValueError("Invalid pinned source SHA")
    tree = git(repo, "ls-tree", "-r", "-z", head, "--", REL.as_posix())
    expected = {}
    for item in tree.split(b"\0"):
        if not item:
            continue
        meta, path = item.split(b"\t", 1)
        mode, typ, sha = meta.decode("ascii").split(" ")
        if typ != "blob" or mode not in ("100644", "100755"):
            raise ValueError("Unsafe Git mode in Skill source: " + path.decode("utf-8"))
        rel = Path(path.decode("utf-8")).relative_to(REL).as_posix()
        expected[rel] = sha
    if set(expected) != set(found):
        raise ValueError("Actual Skill file list differs from pinned Git tree: "
                         + str(sorted(set(expected) ^ set(found))))
    for rel, content in found.items():
        actual_sha = subprocess.check_output(
            ["git", "-C", str(repo), "hash-object", "--stdin"],
            input=content, timeout=30,
        ).decode("ascii").strip()
        if actual_sha != expected[rel]:
            raise ValueError("File bytes differ from pinned Git HEAD: " + rel)


def manifests() -> tuple[bytes, bytes]:
    source = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": SKILL_NAME,
        "version": VERSION,
        "description": DESCRIPTION,
        "extensions": {"com.openai": {"interface": {
            "displayName": "Wiki Knowledge Builder",
            "shortDescription": "Distill reusable knowledge from links, files or past work with deep evidence audits.",
        }}},
    }
    codex = {
        "interface": {
            "displayName": "Wiki Knowledge Builder",
            "shortDescription": source["extensions"]["com.openai"]["interface"]["shortDescription"],
            "longDescription": DESCRIPTION, "developerName": "Workspace upload",
            "category": "Other", "capabilities": [], "defaultPrompt": None,
        },
        "name": SKILL_NAME, "version": VERSION, "description": DESCRIPTION,
        "author": {"name": "Workspace upload"}, "keywords": [], "skills": "./skills",
    }
    encode = lambda value: (json.dumps(value, ensure_ascii=False,
                                       sort_keys=True, indent=2) + "\n").encode("utf-8")
    return encode(source), encode(codex)


def write_archive(path: Path, entries: dict[str, bytes], head: str) -> None:
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.comment = ("source_sha=" + head).encode("ascii")
        for name in sorted(entries):
            if name.startswith("/") or ".." in Path(name).parts:
                raise ValueError("Unsafe ZIP member: " + name)
            meta = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            meta.compress_type = zipfile.ZIP_DEFLATED
            meta.external_attr = (0o100644 << 16)
            archive.writestr(meta, entries[name])


def verify_archive(path: Path, entries: dict[str, bytes], head: str) -> None:
    with zipfile.ZipFile(path, "r") as archive:
        names = archive.namelist()
        if len(names) != len(set(names)) or set(names) != set(entries):
            raise ValueError("Archive does not match expected member list")
        if archive.comment != ("source_sha=" + head).encode("ascii"):
            raise ValueError("Archive source SHA provenance mismatch")
        if archive.testzip() is not None:
            raise ValueError("Archive CRC verification failed")
        for name in names:
            if archive.read(name) != entries[name]:
                raise ValueError("Archive content differs from pinned source: " + name)


def build(repo: Path, output_dir: Path) -> tuple[Path, Path, str]:
    repo = repo.resolve(strict=True)
    head = git(repo, "rev-parse", "HEAD").decode("ascii").strip()
    gov = json.loads((repo / "plugin.json").read_text(encoding="utf-8"))
    if gov.get("name") != "engineering-governance":
        raise ValueError("Unexpected parent repository manifest")
    source = source_files(repo)
    pinned_checkout_files(repo, head, source)
    plugin_manifest, codex_manifest = manifests()
    agent = {f"{SKILL_NAME}/{name}": content for name, content in source.items()}
    plugin = {f"skills/{SKILL_NAME}/{name}": content for name, content in source.items()}
    plugin["plugin.json"] = plugin_manifest
    plugin[".codex-plugin/plugin.json"] = codex_manifest
    if any("engineering-governance" in name for name in agent | plugin):
        raise ValueError("Governance package contamination")
    output_dir.mkdir(parents=True, exist_ok=True)
    agent_path = output_dir / f"{SKILL_NAME}-agent-skill-v{VERSION}-{head[:12]}.zip"
    plugin_path = output_dir / f"{SKILL_NAME}-chatgpt-private-v{VERSION}-{head[:12]}.zip"
    write_archive(agent_path, agent, head)
    write_archive(plugin_path, plugin, head)
    verify_archive(agent_path, agent, head)
    verify_archive(plugin_path, plugin, head)
    return agent_path, plugin_path, head


def main() -> int:
    parser = argparse.ArgumentParser(description="Build ZIPs only; no release/install")
    parser.add_argument("--repo-root", type=Path, default=REPO)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    agent, plugin, sha = build(args.repo_root, args.output_dir)
    print(f"WKB_SOURCE_SHA={sha}")
    print(f"WKB_AGENT_ZIP_VERIFIED={agent}")
    print(f"WKB_CHATGPT_ZIP_VERIFIED={plugin}")
    print("WKB_RELEASE_EXECUTED=NO")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
