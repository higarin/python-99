import math

def is_coprime(num1,num2):
    gcd = math.gcd(num1,num2)
    if gcd == 1:
        return True
    else:
        return False
