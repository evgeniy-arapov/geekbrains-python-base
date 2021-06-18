numbers = []
while len(numbers) < 3:
    user_input = int(input('Введите число: '))
    numbers.append(user_input)

print(min(numbers))
print(max(numbers))
print(sum(numbers))
