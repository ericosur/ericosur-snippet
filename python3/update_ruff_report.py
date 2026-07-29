#!/usr/bin/env python3
"""Generate ruff_report.md from `ruff check` output."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPORT_PATH = ROOT / "ruff_report.md"
GITIGNORE_PATH = ROOT / ".gitignore"


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

    stderr = result.stderr or ""
    missing_module = "No module named ruff" in stderr or "ModuleNotFoundError" in stderr
    if missing_module:
        detail = stderr.strip() or "Unable to import module 'ruff'."
        raise RuntimeError(f"Ruff is not installed in this Python environment. {detail}")

    return "\n".join(part for part in [result.stdout.strip(), stderr.strip()] if part)


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


def _is_report_ignored(gitignore_path: Path) -> bool:
    if not gitignore_path.exists():
        return False

    tracked_patterns = {
        "ruff_report.md",
        "/ruff_report.md",
        "./ruff_report.md",
    }
    for line in gitignore_path.read_text(encoding="utf-8").splitlines():
        rule = line.strip()
        if not rule or rule.startswith("#"):
            continue
        if rule in tracked_patterns:
            return True
    return False


def remind_gitignore_for_report() -> None:
    if _is_report_ignored(GITIGNORE_PATH):
        return

    print("Reminder: ruff_report.md is not listed in .gitignore.")

    if not sys.stdin.isatty():
        print("Non-interactive mode detected; skipping .gitignore update.")
        return

    answer = input("Grant permission to add ruff_report.md to .gitignore? [y/N]: ").strip().lower()
    if answer not in {"y", "yes"}:
        print("Skipped updating .gitignore.")
        return

    existing = GITIGNORE_PATH.read_text(encoding="utf-8") if GITIGNORE_PATH.exists() else ""
    prefix = "\n" if existing and not existing.endswith("\n") else ""
    GITIGNORE_PATH.write_text(f"{existing}{prefix}ruff_report.md\n", encoding="utf-8")
    print("Added ruff_report.md to .gitignore.")


def main() -> None:
    try:
        remind_gitignore_for_report()

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
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
