some_list = [1, 2, 4, 662, 63, 27, 93, 64, 38, 93, 824, 6, 46, 5, 3, 57, 12, 36, -1, -3]

result_list = [number for number in some_list if number % 3 == 0 and number > 0 and number % 4 != 0]

print(result_list)
