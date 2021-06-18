import random


def square_my_velo(arg):
    if arg == 13:
        raise ValueError('13 бля? Нах пошел!')
    return arg ** 2


print(square_my_velo(random.randint(1, 100)))
print(square_my_velo(13))
