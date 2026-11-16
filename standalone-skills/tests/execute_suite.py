#!/usr/bin/env python3
"""Run one standalone unittest suite and reject all-skipped / zero-test PASS claims."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
import unittest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tests-dir", type=Path, required=True)
    args = parser.parse_args(argv)
    directory = args.tests_dir.resolve(strict=True)
    suite = unittest.defaultTestLoader.discover(str(directory), pattern="test_*.py")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    total = result.testsRun
    skipped = len(result.skipped)
    executed = total - skipped
    if not result.wasSuccessful():
        print(f"PACKAGE_TESTS_STOP failed total={total} executed={executed} skipped={skipped}",
              file=sys.stderr)
        return 1
    if total == 0 or executed == 0:
        print(f"PACKAGE_TESTS_STOP no executed tests total={total} skipped={skipped}",
              file=sys.stderr)
        return 2
    print(f"PACKAGE_TESTS_COUNT total={total} executed={executed} skipped={skipped}",
          flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
