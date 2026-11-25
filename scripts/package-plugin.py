#!/usr/bin/env python3
"""Build a clean, toggleable standard plugin archive or staged plugin directory."""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

REQUIRED_DESIGN_PROVENANCE = (
    "anthropic",
    "shadcn-admin",
    "awesome-design-md",
    "microsoft",
)


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


def collect_runtime_files(repo_root: Path) -> list[Path]:
    skills_root = repo_root / "skills"
    entries = []
    for path in sorted(skills_root.rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(repo_root)
        if "__pycache__" in rel.parts or path.suffix in (".pyc", ".pyo") or path.name == ".DS_Store":
            continue
        if rel.parent.as_posix() == "skills/project-governance/scripts" and (
            path.name.startswith("test_") or path.name == "verification-plan.py"
        ):
            continue
        entries.append(rel)

    rules_file = repo_root / "rules" / "AGENTS.md"
    if not rules_file.is_file():
        raise FileNotFoundError("Missing plugin routing rule: rules/AGENTS.md")
    entries.append(Path("rules/AGENTS.md"))

    rel_set = {p.as_posix() for p in entries}
    for module in REQUIRED_DESIGN_PROVENANCE:
        for required_name in ("LICENSE.txt", "PROVENANCE.md"):
            expected = f"skills/design/references/{module}/{required_name}"
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
    entries = collect_runtime_files(repo_root)
    codex_manifest, claude_manifest = build_manifests(original)

    plugin_json_text = json.dumps(original, indent=2, ensure_ascii=False) + "\n"
    codex_json_text = json.dumps(codex_manifest, indent=2, ensure_ascii=False) + "\n"
    claude_json_text = json.dumps(claude_manifest, indent=2, ensure_ascii=False) + "\n"
    sha_text = head + "\n"

    result = {
        "source_sha": head,
        "file_count": len(entries) + 4,
    }

    if output_dir is not None:
        output_dir.mkdir(parents=True, exist_ok=True)
        out = output_dir / f"engineering-governance-web-preview-{version}-{head[:12]}.zip"
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("plugin.json", plugin_json_text)
            archive.writestr(".codex-plugin/plugin.json", codex_json_text)
            archive.writestr(".claude-plugin/plugin.json", claude_json_text)
            for rel in entries:
                archive.write(repo_root / rel, rel.as_posix())
            archive.writestr("PREVIEW_SOURCE_SHA.txt", sha_text)
        result["archive_path"] = str(out)

    if stage_dir is not None:
        if stage_dir.exists():
            shutil.rmtree(stage_dir)
        stage_dir.mkdir(parents=True, exist_ok=True)
        (stage_dir / "plugin.json").write_text(plugin_json_text, encoding="utf-8")
        (stage_dir / ".codex-plugin").mkdir(parents=True, exist_ok=True)
        (stage_dir / ".codex-plugin" / "plugin.json").write_text(codex_json_text, encoding="utf-8")
        (stage_dir / ".claude-plugin").mkdir(parents=True, exist_ok=True)
        (stage_dir / ".claude-plugin" / "plugin.json").write_text(claude_json_text, encoding="utf-8")
        for rel in entries:
            dest = stage_dir / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(repo_root / rel, dest)
        (stage_dir / "PREVIEW_SOURCE_SHA.txt").write_text(sha_text, encoding="utf-8")
        result["stage_dir"] = str(stage_dir)

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Package Engineering Governance runtime plugin.")
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--stage-dir", type=Path, default=None)
    parser.add_argument("--source-sha", default="")
    args = parser.parse_args()

    output_dir = args.output_dir
    if output_dir is None and args.stage_dir is None:
        output_dir = args.repo_root / "dist"

    summary = package_plugin(
        args.repo_root.resolve(),
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
