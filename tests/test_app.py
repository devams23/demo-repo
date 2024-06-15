# tests/test_app.py
import unittest
import sys
import os

# Add the 'app' directory to the Python module search path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

# Now import the functions from app.py
from app import add, subtract

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(2, 5), -3)

if __name__ == "__main__":
    unittest.main()
