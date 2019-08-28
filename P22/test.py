import sys
sys.path.append('../')

import unittest
from P22.main import range_list


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(range_list(0, 4), [0, 1, 2, 3, 4])
        self.assertEqual(range_list(3, 7), [3, 4, 5, 6, 7])
        range_list(3, 100000000)


if __name__ == "__main__":
    unittest.main()
