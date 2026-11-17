"""Standalone source and runner checks; no parent Governance files required."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location(
    "wiki_package_preview_isolation", HERE / "build_wiki_packages.py"
)
builder = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(builder)
REPO = builder.default_repo_root()
SKILL = builder.source_dir(REPO)


class RepositoryIsolationTests(unittest.TestCase):
    def test_real_copy_runs_tests_outside_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            isolated = Path(tmp) / "arbitrary-host-skill-location"
            isolated.mkdir(parents=True)
            for relative, content in builder.source_files(REPO).items():
                target = isolated / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
            result = subprocess.run(
                [sys.executable, "-m", "unittest", "discover", "-s",
                 str(isolated / "tests"), "-p", "test_*.py", "-v"],
                cwd=tmp, capture_output=True, text=True, timeout=90,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_source_is_a_single_independent_skill(self):
        files = builder.source_files(REPO)
        self.assertIn("SKILL.md", files)
        self.assertIn("scripts/validate_note.py", files)
        self.assertTrue(files["SKILL.md"].startswith(b"---\nname: wiki-knowledge-builder\n"))
        self.assertTrue(all(builder.payload_path(p) for p in files))
        self.assertTrue(all(not p.startswith(("skills/", ".github/"))
                            and "project-governance" not in p for p in files))

    def test_packager_has_no_parent_governance_or_ci_contract(self):
        code = (HERE / "build_wiki_packages.py").read_text(encoding="utf-8")
        self.assertNotIn("engineering-governance", code)
        self.assertNotIn(".github/workflows", code)
        self.assertNotIn("governance_preview.py", code)
        self.assertIn("source_dir(repo)", code)

    def test_package_runner_discovers_two_skills_and_rejects_untested_skill(self):
        runner = HERE / "run_package_tests.py"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "skills"
            root.mkdir()
            for name in ("alpha", "beta"):
                pkg = root / name
                (pkg / "tests").mkdir(parents=True)
                (pkg / "SKILL.md").write_text(
                    "---\nname: " + name + "\ndescription: fixture\n---\n")
                (pkg / "tests/test_simple.py").write_text(
                    "import unittest\nclass TestSimple(unittest.TestCase):\n"
                    "    def test_pass(self): self.assertTrue(True)\n")
            result = subprocess.run(
                [sys.executable, str(runner), "--packages-root", str(root),
                 "--no-install"], capture_output=True, text=True, timeout=60)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("PACKAGE_TESTS_PASS alpha", result.stdout)
            self.assertIn("PACKAGE_TESTS_PASS beta", result.stdout)
            (root / "beta" / "tests/test_simple.py").unlink()
            blocked = subprocess.run(
                [sys.executable, str(runner), "--packages-root", str(root),
                 "--no-install"], capture_output=True, text=True, timeout=60)
            self.assertNotEqual(blocked.returncode, 0)
            self.assertIn("PACKAGE_TESTS_STOP", blocked.stderr)

    def test_package_runner_supports_independent_single_skill_repositories(self):
        runner = HERE / "run_package_tests.py"
        for layout in (".", "wiki-knowledge-builder"):
            with self.subTest(layout=layout), tempfile.TemporaryDirectory() as td:
                repo = Path(td)
                skill = repo if layout == "." else repo / layout
                (skill / "tests").mkdir(parents=True)
                (skill / "SKILL.md").write_text(
                    "---\nname: wiki-knowledge-builder\ndescription: test\n---\n")
                (skill / "tests/test_simple.py").write_text(
                    "import unittest\nclass T(unittest.TestCase):\n"
                    "    def test_real(self): self.assertTrue(True)\n")
                (repo / ".github").mkdir(exist_ok=True)
                result = subprocess.run(
                    [sys.executable, str(runner), "--packages-root", str(repo),
                     "--no-install"], capture_output=True, text=True, timeout=60)
                self.assertEqual(result.returncode, 0,
                                 result.stdout + result.stderr)
                self.assertIn("STANDALONE_PACKAGE_COUNT=1", result.stdout)

    def test_package_runner_rejects_skip_only_and_zero_case_suites(self):
        runner = HERE / "run_package_tests.py"
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "skills"
            suite = root / "skip-only"
            (suite / "tests").mkdir(parents=True)
            (suite / "SKILL.md").write_text("---\nname: skip-only\ndescription: fixture\n---\n")
            cases = suite / "tests/test_cases.py"
            cases.write_text(
                "import unittest\nclass Skipped(unittest.TestCase):\n"
                "    @unittest.skip('unavailable')\n"
                "    def test_never_executed(self): self.assertTrue(True)\n")
            skipped = subprocess.run(
                [sys.executable, str(runner), "--packages-root", str(root),
                 "--no-install"], capture_output=True, text=True, timeout=60)
            self.assertNotEqual(skipped.returncode, 0)
            self.assertIn("executed=0", skipped.stderr)
            cases.write_text("# Test file exists but contains zero test cases.\n")
            zero = subprocess.run(
                [sys.executable, str(runner), "--packages-root", str(root),
                 "--no-install"], capture_output=True, text=True, timeout=60)
            self.assertNotEqual(zero.returncode, 0)
            self.assertIn("executed=0", zero.stderr)


if __name__ == "__main__":
    unittest.main()
