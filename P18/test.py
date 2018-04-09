import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.slice([1, 2, 3, 4, 5], 1, 1), [1])
        self.assertEqual(main.slice([1, 2, 3, 4, 5], 1, 3), [1, 2, 3])
        self.assertEqual(main.slice([1, 2, 3, 4, 5], 1, 5), [1, 2, 3, 4, 5])

        self.assertEqual(main.slice([1, 2, 3, 4, 5], 3, 3), [3])
        self.assertEqual(main.slice([1, 2, 3, 4, 5], 3, 5), [3, 4, 5])

        self.assertEqual(main.slice([1, 2, 3, 4, 5], 5, 5), [5])


if __name__ == "__main__":
    unittest.main()
