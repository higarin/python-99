import sys
sys.path.append('../')
from P35.main import prime_factors
from collections import Counter


def prime_factors_multi(num):
    prime_factorslist = prime_factors(num)
    prime_countlist = Counter(prime_factorslist)
    result = []

    for primekey,primevalue in prime_countlist.items():
        result.append([primekey,primevalue])

    return result
