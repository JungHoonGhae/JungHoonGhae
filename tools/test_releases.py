import unittest

from tools.releases import eligible_repositories, render, rewrite


RELEASES = [
    {
        "repository": "alpha",
        "tag": "v2.0.0",
        "url": "https://github.com/JungHoonGhae/alpha/releases/tag/v2.0.0",
        "published_at": "2026-09-03T01:02:03Z",
    },
    {
        "repository": "beta",
        "tag": "v1.4.0",
        "url": "https://github.com/JungHoonGhae/beta/releases/tag/v1.4.0",
        "published_at": "2026-09-01T01:02:03Z",
    },
]


class ReleasesTest(unittest.TestCase):
    def test_keeps_only_active_source_repositories(self):
        repositories = [
            {"name": "alpha", "fork": False, "archived": False},
            {"name": "a-fork", "fork": True, "archived": False},
            {"name": "old", "fork": False, "archived": True},
            {"name": "homebrew-alpha", "fork": False, "archived": False},
            {"name": "JungHoonGhae", "fork": False, "archived": False},
        ]

        self.assertEqual(eligible_repositories(repositories), ["alpha"])

    def test_renders_a_compact_dated_list(self):
        self.assertEqual(
            render(RELEASES),
            """<!-- releases:start -->
- `2026-09-03` — [alpha v2.0.0](https://github.com/JungHoonGhae/alpha/releases/tag/v2.0.0)
- `2026-09-01` — [beta v1.4.0](https://github.com/JungHoonGhae/beta/releases/tag/v1.4.0)
<!-- releases:end -->""",
        )

    def test_rewrite_changes_only_the_marked_region_and_is_idempotent(self):
        readme = """before
<!-- releases:start -->
- stale
<!-- releases:end -->
after
"""

        updated = rewrite(readme, RELEASES)

        self.assertTrue(updated.startswith("before\n<!-- releases:start -->"))
        self.assertTrue(updated.endswith("<!-- releases:end -->\nafter\n"))
        self.assertEqual(rewrite(updated, RELEASES), updated)

    def test_missing_markers_raise_a_clear_error(self):
        with self.assertRaisesRegex(ValueError, "release markers not found"):
            rewrite("no markers here", RELEASES)


if __name__ == "__main__":
    unittest.main()
