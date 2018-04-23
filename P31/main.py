import math


def is_prime(x):
    if x < 2:
        return False

    if x % 2 == 0 and x != 2:
        return False

    for d in range(2, int(math.floor(math.sqrt(x))) + 1):
        if x % d == 0:
            return False

    return True
