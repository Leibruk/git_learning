
def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, (str, bytes)):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

list = [1, [2, [3, 4]], 5, 6, [[7, 8]], 9, [10]]

print(flatten(list))
