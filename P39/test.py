import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.prime_numbers(0, 20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(main.prime_numbers(10, -10), [2, 3, 5, 7])


if __name__ == "__main__":
    unittest.main()
