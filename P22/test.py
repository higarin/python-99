import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.range_list(0, 4), [0, 1, 2, 3, 4])
        self.assertEqual(main.range_list(3, 7), [3, 4, 5, 6, 7])


if __name__ == "__main__":
    unittest.main()
