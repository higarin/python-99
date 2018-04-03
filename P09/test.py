
import unittest
import main

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.pack([]), [[]])
        self.assertEqual(main.pack([1, 2, 3]), [[1], [2], [3]])
        self.assertEqual(main.pack([1, 1, 1, 1, 2, 3, 3, 1, 1, 4, 5, 5, 5, 5]), [[1, 1 , 1, 1], [2], [3, 3],[1, 1], [4], [5, 5, 5, 5]])


if __name__ == "__main__":
    unittest.main()

