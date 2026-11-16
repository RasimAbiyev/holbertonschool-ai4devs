import unittest

from review_analyzer import ReviewAnalyzer, format_report


class TestReviewAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ReviewAnalyzer()

    def test_mutable_list_default(self):
        source = "def process(items=[]):\n    return items\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("MUTABLE_DEFAULT", [i.rule for i in issues])

    def test_mutable_dict_default(self):
        source = "def process(config=dict()):\n    return config\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("MUTABLE_DEFAULT", [i.rule for i in issues])

    def test_bare_except(self):
        source = "try:\n    run()\nexcept:\n    pass\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("BARE_EXCEPT", [i.rule for i in issues])

    def test_eval_call(self):
        source = "result = eval(user_input)\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("DYNAMIC_EXECUTION", [i.rule for i in issues])

    def test_exec_call(self):
        source = "exec(user_code)\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("DYNAMIC_EXECUTION", [i.rule for i in issues])

    def test_clean_code(self):
        source = "def add(a, b):\n    return a + b\n"
        issues = self.analyzer.analyze(source)
        self.assertEqual(issues, [])

    def test_issue_line_number(self):
        source = "\n\nresult = eval('1 + 1')\n"
        issues = self.analyzer.analyze(source)
        self.assertEqual(issues[0].line, 3)

    def test_report_format(self):
        source = "eval('2 + 2')\n"
        issues = self.analyzer.analyze(source)
        report = format_report(issues)
        self.assertIn("DYNAMIC_EXECUTION", report)
        self.assertIn("HIGH", report)

    def test_empty_report(self):
        self.assertEqual(
            format_report([]),
            "No review issues found.",
        )


if __name__ == "__main__":
    unittest.main()
