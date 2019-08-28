import sys
sys.path.append('../')

import unittest
from P39.main import prime_numbers


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(prime_numbers(0, 0), [])

        self.assertEqual(prime_numbers(0, 1), [])
        self.assertEqual(prime_numbers(1, 0), [])

        self.assertEqual(prime_numbers(0, 2), [2])
        self.assertEqual(prime_numbers(2, 0), [2])
        self.assertEqual(prime_numbers(1, 2), [2])
        self.assertEqual(prime_numbers(2, 2), [2])

        self.assertEqual(prime_numbers(0, 20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(prime_numbers(11, 18), [11, 13, 17])
        self.assertEqual(prime_numbers(12, 19), [13, 17, 19])
        self.assertEqual(prime_numbers(10, -10), [2, 3, 5, 7])


if __name__ == "__main__":
    unittest.main()
