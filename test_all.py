
import unittest

def suite():
    suite = unittest.TestSuite()
    all_test_suite = unittest.defaultTestLoader.discover("./", pattern="test.py")

    for ts in all_test_suite:
        suite.addTest(ts)

    return suite


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity = 2).run(suite())
