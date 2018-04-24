import sys

sys.path.append('../')

from P40.main import goldbach


def goldbach_list(lower, upper, limit=0):
    ret = []
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            g = goldbach(i)
            if g and g[0] > limit:
                ret.append([i] + g)

    return ret
