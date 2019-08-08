from itertools import combinations

def combination(a,b):
    d = []
    c = combinations(b,a)
    for i in c:
        d.append(list(i))

    return d
