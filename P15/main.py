def duplicate(elements, size):
    ret = []
    for e in elements:
        ret.extend([e] * size)

    return ret
