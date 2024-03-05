print('______Задача_1______')
# Напишите функцию, которая заполняет файл (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

# Вариант 1
print('__вариант_1__')
import random


def feel_numbers_1(filename, num_lines):
    with open(filename, 'a') as file:
        for _ in range(num_lines):
            int_num = random.randint(-1000.0, 1000.0)
            float_num = random.uniform(-1000, 1000)
            line = f'{int_num} | {float_num}\n'
            file.write(line)


# feel_numbers_1('num_1.txt', 10)

# Вариант 2
print('__вариант_2__')
from pathlib import Path
from random import randint, uniform

MIN_NUM = -1000
MAX_NUM = 1000


def feel_numbers_2(file_name: str | Path, count: int) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(count):
            f.write(f'{randint(MIN_NUM, MAX_NUM)}|{uniform(MIN_NUM, MAX_NUM)}\n')


print('______Задача_2______')
"""
Напишите функцию, которая генерирует
псевдоимена.
✔ Имя должно начинаться с заглавной буквы,
состоять из 4-7 букв, среди которых
обязательно должны быть гласные.
✔ Полученные имена сохраните в файл.
"""
# Вариант 1
print('__вариант_1__')
from random import randint, choice

from pathlib import Path
from random import randint, choice

vowel_letters = set('aoyieu')
min_letter = ord('a')
max_letter = ord('z')


def get_names(count: int, min_len: int, max_len: int, file_1: Path):
    with open(file_1, 'a', encoding='utf-8') as f_1:
        for _ in range(count):
            name = [chr(randint(min_letter, max_letter)) for _ in range(randint(min_len, max_len))]
            if len(vowel_letters.intersection(set(name))) == 0:
                name[randint(0, len(name) - 1)] = choice(list(vowel_letters))
            name = ''.join(name)
            f_1.write((f'{name.capitalize()}\n'))


# Вариант 2
print('__вариант_2__')
from pathlib import Path
from random import randint, choice

VOWES = 'aeiouy'
CONSTONATS = 'bcdfghjklmnqrstvwxz'


def name_gen(count: int, str_len_min: int, str_len_max: int, file_2: Path) -> None:
    with open(file_2, 'a', encoding='utf-8') as f_2:
        for _ in range(count):
            rad_string = ''.join(choice(VOWES) if i % 3 == 0 else choice(CONSTONATS)
                                 for i in range(randint(str_len_min, str_len_max)))
            f_2.write(f'{rad_string.capitalize()}\n')


print('______Задача_3______')
"""Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
Перемножьте пары чисел. В новый файл сохраните имя и произведение:
если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
В результирующем файле должно быть столько же строк, сколько в более длинном файле.
При достижении конца более короткого файла, возвращайтесь в его начало."""
# Вариант 1
print('__вариант_1__')

from pathlib import Path


def mult_value_file(file_3: Path, file_4: Path, file_5: Path):
    with open(file_3, 'r', encoding='utf-8') as numbers, \
            open(file_4, 'r', encoding='utf-8') as names, \
            open(file_5, 'w', encoding='utf-8') as output:
        lines_num = numbers.readlines()
        lines_name = names.readlines()
        max_lines = max(len(lines_name), len(lines_num))
        for i in range(max_lines):
            line_num = lines_num[i % len(lines_num)].strip()
            line_name = lines_name[i % len(lines_name)].strip()
            num_1, num_2 = line_num.split('|')
            mult_1 = int(num_1) * float(num_2)
            if mult_1 < 0:
                line_name = line_name.lower()
                mult_1 = abs(mult_1)
            else:
                line_name = line_name.upper()
                mult_1 = round(mult_1)
            output.write(f'{line_name} | {mult_1}\n')


# Вариант 2
print('__вариант_2__')

from pathlib import Path
from typing import TextIO


def _read_or_begin(fd: TextIO) -> str:
    line = fd.readline()
    if not line:
        fd.seek(0)
        return _read_or_begin(fd)
    return line[:-1]


def two_files_in_one(numbers: Path, words: Path, result: Path) -> None:
    with (open(numbers, 'r', encoding='utf-8') as f_num,
          open(words, 'r', encoding='utf-8') as f_word,
          open(result, 'w', encoding='utf-8') as f_res
          ):
        len_numbers = sum(1 for _ in f_num)
        len_word = sum(1 for _ in f_word)
        for _ in range(max(len_numbers, len_word)):
            num = _read_or_begin(f_num)
            word = _read_or_begin(f_word)
            num_a, num_b = num.split('|')
            mult = int(num_a) * float(num_b)
            if mult < 0:
                f_res.write(f'{word.lower()} | {abs(mult)}\n')
            elif mult > 0:
                f_res.write(f'{word.upper()} | {round(mult)}\n')


print('______Задача_4______')
"""Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""

import os
import shutil


def sort_files_by_extension(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = os.path.splitext(file)[1]

            if file_extension.lower() in ('.jpg', '.jpeg', '.png', '.gif'):
                # папку с изображениями
                image_folder = os.path.join(destination_folder, 'Изображения')
                if not os.path.exists(image_folder):
                    os.makedirs(image_folder)
                shutil.move(file_path, os.path.join(image_folder, file))

            elif file_extension.lower() in ('.txt', '.doc', '.pdf'):
                # папку с текстовыми документами
                text_folder = os.path.join(destination_folder, 'Текст')
                if not os.path.exists(text_folder):
                    os.makedirs(text_folder)
                shutil.move(file_path, os.path.join(text_folder, file))

            elif file_extension.lower() in ('.mp4', '.avi', '.mkv'):
                # в папку с видео
                video_folder = os.path.join(destination_folder, 'Видео')
                if not os.path.exists(video_folder):
                    os.makedirs(video_folder)
                shutil.move(file_path, os.path.join(video_folder, file))


sort_files_by_extension("source", "destination")

print('______Задача_5______')
"""Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры:
расширение
минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона."""

# from random import choice, randint
# from string import ascii_letters, digits
#
#
# def make_files(extension: str, min_name: int = 6, max_name: int = 30,
#                min_size: int = 256, max_size: int = 4096, count: int = 42):
#     for _ in range(count):
#         name = ''.join(choices(ascii_letters + digits, k=randint(min_name, max_name)))
#         data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
#         with open(f'{name}.{extension}', 'wb') as f:
#             f.write(data)
