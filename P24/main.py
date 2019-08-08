import random

def rnd_select(a,b):
    result = []
    for i in range(a):
        result.append(random.choice((range(b+1))))

    return result

    #return [random.choice(range(b+1)) for i in range(a)]
