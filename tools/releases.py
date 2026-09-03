#!/usr/bin/env python3
"""Refresh the latest stable releases shown in the profile README."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parent.parent
OWNER = "JungHoonGhae"
START = "<!-- releases:start -->"
END = "<!-- releases:end -->"
SKIP_PREFIXES = ("homebrew-",)
SKIP_REPOSITORIES = {
    OWNER,
    "thecamp-aitrading",  # Public classroom material, not an OSS portfolio project.
}


def fetch_json(endpoint: str) -> object:
    result = subprocess.run(
        ["gh", "api", endpoint],
        capture_output=True,
        check=True,
        text=True,
    )
    return json.loads(result.stdout)


def eligible_repositories(repositories: Iterable[dict]) -> list[str]:
    """Keep active source repositories, excluding profile and package-manager mirrors."""
    return [
        repository["name"]
        for repository in repositories
        if not repository.get("fork")
        and not repository.get("archived")
        and repository["name"] not in SKIP_REPOSITORIES
        and not repository["name"].startswith(SKIP_PREFIXES)
    ]


def fetch_releases() -> list[dict]:
    repositories = fetch_json(
        f"users/{OWNER}/repos?per_page=100&type=owner&sort=pushed"
    )
    releases: list[dict] = []
    for repository in eligible_repositories(repositories):
        candidates = fetch_json(f"repos/{OWNER}/{repository}/releases?per_page=10")
        stable = next(
            (
                release
                for release in candidates
                if not release.get("draft")
                and not release.get("prerelease")
                and release.get("published_at")
            ),
            None,
        )
        if stable:
            releases.append(
                {
                    "repository": repository,
                    "tag": stable["tag_name"],
                    "url": stable["html_url"],
                    "published_at": stable["published_at"],
                }
            )
    return sorted(releases, key=lambda release: release["published_at"], reverse=True)


def render(releases: Iterable[dict], limit: int = 3) -> str:
    lines = []
    for release in list(releases)[:limit]:
        date = release["published_at"][:10]
        label = f'{release["repository"]} {release["tag"]}'.replace("]", r"\]")
        lines.append(f'- `{date}` — [{label}]({release["url"]})')
    return f'{START}\n' + "\n".join(lines) + f'\n{END}'


def rewrite(readme: str, releases: Iterable[dict]) -> str:
    if START not in readme or END not in readme:
        raise ValueError("release markers not found")
    before, remainder = readme.split(START, 1)
    _, after = remainder.split(END, 1)
    return before + render(releases) + after


def refresh(path: Path) -> bool:
    current = path.read_text()
    updated = rewrite(current, fetch_releases())
    if updated == current:
        print(f"releases: {path.name} is current")
        return False
    path.write_text(updated)
    print(f"releases: updated {path.name}")
    return True


def main() -> None:
    arguments = sys.argv[1:] or ["README.md"]
    for argument in arguments:
        path = Path(argument)
        refresh(path if path.is_absolute() else ROOT / path)


if __name__ == "__main__":
    main()
