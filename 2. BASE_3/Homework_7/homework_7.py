print("Задача 1")
"""Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из 
исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
# Вариант 1
print('__вариант_1__')

# import os
# from pathlib import Path
#
#
# def rename_groups(count_len: int, extension: str, new_extension: str, interval: list[int], new_name=''):
#     print(f'has been:\n {os.listdir()}')
#     count = 0
#     for file in os.listdir():
#         if file.endswith(extension):
#             count += 1
#             Path(file).rename(f"{file.split('.')[0][interval[0]:interval[1]]}"
#                               f"{new_name}{count:0>{count_len}}.{new_extension}")
#
#
# rename_groups(2, 'mdv', 'zxc', [0, 7], "_new_")
# print(f'has become:\n {os.listdir()}')

# Вариант 2
print('__вариант_2__')
import os


# 1 - новое имя, 2 - начальное число порядковых номеров 3 - выбор элементов по расширению
# 4 - изменить на заданное расширение, 5 - срез символов от старого имени, сохранённых в новое имя файла
def renames(new_name: str, start_count_number: int = '', current_expansion: str = '',
            next_expansion: str = '', range_char_old_name: list = []):
    print(f'has been:\n {os.listdir()}')
    # Проходимся по каждому файлу в текущей директории
    for file in os.listdir():
        if file == "main.py":
            continue
        # Создаём две переменные (количество символов старого имени, расширение старого имени)
        count_char_old_name, expansion_old_file = '', file.split('.')[-1]
        # print(count_char_old_name)
        # print(expansion_old_file)
        # Если при указании аргументов задали выбранное расширение и такого нет в списке файлов, то пропускаем итерацию
        if current_expansion != '' and expansion_old_file != current_expansion:
            continue
        # Если не указывали аргумент изменения расширения, то оставляем прежнее расширение
        if next_expansion == '':
            next_expansion = expansion_old_file
        # Если в аргументах указали с какого по какой символ нужно сохранить от старого имени, то формируем срез
        if len(range_char_old_name) == 2:
            count_char_old_name = file[range_char_old_name[0] - 1:range_char_old_name[1]:]
        # Вызываем метод переименования файла для склейки получившегося имени
        os.rename(file, f'{count_char_old_name}{new_name}{str(start_count_number)}.{next_expansion}')
        # если указано в аргументах число с которого нужно начать номерацию, то запускается счётчик
        if start_count_number != '':
            start_count_number += 1
    print(f'has become:\n {os.listdir()}')

#renames('_new_', 100, 'mdv', 'zxc', [1, 7])


