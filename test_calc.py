"""calc.py 的測試（用 pytest 或 python -m unittest 皆可執行）"""
import unittest

from calc import add, average


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_average(self):
        self.assertEqual(average([1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
