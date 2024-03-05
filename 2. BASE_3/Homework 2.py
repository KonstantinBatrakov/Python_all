'''
Задание 1.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. .
'''

from Homework_6_1_1 import calendar

if __name__ == '__main__':
    print(calendar('29.02.2000'))
    print(calendar('30.02.2000'))
    print(calendar(input('Введите дату в формате 01.01.2010: ')))

'''
Задание 2.
В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку. .
'''

from sys import argv


def calendar(date: str):
    print(date)
    day_1, month_1, year_1 = map(int, date.split('.'))
    if 1 <= year_1 <= 9999:
        if month_1 in [1, 3, 5, 7, 8, 10, 12] and 1 <= day_1 <= 31:
            return "Дата существует"
        elif month_1 in [4, 6, 9, 11] and 1 <= day_1 <= 30:
            return "Дата существует"
        elif 1 <= day_1 < 30 and (year_1 % 4 == 0 and year_1 % 100 != 0 or year_1 % 400 == 0):
            return "Високосный год. Дата существует."
        else:
            "Такой даты нет"
    return "Такой даты нет"

"""
Задание 3.
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""

from Homework_6_2_1 import queen_check

if __name__ == '__main__':
    print(queen_check([(1, 6), (2, 3), (3, 5), (4, 7), (5, 1), (6, 4), (7, 2), (8, 8)]))
    print(queen_check([(1, 4), (2, 3), (3, 5), (4, 7), (5, 1), (6, 4), (7, 2), (8, 8)]))

"""
Задание 4.
Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
"""


def queen_check(position):
    n = 8
    num = []
    abc = []
    for i in range(n):
        num.append(position[i][0])
        abc.append(position[i][1])
        # print(num, abc)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if num[i] == num[j] or abc[i] == abc[j] or abs(num[i] - num[j]) == abs(abc[i] - abc[j]):
                count += 1
                # print(f'Ферзи бьют друг друга')
            else:
                count += 0
                # print('Ферзи не бьют друг друга')
    if count > 0:
        print(f'При позиции: {position}\nФерзи бьют друг друга')
    else:
        print(f'При позиции: {position}\nФерзи не бьют друг друга')
    return count

'''
Задание 5.
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''

from Homework_6_3_1 import best_position

if __name__ == '__main__':
    best_position(1)

'''
Задание 6.
Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
'''
import random


def queen_check(position):
    n = 8
    num = []
    abc = []
    for i in range(n):
        num.append(position[i][0])
        abc.append(position[i][1])
        # print(num, abc)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if num[i] == num[j] or abc[i] == abc[j] or abs(num[i] - num[j]) == abs(abc[i] - abc[j]):
                count += 1
                # print(f'Ферзи бьют друг друга')
            else:
                count += 0
                # print('Ферзи не бьют друг друга')
    return count


def best_position(count_full):
    position = []
    n = 8
    count = 1
    count_iter = 0
    print('Ждите, это может занять до 10 минут')
    while count <= count_full:
        count_iter += 1
        i = 1
        while i <= n:
            num = random.randint(1, 8)
            abc = random.randint(1, 8)
            if [num, abc] not in position:
                position.append([num, abc])
                i += 1
        #        print(position)
        if queen_check(position) == 0:
            print('Вариант = ', count_iter, position)
            count += 1
        else:
            print(f'Ждите, я в поиске! Проработано вариантов = {round(count_iter / 1_000_000, 1)} млн вариантов')
        position.clear()

