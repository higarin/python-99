def drop(elements, n):
    ret = []
    for idx, e in enumerate(elements):
        if (idx + 1) % n != 0:
            ret.append(e)

    return ret
