import sys
sys.path.append('../')

import unittest
from P36.main import prime_factors_multi


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_factors_multi(315), [[3, 2], [5, 1], [7, 1]])
        self.assertEqual(prime_factors_multi(700), [[2, 2], [5, 2], [7, 1]])


if __name__ == "__main__":
    unittest.main()
