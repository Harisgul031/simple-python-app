# test.py - Test cases for app.py

import unittest
from app import add, subtract, multiply, square

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(4, 3), 12)

    def test_square(self):
        self.assertEqual(square(2), 4)
        self.assertEqual(square(-3), 9)
        self.assertEqual(square(0), 0)
        self.assertEqual(square(5), 25)

if __name__ == "__main__":
    unittest.main()
