def append(to_list, content_list):
    if len(content_list) > 1:
        to_list.append([len(content_list), content_list[0]])
    else:
        to_list.append(content_list[0])


def encode_direct(elements):
    ret = []
    tmp = []  # working

    for e in elements:
        if not tmp:
            tmp = [e]
        elif tmp and tmp[-1] != e:
            append(ret, tmp)
            tmp = [e]
        else:
            tmp.append(e)

    append(ret, tmp)

    return ret
