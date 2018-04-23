import sys
sys.path.append('../')

from P33.main import is_coprime


def totient_phi(x):
    ret = 0
    for i in range(1, x + 1):
        if is_coprime(i, x):
            ret += 1

    return ret
