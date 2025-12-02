# test_safe_calculator.py

import unittest
from simpleeval import simple_eval

class TestSafeCalculator(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(simple_eval("2 + 3"), 5)
        self.assertAlmostEqual(simple_eval("10 / 4"), 2.5)
        self.assertEqual(simple_eval("2 * 3 + 5"), 11)

    def test_precedence(self):
        self.assertEqual(simple_eval("2 + 3 * 4"), 14)
        self.assertEqual(simple_eval("(2 + 3) * 4"), 20)

    def test_power_modulo(self):
        self.assertEqual(simple_eval("2 ** 3"), 8)
        self.assertEqual(simple_eval("10 % 3"), 1)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            simple_eval("10 / 0")

    def test_invalid(self):
        with self.assertRaises(Exception):
            simple_eval("import os; os.system('ls')")

if __name__ == "__main__":
    unittest.main()
