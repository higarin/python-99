import sys
sys.path.append('../')

import unittest
from P08.main import compress


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(compress([]), [])
        self.assertEqual(compress([1, 2, 3, 1, 4, 5]), [1, 2, 3, 1, 4, 5])
        self.assertEqual(compress([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]), [1, 2, 3, 1, 4, 5])


if __name__ == "__main__":
    unittest.main()
