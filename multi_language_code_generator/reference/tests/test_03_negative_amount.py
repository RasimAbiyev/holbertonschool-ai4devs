import unittest
from transaction_analyzer import analyze_transactions

class TestTransactionAnalyzer(unittest.TestCase):
    def test_negative_amount(self):
        data = [{"id": "T1", "category": "food", "amount_cents": -500}]
        result = analyze_transactions(data)
        self.assertEqual(result["rejected_transactions"], 1)

if __name__ == '__main__':
    unittest.main()
