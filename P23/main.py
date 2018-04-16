import random


def rnd_select(elements, count):
    ret = []
    size = len(elements)

    for i in range(0, count):
        rnd = random.randint(0, size - 1)
        ret.append(elements[rnd])

    return ret
