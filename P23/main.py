import random


def rnd_select(elements, count):
    ret = []
    size = len(elements)

    for _ in range(count):
        rnd = random.randint(0, size - 1)
        ret.append(elements[rnd])

    return ret
