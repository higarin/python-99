import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.split([1, 2, 3, 4, 5], 0), [[], [1, 2, 3, 4, 5]])
        self.assertEqual(main.split([1, 2, 3, 4, 5], 1), [[1], [2, 3, 4, 5]])
        self.assertEqual(main.split([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4, 5]])
        self.assertEqual(main.split([1, 2, 3, 4, 5], 3), [[1, 2, 3], [4, 5]])
        self.assertEqual(main.split([1, 2, 3, 4, 5], 4), [[1, 2, 3, 4], [5]])
        self.assertEqual(main.split([1, 2, 3, 4, 5], 5), [[1, 2, 3, 4, 5], []])


if __name__ == "__main__":
    unittest.main()
