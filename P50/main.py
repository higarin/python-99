def huffman(fs):
    tree, _ = make_tree(fs)
    symbols = make_symbol(tree)
    return sorted(symbols, key=lambda x: x[0])


def make_tree(fs):
    if len(fs) == 1:
        return fs[0]

    sorted_list = sorted(fs, key=lambda x: x[1])
    (e1_s, e1_f), (e2_s, e2_f) = sorted_list.pop(0), sorted_list.pop(0)
    work = [[e1_s, e2_s], e1_f + e2_f]

    return make_tree([work] + sorted_list)


def make_symbol(tree, b=''):
    ret = []

    for idx in range(2):
        e = tree[idx]

        if isinstance(e, list):
            ret.extend(make_symbol(e, b + str(idx)))
        else:
            ret.append([e, b + str(idx)])

    return ret
