def flatten(elements):
    ret = []

    for e in elements:
        if isinstance(e, (list,)):
            ret.extend(flatten(e))
        else:
            ret.append(e)

    return ret

