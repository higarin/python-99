import sys
sys.path.append('../')

from P09.main import pack


def encode_modified(elements):
    ret = pack(elements)

    encoded = []
    for e in ret:
        size = len(e)
        value = e[0]
        if size > 1:
            encoded.append([size, value])
        else:
            encoded.append(value)

    return encoded
