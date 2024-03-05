"""
Main run
"""
print("Задача 2")
"""Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами."""

import os
from pathlib import Path

from Lesson_7 import feel_numbers_1
from Lesson_7 import feel_numbers_2
from Lesson_7 import get_names
from Lesson_7 import name_gen
from Lesson_7 import mult_value_file
from Lesson_7 import two_files_in_one
from homework_7 import renames

if __name__ == "__main__":
    print(__name__)
    feel_numbers_1('num_1.txt', 9)
    feel_numbers_2('num_2.txt', 10)
    get_names(8, 4, 7, Path('list_name_1.txt'))
    name_gen(10, 4, 7, Path('name_gen.txt'))
    mult_value_file(Path('num_1.txt'), Path('list_name_1.txt'), Path('result_num_name_1.txt'))
    two_files_in_one(Path('num_1.txt'), Path('list_name_1.txt'), Path('result_num_name_2.txt'))
    renames('_new_', 100, 'mdv', 'zxc', [1, 7])
