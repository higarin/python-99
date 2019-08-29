def gcd(x, y):
    if y > x:
        # swap
        x, y = y, x

    z = x % y

    if z == 0:
        return y
    else:
        return gcd(y, z)
