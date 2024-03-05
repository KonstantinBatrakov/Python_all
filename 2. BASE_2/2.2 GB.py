# 2. Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

# Решение №1
q = int(input("Из скольких элементов список?\n\t Введите количество: "))
my_lst = []
for i in range(q):
    my_lst.append(input(f"Элемент # {i + 1} : "))
print(f"Ваш текущий список:\n{my_lst}")
for x in range(0, (len(my_lst) - 1), 2):
    my_lst[x], my_lst[x + 1] = my_lst[x + 1], my_lst[x]
print(f"Ваш измененный список:\n{my_lst}")

# Решение №2
my_list = input("введите числа через пробел: ").split(' ')
print(f"now_len:\n{my_list}")
i, j = 0, 1
while j < len(my_list):
    my_list[i], my_list[j] = my_list[j], my_list[i]
    i += 2
    j += 2
print(f"after_list:\n{my_list}")
print("after_list:", my_list)
