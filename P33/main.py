import sys
sys.path.append('../')

from P32.main import gcd


def is_coprime(x, y):
    return gcd(x, y) == 1
