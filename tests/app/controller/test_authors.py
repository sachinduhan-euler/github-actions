import unittest
from app.controller.authors import RandomNameGenerator

class TestRandomNameGenerator(unittest.TestCase):
    def setUp(self):
        self.rng = RandomNameGenerator(num_names=5)
    
    def test_generate_names(self):
        names = self.rng.generate_names()
        self.assertEqual(len(names), 5)
        self.assertIsInstance(names, list)
    
    def test_generate_unique_names(self):
        unique_names = self.rng.generate_unique_names()
        self.assertEqual(len(unique_names), 5)
        self.assertIsInstance(unique_names, list)
        self.assertEqual(len(set(unique_names)), 5)
    
    def test_generate_random_pairs(self):
        pairs = self.rng.generate_random_pairs()
        self.assertEqual(len(pairs[0]), 2)
        self.assertIsInstance(pairs, list)
        for pair in pairs:
            self.assertEqual(len(pair), 2)
    
if __name__ == '__main__':
    unittest.main()
