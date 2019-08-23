def prime_factors(num):
    result = []
    for i in range(2,num):
        while num % i == 0:
            num //= i
            result.append(i)
        if i * i >= num:
            result.append(num)
            break
    return result
