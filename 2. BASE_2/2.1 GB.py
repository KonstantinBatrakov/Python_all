# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

# Решение №1, которое лучше не делать. Но оно рабочее.
my_list = [1, None, 9.5, -20, True, 'False', 9 / 5, (1, 2)]
for i in range(len(my_list)):
    print(f"Тип переменной {my_list[i]}: {type(my_list[i])}")

# Решение №2.
my_list = [1, None, 9.5, -20, True, 'False', 9 / 5, (1, 2)]
for el in my_list:
    print(type(el))
