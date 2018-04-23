import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.is_coprime(35, 64), True)
        self.assertEqual(main.is_coprime(36, 63), False)


if __name__ == "__main__":
    unittest.main()
