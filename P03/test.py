import sys
sys.path.append('../')

import unittest
from P03.main import at


class Test(unittest.TestCase):
    # def test_size_0(self):
    #     with self.assertRaises(IndexError):
    #         at([], 0)

    def test_size_1(self):
        self.assertTrue(at([1], 1), 1)

    # def test_size_1_out_of_lower_limit(self):
    #     with self.assertRaises(IndexError):
    #         at([1], 0)

    def test_size_1_out_of_upper_limit(self):
        with self.assertRaises(IndexError):
            at([1], 2)

    def test_size_2(self):
        self.assertTrue(at([1, 2], 1), 1)
        self.assertTrue(at([1, 2], 2), 2)

    # def test_size_2_out_of_lower_limit(self):
    #     with self.assertRaises(IndexError):
    #         at([1, 2], 0)

    def test_size_2_out_of_upper_limit(self):
        with self.assertRaises(IndexError):
            at([1, 2], 3)

    def test_size_3(self):
        self.assertTrue(at([1, 2, 3], 1), 1)
        self.assertTrue(at([1, 2, 3], 2), 2)
        self.assertTrue(at([1, 2, 3], 3), 3)

    # def test_size_3_out_of_lower_limit(self):
    #     with self.assertRaises(IndexError):
    #         at([1, 2, 3], 0)

    def test_size_3_out_of_upper_limit(self):
        with self.assertRaises(IndexError):
            at([1, 2, 3], 4)


if __name__ == "__main__":
    unittest.main()
