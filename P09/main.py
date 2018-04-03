def pack(elements):
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

    return ret
