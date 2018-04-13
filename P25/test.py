import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertCountEqual(main.random_permute([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertCountEqual(main.random_permute([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
