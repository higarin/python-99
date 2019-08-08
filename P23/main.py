import random

def rnd_select(a,b):
    result = []
    for i in range(b):
        result.append(random.choice(a))

    return result
