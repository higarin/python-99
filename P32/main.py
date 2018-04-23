def gcd(x, y):
    if y > x:
        # swap
        temp = x
        x = y
        y = temp

    z = x % y

    if z == 0:
        return y
    else:
        return gcd(y, z)
