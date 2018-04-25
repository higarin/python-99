import sys
import unittest

from main import table

sys.path.append('../')
from P46.main import AND, OR, EQ


class Test(unittest.TestCase):
    def test_size2(self):
        self.assertEqual(table(lambda a, b: AND(a, OR(a, b))),
                         [
                             [True, True, True],
                             [True, False, True],
                             [False, True, False],
                             [False, False, False]
                         ])

    def test_size3(self):
        self.assertEqual(table(lambda a, b, c: EQ(AND(a, OR(b, c)), OR(AND(a, b), AND(a, c)))),
                         [
                             [True, True, True, True],
                             [True, True, False, True],
                             [True, False, True, True],
                             [True, False, False, True],
                             [False, True, True, True],
                             [False, True, False, True],
                             [False, False, True, True],
                             [False, False, False, True]
                         ])


if __name__ == "__main__":
    unittest.main()
