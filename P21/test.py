import sys
sys.path.append('../')

import unittest
from P21.main import insert_at


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(insert_at(0, -1, [1, 2, 3, 4]), [-1, 1, 2, 3, 4])
        self.assertEqual(insert_at(2, -1, [1, 2, 3, 4]), [1, 2, -1, 3, 4])
        self.assertEqual(insert_at(4, -1, [1, 2, 3, 4]), [1, 2, 3, 4, -1])


if __name__ == "__main__":
    unittest.main()
