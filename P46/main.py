# -*- coding: utf-8 -*-


# 論理積
def AND(x, y):
    return x and y


# 論理和
def OR(x, y):
    return x or y


# 否定論理積
def NAND(x, y):
    return not AND(x, y)


# 否定論理和
def NOR(x, y):
    return not OR(x, y)


# 排他的論理和
def XOR(x, y):
    return AND(OR(x, y), not AND(x, y))


# 論理包含
def IMP(x, y):
    return OR(not x, y)


# 同値
def EQ(x, y):
    return x == y


def table(expression):
    ret = []

    for a in [True, False]:
        for b in [True, False]:
            result = expression(a, b)
            ret.append([a, b, result])

    return ret
