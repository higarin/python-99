def prime_factors(n):
    ret = []

    f = 2
    while n > 1:
        if n % f == 0:
            ret.append(f)
            n /= f
        elif f == 2:
            f += 1
        else:
            f += 2

    return ret
