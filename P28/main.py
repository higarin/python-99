def lsort(elements):
    return sorted(elements, key=lambda e: len(e))


def lfsort(elements):
    work = {}

    for e in elements:
        size = len(e)

        if size not in work:
            work[size] = [e]
        else:
            work[size].append(e)

    sort_result = sorted(work.items(), key=lambda x: len(x[1]))

    ret = []
    for e in sort_result:
        ret.extend(e[1])

    return ret
