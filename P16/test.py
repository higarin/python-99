import sys
sys.path.append('../')

import unittest
from P16.main import drop


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 2),
                         ['a', 'c', 'e', 'g', 'i'])
        self.assertEqual(drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 3),
                         ['a', 'b', 'd', 'e', 'g', 'h', 'j'])
        self.assertEqual(drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 4),
                         ['a', 'b', 'c', 'e', 'f', 'g', 'i', 'j'])


if __name__ == "__main__":
    unittest.main()
