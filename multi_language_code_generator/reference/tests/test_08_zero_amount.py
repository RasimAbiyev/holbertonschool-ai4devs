import unittest
from transaction_analyzer import analyze_transactions

class TestTransactionAnalyzer(unittest.TestCase):
    def test_zero_amount(self):
        data = [{"id": "T1", "category": "food", "amount_cents": 0}]
        result = analyze_transactions(data)
        self.assertEqual(result["valid_transactions"], 1)
        self.assertEqual(result["total_amount_cents"], 0)

if __name__ == '__main__':
    unittest.main()
