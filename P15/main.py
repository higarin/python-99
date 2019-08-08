def duplicate(a,b):
    c = []
    for i in range(len(a)):
        c += [a[i]]*b

    return c
