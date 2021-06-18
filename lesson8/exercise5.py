def my_filter(numbers, predicate):
    result = []
    for number in numbers:
        if predicate(number):
            result.append(number)
    return result


some_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(my_filter(some_numbers, lambda number: number % 2 != 0))
print(my_filter(some_numbers, lambda number: number % 2 == 0))
print(my_filter(some_numbers, lambda number: number > 4))
print(my_filter(some_numbers, lambda number: number <= 4))
