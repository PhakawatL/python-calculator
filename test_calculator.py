import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    # ---------- add() ----------
    def test_add_with_zero(self):
        self.assertEqual(self.calc.add(7, 0), 7)

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-4, 10), 6)

    # ---------- subtract() ----------
    def test_subtract_basic(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(2, 9), -7)

    # ---------- multiply() ----------
    def test_multiply_basic(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calc.multiply(5, 0), 0)

    # ---------- divide() ----------
    def test_divide_exact(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_with_remainder(self):
        self.assertEqual(self.calc.divide(5, 2), 2)

    # ---------- modulo() ----------
    def test_modulo_basic(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_no_remainder(self):
        self.assertEqual(self.calc.modulo(6, 3), 0)

if __name__ == '__main__':
    unittest.main()
