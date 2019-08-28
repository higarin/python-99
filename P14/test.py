import sys
sys.path.append('../')

import unittest
from P14.main import duplicate


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(duplicate([1, 2, 3, 3, 4]), [1, 1, 2, 2, 3, 3, 3, 3, 4, 4])


if __name__ == "__main__":
    unittest.main()
