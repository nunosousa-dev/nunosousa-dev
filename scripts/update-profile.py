#!/usr/bin/env python3
"""Refresh only the marked README section using public GitHub endpoints."""

import datetime as dt
import json
import os
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
USERNAME = "nunosousa-dev"
START = "<!-- PROFILE:START -->"
END = "<!-- PROFILE:END -->"
EVENT_LABELS = {
    "PushEvent": "Pushed code to",
    "PullRequestEvent": "Updated a pull request in",
    "IssuesEvent": "Updated an issue in",
    "ReleaseEvent": "Published a release in",
    "CreateEvent": "Created a repository or ref in",
}


def get_public_json(endpoint):
    # Intentionally unauthenticated: the token used to commit is never sent here.
    request = urllib.request.Request(
        f"https://api.github.com/users/{USERNAME}{endpoint}",
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": f"{USERNAME}-profile",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def render_snapshot(profile, events, now):
    """Keep API strings out of raw Markdown; use only validated names and dates."""
    repos = profile["public_repos"]
    if type(repos) is not int or repos < 0:
        raise ValueError("Invalid public repository count")
    lines = [
        f"**{repos} public repositories** · "
        f"Snapshot: **{now:%Y-%m-%d %H:%M} UTC**",
        "",
        "| Date (UTC) | Recent public signal |",
        "| :--- | :--- |",
    ]
    seen = set()
    for event in events:
        if event.get("public") is not True:
            continue
        label = EVENT_LABELS.get(event.get("type"))
        repo = event.get("repo", {}).get("name", "")
        if not label or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            continue
        day = dt.datetime.fromisoformat(event["created_at"].replace("Z", "+00:00")).date()
        key = (str(day), label, repo)
        if key in seen:
            continue
        seen.add(key)
        # HTML entities prevent underscores from becoming Markdown emphasis.
        display_repo = repo.replace("_", "&#95;")
        lines.append(f"| {day} | {label} [{display_repo}](https://github.com/{repo}) |")
        if len(seen) == 3:
            break
    if not seen:
        lines.append("| — | No recent supported public events in GitHub's activity window. |")
    lines.extend([
        "",
        "[View public activity ↗](https://github.com/nunosousa-dev?tab=overview)",
        "· [Refresh workflow](https://github.com/nunosousa-dev/nunosousa-dev/actions/workflows/profile.yml)",
        "",
        "<sub>Up to three recent signals from GitHub's public events feed; "
        "not a complete contribution history. Updates may be delayed.</sub>",
    ])
    return "\n".join(lines)


def replace_snapshot(readme, snapshot):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must contain exactly one pair of profile markers")
    before, remainder = readme.split(START)
    _, after = remainder.split(END)
    return f"{before}{START}\n{snapshot}\n{END}{after}"


def main():
    # Fetch and validate everything before touching the last successful snapshot.
    profile = get_public_json("")
    events = get_public_json("/events/public?per_page=100")
    snapshot = render_snapshot(profile, events, dt.datetime.now(dt.timezone.utc))
    path = ROOT / "README.md"
    updated = replace_snapshot(path.read_text(encoding="utf-8"), snapshot)
    temporary = path.with_suffix(".md.tmp")
    try:
        temporary.write_text(updated, encoding="utf-8")
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
