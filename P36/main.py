def prime_factors_multi(n):
    ret = []
    count = 0

    f = 2
    while n > 1:
        if n % f == 0:
            count += 1
            n /= f
        else:
            if count > 0:
                ret.append([f, count])
                count = 0

            if f == 2:
                f += 1
            else:
                f += 2

    if count > 0:
        ret.append([f, count])

    return ret
