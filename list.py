
# def flatten_list(list):
#     flat_list = []
#     for element in list:
#         if type(element) is list:
#             for item in element:
#                 flat_list.append(item)
#         else:
#             flat_list.append(element)
#     return flat_list

# print(flatten_list(list))

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
