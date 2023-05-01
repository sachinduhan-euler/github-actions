import unittest
from unittest.mock import patch
from app.main import hello

class TestHello(unittest.TestCase):
    @patch('app.main.LOGGER')
    def test_hello(self, mock_logger):
        result = hello()
        mock_logger.info.assert_called_once_with("Hello world")
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
