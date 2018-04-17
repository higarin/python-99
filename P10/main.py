import sys
sys.path.append('../')

from P09.main import pack


def encode(elements):
    ret = pack(elements)

    encoded = []
    for e in ret:
        value = e[0]
        size = len(e)
        encoded.append([size, value])

    return encoded
