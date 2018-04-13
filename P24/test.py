import unittest

import main


# FIXME: Property-based Testing
class Test(unittest.TestCase):
    def test(self):
        ret = main.rnd_select(6, 10)
        self.assertEqual(len(ret), 6)
        self.assertGreaterEqual(min(ret), 0)
        self.assertLessEqual(max(ret), 10)


if __name__ == "__main__":
    unittest.main()
