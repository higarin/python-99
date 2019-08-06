def flatten(a):
    return [element
    for item in a
    for element in (flatten(item) if hasattr(item, '__iter__') else [item])]
