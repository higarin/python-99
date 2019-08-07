def decode(a):
    b = []

    for i in a:
        if type(i) is list:
            b += [i[1] for y in range(i[0])]
        elif type(i) is int:
            b.append(i)

    return b
