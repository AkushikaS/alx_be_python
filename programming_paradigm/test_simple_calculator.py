import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a new calculator before each test."""
        self.calc = SimpleCalculator()

    # ---- Addition Tests ----
    def test_addition_basic(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-3, -4), -7)

    def test_addition_large_numbers(self):
        self.assertEqual(self.calc.add(1_000_000, 2_000_000), 3_000_000)

    def test_addition_floats(self):
        self.assertAlmostEqual(self.calc.add(2.5, 0.3), 2.8)


    # ---- Subtraction Tests ----
    def test_subtraction_basic(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)

    def test_subtraction_floats(self):
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)


    # ---- Multiplication Tests ----
    def test_multiplication_basic(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 3), -9)
        self.assertEqual(self.calc.multiply(-2, -2), 4)

    def test_multiplication_by_zero(self):
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(0, 99), 0)

    def test_multiplication_floats(self):
        self.assertAlmostEqual(self.calc.multiply(2.5, 2), 5.0)


    # ---- Division Tests ----
    def test_division_basic(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertAlmostEqual(self.calc.divide(5.5, 2), 2.75)

    def test_division_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_by_zero(self):
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

    def test_division_float_zero(self):
        """Edge case: dividing zero by a number should be valid."""
        self.assertEqual(self.calc.divide(0, 5), 0)


if __name__ == "__main__":
    unittest.main()
