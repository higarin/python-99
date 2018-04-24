import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.goldbach(4),  [2, 2])
        self.assertEqual(main.goldbach(6),  [3, 3])
        self.assertEqual(main.goldbach(8),  [3, 5])
        self.assertEqual(main.goldbach(10), [3, 7])
        self.assertEqual(main.goldbach(12), [5, 7])
        self.assertEqual(main.goldbach(14), [3, 11])
        self.assertEqual(main.goldbach(16), [3, 13])
        self.assertEqual(main.goldbach(18), [5, 13])
        self.assertEqual(main.goldbach(20), [3, 17])
        self.assertEqual(main.goldbach(22), [3, 19])
        self.assertEqual(main.goldbach(24), [5, 19])
        self.assertEqual(main.goldbach(26), [3, 23])
        self.assertEqual(main.goldbach(28), [5, 23])

        # > 2
        self.assertEqual(main.goldbach(0), [])
        self.assertEqual(main.goldbach(2), [])

        # Only Even number
        self.assertEqual(main.goldbach(1), [])
        self.assertEqual(main.goldbach(3), [])


if __name__ == "__main__":
    unittest.main()
