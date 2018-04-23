import sys
sys.path.append('../')

from P36.main import prime_factors_multi


def totient_phi(x):
    factors = prime_factors_multi(x)
    ret = 1

    for factor in factors:
        ret *= ((factor[0] - 1) * factor[0] ** (factor[1] - 1))

    return ret
