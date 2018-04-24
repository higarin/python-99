import sys

sys.path.append('../')

from P39.main import prime_numbers


def goldbach(x):
    if x <= 2 or x % 2 != 0:
        return []

    primes = prime_numbers(2, x)

    for p in primes:
        diff = x - p
        if diff in primes:
            return [p, diff]
