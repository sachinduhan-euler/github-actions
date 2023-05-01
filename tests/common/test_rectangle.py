import unittest
from common.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle1 = Rectangle(2, 3)
        self.rectangle2 = Rectangle(0.1, 0.2)
        self.rectangle3 = Rectangle(4, 4)
    
    def test_area(self):
        self.assertEqual(self.rectangle1.area(), 6)
        self.assertEqual(self.rectangle2.area(), 0.02)
        self.assertEqual(self.rectangle3.area(), 16)
    
    def test_perimeter(self):
        self.assertEqual(self.rectangle1.perimeter(), 10)
        self.assertEqual(self.rectangle2.perimeter(), 0.6)
        self.assertEqual(self.rectangle3.perimeter(), 16)

if __name__ == '__main__':
    unittest.main()
