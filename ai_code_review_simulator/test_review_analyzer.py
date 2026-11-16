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

    def test_mutable_keyword_only_default(self):
        source = "def process(*, items=[]):\n    return items\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("MUTABLE_DEFAULT", [i.rule for i in issues])

    def test_async_mutable_default(self):
        source = "async def process(items=[]):\n    return items\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("MUTABLE_DEFAULT", [i.rule for i in issues])

    def test_mutable_set_default(self):
        source = "def process(items=set()):\n    return items\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("MUTABLE_DEFAULT", [i.rule for i in issues])

    def test_mutable_comprehension_default(self):
        source = "def process(items=[x for x in range(3)]):\n    return items\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("MUTABLE_DEFAULT", [i.rule for i in issues])

    def test_mutable_default_line_number(self):
        source = "\n\ndef process(items=[]):\n    return items\n"
        issues = self.analyzer.analyze(source)
        self.assertEqual(issues[0].line, 3)

    def test_nested_mutable_tuple_default(self):
        source = "def process(items=([],)):\n    return items\n"
        issues = self.analyzer.analyze(source)
        self.assertIn("MUTABLE_DEFAULT", [i.rule for i in issues])



    def test_subprocess_shell_true(self):
        source = (
            "import subprocess\n"
            "subprocess.run(user_command, shell=True)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("SUBPROCESS_SHELL_TRUE", [i.rule for i in issues])

    def test_subprocess_shell_false(self):
        source = (
            "import subprocess\n"
            "subprocess.run(['ls'], shell=False)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertNotIn("SUBPROCESS_SHELL_TRUE", [i.rule for i in issues])

    def test_pickle_load(self):
        source = (
            "import pickle\n"
            "data = pickle.load(file)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("UNSAFE_DESERIALIZATION", [i.rule for i in issues])

    def test_pickle_loads(self):
        source = (
            "import pickle\n"
            "data = pickle.loads(raw_data)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("UNSAFE_DESERIALIZATION", [i.rule for i in issues])

    def test_pickle_import_alias(self):
        source = (
            "from pickle import loads as deserialize\n"
            "data = deserialize(raw_data)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("UNSAFE_DESERIALIZATION", [i.rule for i in issues])

    def test_safe_json_deserialization(self):
        source = (
            "import json\n"
            "data = json.loads(raw_data)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertNotIn("UNSAFE_DESERIALIZATION", [i.rule for i in issues])


    def test_subprocess_import_alias(self):
        source = (
            "from subprocess import run as execute\n"
            "execute(user_command, shell=True)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("SUBPROCESS_SHELL_TRUE", [i.rule for i in issues])


    def test_subprocess_module_alias(self):
        source = (
            "import subprocess as sp\n"
            "sp.run(command, shell=True)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("SUBPROCESS_SHELL_TRUE", [i.rule for i in issues])

    def test_pickle_module_alias(self):
        source = (
            "import pickle as p\n"
            "data = p.loads(raw_data)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("UNSAFE_DESERIALIZATION", [i.rule for i in issues])

    def test_subprocess_direct_import(self):
        source = (
            "from subprocess import run\n"
            "run(command, shell=True)\n"
        )
        issues = self.analyzer.analyze(source)
        self.assertIn("SUBPROCESS_SHELL_TRUE", [i.rule for i in issues])


    def test_subprocess_without_import(self):
        source = "subprocess.run(command, shell=True)\n"
        issues = self.analyzer.analyze(source)
        self.assertNotIn("SUBPROCESS_SHELL_TRUE", [i.rule for i in issues])

    def test_pickle_without_import(self):
        source = "data = pickle.loads(raw_data)\n"
        issues = self.analyzer.analyze(source)
        self.assertNotIn("UNSAFE_DESERIALIZATION", [i.rule for i in issues])

if __name__ == "__main__":
    unittest.main()
