def encode_direct(elements):
    ret = []

    for e in elements:
        if ret and ret[-1] == e:
            ret[-1] = [2, e]
        elif ret and isinstance(ret[-1], list) and ret[-1][1] == e:
            ret[-1][0] += 1
        else:
            ret.append(e)

    return ret
