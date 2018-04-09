import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.duplicate([1, 2, 3], 1), [1, 2, 3])
        self.assertEqual(main.duplicate([1, 2, 3], 2), [1, 1, 2, 2, 3, 3])
        self.assertEqual(main.duplicate([1, 2, 3], 3), [1, 1, 1, 2, 2, 2, 3, 3, 3])


if __name__ == "__main__":
    unittest.main()
