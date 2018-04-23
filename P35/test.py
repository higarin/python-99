import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.prime_factors(315), [3, 3, 5, 7])
        self.assertEqual(main.prime_factors(700), [2, 2, 5, 5, 7])


if __name__ == "__main__":
    unittest.main()
