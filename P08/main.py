def compress(a):
    b = []
    for i in range(len(a)-1):
        if a[i] != a[i + 1]:
            b += a[i],a[i + 1]
            if len(b)> 2 and b[-2] == b[-3]:
                del(b[-3])
    return b
