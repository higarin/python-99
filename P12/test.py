import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.decode([[4, 1], 2, [2, 3], [2, 1], 4, [4, 5]]),
                         [1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5])


if __name__ == "__main__":
    unittest.main()
