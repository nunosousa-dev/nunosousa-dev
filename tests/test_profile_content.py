from pathlib import Path
import unittest


README = Path(__file__).resolve().parents[1] / "README.md"


class ProfileContentTests(unittest.TestCase):
    def setUp(self):
        self.readme = README.read_text(encoding="utf-8")

    def test_current_stack_and_interests_come_before_older_experience(self):
        current = self.readme.index("## What I work with now")
        interests = self.readme.index("## Current interests")
        background = self.readme.index("Background and outside work")
        personal = self.readme.index("Personal-project tools")
        self.assertLess(current, interests)
        self.assertLess(interests, background)
        self.assertLess(interests, personal)

    def test_current_stack_stays_separate_from_personal_and_older_tools(self):
        current = self.readme.split("## What I work with now", 1)[1].split("## ", 1)[0]
        for tool in ["Argo Workflows", "Ray", "MLflow", "AWS", "Kubernetes", "Helm",
                     "GitHub Actions", "Argo CD", "Prometheus", "Grafana"]:
            with self.subTest(tool=tool):
                self.assertIn(tool, current)
        for tool in ["Jenkins", "SAP", "Terraform", "Python", "Proxmox", "Next.js"]:
            with self.subTest(tool=tool):
                self.assertNotIn(tool, current)

    def test_interests_do_not_imply_a_publication_plan(self):
        interests = self.readme.split("## Current interests", 1)[1].split("<details>", 1)[0]
        self.assertIn("A few topics I'm interested in:", interests)
        self.assertNotRegex(interests.lower(), r"\b(posts?|articles?|publish\w*|writ\w*|planned)\b")


if __name__ == "__main__":
    unittest.main()
