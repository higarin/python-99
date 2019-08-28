import sys
sys.path.append('../')

import unittest
from P33.main import is_coprime


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_coprime(35, 64), True)
        self.assertEqual(is_coprime(36, 63), False)


if __name__ == "__main__":
    unittest.main()
