def encode(a):
    i = 0
    b = []
    c = []

    while len(a) > 0:
        if len(a) == 1:
            b.append([a[0]])
            break
        if a[i]== a[i + 1]:
            i += 1
        if len(a) == i + 1:
            b.append(a)
            break
        elif a[i] != a[i + 1]:
            b.append(a[0:i + 1])
            del a[0:i + 1]
            i = 0

    for i in b:
        c.append([len(i),i[0]])
    return c
