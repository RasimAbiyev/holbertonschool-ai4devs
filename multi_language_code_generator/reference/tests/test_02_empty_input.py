import unittest
from transaction_analyzer import analyze_transactions

class TestTransactionAnalyzer(unittest.TestCase):
    def test_empty_input(self):
        result = analyze_transactions([])
        self.assertEqual(result["valid_transactions"], 0)
        self.assertEqual(result["total_amount_cents"], 0)

if __name__ == '__main__':
    unittest.main()
