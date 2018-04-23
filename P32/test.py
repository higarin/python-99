import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.gcd(63, 36), 9)
        self.assertEqual(main.gcd(36, 63), 9)


if __name__ == "__main__":
    unittest.main()
