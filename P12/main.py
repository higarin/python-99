def decode(elements):
    ret = []

    for e in elements:
        if isinstance(e, (list,)):
            ret.extend([e[1]] * e[0])
        else:
            ret.append(e)

    return ret
