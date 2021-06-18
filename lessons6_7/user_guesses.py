import random


def play():
    number = random.randint(1, 100)

    user_number = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}

    difficulty_level = None
    while not (difficulty_level in levels.keys()):
        if not (difficulty_level is None):
            print('За пределами диапазона.')

        try:
            difficulty_level = int(input('Выберите уровень сложности(1,2,3): '))
        except ValueError:
            print('Это должно быть число')
            break

    users_count = None
    while users_count is None:
        try:
            users_count = int(input('Количество пользователей: '))
        except ValueError:
            print('Это должно быть число')

    users = []

    for index in range(users_count):
        user_name = input(f'Имя пользователя {index + 1}: ')
        users.append(user_name)

    print(users)

    max_count = levels[difficulty_level]

    while number != user_number:
        count += 1
        print(f'\nПопытка № {count}')
        print(f'Ход пользователя {users[(count - 1) % users_count]}:')

        if count > max_count:
            print('Вы проиграли!')
            break

        try:
            user_number = int(input('Введите число: '))
        except ValueError:
            print('Это не число')
            continue

        if number > user_number:
            print('Больше')
        elif number < user_number:
            print('Меньше')
    else:
        print(f'Победил пользователь {users[(count - 1) % users_count]}!')


if __name__ == '__main__':
    play()
