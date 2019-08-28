import sys
sys.path.append('../')

import unittest
from P07.main import flatten


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([[1], [2], [3], [4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([[1, 2, 3, 4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([[[1, 2, 3, 4, 5]]]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([1, [2, [3, 4], 5]]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
