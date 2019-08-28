import sys
sys.path.append('../')

import unittest
from P32.main import gcd


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(1, 2), 1)
        self.assertEqual(gcd(2, 3), 1)
        self.assertEqual(gcd(2, 4), 2)
        self.assertEqual(gcd(63, 36), 9)
        self.assertEqual(gcd(36, 63), 9)


if __name__ == "__main__":
    unittest.main()
