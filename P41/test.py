import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.goldbach_list(9, 20),
                         [
                             [10, 3, 7],
                             [12, 5, 7],
                             [14, 3, 11],
                             [16, 3, 13],
                             [18, 5, 13],
                             [20, 3, 17]
                         ])

    def test_set_limit(self):
        self.assertEqual(main.goldbach_list(1, 2000, 50),
                         [
                             [992,  73, 919],
                             [1382, 61, 1321],
                             [1856, 67, 1789],
                             [1928, 61, 1867]
                         ])


if __name__ == "__main__":
    unittest.main()
