def encode_modified(a):
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

    from P09.main import pack

    d = pack(a)
    c = []

    for i in d:
        if len(i) == 1:
            c.append(i[0])
        else:
            c.append([len(i),i[0]])
    return c
