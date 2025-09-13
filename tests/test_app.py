import unittest
from utils.helper import greet

class TestHelper(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("GitLab"), "Hello, GitLab! Welcome to GitLab practice repo.")

if __name__ == "__main__":
    unittest.main()

return true;
