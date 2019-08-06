def encode_modified(a):
    from main2 import pack
    d = pack(a)
    c = []

    for i in d:
        if len(i) == 1:
            c.append(i[0])
        else:
            c.append([len(i),i[0]])
    return c
