import sys
sys.path.append('../')

import unittest
from P35.main import prime_factors


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_factors(315), [3, 3, 5, 7])
        self.assertEqual(prime_factors(700), [2, 2, 5, 5, 7])


if __name__ == "__main__":
    unittest.main()
