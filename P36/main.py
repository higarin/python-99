import sys
sys.path.append('../')
from P35.main import prime_factors

def prime_factors_multi(num):
    result = []
    prime_num = [2,3,5,7]
    prime_factor = prime_factors(num)
    
    for i in prime_num:
        if prime_factor.count(i) != 0:
            result.append([i,prime_factor.count(i)])

    return result
