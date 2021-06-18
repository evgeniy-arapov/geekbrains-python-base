my_list_1 = [1, 1, 1, 2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3, 1]
print(sorted(my_list_1))
print(sorted(my_list_2))

# Уникальные
print(list(set(my_list_1) | set(my_list_2)))

copy_of_my_list_1 = my_list_1[:]
for list_2_item in my_list_2:
    if list_2_item in copy_of_my_list_1:
        copy_of_my_list_1.remove(list_2_item)

# Убрать по одному вхождению каждого элемента
print(copy_of_my_list_1)

copy_of_my_list_1_1 = my_list_1[:]
for item in copy_of_my_list_1_1:
    if item in my_list_2:
        copy_of_my_list_1_1.remove(item)

# Попытка убрать все вхождения элементов из второго списка. Cбивается индексация...
print(copy_of_my_list_1_1)

copy_of_my_list_1_2 = my_list_1[:]
for item in my_list_1:
    if item in my_list_2:
        copy_of_my_list_1_2.remove(item)

# убрать все вхождения элементов из второго списка
print(copy_of_my_list_1_2)
