import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.remove_at([1, 2, 3, 4], 2), [[1, 3, 4], 2])


if __name__ == "__main__":
    unittest.main()
