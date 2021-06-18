from random import choice


def return_random_choice(str_arr):
    if len(str_arr):
        return choice(str_arr)


if __name__ == '__main__':
    print(return_random_choice([1, 43, 53, 'v', 533, 3]))
    print(return_random_choice([]))
