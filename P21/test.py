import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.insert_at(0, -1, [1, 2, 3, 4]), [-1, 1, 2, 3, 4])
        self.assertEqual(main.insert_at(2, -1, [1, 2, 3, 4]), [1, 2, -1, 3, 4])
        self.assertEqual(main.insert_at(4, -1, [1, 2, 3, 4]), [1, 2, 3, 4, -1])


if __name__ == "__main__":
    unittest.main()
