import sys
sys.path.append('../')

import unittest
from P31.main import is_prime


def prime_numbers(min_number, max_number):
    if min_number > max_number:
        # swap
        min_number, max_number = max_number, min_number

    ret = []
    for i in range(min_number, max_number + 1):
        if is_prime(i):
            ret.append(i)

    return ret
