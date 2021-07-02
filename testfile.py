import unittest
from math.py import add

class testadd(unittest.testadd):
    def test_function1(self):
        self.assertEqual(add(3,8),0)
        self.assertEqual(add(3,8),11)

if __name__ == '__main__':
    unittest.main()