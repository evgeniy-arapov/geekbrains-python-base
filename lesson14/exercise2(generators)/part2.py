import random

numbers = [random.randint(1, 100) for i in range(1, 10)]

print(numbers)


numbers = [1, 2, 3, -4]

numbers = [number ** 2 for number in numbers]

print(numbers)

names = ['Артурт', 'Генадий', 'Виолета', 'Тимофей']

names = [name for name in names if name.startswith('А')]

print(names)
