def search_combination(n, r, elements, last_index=0):
    ret = []

    for i in range(last_index, n):
        work = elements.copy()
        work[i] = True
        if work.count(True) == r:
            ret.append(work)
        else:
            ret.extend(search_combination(n, r, work, i + 1))

    return ret


def combination(r, elements):
    size = len(elements)

    cs = search_combination(size, r, [False] * size)

    ret = []
    for c in cs:
        tmp = []

        for (a, b) in zip(elements, c):
            if b:
                tmp.append(a)

        ret.append(tmp)

    return ret
