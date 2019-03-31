"""
Unit tests for the calculator library
"""

import calculator as calc

import unittest

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calc.add(1, 3), 4)

    def test_subtraction(self):
        self.assertEqual(calc.sub(5, 2), 3)

    def test_multiplication(self):
        self.assertEqual(calc.mult(2, 3), 6)

    def test_division(self):
        self.assertEqual(calc.div(6, 2), 3)

if __name__ == '__main__':
    unittest.main()
