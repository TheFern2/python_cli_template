# https://realpython.com/python-testing/

import unittest
from main import test_hello

class SampleTest(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(test_hello("John"), "Hello John")


if __name__ == '__main__':
    unittest.main()
