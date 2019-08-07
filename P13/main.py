def encode_direct(a):
    b = []
    i = 0
    count = 1

    while i < len(a)-1:
        if a[i] == a[i + 1]:
            count += 1
            i += 1
        elif a[i] != a[i + 1] and count == 1:
            b.append(a[i])
            i += 1
        else:
            b.append([count,a[i]])
            count = 1
            i += 1

    if count > 1:
        b.append([count,a[i]])
    elif count == 1:
        b.append(a[i])
    return b
