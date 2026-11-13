import unittest
from transaction_analyzer import analyze_transactions

class TestTransactionAnalyzer(unittest.TestCase):
    def test_empty_id(self):
        data = [{"id": "", "category": "food", "amount_cents": 100}]
        self.assertEqual(analyze_transactions(data)["rejected_transactions"], 1)

if __name__ == '__main__':
    unittest.main()
