import random
result = []

def rnd_select(a,b):
    for i in range(b):
        result.append(random.choice(a))

    return result
