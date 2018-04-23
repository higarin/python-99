import copy


def group(groups, elements, index=0, temp=None):
    if temp is None:
        temp = [[] for _ in range(len(groups))]

    ret = []
    for j in range(0, len(groups)):
        work = copy.deepcopy(temp)

        work[j] += [elements[index]]

        if len(work[j]) <= groups[j]:
            if index + 1 < len(elements):
                ret += group(groups, elements, index + 1, work)
            else:
                ret += [work]

    return ret


def group3(elements):
    return group([2, 3, 4], elements)
