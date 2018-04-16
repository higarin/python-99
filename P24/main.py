import random


def rnd_select(count, to):
    randoms = set()
    while len(randoms) != count:
        randoms.add(random.randint(0, to))

    source = list(range(0, to + 1))
    ret: list = []
    for rnd in randoms:
        ret.append(source[rnd])

    return ret
