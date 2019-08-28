import sys
sys.path.append('../')

import unittest
from P10.main import encode


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(encode([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]),
                         [[4, 1], [1, 2], [2, 3], [2, 1], [1, 4], [4, 5]])


if __name__ == "__main__":
    unittest.main()
