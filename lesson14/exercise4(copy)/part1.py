import copy

list_of_vars = [1, 2, 3, 4, ['a', 'b', 'c', 'd']]

list_ravno_copy = list_of_vars

list_slice_copy = list_of_vars[:]

list_method_copy = list_of_vars.copy()

list_module_copy = copy.deepcopy(list_of_vars)

list_ravno_copy[0] *= 10
list_ravno_copy[4][0] *= 10
# Занчения меняются по ссылке
print(list_of_vars)

list_slice_copy[1] *= 10
list_slice_copy[4][1] *= 10
# Сылка, другая, первый уровень не меняется, но зачения копируются как есть,
# то есть по массивы копируются по ссылке и все вложенности уже меняются
print(list_of_vars)

list_method_copy[2] *= 10
list_method_copy[4][2] *= 10
# Идентично срезу
print(list_of_vars)

list_module_copy[3] *= 10
list_module_copy[4][3] *= 10
# Полная копия, все элементы копируется, по ссылке ничего не передается
print(list_of_vars)
