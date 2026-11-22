import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from validate_csv import validate


class ValidateCSVTests(unittest.TestCase):
    def test_valid_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "orders.csv"
            file.write_text("order_id,amount\n1,12\n2,20\n", encoding="utf-8")
            rows, missing = validate(file, ["order_id", "amount"])
            self.assertEqual((rows, missing), (2, []))

    def test_missing_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            file = Path(directory) / "orders.csv"
            file.write_text("id\n1\n", encoding="utf-8")
            rows, missing = validate(file, ["amount"])
            self.assertEqual(rows, 1)
            self.assertEqual(missing, ["amount"])


if __name__ == "__main__":
    unittest.main()
