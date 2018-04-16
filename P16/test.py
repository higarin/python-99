import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 2),
                         ['a', 'c', 'e', 'g', 'i'])
        self.assertEqual(main.drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 3),
                         ['a', 'b', 'd', 'e', 'g', 'h', 'j'])
        self.assertEqual(main.drop(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'], 4),
                         ['a', 'b', 'c', 'e', 'f', 'g', 'i', 'j'])


if __name__ == "__main__":
    unittest.main()
