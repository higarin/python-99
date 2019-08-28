import sys
sys.path.append('../')

import unittest
from P34.main import totient_phi


class Test(unittest.TestCase):
    def test(self):
        # 1, 5
        self.assertEqual(totient_phi(6), 2)
        # 1, 2, 3, 4, 5, 6
        self.assertEqual(totient_phi(7), 6)
        # 1, 3, 7, 9
        self.assertEqual(totient_phi(10), 4)
        # 1, 5, 7, 11
        self.assertEqual(totient_phi(12), 4)
        #
        self.assertEqual(totient_phi(180), 48)


if __name__ == "__main__":
    unittest.main()
