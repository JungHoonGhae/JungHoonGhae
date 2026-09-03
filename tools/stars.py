#!/usr/bin/env python3
"""Refresh star counts shown next to this account's repository links."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parent.parent
OWNER = "JungHoonGhae"
STAR_COUNT = re.compile(
    r"(?P<prefix>\[[^\]\n]+\]\(https://github\.com/"
    + re.escape(OWNER)
    + r"/(?P<repo>[A-Za-z0-9_.-]+)\)(?:\*\*)?\s+\()"
    r"(?P<count>\d[\d,]*)(?P<suffix>★\))"
)


def repositories_in(readme: str) -> List[str]:
    """Return linked repositories with displayed star counts, in first-seen order."""
    return list(dict.fromkeys(match.group("repo") for match in STAR_COUNT.finditer(readme)))


def fetch_stars(repository: str) -> int:
    result = subprocess.run(
        ["gh", "api", f"repos/{OWNER}/{repository}", "--jq", ".stargazers_count"],
        capture_output=True,
        check=True,
        text=True,
    )
    return int(result.stdout.strip())


def rewrite(readme: str, stars: Dict[str, int]) -> str:
    """Replace only counts attached to this account's direct repository links."""

    def replace(match: re.Match[str]) -> str:
        repository = match.group("repo")
        if repository not in stars:
            return match.group(0)
        return f'{match.group("prefix")}{stars[repository]:,}{match.group("suffix")}'

    return STAR_COUNT.sub(replace, readme)


def refresh(path: Path) -> bool:
    current = path.read_text()
    repositories = repositories_in(current)
    counts = {repository: fetch_stars(repository) for repository in repositories}
    updated = rewrite(current, counts)
    if updated == current:
        print(f"stars: {path.name} is current ({len(repositories)} repositories)")
        return False
    path.write_text(updated)
    print(f"stars: updated {path.name} ({len(repositories)} repositories)")
    return True


def main() -> None:
    arguments = sys.argv[1:] or ["README.md"]
    for argument in arguments:
        path = Path(argument)
        refresh(path if path.is_absolute() else ROOT / path)


if __name__ == "__main__":
    main()
