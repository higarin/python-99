import sys
sys.path.append('../')
from P36.main import prime_factors_multi

def totient_phi(num):
    base = prime_factors_multi(num)
    formula = 0 #後ほど式を入れる

    for i in range(len(base)):
        if formula > 0:
            formula *= (base[i][0]-1) * base[i][0] ** (base[i][1]-1)
        else:
            formula = (base[i][0]-1) * base[i][0] ** (base[i][1]-1)
            
    return formula
