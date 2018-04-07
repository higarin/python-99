import unittest
import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.compress([]), [])
        self.assertEqual(main.compress([1, 2, 3, 1, 4, 5]), [1, 2, 3, 1, 4, 5])
        self.assertEqual(main.compress([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]), [1, 2, 3, 1, 4, 5])


if __name__ == "__main__":
    unittest.main()
