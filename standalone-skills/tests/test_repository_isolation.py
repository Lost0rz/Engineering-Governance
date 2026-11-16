"""Tests of repository-only installation and CI boundaries; excluded from copied Skill."""
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

import yaml

REPO = Path(__file__).resolve().parents[2]
SKILL = REPO / "standalone-skills/wiki-knowledge-builder"
GOVERNANCE = REPO / ".github/workflows/governance-contract-checks.yml"
INDEPENDENT = REPO / ".github/workflows/standalone-skills-ci.yml"


class RepositoryIsolationTests(unittest.TestCase):
    def test_real_copy_runs_tests_outside_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            isolated = Path(tmp) / "arbitrary-host-skill-location"
            shutil.copytree(SKILL, isolated,
                            ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
            result = subprocess.run(
                [sys.executable, "-m", "unittest", "discover", "-s",
                 str(isolated / "tests"), "-p", "test_*.py", "-v"],
                cwd=tmp, capture_output=True, text=True, timeout=60,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_skill_not_part_of_plugin_manifest(self):
        self.assertTrue((SKILL / "SKILL.md").is_file())
        self.assertFalse((REPO / "skills/wiki-knowledge-builder").exists())
        plugin = json.loads((REPO / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["name"], "engineering-governance")
        marketplace = json.loads((REPO / ".agents/plugins/marketplace.json").read_text())
        self.assertEqual([p["name"] for p in marketplace["plugins"]], ["engineering-governance"])

    def test_plugin_preview_excludes_standalone_tree(self):
        src = GOVERNANCE.read_text(encoding="utf-8")
        self.assertIn('Path("skills").rglob("*")', src)
        self.assertIn('Path("references").rglob("*")', src)
        self.assertNotIn('Path("standalone-skills").rglob("*")', src)
        self.assertIn('"skills": "./skills"', src)

    def test_ci_events_route_standalone_and_mixed_changes(self):
        gov = yaml.load(GOVERNANCE.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        own = yaml.load(INDEPENDENT.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)
        self.assertIn("standalone-skills/**", gov["on"]["pull_request"]["paths-ignore"])
        self.assertIn("standalone-skills/**", own["on"]["pull_request"]["paths"])
        self.assertIn(".github/workflows/standalone-skills-ci.yml", own["on"]["pull_request"]["paths"])
        self.assertIn("workflow_dispatch", gov["on"])
        self.assertIn("workflow_dispatch", own["on"])
        src = INDEPENDENT.read_text(encoding="utf-8")
        self.assertIn("unittest discover -s standalone-skills/wiki-knowledge-builder/tests", src)
        self.assertIn("unittest discover -s standalone-skills/tests", src)
        self.assertNotIn("secrets.", src)

    def test_governance_workflow_manifest_recognizes_new_ci(self):
        manifest = sorted(x.name for x in (REPO / ".github/workflows").glob("*.yml"))
        self.assertEqual(manifest, [
            "ci-router-reusable.yml", "governance-contract-checks.yml",
            "standalone-skills-ci.yml",
        ])
        self.assertIn('"standalone-skills-ci.yml"', GOVERNANCE.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
