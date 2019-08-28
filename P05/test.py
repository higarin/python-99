import sys
sys.path.append('../')

import unittest
from P05.main import reverse


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(reverse([]), [])
        self.assertEqual(reverse([1]), [1])
        self.assertEqual(reverse([1, 2]), [2, 1])
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])
        self.assertEqual(reverse([1, 2, 3, 4]), [4, 3, 2, 1])


if __name__ == "__main__":
    unittest.main()
