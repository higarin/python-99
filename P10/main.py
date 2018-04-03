def encode(elements):
    ret = []
    tmp = []  # working

    for e in elements:
        if not tmp:
            tmp = [e]
        elif tmp and tmp[-1] != e:
            ret.append(tmp)
            tmp = [e]
        else:
            tmp.append(e)

    ret.append(tmp)

    encoded = []
    for e in ret:
        value = e[0]
        size = len(e)
        encoded.append([size, value])

    return encoded
