#!/usr/bin/env python3
"""Generate ruff_report.md from `ruff check` output."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT_PATH = ROOT / "ruff_report.md"


def run_ruff(*args: str) -> str:
    """Run Ruff and return combined text output.

    Ruff returns exit code 1 when violations are found; that is expected.
    """
    cmd = [sys.executable, "-m", "ruff", "check", str(ROOT), *args]
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    return "\n".join(part for part in [result.stdout.strip(), result.stderr.strip()] if part)


def build_report() -> str:
    statistics = run_ruff("--statistics")
    details = run_ruff()

    return "\n".join(
        [
            "# Ruff Linting Report",
            "",
            "This file lists all the linting issues found by `ruff check` in this workspace.",
            "",
            "## Summary Statistics",
            "",
            "```text",
            statistics or "All checks passed!",
            "```",
            "",
            "## Detailed Issues",
            "",
            "```text",
            details or "All checks passed!",
            "```",
            "",
        ]
    )


def main() -> None:
    # Process CLI options for auto-fixes
    if "--unsafe-fixes" in sys.argv:
        print("Applying safe and unsafe auto-fixes...")
        fix_output = run_ruff("--fix", "--unsafe-fixes")
        if fix_output:
            print(fix_output)
    elif "--fix" in sys.argv:
        print("Applying safe auto-fixes...")
        fix_output = run_ruff("--fix")
        if fix_output:
            print(fix_output)

    # Regenerate the report
    REPORT_PATH.write_text(build_report(), encoding="utf-8")
    print(f"Updated {REPORT_PATH}")


if __name__ == "__main__":
    main()

