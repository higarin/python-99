def is_palindrome(elements):
    size = len(elements)

    for i in range(0, int(size / 2)):
        if elements[i] != elements[(i + 1) * -1]:
            return False

    return True
