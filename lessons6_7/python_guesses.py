import random


def play():
    number = None

    while not isinstance(number, int) or not (1 <= number <= 100):
        number = input('Введите число от 1 до 100: ')

        try:
            number = int(number)
        except ValueError:
            print("Это не число")
            continue

        if number > 100 or number < 1:
            print('За пределами диапазона')
    else:
        print('Угадываю')

    start_border = 1
    end_border = 100

    user_input = None
    while user_input != '=':
        guesses_number = random.randint(start_border, end_border)
        print(guesses_number)
        user_input = input('Правильно? (>, <, =): ')

        if user_input == '<':
            end_border = guesses_number - 1
        if user_input == '>':
            start_border = guesses_number + 1


    else:
        print('Good game!')


if __name__ == '__main__':
    play()
