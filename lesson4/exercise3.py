some_list = [2, 3, 4, 5, 2, 2, 4, 3, 2, 3, 4, 5, 3, 33]

# Только уникальные в моем понимании
print(sorted(list(set(some_list))))

result_list = []
for el in some_list:
    if some_list.count(el) == 1:
        result_list.append(el)

# Толко уникальные в понимании препода)
print(result_list)
