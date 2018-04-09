def remove_at(elements, index):
    # pop() is Bang Method
    removed = elements.pop(index - 1)
    return [elements, removed]
