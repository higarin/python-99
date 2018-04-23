import unittest

import main


class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(main.is_prime(0), False)
        self.assertEqual(main.is_prime(1), False)
        self.assertEqual(main.is_prime(2), True)
        self.assertEqual(main.is_prime(3), True)
        self.assertEqual(main.is_prime(4), False)
        self.assertEqual(main.is_prime(5), True)

        # Carmichael number
        self.assertEqual(main.is_prime(561), False)
        self.assertEqual(main.is_prime(1105), False)
        self.assertEqual(main.is_prime(1729), False)
        self.assertEqual(main.is_prime(2465), False)
        self.assertEqual(main.is_prime(2821), False)
        self.assertEqual(main.is_prime(6601), False)
        self.assertEqual(main.is_prime(8911), False)
        self.assertEqual(main.is_prime(10585), False)
        self.assertEqual(main.is_prime(15841), False)
        self.assertEqual(main.is_prime(29341), False)

        # ~ 1 million
        self.assertEqual(main.is_prime(999983), True)


if __name__ == "__main__":
    unittest.main()
