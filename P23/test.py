import unittest

import main


# FIXME: Property-based Testing
class Test(unittest.TestCase):
    def test(self):
        ret = main.rnd_select([1, 2, 3, 4], 4)
        self.assertEqual(len(ret), 4)
        self.assertGreaterEqual(min(ret), 1)
        self.assertLessEqual(max(ret), 4)


if __name__ == "__main__":
    unittest.main()
