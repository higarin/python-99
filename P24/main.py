import random
result = []

def rnd_select(a,b):
    for i in range(a):
        result.append(random.choice(list(range(b))))

    return result
