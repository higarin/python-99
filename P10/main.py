def encode(a):
    import os
    import sys

    sys.path.append(os.path.join(os.path.dirname(__file__),'..'))

    from P09 import main

    b = main.pack(a)
    c = []

    for i in b:
        c.append([len(i),i[0]])
    return c
