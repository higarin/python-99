import sys
sys.path.append('../')

import unittest
from P20.main import remove_at


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_at(['a', 'b', 'c', 'd', 'e'], 1), [['b', 'c', 'd', 'e'], 'a'])
        self.assertEqual(remove_at(['a', 'b', 'c', 'd', 'e'], 3), [['a', 'b', 'd', 'e'], 'c'])
        self.assertEqual(remove_at(['a', 'b', 'c', 'd', 'e'], 5), [['a', 'b', 'c', 'd'], 'e'])


if __name__ == "__main__":
    unittest.main()
