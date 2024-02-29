# Сортировка Вставкой
self_4 = [7, 9, 1, 5, 4, 3, 2, 8, 0, 6]
print(f'Текущий список: {self_4=}')


# Создадим функцию selection_sort, которая принимает на вход список.
def insertion_sort(self):
    # Итерация по неотсортированным вставкам
    total_iteration = 1
    for i in range(1, len(self)):
        # получаем значение элемента
        val = self[i]
        # Установим индекс j
        j = i - 1
        # Проходим по массиву в обратную сторону пока не найдем элемент больше текущего
        while j >= 0 and val < self[j]:
            # Переставляем элементы местами, чтобы получить правильную позицию
            self[j + 1] = self[j]
            j -= 1
            total_iteration += 1
        self[j + 1] = val
    print(f'{total_iteration= }')
    return self


print(f'Отсортированный список:{insertion_sort(self_4)=}')
