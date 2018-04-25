def gray(n):
    ret = []

    for i in range(2 ** n):
        ret.append('{1:0{0}b}'.format(n, i ^ (i >> 1)))

    return ret
