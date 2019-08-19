from itertools import combinations

def combination(int_split,int_list):
    result = []
    temp = combinations(int_list,int_split)
    for i in temp:
        result.append(list(i))

    return result
