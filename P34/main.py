import math

def totient_phi(num):
    gcd_list = []
    for i in range(1,num):   
        if math.gcd(i,num) == 1:
            gcd_list.append(i)
    return len(gcd_list)
