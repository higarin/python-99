import unittest

from main import *


class Test(unittest.TestCase):
    def test_and(self):
        self.assertEqual(AND(True, True),   True)
        self.assertEqual(AND(True, False),  False)
        self.assertEqual(AND(False, True),  False)
        self.assertEqual(AND(False, False), False)

    def test_or(self):
        self.assertEqual(OR(True, True),   True)
        self.assertEqual(OR(True, False),  True)
        self.assertEqual(OR(False, True),  True)
        self.assertEqual(OR(False, False), False)

    def test_nand(self):
        self.assertEqual(NAND(True, True),   False)
        self.assertEqual(NAND(True, False),  True)
        self.assertEqual(NAND(False, True),  True)
        self.assertEqual(NAND(False, False), True)

    def test_nor(self):
        self.assertEqual(NOR(True, True),   False)
        self.assertEqual(NOR(True, False),  False)
        self.assertEqual(NOR(False, True),  False)
        self.assertEqual(NOR(False, False), True)

    def test_xor(self):
        self.assertEqual(XOR(True, True),   False)
        self.assertEqual(XOR(True, False),  True)
        self.assertEqual(XOR(False, True),  True)
        self.assertEqual(XOR(False, False), False)

    def test_imp(self):
        self.assertEqual(IMP(True, True),   True)
        self.assertEqual(IMP(True, False),  False)
        self.assertEqual(IMP(False, True),  True)
        self.assertEqual(IMP(False, False), True)

    def test_eq(self):
        self.assertEqual(EQ(True, True),   True)
        self.assertEqual(EQ(True, False),  False)
        self.assertEqual(EQ(False, True),  False)
        self.assertEqual(EQ(False, False), True)

    def test_table(self):
        self.assertEqual(table(lambda a, b: AND(a, OR(a, b))),
                         [
                             [True, True, True],
                             [True, False, True],
                             [False, True, False],
                             [False, False, False]
                         ])


if __name__ == "__main__":
    unittest.main()
