#!/usr/bin/env python3
"""Build a deterministic, symlink-safe, toggleable standard plugin archive or staged directory."""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path

REQUIRED_DESIGN_PROVENANCE = (
    "anthropic",
    "shadcn-admin",
    "awesome-design-md",
    "microsoft",
)
FALLBACK_ZIP_DATE = (2026, 1, 1, 0, 0, 0)


def resolve_source_sha(repo_root: Path, explicit_sha: str = "") -> str:
    if explicit_sha:
        sha = explicit_sha.strip()
    else:
        sha = subprocess.check_output(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            text=True,
        ).strip()
    if len(sha) != 40 or any(c not in "0123456789abcdef" for c in sha):
        raise ValueError(f"Invalid 40-char git source SHA: {sha!r}")
    return sha


def resolve_deterministic_datetime(repo_root: Path, source_sha: str) -> tuple[int, int, int, int, int, int]:
    proc = subprocess.run(
        ["git", "-C", str(repo_root), "show", "-s", "--format=%ct", source_sha],
        capture_output=True,
        text=True,
    )
    if proc.returncode == 0:
        raw_ts = proc.stdout.strip()
        if raw_ts.isdigit():
            ts = max(int(raw_ts), 315532800)  # zip format requires year >= 1980
            gm = time.gmtime(ts)
            return (gm.tm_year, gm.tm_mon, gm.tm_mday, gm.tm_hour, gm.tm_min, gm.tm_sec)
    return FALLBACK_ZIP_DATE


def _reject_symlink(path: Path) -> None:
    if path.is_symlink():
        raise ValueError(f"Symlink forbidden in plugin package: {path}")


def collect_runtime_files(repo_root: Path) -> list[Path]:
    _reject_symlink(repo_root / "plugin.json")
    skills_root = repo_root / "skills"
    _reject_symlink(skills_root)
    entries = []
    for root_dir, dirnames, filenames in os.walk(skills_root, followlinks=False):
        root_path = Path(root_dir)
        for dirname in dirnames:
            _reject_symlink(root_path / dirname)
        dirnames[:] = sorted(d for d in dirnames if d != "__pycache__")
        for filename in sorted(filenames):
            path = root_path / filename
            _reject_symlink(path)
            if not path.is_file():
                continue
            rel = path.relative_to(repo_root)
            if path.suffix in (".pyc", ".pyo") or path.name == ".DS_Store":
                continue
            if "scripts" in rel.parts and (
                path.name.startswith("test_") or path.name == "verification-plan.py"
            ):
                continue
            entries.append(rel)

    rules_file = repo_root / "rules" / "AGENTS.md"
    _reject_symlink(repo_root / "rules")
    _reject_symlink(rules_file)
    if not rules_file.is_file():
        raise FileNotFoundError("Missing plugin routing rule: rules/AGENTS.md")
    entries.append(Path("rules/AGENTS.md"))

    rel_set = {p.as_posix() for p in entries}
    for module in REQUIRED_DESIGN_PROVENANCE:
        for required_name in ("LICENSE.txt", "PROVENANCE.md"):
            expected = f"skills/ui-design/references/{module}/{required_name}"
            if expected not in rel_set:
                raise ValueError(f"Missing required provenance/license file: {expected}")
    for rel_str in rel_set:
        if "/test_" in rel_str or rel_str.startswith(("tests/", "archive/")):
            raise ValueError(f"Non-runtime file leaked into package list: {rel_str}")
    return sorted(entries, key=lambda p: p.as_posix())


def build_manifests(original: dict) -> tuple[dict, dict]:
    version = original["version"]
    short_desc = original["extensions"]["com.openai"]["interface"]["shortDescription"]
    codex_manifest = {
        "interface": {
            "displayName": "Engineering Governance",
            "shortDescription": short_desc,
            "longDescription": original["description"],
            "developerName": "Workspace upload",
            "category": "Other",
            "capabilities": [],
            "defaultPrompt": None,
        },
        "name": original["name"],
        "version": version,
        "description": original["description"],
        "author": {"name": "Workspace upload"},
        "keywords": [],
        "skills": "./skills",
    }
    claude_manifest = {
        "name": original["name"],
        "version": version,
        "description": original["description"],
        "repository": original.get("repository", "https://github.com/Lost0rz/Engineering-Governance"),
        "license": original.get("license", "MIT"),
    }
    return codex_manifest, claude_manifest


