def search_group(size, condition, elements, last_index=0):
    if elements.count(-1) == 0:
        return [elements]

    ret = []
    for i in range(last_index, size):
        for group_idx in range(0, len(condition)):
            work = elements.copy()
            work[i] = group_idx
            if work.count(group_idx) <= condition[group_idx]:
                ret.extend(search_group(size, condition, work, i + 1))

    return ret


def group(condition, elements):
    size = len(elements)

    cs = search_group(size, condition, [-1] * size)

    ret = []
    for c in cs:
        tmp = [[] for _ in range(len(condition))]
        for (a, b) in zip(elements, c):
            tmp[b].append(a)

        ret.append(tmp)

    return ret


def group3(elements):
    return group([2, 3, 4], elements)
