import unittest

import main


class Test(unittest.TestCase):
    def test_5C2(self):
        self.assertCountEqual(main.combination(2, [1, 2, 3, 4, 5]),
                              [
                                  [1, 2],
                                  [1, 3],
                                  [1, 4],
                                  [1, 5],
                                  [2, 3],
                                  [2, 4],
                                  [2, 5],
                                  [3, 4],
                                  [3, 5],
                                  [4, 5],
                              ])

    def test_5C3(self):
        self.assertCountEqual(main.combination(3, [1, 2, 3, 4, 5]),
                              [
                                  [1, 2, 3],
                                  [1, 2, 4],
                                  [1, 2, 5],
                                  [1, 3, 4],
                                  [1, 3, 5],
                                  [1, 4, 5],
                                  [2, 3, 4],
                                  [2, 3, 5],
                                  [2, 4, 5],
                                  [3, 4, 5],
                              ])

    def test_5C4(self):
        self.assertCountEqual(main.combination(4, [1, 2, 3, 4, 5]),
                              [
                                  [1, 2, 3, 4],
                                  [1, 2, 3, 5],
                                  [1, 2, 4, 5],
                                  [1, 3, 4, 5],
                                  [2, 3, 4, 5],
                              ])

    def test_5C5(self):
        self.assertCountEqual(main.combination(5, [1, 2, 3, 4, 5]),
                              [
                                  [1, 2, 3, 4, 5],
                              ])


if __name__ == "__main__":
    unittest.main()
