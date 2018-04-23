def prime_numbers(min_number, max_number):
    ret = []

    if min_number > max_number:
        # swap
        temp = min_number
        min_number = max_number
        max_number = temp

    if min_number < 2:
        # min is 2
        min_number = 2

    for i in range(min_number, max_number + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            ret.append(i)

    return ret
