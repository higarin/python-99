def duplicate(elements):
    ret = []
    for e in elements:
        ret.extend([e] * 2)

    return ret
