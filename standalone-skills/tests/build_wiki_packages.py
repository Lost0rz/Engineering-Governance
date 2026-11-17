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

SKILL_NAME = "wiki-knowledge-builder"
VERSION = "0.2.2"
DESCRIPTION = ("Independent context-aware knowledge distillation Skill with deep source audits, "
               "actionable technical detail, and canonical Wiki Markdown. No automatic Wiki writes.")
ROOT_FILES = frozenset({"SKILL.md", "README.md"})
ROOT_FOLDERS = frozenset({"adapters", "assets", "examples", "references", "scripts", "tests"})
# Explicit runtime payload types prevent accidentally packaging a committed
# .env, private fixture, debug log, or unrelated repository asset.
PAYLOAD_EXTENSIONS = {
    "adapters": frozenset({".md"}),
    "assets": frozenset({".md"}),
    "examples": frozenset({".md"}),
    "references": frozenset({".md"}),
    "scripts": frozenset({".py"}),
    "tests": frozenset({".py"}),
}

REPOSITORY_ONLY_FILES = frozenset({
    "tests/build_wiki_packages.py",
    "tests/test_release_packaging.py",
    "tests/test_repository_isolation.py",
    "tests/execute_suite.py",
    "tests/run_package_tests.py",
})


def default_repo_root() -> Path:
    for candidate in Path(__file__).resolve().parents:
        if (candidate / ".git").exists():
            return candidate
    return Path.cwd()


def source_dir(repo: Path) -> Path:
    """Recognize the staging layout, a named Skill directory, or a standalone root."""
    candidates = (repo / "standalone-skills" / SKILL_NAME, repo / SKILL_NAME, repo)
    roots = [p for p in candidates if (p / "SKILL.md").is_file()]
    if len(roots) != 1 or roots[0].is_symlink():
        raise ValueError("Expected exactly one independent Skill source root")
    return roots[0]


def payload_path(relative: str) -> bool:
    parts = Path(relative).parts
    if not parts or relative.startswith("/") or ".." in parts:
        return False
    if "__pycache__" in parts or relative.endswith(".pyc") or relative in REPOSITORY_ONLY_FILES:
        return False
    if any(part.startswith(".") for part in parts):
        return False
    if len(parts) == 1:
        return parts[0] in ROOT_FILES
    if len(parts) < 2 or parts[0] not in ROOT_FOLDERS:
        return False
    if relative == "tests/requirements.txt":
        return True
    return Path(relative).suffix.lower() in PAYLOAD_EXTENSIONS[parts[0]]


def git(repo: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", "-C", str(repo), *args],
                                   stderr=subprocess.PIPE, timeout=30)


def source_files(repo: Path) -> dict[str, bytes]:
    """Return only allowlisted Skill payload files, rejecting linked payloads."""
    root = source_dir(repo)
    found: dict[str, bytes] = {}
    entries = [root / name for name in ROOT_FILES if (root / name).exists()]
    for folder in sorted(ROOT_FOLDERS):
        parent = root / folder
        if parent.exists() or parent.is_symlink():
            entries.extend([parent, *parent.rglob("*")])
    for path in sorted(entries):
        relative = path.relative_to(root).as_posix()
        if path.is_symlink():
            raise ValueError("Unexpected symlink in Skill package: " + relative)
        mode = path.lstat().st_mode
        if stat.S_ISDIR(mode):
            continue
        if not stat.S_ISREG(mode):
            raise ValueError("Non-regular Skill source: " + relative)
        if not payload_path(relative):
            continue
        if relative in found:
            raise ValueError("Duplicate Skill file: " + relative)
        found[relative] = path.read_bytes()
    if "SKILL.md" not in found or "scripts/validate_note.py" not in found:
        raise ValueError("Required independent Skill files absent")
    if f"# Wiki Knowledge Builder v{VERSION}" not in found["SKILL.md"].decode("utf-8"):
        raise ValueError("Source Skill version does not match archive version")
    return found


def pinned_checkout_files(repo: Path, head: str, found: dict[str, bytes]) -> None:
    """Every payload file must match a real blob at the pinned checkout HEAD."""
    if not re.fullmatch(r"[0-9a-f]{40}", head):
        raise ValueError("Invalid pinned source SHA")
    prefix = source_dir(repo).relative_to(repo).as_posix()
    if prefix == ".":
        prefix = ""
    tree = git(repo, "ls-tree", "-r", "-z", head, "--", prefix or ".")
    expected: dict[str, str] = {}
    for item in tree.split(b"\0"):
        if not item:
            continue
        meta, path = item.split(b"\t", 1)
        mode, kind, sha = meta.decode("ascii").split(" ")
        rel = path.decode("utf-8")
        if prefix:
            if not rel.startswith(prefix + "/"):
                continue
            rel = rel[len(prefix) + 1:]
        if not payload_path(rel):
            continue
        if kind != "blob" or mode not in ("100644", "100755"):
            raise ValueError("Unsafe Git mode in Skill source: " + rel)
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
    parser.add_argument("--repo-root", type=Path, default=default_repo_root())
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
