def remove_at(a,b):
    e = a.pop(b-1)
    return list([a] + [e])
