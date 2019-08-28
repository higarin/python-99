import sys
sys.path.append('../')

import unittest
from P15.main import duplicate


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(duplicate(['p', 'y', 't', 'h', 'o', 'n'], 1), ['p', 'y', 't', 'h', 'o', 'n'])
        self.assertEqual(duplicate(['p', 'y', 't', 'h', 'o', 'n'], 2),
            ['p', 'p', 'y', 'y', 't', 't', 'h', 'h', 'o', 'o', 'n', 'n'])


if __name__ == "__main__":
    unittest.main()
