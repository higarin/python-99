import sys
sys.path.append('../')

import unittest
from P09.main import pack


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pack([]), [])
        self.assertEqual(pack([1, 2, 3]), [[1], [2], [3]])
        self.assertEqual(pack([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]),
                         [[1, 1, 1, 1], [2], [3, 3], [1, 1], [4], [5, 5, 5, 5]])


if __name__ == "__main__":
    unittest.main()
