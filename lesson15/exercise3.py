some_list = [2, 34, 53, 56, 2, 44, 5335465, -6, 6, -33, 2, 3]


def square_list(listArg):
    return [item ** 2 if item > 0 else item for item in listArg]


print(square_list(some_list))