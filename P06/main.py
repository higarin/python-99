def is_palindrome(elements):
    size = len(elements)

    for i in range(0, int(size / 2)):
        if elements[i] != elements[size - 1 - i]:
            return False

    return True
