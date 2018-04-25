import unittest

from main import huffman


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(huffman(
            [['a', 45], ['b', 13], ['c', 12], ['d', 16], ['e', 9], ['f', 5]]),
            [['a', '0'], ['b', '101'], ['c', '100'], ['d', '111'], ['e', '1101'],['f', '1100']])


if __name__ == "__main__":
    unittest.main()
