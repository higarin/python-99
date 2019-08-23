import sys
sys.path.append('../')
from P32.main import gcd

def is_coprime(num1,num2):
    gcd_num = gcd(num1,num2)
    if gcd_num == 1:
        return True
    else:
        return False
    
