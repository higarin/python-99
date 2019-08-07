def duplicate(a):
    i = 0
    for y in a[:]:
        a.insert(i,y)
        i += 2
    return a
