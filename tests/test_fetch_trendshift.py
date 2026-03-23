import unittest
from pathlib import Path
import sys
import shutil

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from sources.trendshift.fetch_trendshift import (
    RepositoryRecord,
    dated_snapshot_paths,
    dedupe_repositories,
    normalize_repository,
    extract_repositories_from_html,
    write_normalized_records,
)


class TrendshiftHelpersTest(unittest.TestCase):
    def test_dated_snapshot_paths_uses_expected_file_names(self):
        tmp = ROOT / ".tmp-test-fetch-trendshift"
        tmp.mkdir(exist_ok=True)
        try:
            paths = dated_snapshot_paths(tmp, "2026-03-23")
            self.assertEqual(
                paths["trendshift_home"],
                tmp / "trendshift_home_2026-03-23.html",
            )
            self.assertEqual(
                paths["trendshift_github"],
                tmp / "trendshift_github_2026-03-23.html",
            )
        finally:
            shutil.rmtree(tmp, ignore_errors=True)

    def test_dedupe_repositories_keeps_first_seen_repo(self):
        records = [
            RepositoryRecord("owner/a", "TS", "2026-03-23", "first"),
            RepositoryRecord("owner/b", "GH", "2026-03-23", "second"),
            RepositoryRecord("owner/a", "GH", "2026-03-23", "duplicate"),
        ]
        deduped = dedupe_repositories(records)
        self.assertEqual([r.repo for r in deduped], ["owner/a", "owner/b"])
        self.assertEqual(deduped[0].description, "first")

    def test_normalize_repository_splits_owner_and_name(self):
        record = RepositoryRecord(
            repo="octocat/hello-world",
            source_page="TS",
            snapshot_date="2026-03-23",
            description="demo",
        )
        normalized = normalize_repository(record, "trendshift")
        self.assertEqual(normalized["owner"], "octocat")
        self.assertEqual(normalized["name"], "hello-world")
        self.assertEqual(
            normalized["repo_url"],
            "https://github.com/octocat/hello-world",
        )

    def test_extract_repositories_from_html_reads_embedded_json_records(self):
        html = (
            '\\"full_name\\":\\"octocat/hello-world\\",'
            '\\"repository_description\\":\\"First repo\\"'
            '\\"full_name\\":\\"openai/codex\\",'
            '\\"description\\":\\"Coding agent\\"'
        )
        records = extract_repositories_from_html(html, "TS", "2026-03-23")
        self.assertEqual(
            records,
            [
                RepositoryRecord("octocat/hello-world", "TS", "2026-03-23", "First repo"),
                RepositoryRecord("openai/codex", "TS", "2026-03-23", "Coding agent"),
            ],
        )

    def test_write_normalized_records_writes_json_file(self):
        tmp = ROOT / ".tmp-test-normalized"
        tmp.mkdir(exist_ok=True)
        output = tmp / "records.json"
        try:
            records = [
                RepositoryRecord("octocat/hello-world", "TS", "2026-03-23", "First repo")
            ]
            write_normalized_records(records, "trendshift", output)
            content = output.read_text(encoding="utf-8")
            self.assertIn('"repo": "octocat/hello-world"', content)
            self.assertIn('"source": "trendshift"', content)
            self.assertIn('"snapshot_date": "2026-03-23"', content)
        finally:
            shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
