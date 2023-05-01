import unittest
from app.controller.math import MathFunctions

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(MathFunctions.add(2, 3), 5)
        self.assertEqual(MathFunctions.add(-2, 3), 1)
        self.assertEqual(MathFunctions.add(0.1, 0.2), 0.3)
    
    def test_subtract(self):
        self.assertEqual(MathFunctions.subtract(5, 3), 2)
        self.assertEqual(MathFunctions.subtract(-2, 3), -5)
        self.assertEqual(MathFunctions.subtract(0.1, 0.2), -0.1)
    
    def test_multiply(self):
        self.assertEqual(MathFunctions.multiply(2, 3), 6)
        self.assertEqual(MathFunctions.multiply(-2, 3), -6)
        self.assertEqual(MathFunctions.multiply(0.1, 0.2), 0.02)
    
    def test_divide(self):
        self.assertEqual(MathFunctions.divide(6, 3), 2)
        self.assertEqual(MathFunctions.divide(-6, 3), -2)
        self.assertAlmostEqual(MathFunctions.divide(1, 3), 0.3333333, places=6)
        with self.assertRaises(ValueError):
            MathFunctions.divide(5, 0)
    
    def test_square_root(self):
        self.assertAlmostEqual(MathFunctions.square_root(4), 2)
        self.assertAlmostEqual(MathFunctions.square_root(2), 1.4142135, places=6)
        with self.assertRaises(ValueError):
            MathFunctions.square_root(-1)

if __name__ == '__main__':
    unittest.main()
