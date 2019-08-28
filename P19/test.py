import sys
sys.path.append('../')

import unittest
from P19.main import rotate


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(rotate([1, 2, 3, 4, 5, 6], 3), [4, 5, 6, 1, 2, 3])
        self.assertEqual(rotate([1, 2, 3, 4, 5, 6], -2), [5, 6, 1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
