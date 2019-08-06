def encode(a):
    from P09 import pack
    b = pack(a)
    c = []

    for i in b:
        c.append([len(i),i[0]])
    return c
