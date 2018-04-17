import sys
sys.path.append('../')

from P09.main import pack


def encode_modified(elements):
    ret = pack(elements)

    encoded = []
    for e in ret:
        value = e[0]
        size = len(e)
        if size > 1:
            encoded.append([size, value])
        else:
            encoded.append(value)

    return encoded
