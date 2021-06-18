try:
    raise Exception('Что-то пошло не так')
    print('Чики пики')
except Exception as err:
    print(err)
