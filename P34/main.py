import sys
sys.path.append('../')
from P32.main import gcd


def totient_phi(num):
    count = 0
    for i in range(1,num):
        if gcd(i,num) == 1:
            count += 1
    return count
