"""Packaging tests for deterministic, symlink-safe multi-host plugin archives."""
from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGER = ROOT / "scripts/package-plugin.py"

EXPECTED_SKILLS = (
    "engineering-workflow",
    "ci-governance",
    "ui-design",
    "architecture",
    "incident-doctor",
    "evidence-audit",
    "codebase-context",
)

DESIGN_MODULES = (
    "anthropic",
    "shadcn-admin",
    "awesome-design-md",
    "microsoft",
)


class PluginPackagingTests(unittest.TestCase):
    def test_package_plugin_archive_determinism_permissions_and_stage_dir(self):
        pkg_meta = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        version = pkg_meta["version"]
        fake_sha = "a" * 40
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            out1 = tmp_path / "out1"
            out2 = tmp_path / "out2"
            stage_dir = tmp_path / "staged" / "engineering-governance"

            proc1 = subprocess.run(
                [
                    sys.executable,
                    str(PACKAGER),
                    "--repo-root",
                    str(ROOT),
                    "--output-dir",
                    str(out1),
                    "--stage-dir",
                    str(stage_dir),
                    "--source-sha",
                    fake_sha,
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc1.returncode, 0, proc1.stderr)
            self.assertIn("WEB_PREVIEW_PACKAGE=", proc1.stdout)
            self.assertIn(f"WEB_PREVIEW_SOURCE_SHA={fake_sha}", proc1.stdout)

            proc2 = subprocess.run(
                [
                    sys.executable,
                    str(PACKAGER),
                    "--repo-root",
                    str(ROOT),
                    "--output-dir",
                    str(out2),
                    "--source-sha",
                    fake_sha,
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc2.returncode, 0, proc2.stderr)

            zip1 = out1 / f"engineering-governance-web-preview-{version}-{fake_sha[:12]}.zip"
            zip2 = out2 / f"engineering-governance-web-preview-{version}-{fake_sha[:12]}.zip"
            self.assertTrue(zip1.is_file())
            self.assertEqual(
                hashlib.sha256(zip1.read_bytes()).hexdigest(),
                hashlib.sha256(zip2.read_bytes()).hexdigest(),
                "Zip archive must be deterministic for the same source SHA",
            )

            with zipfile.ZipFile(zip1, "r") as zf:
                names = set(zf.namelist())
                self.assertIn("plugin.json", names)
                self.assertIn(".codex-plugin/plugin.json", names)
                self.assertIn(".claude-plugin/plugin.json", names)
                self.assertIn("rules/AGENTS.md", names)
                self.assertIn("PREVIEW_SOURCE_SHA.txt", names)
                self.assertIn("skills/ci-governance/scripts/ci-router.py", names)

                for name in (
                    "plugin.json",
                    ".codex-plugin/plugin.json",
                    ".claude-plugin/plugin.json",
                    "rules/AGENTS.md",
                    "PREVIEW_SOURCE_SHA.txt",
                ):
                    mode = (zf.getinfo(name).external_attr >> 16) & 0o777
                    self.assertEqual(mode, 0o644, f"{name} expected mode 0644, got {oct(mode)}")

                router_mode = (
                    zf.getinfo("skills/ci-governance/scripts/ci-router.py").external_attr >> 16
                ) & 0o777
                self.assertEqual(router_mode, 0o755)

                for skill in EXPECTED_SKILLS:
                    self.assertIn(f"skills/{skill}/SKILL.md", names)
                for mod in DESIGN_MODULES:
                    self.assertIn(f"skills/ui-design/references/{mod}/LICENSE.txt", names)
                    self.assertIn(f"skills/ui-design/references/{mod}/PROVENANCE.md", names)

                for forbidden_prefix in ("archive/", "tests/", "references/"):
                    self.assertFalse(
                        any(n.startswith(forbidden_prefix) for n in names),
                        f"Unexpected non-runtime prefix {forbidden_prefix} in {names}",
                    )
                for forbidden_name in (
                    "verification-plan.py",
                    "test_ci_router.py",
                    "test_workflow_contracts.py",
                    "test_plugin_packaging.py",
                ):
                    self.assertFalse(
                        any(forbidden_name in n for n in names),
                        f"Unexpected test/legacy script {forbidden_name} in zip",
                    )
                self.assertFalse(any("__pycache__" in n or n.endswith(".pyc") for n in names))

                codex = json.loads(zf.read(".codex-plugin/plugin.json").decode("utf-8"))
                claude = json.loads(zf.read(".claude-plugin/plugin.json").decode("utf-8"))
                self.assertEqual(codex["version"], version)
                self.assertEqual(codex["skills"], "./skills")
                self.assertEqual(claude["name"], "engineering-governance")
                self.assertEqual(claude["version"], version)
                self.assertEqual(zf.read("PREVIEW_SOURCE_SHA.txt").decode("utf-8").strip(), fake_sha)

            self.assertTrue((stage_dir / "plugin.json").is_file())
            self.assertTrue((stage_dir / "rules/AGENTS.md").is_file())
            self.assertTrue((stage_dir / ".codex-plugin/plugin.json").is_file())
            self.assertTrue((stage_dir / ".claude-plugin/plugin.json").is_file())
            self.assertTrue((stage_dir / "skills/ci-governance/scripts/ci-router.py").is_file())
            self.assertFalse((stage_dir / "tests").exists())
            self.assertFalse((stage_dir / "archive").exists())

    def test_package_plugin_rejects_symlinks_inside_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            repo.mkdir()
            shutil.copy2(ROOT / "plugin.json", repo / "plugin.json")
            shutil.copytree(ROOT / "rules", repo / "rules")
            shutil.copytree(ROOT / "skills", repo / "skills")
            outside = Path(tmp) / "secret.txt"
            outside.write_text("SECRET", encoding="utf-8")
            (repo / "skills/ci-governance/leak.txt").symlink_to(outside)

            proc = subprocess.run(
                [
                    sys.executable,
                    str(PACKAGER),
                    "--repo-root",
                    str(repo),
                    "--output-dir",
                    str(Path(tmp) / "out"),
                    "--source-sha",
                    "b" * 40,
                ],
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("Symlink forbidden", proc.stderr)

    def test_package_plugin_stage_dir_rejects_unsafe_targets(self):
        packager_mod = self._load_packager()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            unrelated = tmp_path / "unrelated_plugins"
            unrelated.mkdir()
            (unrelated / "other-plugin.txt").write_text("keep me", encoding="utf-8")

            git_repo = tmp_path / "other_git_repo"
            git_repo.mkdir()
            (git_repo / ".git").mkdir()

            for unsafe in (ROOT, tmp_path, unrelated, git_repo):
                with self.subTest(unsafe=unsafe):
                    with self.assertRaises(ValueError):
                        packager_mod.package_plugin(
                            ROOT, stage_dir=unsafe, source_sha="c" * 40
                        )
            self.assertEqual((unrelated / "other-plugin.txt").read_text(encoding="utf-8"), "keep me")

            # Existing empty or previously staged engineering-governance dir may be refreshed safely.
            staged = tmp_path / "staged" / "engineering-governance"
            packager_mod.package_plugin(ROOT, stage_dir=staged, source_sha="c" * 40)
            packager_mod.package_plugin(ROOT, stage_dir=staged, source_sha="d" * 40)
            self.assertEqual((staged / "PREVIEW_SOURCE_SHA.txt").read_text(encoding="utf-8").strip(), "d" * 40)

    @staticmethod
    def _load_packager():
        import importlib.util
        spec = importlib.util.spec_from_file_location("eg_packager", PACKAGER)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return mod


if __name__ == "__main__":
    unittest.main()
