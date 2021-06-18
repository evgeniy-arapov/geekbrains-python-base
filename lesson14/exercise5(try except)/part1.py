try:
    print(1000 / зх)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print('Ошибок небыло, но зачем в таком сучае нам лезть аж сюда, если можно было все сделать в блоке трай...')
finally:
    print('А вот это полезно, закрыть файл там, или еще чего')

print('End')
