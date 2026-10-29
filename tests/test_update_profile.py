import datetime as dt
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location(
    "profile", Path(__file__).resolve().parents[1] / "scripts/update-profile.py"
)
profile = importlib.util.module_from_spec(spec)
spec.loader.exec_module(profile)


def event(repo="nunosousa-dev/example", kind="PushEvent", public=True):
    return {
        "type": kind,
        "public": public,
        "repo": {"name": repo},
        "created_at": "2026-10-29T12:00:00Z",
    }


class ProfileTests(unittest.TestCase):
    def render(self, events):
        return profile.render_snapshot(
            {"public_repos": 17}, events,
            dt.datetime(2026, 10, 29, 13, tzinfo=dt.timezone.utc),
        )

    def test_snapshot_is_dated_and_deduplicated(self):
        rendered = self.render([event(), event()])
        self.assertIn("17 public repositories", rendered)
        self.assertIn("2026-10-29 13:00 UTC", rendered)
        self.assertEqual(rendered.count("Pushed code to"), 1)

    def test_private_unknown_and_unsafe_events_are_excluded(self):
        rendered = self.render([
            event(public=False), event(kind="WatchEvent"),
            event(repo='bad](https://example.com)/repo'),
        ])
        self.assertIn("No recent activity to show", rendered)
        self.assertNotIn("example.com", rendered)
        self.assertNotIn("Pushed code to", rendered)

    def test_at_most_three_signals(self):
        rendered = self.render([event(repo=f"user/repo-{i}") for i in range(5)])
        self.assertEqual(rendered.count("Pushed code to"), 3)

    def test_profile_copy_uses_no_em_dashes(self):
        em_dash = chr(0x2014)
        self.assertNotIn(em_dash, self.render([]))
        self.assertNotIn(em_dash, self.render([event()]))
        readme = Path(__file__).resolve().parents[1] / "README.md"
        self.assertNotIn(em_dash, readme.read_text(encoding="utf-8"))

    def test_markdown_sensitive_repository_name(self):
        self.assertIn("user/a&#95;b", self.render([event(repo="user/a_b")]))

    def test_preserves_content_outside_markers(self):
        original = f"intro\n{profile.START}\nold\n{profile.END}\nfooter"
        self.assertEqual(
            profile.replace_snapshot(original, "new"),
            f"intro\n{profile.START}\nnew\n{profile.END}\nfooter",
        )

    def test_invalid_markers_fail_instead_of_overwriting(self):
        for text in ["no markers", profile.END + profile.START,
                     profile.START * 2 + profile.END]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                profile.replace_snapshot(text, "new")

    def test_invalid_counts_are_rejected(self):
        for value in ["17", -1, True]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                profile.render_snapshot({"public_repos": value}, [], dt.datetime.now())

    def test_fetch_failure_never_writes_readme(self):
        with patch.object(profile, "get_public_json", side_effect=OSError("offline")), \
             patch.object(Path, "write_text") as write:
            with self.assertRaises(OSError):
                profile.main()
            write.assert_not_called()


if __name__ == "__main__":
    unittest.main()
