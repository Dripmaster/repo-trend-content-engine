#!/usr/bin/env python3
"""Minimal Trendshift source helpers and CLI scaffolding."""

from __future__ import annotations

import argparse
import html
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.request import urlopen


TRENDshift_HOME_URL = "https://trendshift.io/"
TRENDshift_GH_URL = "https://trendshift.io/github-trending-repositories"


@dataclass(frozen=True)
class RepositoryRecord:
    repo: str
    source_page: str
    snapshot_date: str
    description: str = ""


def dated_snapshot_paths(base_dir: str | Path, snapshot_date: str) -> dict[str, Path]:
    """Return canonical snapshot file paths for a given date."""
    root = Path(base_dir)
    return {
        "trendshift_home": root / f"trendshift_home_{snapshot_date}.html",
        "trendshift_github": root / f"trendshift_github_{snapshot_date}.html",
    }


def dedupe_repositories(records: Iterable[RepositoryRecord]) -> list[RepositoryRecord]:
    """Keep the first record for each repo name."""
    seen: set[str] = set()
    output: list[RepositoryRecord] = []
    for record in records:
        if record.repo in seen:
            continue
        seen.add(record.repo)
        output.append(record)
    return output


def normalize_repository(record: RepositoryRecord, source: str) -> dict[str, str]:
    """Convert a raw repository record into the repository's normalized shape."""
    owner, name = record.repo.split("/", 1)
    return {
        "repo": record.repo,
        "owner": owner,
        "name": name,
        "source": source,
        "source_page": record.source_page,
        "snapshot_date": record.snapshot_date,
        "repo_url": f"https://github.com/{record.repo}",
        "description": record.description,
    }


def extract_repositories_from_html(
    raw_html: str, source_page: str, snapshot_date: str
) -> list[RepositoryRecord]:
    """Extract repository records from embedded JSON-like page content."""
    token_pattern = re.compile(
        r'\\"full_name\\":\\"(?P<repo>[^\\"]+)\\"|'
        r'\\"(?:repository_description|description)\\":\\"(?P<desc>(?:\\\\.|[^\\"])*)\\"'
    )
    pending_repo: str | None = None
    output: list[RepositoryRecord] = []

    for match in token_pattern.finditer(raw_html):
        repo = match.group("repo")
        desc = match.group("desc")
        if repo is not None:
            if pending_repo is not None:
                output.append(RepositoryRecord(pending_repo, source_page, snapshot_date, ""))
            pending_repo = repo
            continue
        if desc is not None and pending_repo is not None:
            decoded = html.unescape(
                desc.replace("\\u0026", "&")
                .replace("\\u003c", "<")
                .replace("\\u003e", ">")
                .replace("\\n", " ")
                .replace('\\"', '"')
            )
            output.append(
                RepositoryRecord(
                    pending_repo,
                    source_page,
                    snapshot_date,
                    " ".join(decoded.split()),
                )
            )
            pending_repo = None

    if pending_repo is not None:
        output.append(RepositoryRecord(pending_repo, source_page, snapshot_date, ""))

    return output


def write_normalized_records(
    records: Iterable[RepositoryRecord], source: str, output_path: str | Path
) -> Path:
    """Write normalized repository records to a JSON file."""
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = [normalize_repository(record, source) for record in records]
    path.write_text(json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def fetch_html(url: str) -> str:
    """Fetch raw HTML for a single page."""
    with urlopen(url) as response:
        return response.read().decode("utf-8", errors="replace")


def snapshot(snapshot_date: str, output_dir: str | Path) -> dict[str, Path]:
    """Fetch the two Trendshift pages and write them to dated snapshot files."""
    paths = dated_snapshot_paths(output_dir, snapshot_date)
    html_map = {
        "trendshift_home": fetch_html(TRENDshift_HOME_URL),
        "trendshift_github": fetch_html(TRENDshift_GH_URL),
    }
    for key, html in html_map.items():
        paths[key].parent.mkdir(parents=True, exist_ok=True)
        paths[key].write_text(html, encoding="utf-8")
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Trendshift snapshot helper")
    parser.add_argument("snapshot_date", help="Snapshot date in YYYY-MM-DD format")
    parser.add_argument(
        "--output-dir",
        default="archives/raw/trendshift",
        help="Directory for dated HTML snapshots",
    )
    parser.add_argument(
        "--print-paths",
        action="store_true",
        help="Print written file paths as JSON",
    )
    parser.add_argument(
        "--extract-json",
        help="Optional path to write normalized extracted records as JSON",
    )
    args = parser.parse_args()

    paths = snapshot(args.snapshot_date, args.output_dir)
    if args.extract_json:
        combined = []
        for source_page, path in (
            ("TS", paths["trendshift_home"]),
            ("GH", paths["trendshift_github"]),
        ):
            combined.extend(
                extract_repositories_from_html(
                    path.read_text(encoding="utf-8"),
                    source_page,
                    args.snapshot_date,
                )
            )
        deduped = dedupe_repositories(combined)
        write_normalized_records(deduped, "trendshift", args.extract_json)
    if args.print_paths:
        print(json.dumps({k: str(v) for k, v in paths.items()}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