def _is_executable(rel: Path) -> bool:
    return "scripts" in rel.parts and rel.suffix in (".py", ".sh")


def _write_zip_bytes(
    archive: zipfile.ZipFile,
    arcname: str,
    data: bytes,
    date_time: tuple[int, int, int, int, int, int],
    executable: bool = False,
) -> None:
    zi = zipfile.ZipInfo(filename=arcname, date_time=date_time)
    zi.compress_type = zipfile.ZIP_DEFLATED
    zi.create_system = 3  # Unix permissions preserved across extractors
    zi.external_attr = (0o100755 if executable else 0o100644) << 16
    archive.writestr(zi, data)


def validate_safe_stage_dir(stage_dir: Path, repo_root: Path) -> Path:
    """Prevent accidental deletion of repo roots, parent directories, git repos, or unrelated trees."""
    _reject_symlink(stage_dir)
    stage_resolved = stage_dir.resolve()
    repo_resolved = repo_root.resolve()
    home_resolved = Path.home().resolve()

    if len(stage_resolved.parts) <= 2 or stage_resolved == home_resolved:
        raise ValueError(f"Refusing unsafe stage-dir root/home target: {stage_resolved}")
    if stage_resolved == repo_resolved or repo_resolved.is_relative_to(stage_resolved):
        raise ValueError(f"Refusing stage-dir that covers or equals repo root: {stage_resolved}")
    if stage_resolved.is_relative_to(repo_resolved) and not (
        stage_resolved.is_relative_to(repo_resolved / "dist")
        or stage_resolved.is_relative_to(repo_resolved / "build")
    ):
        raise ValueError(f"Refusing stage-dir inside repo tree outside dist/ or build/: {stage_resolved}")
    if (stage_resolved / ".git").exists():
        raise ValueError(f"Refusing to overwrite git repository at stage-dir: {stage_resolved}")

    if stage_resolved.exists():
        if not stage_resolved.is_dir():
            raise ValueError(f"stage-dir exists and is not a directory: {stage_resolved}")
        if any(stage_resolved.iterdir()):
            has_sha = (stage_resolved / "PREVIEW_SOURCE_SHA.txt").is_file()
            plugin_file = stage_resolved / "plugin.json"
            is_eg_plugin = False
            if plugin_file.is_file() and not (stage_resolved / "tests").exists():
                try:
                    meta = json.loads(plugin_file.read_text(encoding="utf-8"))
                    is_eg_plugin = isinstance(meta, dict) and meta.get("name") == "engineering-governance"
                except (OSError, UnicodeError, json.JSONDecodeError):
                    is_eg_plugin = False
            if not (has_sha or is_eg_plugin):
                raise ValueError(f"Refusing to overwrite non-empty non-plugin directory: {stage_resolved}")
    return stage_resolved


