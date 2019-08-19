def is_prime(num):
    if num == 0:
        return False
    elif num == 1:
        return False
    else:#2以降の素数を処理
        for i in range(2,num):
            if num % i == 0:
                return False
        return True
