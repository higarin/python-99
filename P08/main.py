def compress(a):
    b = 0
    while len(a)-1 > b:
        if a[b] == a[b+1]:
            del a[b]
        else:
            b += 1
    return a
