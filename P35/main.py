def prime_factors(n):
    ret = []

    while n % 2 == 0:
        ret.append(2)
        n /= 2
    f = 3
    while n > 1:
        if n % f == 0:
            ret.append(f)
            n /= f
        else:
            f += 2

    return ret
