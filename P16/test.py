import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), [1, 3, 5, 7, 9])
        self.assertEqual(main.drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3), [1, 2, 4, 5, 7, 8, 10])
        self.assertEqual(main.drop([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4), [1, 2, 3, 5, 6, 7, 9, 10])


if __name__ == "__main__":
    unittest.main()
