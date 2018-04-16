import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.remove_at(['a', 'b', 'c', 'd', 'e'], 1), [['b', 'c', 'd', 'e'], 'a'])
        self.assertEqual(main.remove_at(['a', 'b', 'c', 'd', 'e'], 3), [['a', 'b', 'd', 'e'], 'c'])
        self.assertEqual(main.remove_at(['a', 'b', 'c', 'd', 'e'], 5), [['a', 'b', 'c', 'd'], 'e'])


if __name__ == "__main__":
    unittest.main()
