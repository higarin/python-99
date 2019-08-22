from collections import Counter

def lsort(str_list):
    return sorted(str_list,key = len)

def lfsort(str_list):
    counter = Counter([len(i) for i in str_list])
    result = sorted(str_list,key = lambda x : (counter[len(x)]))


    ###key = lambda x : (counter[len(x)])についてメモ####################################### 
    #                                                                        　　　　　#
    #xにstr_listを代入して、要素の長さをcounterに入れる。                    　　　　　#
    #この時のcounterは→Counter({2: 3, 3: 2, 4: 1, 1: 1})                    　　　　　#
    #['a','b','c']が入ったらlen(x) = 3、counter[3]は2                        　　　　　#
    #その次も同じように当てはめていって、counterの値が小さい順 = value値が小さい順？   #
    #にソートしていっている。と思われる。                                   　　　　　 #
    ####################################################################################

    return result
