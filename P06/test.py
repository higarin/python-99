import unittest
import main


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(main.is_palindrome([]))
        self.assertTrue(main.is_palindrome([1]))
        self.assertTrue(main.is_palindrome([1, 2, 1]))
        self.assertTrue(main.is_palindrome([1, 2, 2, 1]))
        self.assertTrue(main.is_palindrome([1, 2, 3, 2, 1]))
        self.assertTrue(main.is_palindrome([1, 2, 3, 3, 2, 1]))

    def test_is_not_palindrome(self):
        self.assertFalse(main.is_palindrome([1, 2]))
        self.assertFalse(main.is_palindrome([1, 2, 2]))
        self.assertFalse(main.is_palindrome([1, 2, 3, 1]))


if __name__ == "__main__":
    unittest.main()
