import unittest

from main import gray


class Test(unittest.TestCase):
    def test_1bit(self):
        self.assertEqual(gray(1),
                         ['0',
                          '1'])

    def test_2bit(self):
        self.assertEqual(gray(2),
                         ['00',
                          '01',
                          '11',
                          '10'])

    def test_3bit(self):
        self.assertEqual(gray(3),
                         ['000',
                          '001',
                          '011',
                          '010',
                          '110',
                          '111',
                          '101',
                          '100'])


if __name__ == "__main__":
    unittest.main()
