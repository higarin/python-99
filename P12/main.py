def decode(a):
    j = []

    for i in a:
        if type(i) is int:
            j.append(i)
        elif len(i) == 2:
            j.append([i[1]] * i[0])
    
    flatten = lambda x: [z for y in x for z in (flatten(y) if hasattr(y, '__iter__') and not isinstance(y, str) else (y,))]
    return flatten(j)

