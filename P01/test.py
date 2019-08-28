import sys
sys.path.append('../')

import unittest
from P01.main import last


class Test(unittest.TestCase):
    def test_empty_list(self):
        with self.assertRaises(IndexError):
            last([])

    def test(self):
        self.assertEqual(last(["python"]), "python")
        self.assertEqual(last(['p', 'y', 't', 'h', 'o', 'n']), 'n')


if __name__ == "__main__":
    unittest.main()
