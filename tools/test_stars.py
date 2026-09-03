import unittest

from tools.stars import repositories_in, rewrite


class StarsTest(unittest.TestCase):
    def test_finds_each_profile_repository_once(self):
        readme = """\
- **[alpha](https://github.com/JungHoonGhae/alpha)** (12★)
- [alpha](https://github.com/JungHoonGhae/alpha) (12★)
- **[someone else's](https://github.com/example/alpha)** (99★)
"""

        self.assertEqual(repositories_in(readme), ["alpha"])

    def test_rewrites_only_star_counts_attached_to_profile_repository_links(self):
        readme = """\
- **[alpha](https://github.com/JungHoonGhae/alpha)** (12★) — first
- [beta](https://github.com/JungHoonGhae/beta) (999★) — second
- **[someone else's](https://github.com/example/alpha)** (99★)
- unrelated proof (42★)
"""

        updated = rewrite(readme, {"alpha": 34, "beta": 1_234})

        self.assertEqual(
            updated,
            """\
- **[alpha](https://github.com/JungHoonGhae/alpha)** (34★) — first
- [beta](https://github.com/JungHoonGhae/beta) (1,234★) — second
- **[someone else's](https://github.com/example/alpha)** (99★)
- unrelated proof (42★)
""",
        )

    def test_rewrite_is_idempotent(self):
        readme = "- [alpha](https://github.com/JungHoonGhae/alpha) (34★)\n"

        once = rewrite(readme, {"alpha": 34})

        self.assertEqual(rewrite(once, {"alpha": 34}), once)


if __name__ == "__main__":
    unittest.main()
