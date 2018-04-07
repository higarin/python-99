import unittest
import main


class Test(unittest.TestCase):
    def test_size_0(self):
        with self.assertRaises(IndexError):
            main.penultimate([])

    def test_size_1(self):
        with self.assertRaises(IndexError):
            main.penultimate([1])

    def test_size_2(self):
        self.assertEqual(main.penultimate([1, 2]), 1)

    def test_size_3(self):
        self.assertEqual(main.penultimate([1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
