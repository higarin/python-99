import unittest
import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.flatten([]), [])
        self.assertEqual(main.flatten([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(main.flatten([[1, 2], [3, 4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(main.flatten([[1], [2], [3], [4], [5]]), [1, 2, 3, 4, 5])
        self.assertEqual(main.flatten([[1, 2, 3, 4, 5]]), [1, 2, 3, 4, 5])
        self.assertEqual(main.flatten([[[1, 2, 3, 4, 5]]]), [1, 2, 3, 4, 5])


if __name__ == "__main__":
    unittest.main()
