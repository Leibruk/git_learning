
def flatten_list(list):
    flat_list = []
    for element in list:
        if type(element) is list:
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


list = [1, [2, [3, 4]], 5, 6, [[7, 8]], 9, [10]]
print(flatten_list(list))
