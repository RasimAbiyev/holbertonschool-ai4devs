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

if __name__ == '__main__':
    unittest.main()
