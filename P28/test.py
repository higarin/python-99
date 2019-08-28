import sys
sys.path.append('../')

import unittest
from P28.main import lsort, lfsort


class Test(unittest.TestCase):
    def test_lsort(self):
        self.assertEqual(lsort(
            [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']]),
            [['o'], ['d', 'e'], ['d', 'e'], ['m', 'n'], ['a', 'b', 'c'], ['f', 'g', 'h'], ['i', 'j', 'k', 'l']])

    def test_lfsort(self):
        self.assertEqual(lfsort(
            [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h'], ['d', 'e'], ['i', 'j', 'k', 'l'], ['m', 'n'], ['o']]),
            [['i', 'j', 'k', 'l'], ['o'], ['a', 'b', 'c'], ['f', 'g', 'h'], ['d', 'e'], ['d', 'e'], ['m', 'n']])


if __name__ == "__main__":
    unittest.main()
