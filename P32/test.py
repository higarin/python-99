import sys
sys.path.append('../')

import unittest
from P32.main import gcd


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(gcd(63, 36), 9)
        self.assertEqual(gcd(36, 63), 9)


if __name__ == "__main__":
    unittest.main()
