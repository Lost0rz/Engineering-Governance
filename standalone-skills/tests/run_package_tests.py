#!/usr/bin/env python3
"""Discover and test every standalone Skill source package; fail if any is untested."""
from __future__ import annotations
import argparse
from pathlib import Path
import subprocess
import sys


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--packages-root", type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument("--no-install", action="store_true",
                        help="Only for dependency-free runner regression fixtures")
    args = parser.parse_args(argv)
    root = args.packages_root.resolve()
    if not root.is_dir():
        print("PACKAGE_TESTS_STOP missing packages root", file=sys.stderr)
        return 2
    packages = sorted(p for p in root.iterdir()
                      if p.is_dir() and p.name != "tests" and not p.name.startswith("."))
    if not packages:
        print("PACKAGE_TESTS_STOP no standalone packages", file=sys.stderr)
        return 2
    for package in packages:
        if package.is_symlink() or not (package / "SKILL.md").is_file():
            print(f"PACKAGE_TESTS_STOP invalid package root: {package.name}", file=sys.stderr)
            return 2
        testdir = package / "tests"
        if not testdir.is_dir() or not list(testdir.glob("test_*.py")):
            print(f"PACKAGE_TESTS_STOP missing tests: {package.name}", file=sys.stderr)
            return 2
        requirements = testdir / "requirements.txt"
        if requirements.is_file() and not args.no_install:
            subprocess.run([sys.executable, "-m", "pip", "install", "-r",
                            str(requirements)], check=True, timeout=120)
        subprocess.run([sys.executable, "-m", "compileall", "-q", str(testdir)],
                       check=True, timeout=30)
        scripts = package / "scripts"
        if scripts.exists():
            subprocess.run([sys.executable, "-m", "compileall", "-q", str(scripts)],
                           check=True, timeout=30)
        outcome = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(testdir),
             "-p", "test_*.py", "-v"],
            cwd=root, check=False, timeout=90)
        if outcome.returncode:
            print(f"PACKAGE_TESTS_STOP failed suite: {package.name}", file=sys.stderr)
            return outcome.returncode
        print(f"PACKAGE_TESTS_PASS {package.name}", flush=True)
    print(f"STANDALONE_PACKAGE_COUNT={len(packages)}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
