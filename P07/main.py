def _flatten(elements):
    ret = []

    for e in elements:
        if isinstance(e, (list,)):
            ret.extend(_flatten(e))
        else:
            ret.append(e)

    return ret


def flatten(x):
    return _flatten(x)