def package_plugin(
    repo_root: Path,
    output_dir: Path | None = None,
    stage_dir: Path | None = None,
    source_sha: str = "",
) -> dict:
    original = json.loads((repo_root / "plugin.json").read_text(encoding="utf-8"))
    if original.get("name") != "engineering-governance":
        raise ValueError("Unexpected plugin name in plugin.json")
    version = original.get("version")
    if not version or not isinstance(version, str):
        raise ValueError("Missing version in plugin.json")

    head = resolve_source_sha(repo_root, source_sha)
    date_time = resolve_deterministic_datetime(repo_root, head)
    entries = collect_runtime_files(repo_root)
    codex_manifest, claude_manifest = build_manifests(original)

    plugin_json_bytes = (json.dumps(original, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    codex_json_bytes = (json.dumps(codex_manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    claude_json_bytes = (json.dumps(claude_manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
    sha_bytes = (head + "\n").encode("utf-8")

    result = {
        "source_sha": head,
        "file_count": len(entries) + 4,
    }

    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
        out = output_dir / f"engineering-governance-web-preview-{version}-{head[:12]}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
            _write_zip_bytes(archive, "plugin.json", plugin_json_bytes, date_time)
            _write_zip_bytes(archive, ".codex-plugin/plugin.json", codex_json_bytes, date_time)
            _write_zip_bytes(archive, ".claude-plugin/plugin.json", claude_json_bytes, date_time)
            for rel in entries:
                _write_zip_bytes(
                    archive,
                    rel.as_posix(),
                    (repo_root / rel).read_bytes(),
                    date_time,
                    executable=_is_executable(rel),
                )
            _write_zip_bytes(archive, "PREVIEW_SOURCE_SHA.txt", sha_bytes, date_time)
        result["archive_path"] = str(out)

    if stage_dir is not None:
        safe_stage = validate_safe_stage_dir(stage_dir, repo_root)
        if safe_stage.exists():
            shutil.rmtree(safe_stage)
        safe_stage.mkdir(parents=True, exist_ok=True)
        static_files = (
            (safe_stage / "plugin.json", plugin_json_bytes),
            (safe_stage / ".codex-plugin" / "plugin.json", codex_json_bytes),
            (safe_stage / ".claude-plugin" / "plugin.json", claude_json_bytes),
            (safe_stage / "PREVIEW_SOURCE_SHA.txt", sha_bytes),
        )
        for dest, data in static_files:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(data)
            os.chmod(dest, 0o644)
        for rel in entries:
            dest = safe_stage / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(repo_root / rel, dest)
            os.chmod(dest, 0o755 if _is_executable(rel) else 0o644)
        result["stage_dir"] = str(stage_dir)

    return result


def sync_marketplace_ref(repo_root: Path, source_sha: str = "") -> str:
    """Update .agents/plugins/marketplace.json source.ref to HEAD (or explicit source_sha)."""
    _reject_symlink(repo_root / ".agents")
    _reject_symlink(repo_root / ".agents" / "plugins")
    mp_path = repo_root / ".agents" / "plugins" / "marketplace.json"
    _reject_symlink(mp_path)
    if not mp_path.is_file():
        raise FileNotFoundError(f"Missing marketplace manifest: {mp_path}")
    head = resolve_source_sha(repo_root, source_sha)
    data = json.loads(mp_path.read_text(encoding="utf-8"))
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins or not isinstance(plugins[0], dict):
        raise ValueError("Invalid plugins structure in marketplace.json")
    source = plugins[0].get("source")
    if not isinstance(source, dict):
        raise ValueError("Invalid plugins[0].source structure in marketplace.json")
    source["ref"] = head
    mp_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return head


def main() -> int:
    parser = argparse.ArgumentParser(description="Package Engineering Governance runtime plugin.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--stage-dir", type=Path, default=None)
    parser.add_argument("--source-sha", default="")
    parser.add_argument(
        "--sync-marketplace",
        action="store_true",
        help="Update .agents/plugins/marketplace.json source.ref to HEAD (or --source-sha).",
    )
    args = parser.parse_args()

    repo_resolved = args.repo_root.resolve()
    if args.sync_marketplace:
        synced = sync_marketplace_ref(repo_resolved, args.source_sha)
        print(f"MARKETPLACE_SYNCED_REF={synced}")
        if args.output_dir is None and args.stage_dir is None:
            return 0

    output_dir = args.output_dir
    if output_dir is None and args.stage_dir is None:
        output_dir = args.repo_root / "dist"

    summary = package_plugin(
        repo_resolved,
        output_dir=output_dir,
        stage_dir=args.stage_dir,
        source_sha=args.source_sha,
    )
    if "archive_path" in summary:
        print(f"WEB_PREVIEW_PACKAGE={summary['archive_path']}")
    if "stage_dir" in summary:
        print(f"STAGED_PLUGIN_DIR={summary['stage_dir']}")
    print(f"WEB_PREVIEW_SOURCE_SHA={summary['source_sha']}")
    print(f"WEB_PREVIEW_FILE_COUNT={summary['file_count']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
