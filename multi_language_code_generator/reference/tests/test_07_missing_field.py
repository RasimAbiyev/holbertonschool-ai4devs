import unittest
from transaction_analyzer import analyze_transactions

class TestTransactionAnalyzer(unittest.TestCase):
    def test_missing_field(self):
        data = [{"id": "T1", "category": "food"}]
        self.assertEqual(analyze_transactions(data)["rejected_transactions"], 1)

if __name__ == '__main__':
    unittest.main()
