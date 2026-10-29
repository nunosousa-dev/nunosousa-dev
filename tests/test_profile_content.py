from pathlib import Path
import unittest


README = Path(__file__).resolve().parents[1] / "README.md"


class ProfileContentTests(unittest.TestCase):
    def setUp(self):
        self.readme = README.read_text(encoding="utf-8")

    def test_current_stack_and_writing_come_before_older_experience(self):
        current = self.readme.index("## What I work with now")
        writing = self.readme.index("## Things I'd like to write about")
        background = self.readme.index("Background and outside work")
        personal = self.readme.index("Personal-project tools")
        self.assertLess(current, writing)
        self.assertLess(writing, background)
        self.assertLess(writing, personal)

    def test_current_stack_stays_separate_from_personal_and_older_tools(self):
        current = self.readme.split("## What I work with now", 1)[1].split("## ", 1)[0]
        for tool in ["Argo Workflows", "Ray", "MLflow", "AWS", "Kubernetes", "Helm",
                     "GitHub Actions", "Argo CD", "Prometheus", "Grafana"]:
            with self.subTest(tool=tool):
                self.assertIn(tool, current)
        for tool in ["Jenkins", "SAP", "Terraform", "Python", "Proxmox", "Next.js"]:
            with self.subTest(tool=tool):
                self.assertNotIn(tool, current)

    def test_writing_topics_are_not_presented_as_published_articles(self):
        self.assertIn("These are planned topics, not published posts yet.", self.readme)


if __name__ == "__main__":
    unittest.main()
