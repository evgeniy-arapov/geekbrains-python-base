numbers = [2, 3, -5, 7, 1, -34, -6, 7, 34, -5, 5]

result = [number for number in numbers if number > 0]

print(result)
print(type(result))

pairs = {(1, 'a'), (2, 'b'), (3, 'c')}

result = {pair[0]: pair[1] for pair in pairs}

print(result)
print(type(result))

