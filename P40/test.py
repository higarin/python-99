import sys
sys.path.append('../')

import unittest
from P40.main import goldbach


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(goldbach(4),  [2, 2])
        self.assertEqual(goldbach(6),  [3, 3])
        self.assertEqual(goldbach(8),  [3, 5])
        self.assertEqual(goldbach(10), [3, 7])
        self.assertEqual(goldbach(12), [5, 7])
        self.assertEqual(goldbach(14), [3, 11])
        self.assertEqual(goldbach(16), [3, 13])
        self.assertEqual(goldbach(18), [5, 13])
        self.assertEqual(goldbach(20), [3, 17])
        self.assertEqual(goldbach(22), [3, 19])
        self.assertEqual(goldbach(24), [5, 19])
        self.assertEqual(goldbach(26), [3, 23])
        self.assertEqual(goldbach(28), [5, 23])

        # > 2
        self.assertEqual(goldbach(0), [])
        self.assertEqual(goldbach(2), [])

        # Only Even number
        self.assertEqual(goldbach(1), [])
        self.assertEqual(goldbach(3), [])


if __name__ == "__main__":
    unittest.main()
