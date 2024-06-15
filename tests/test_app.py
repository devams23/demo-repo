# tests/test_app.py
import unittest
from app.app import add , subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)

if __name__ == "__main__":
    unittest.main()