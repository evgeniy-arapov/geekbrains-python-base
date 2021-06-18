result = None
print('Ну че пялишся? Хочешь по гадаю? Вот тебе сколько годков?')
while not isinstance(result, int):
    result = input()
    if result.isdigit():
        result = int(result)
    else:
        print('Че, в школу не ходил? Цифру мне говори, а то: "{}"...'.format(result.upper()))

if result < 16:
    print('Шел бы ты отсюда, сопляк!')
elif result == 16:
    print('Чет стремный ты какой-то... Ты лучше проваливай. Давай, давай!')
else:
    plus = result + 100500
    print(type(plus))

    print('Вот если даш мне денежку, то проживешь еще ', plus, ' лет')

    minus = result - (result - 1)
    print(type(minus))

    print('А коли жлобится вздумаешь, то как бы тебе ', minus, ' прожить...')

    multiply = result * 4
    print(type(multiply))

    print('Но деньжать тебе придется отбашлять, минимум ', multiply, ' вечно полезных')

    divide = result / 4
    print(type(divide))

    print('А то придется поломать тебе ', divide, ' косточек')

    divide_natural = result // 4
    print(type(divide_natural))

    print('Но, так уж и быть, у нас скидка сегодня. Поломаем только ', divide_natural)

    divide_other = result % 4
    print(type(divide_other))

    print(divide_other, ' только по массажируем')

    pow = result ** 30000
    print(type(pow))

    print('Ты не думай, что мы злые. Это спасет тебе от', pow, 'лет чистилища')

    normul = False

    pay_variants = {
        'золото': multiply / 3,
        'серебро': multiply / 2,
        'алмазы': multiply / 10,
        'вечно полезные': multiply
    }

    pay_variants_index = 0

    print('Вот варианты чем судьбу задобрить:')

    for key, val in pay_variants.items():
        print(key, val, sep=": ")

    while not normul:
        try:
            cash = int(input('Ну так че? Сикока дашь? давай в вечно полезных, а там разберемся.\n'))
        except ValueError:
            print('Да ну, че это за дичь. Высунь со рта, че ты там взял и повтори.')
            continue

        if cash < 0:
            print('Ну это уже борзость паря, а ну пошли выйдем!')
            break

        normul = (result < 18 and cash > 0) or cash >= multiply

        if not normul:
            print('Неее паря, ты чет попутал. Ты че думаешь я тут в игрушку играю? А ну давай еще разок подумай!')
    else:
        print('Я думаю паря, что это будет отличная сделка)')
