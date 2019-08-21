def prime_factors(num):
    prime_num = [2,3,5,7]
    i = 0
    result = []

    while num > 1:
        if num % prime_num[i] == 0:
            num = int(num / prime_num[i])
            result.append(prime_num[i])
        else:
            i += 1
            if i == 4:#[2,3,5,7]で割り切れなかった場合
                result.append(2)
                num = int(num / 2)
                i = 0
    return result
