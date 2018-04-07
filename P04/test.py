import unittest
import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.length([]), 0)
        self.assertEqual(main.length([1]), 1)
        self.assertEqual(main.length([1, 2]), 2)
        self.assertEqual(main.length([1, 2, 3]), 3)


if __name__ == "__main__":
    unittest.main()
