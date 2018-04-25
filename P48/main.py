import inspect


def table(expression):
    signature = inspect.signature(expression)
    parameters = signature.parameters

    conditions = [[]]
    for _ in range(len(parameters)):
        temp = []
        for condition in conditions:
            for b in [True, False]:
                temp.append(condition + [b])
        conditions = temp

    ret = []
    for condition in conditions:
        result = expression(*condition)
        ret.append(condition + [result])

    return ret
