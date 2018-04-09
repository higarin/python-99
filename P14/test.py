import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.duplicate([1, 2, 3, 3, 4]), [1, 1, 2, 2, 3, 3, 3, 3, 4, 4])


if __name__ == "__main__":
    unittest.main()
