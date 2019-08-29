import sys
sys.path.append('../')

from P09.main import pack


def encode(elements):
    ret = pack(elements)

    encoded = []
    for e in ret:
        encoded.append([len(e), e[0]])

    return encoded
