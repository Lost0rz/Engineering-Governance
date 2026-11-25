"""Packaging tests for multi-host standard plugin archives and staged directories."""
import json
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGER = ROOT / "scripts/package-plugin.py"

EXPECTED_SKILLS = (
    "project-governance",
    "design",
    "solution-design",
    "domain-navigation",
    "incident-doctor",
    "execution-orchestrator",
    "agent-handoff",
    "evidence-audit",
    "project-profile",
)

DESIGN_MODULES = (
    "anthropic",
    "shadcn-admin",
    "awesome-design-md",
    "microsoft",
)


class PluginPackagingTests(unittest.TestCase):
    def test_package_plugin_archive_and_stage_dir(self):
        pkg_meta = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        version = pkg_meta["version"]
        fake_sha = "a" * 40
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            out_dir = tmp_path / "out"
            stage_dir = tmp_path / "staged" / "engineering-governance"
            proc = subprocess.run(
                [
                    sys.executable,
                    str(PACKAGER),
                    "--repo-root",
                    str(ROOT),
                    "--output-dir",
                    str(out_dir),
                    "--stage-dir",
                    str(stage_dir),
                    "--source-sha",
                    fake_sha,
                ],
                capture_output=True,
                text=True,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertIn("WEB_PREVIEW_PACKAGE=", proc.stdout)
            self.assertIn(f"WEB_PREVIEW_SOURCE_SHA={fake_sha}", proc.stdout)

            expected_zip = out_dir / f"engineering-governance-web-preview-{version}-{fake_sha[:12]}.zip"
            self.assertTrue(expected_zip.is_file())

            with zipfile.ZipFile(expected_zip, "r") as zf:
                names = set(zf.namelist())
                self.assertIn("plugin.json", names)
                self.assertIn(".codex-plugin/plugin.json", names)
                self.assertIn(".claude-plugin/plugin.json", names)
                self.assertIn("rules/AGENTS.md", names)
                self.assertIn("PREVIEW_SOURCE_SHA.txt", names)
                self.assertIn("skills/project-governance/scripts/ci-router.py", names)

                for skill in EXPECTED_SKILLS:
                    self.assertIn(f"skills/{skill}/SKILL.md", names)
                for mod in DESIGN_MODULES:
                    self.assertIn(f"skills/design/references/{mod}/LICENSE.txt", names)
                    self.assertIn(f"skills/design/references/{mod}/PROVENANCE.md", names)

                for forbidden_prefix in ("archive/", "tests/", "references/"):
                    self.assertFalse(
                        any(n.startswith(forbidden_prefix) for n in names),
                        f"Unexpected non-runtime prefix {forbidden_prefix} in {names}",
                    )
                for forbidden_name in ("verification-plan.py", "test_ci_router.py", "test_workflow_contracts.py"):
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

            # Verify standalone staged directory (Antigravity / Codex / Claude compatible).
            self.assertTrue((stage_dir / "plugin.json").is_file())
            self.assertTrue((stage_dir / "rules/AGENTS.md").is_file())
            self.assertTrue((stage_dir / ".codex-plugin/plugin.json").is_file())
            self.assertTrue((stage_dir / ".claude-plugin/plugin.json").is_file())
            self.assertTrue((stage_dir / "skills/project-governance/scripts/ci-router.py").is_file())
            self.assertFalse((stage_dir / "tests").exists())
            self.assertFalse((stage_dir / "archive").exists())


if __name__ == "__main__":
    unittest.main()
