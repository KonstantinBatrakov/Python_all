# Сортировка выбором
# Создадим функцию selection_sort, которая принимает на вход список.
def selecton_sort_4(self):
    # Внутри функции создадим цикл с переменной i, которая будет исчисляться с 0 до (длины списка - 1)
    total_iteration = 0
    for i in range(0, len(self) - 1):
        # Создадим переменную smallest = i.
        smallest = i
        # Создадим внутренний цикл с переменной j от i + 1 до (длины списка).
        for j in range(i + 1, len(self)):
            # Внутри этого цикла, если j-элемент (элемент под индексом j) меньше,
            # чем элемент с индексом smallest, тогда устанавливаем smallest = j.
            total_iteration += 1
            if self[j] < self[smallest]:
                smallest = j
        # После завершения внутреннего цикла меняем местами элементы под индексами i и smallest.
        self[i], self[smallest] = self[smallest], self[i]
    print(f'{total_iteration=}')
    return self


self_4 = [1, 9, 7, 2, 3, 6, 5, 4, 8, 0]
print(f'Текущий список: {self_4=}')
print(f'Отсортированный спсиок:{selecton_sort_4(self_4)=}')
