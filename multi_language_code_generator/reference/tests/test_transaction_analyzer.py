import unittest
from transaction_analyzer import analyze_transactions


class TestTransactionAnalyzer(unittest.TestCase):

    def test_valid_transactions(self):
        data = [
            {"id": "T001", "category": "food", "amount_cents": 1500},
            {"id": "T002", "category": "transport", "amount_cents": 2500}
        ]
        result = analyze_transactions(data)
        self.assertEqual(result["valid_transactions"], 2)
        self.assertEqual(result["total_amount_cents"], 4000)

    def test_empty_input(self):
        result = analyze_transactions([])
        self.assertEqual(result["valid_transactions"], 0)
        self.assertEqual(result["total_amount_cents"], 0)

    def test_negative_amount(self):
        data = [{"id": "T1", "category": "food", "amount_cents": -500}]
        result = analyze_transactions(data)
        self.assertEqual(result["rejected_transactions"], 1)

    def test_duplicate_id(self):
        data = [
            {"id": "T1", "category": "food", "amount_cents": 100},
            {"id": "T1", "category": "travel", "amount_cents": 200}
        ]
        result = analyze_transactions(data)
        self.assertEqual(result["valid_transactions"], 1)
        self.assertEqual(result["total_amount_cents"], 100)

    def test_empty_id(self):
        data = [{"id": "", "category": "food", "amount_cents": 100}]
        self.assertEqual(analyze_transactions(data)["rejected_transactions"], 1)

    def test_empty_category(self):
        data = [{"id": "T1", "category": "", "amount_cents": 100}]
        self.assertEqual(analyze_transactions(data)["rejected_transactions"], 1)

    def test_missing_field(self):
        data = [{"id": "T1", "category": "food"}]
        self.assertEqual(analyze_transactions(data)["rejected_transactions"], 1)

    def test_zero_amount(self):
        data = [{"id": "T1", "category": "food", "amount_cents": 0}]
        result = analyze_transactions(data)
        self.assertEqual(result["valid_transactions"], 1)
        self.assertEqual(result["total_amount_cents"], 0)

    def test_non_integer_amount(self):
        data = [{"id": "T1", "category": "food", "amount_cents": 10.5}]
        self.assertEqual(analyze_transactions(data)["rejected_transactions"], 1)

    def test_category_totals(self):
        data = [
            {"id": "T1", "category": "food", "amount_cents": 100},
            {"id": "T2", "category": "food", "amount_cents": 200},
            {"id": "T3", "category": "books", "amount_cents": 300}
        ]
        result = analyze_transactions(data)
        self.assertEqual(
            result["category_totals"],
            {"books": 300, "food": 300}
        )


if __name__ == "__main__":
    unittest.main()
