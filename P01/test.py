import unittest
import main


class Test(unittest.TestCase):
    def test_size_0(self):
        with self.assertRaises(IndexError):
            main.last([])

    def test_size_1(self):
        self.assertEqual(main.last([1]), 1)

    def test_size_2(self):
        self.assertEqual(main.last([1, 2]), 2)


if __name__ == "__main__":
    unittest.main()
