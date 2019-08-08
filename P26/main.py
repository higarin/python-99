from itertools import combinations
import pprint

def combination(a,b):
    d = []
    c = combinations(b,a)
    for i in c:
        d.append(list(i))

    return d
