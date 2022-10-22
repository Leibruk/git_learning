
list = [1, [2, [3, 4]], 5, 6, [[7, 8]], 9, [10]]

# def sorted_list(x):
#     y = []
#     for _ in x:
#         for i in sublist:
#             y.append(i)


def flatten(l):
    return [item for sublist in l for item in sublist]

# sorted_list(list)

flatten(list)