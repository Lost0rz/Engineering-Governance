"""Actual ZIP build/verification against pinned HEAD; no publishing or installs."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

REPO = Path(__file__).resolve().parents[2]
SCRIPT = REPO / "standalone-skills/scripts/build_wiki_packages.py"
spec = importlib.util.spec_from_file_location("wiki_package_preview", SCRIPT)
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class IndependentArchiveTests(unittest.TestCase):
    def test_actual_checked_out_repository_builds_both_isolated_archives(self):
        with tempfile.TemporaryDirectory() as td:
            agent, plugin, head = builder.build(REPO, Path(td))
            actual = subprocess.check_output(
                ["git", "-C", str(REPO), "rev-parse", "HEAD"], text=True).strip()
            self.assertEqual(head, actual)
            self.assertIn(head[:12], agent.name)
            self.assertIn(head[:12], plugin.name)
            self.assertIn("v0.2.0", agent.name)
            self.assertIn("v0.2.0", plugin.name)
            source = builder.source_files(REPO)
            with zipfile.ZipFile(agent) as a, zipfile.ZipFile(plugin) as b:
                expect_agent = {f"wiki-knowledge-builder/{x}" for x in source}
                expect_plugin = {f"skills/wiki-knowledge-builder/{x}" for x in source}
                expect_plugin |= {"plugin.json", ".codex-plugin/plugin.json"}
                self.assertEqual(set(a.namelist()), expect_agent)
                self.assertEqual(set(b.namelist()), expect_plugin)
                self.assertEqual(a.testzip(), None)
                self.assertEqual(b.testzip(), None)
                self.assertEqual(json.loads(b.read("plugin.json"))["name"], "wiki-knowledge-builder")
                self.assertEqual(json.loads(b.read("plugin.json"))["version"], "0.2.0")
                self.assertEqual(json.loads(b.read(".codex-plugin/plugin.json"))["skills"], "./skills")
                self.assertTrue(all(not x.startswith("skills/project-governance/")
                                    for x in a.namelist() + b.namelist()))
                for rel, content in source.items():
                    self.assertEqual(a.read("wiki-knowledge-builder/" + rel), content)
                    self.assertEqual(b.read("skills/wiki-knowledge-builder/" + rel), content)

    def test_build_rejects_wrong_git_identity_or_changed_sources(self):
        sources = builder.source_files(REPO)
        head = builder.git(REPO, "rev-parse", "HEAD").decode().strip()
        builder.pinned_checkout_files(REPO, head, sources)
        changed = dict(sources)
        changed["SKILL.md"] = changed["SKILL.md"] + b"\nUNCOMMITTED CHANGE\n"
        with self.assertRaisesRegex(ValueError, "differ from pinned Git HEAD"):
            builder.pinned_checkout_files(REPO, head, changed)
        with self.assertRaisesRegex(ValueError, "Actual Skill file list"):
            builder.pinned_checkout_files(REPO, head, {k: v for k, v in sources.items() if k != "README.md"})

    def test_unsafe_symlink_not_packaged(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "standalone-skills/wiki-knowledge-builder"
            (root / "scripts").mkdir(parents=True)
            (root / "SKILL.md").write_text("# Wiki Knowledge Builder v0.2.0\n")
            (root / "scripts/validate_note.py").write_text("ok\n")
            outside = Path(td) / "sensitive.txt"
            outside.write_text("outside\n")
            (root / "references").symlink_to(outside)
            with self.assertRaisesRegex(ValueError, "symlink"):
                builder.source_files(Path(td))

    def test_wrong_version_is_not_packaged(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td) / "standalone-skills/wiki-knowledge-builder"
            (root / "scripts").mkdir(parents=True)
            (root / "SKILL.md").write_text("# Wiki Knowledge Builder v0.1.0\n")
            (root / "scripts/validate_note.py").write_text("ok\n")
            with self.assertRaisesRegex(ValueError, "version"):
                builder.source_files(Path(td))

    def test_tampered_zip_or_manifest_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            output = Path(td) / "build.zip"
            source_sha = "a" * 40
            expected = {"wiki-knowledge-builder/SKILL.md": b"safe"}
            builder.write_archive(output, expected, source_sha)
            builder.verify_archive(output, expected, source_sha)
            with self.assertRaisesRegex(ValueError, "source SHA"):
                builder.verify_archive(output, expected, "b" * 40)
            with self.assertRaisesRegex(ValueError, "content differs"):
                builder.verify_archive(output, {"wiki-knowledge-builder/SKILL.md": b"unsafe"}, source_sha)
            with self.assertRaisesRegex(ValueError, "member list"):
                builder.verify_archive(output, {"wiki-knowledge-builder/OTHER.md": b"safe"}, source_sha)

    def test_source_archive_workflow_does_not_upload_or_release(self):
        code = SCRIPT.read_text(encoding="utf-8")
        self.assertIn("WKB_RELEASE_EXECUTED=NO", code)
        self.assertNotIn("create_release", code)
        self.assertNotIn("update_plugin", code)
        self.assertNotIn("upload-artifact", code)
        self.assertIn("source_sha=", code)
        self.assertIn("source_files(repo)", code)


if __name__ == "__main__":
    unittest.main()
