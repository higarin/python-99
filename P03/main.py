
def at(elements, index):
    if index <= 0:
        raise IndexError

    return elements[index - 1]

