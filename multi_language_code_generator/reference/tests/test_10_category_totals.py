import unittest
from transaction_analyzer import analyze_transactions

class TestTransactionAnalyzer(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
