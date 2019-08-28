import sys
sys.path.append('../')

import unittest
from P04.main import length


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(length([]), 0)
        self.assertEqual(length([1]), 1)
        self.assertEqual(length([1, 2]), 2)
        self.assertEqual(length([1, 2, 3]), 3)


if __name__ == "__main__":
    unittest.main()
