# Сортировка Пузырьком
self_4 = [7, 9, 1, 5, 4, 3, 2, 8, 6, 0]
print(f'Текущий список: {self_4=}')


# Создадим функцию, которая принимает на вход список.
def bubble_sort(self):
    # Внутри функции создадим цикл с переменной i, которая будет исчисляться с 0 до (длины списка - 1)
    total_iteration = 0
    for i in range(0, len(self) - 1):
        # Создадим внутренний цикл с переменной j от 0 до (длины списка-1).
        for j in range(0, len(self) - 1):
            total_iteration += 1
            # Внутри этого цикла, если j-элемент (элемент под индексом j) больше,
            # чем элемент с индексом j+1, тогда меняем их местами.
            if self[j] > self[j + 1]:
                self[j], self[j + 1] = self[j + 1], self[j]
    print(f'{total_iteration=}')
    return self


print(f'Отсортированный список:{bubble_sort(self_4)=}')


# Оптимизация 1 реализации кода Python
# Мы можем предотвратить ненужную оценку, используя логический флаг и проверяя, были ли сделаны какие - либо свопы в предыдущем разделе.
def bubble_sort_swap(list1):
    # We can stop the iteration once the swap has done
    has_swapped = True
    total_iteration = 0
    while (has_swapped):
        has_swapped = False
        for i in range(len(list1) - 1):
            total_iteration += 1
            if list1[i] > list1[i + 1]:
                # Swap
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
    print(f'{total_iteration=}')
    return list1


print(f'Отсортированный список:{bubble_sort_swap(self_4)=}')


# Оптимизация реализации кода Python
# На каждой последующей итерации мы можем сравнивать на один элемент меньше, чем раньше. Точнее, на k-й итерации нужно сравнить только первые n – k + 1 элементов:
def bubble_sort_swap_2(list1):
    has_swapped = True
    total_iteration = 0
    while (has_swapped):
        has_swapped = False
        for i in range(len(list1) - total_iteration - 1):
            total_iteration += 1
            if list1[i] > list1[i + 1]:
                # Swap
                list1[i], list1[i + 1] = list1[i + 1], list1[i]
                has_swapped = True
    print(f'{total_iteration=}')
    return list1


print(f'Отсортированный список:{bubble_sort_swap_2(self_4)=}')
