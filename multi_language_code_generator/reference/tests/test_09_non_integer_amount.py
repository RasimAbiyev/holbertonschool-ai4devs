import unittest
from transaction_analyzer import analyze_transactions

class TestTransactionAnalyzer(unittest.TestCase):
    def test_non_integer_amount(self):
        data = [{"id": "T1", "category": "food", "amount_cents": 10.5}]
        self.assertEqual(analyze_transactions(data)["rejected_transactions"], 1)

if __name__ == '__main__':
    unittest.main()
