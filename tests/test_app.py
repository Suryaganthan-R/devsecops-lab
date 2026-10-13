import unittest
from app import greet


class TestGreet(unittest.TestCase):

    def test_valid_name(self):
        self.assertEqual(greet("Astra"), "Hello, Astra!")

    def test_empty_name(self):
        with self.assertRaises(ValueError):
            greet("")


if __name__ == "__main__":
    unittest.main()
