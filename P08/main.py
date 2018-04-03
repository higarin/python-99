def compress(elements):
    ret = []

    for e in elements:
        if not ret or ret[-1] != e:
            ret.append(e)

    return ret
