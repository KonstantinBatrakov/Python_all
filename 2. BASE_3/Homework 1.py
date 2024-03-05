# 1. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def chek_namber(a):
    if a <= 1 or a >= 100000:
        print('Число не из заданного диапазона')
    elif a <= 3:
        print('Это простое число')
    else:
        i = 2
        count = 0
        while i <= a // 2:
            if a % i == 0:
                print('Число составное')
                count += 1
                break
            else:
                i += 1
    if count == 0:
        print('Число простое')

try:
    a = int(input("Введите число от 1 до 100 000: "))
    result = chek_namber(a)
    print(result)
except ValueError:
    print("Пожалуйста, введите целое число.")

# 2. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код: from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
attempts = 10
secret_number = randint(LOWER_LIMIT, UPPER_LIMIT)

print("Добро пожаловать в игру Угадай число от 1 до 1000!")
print(f"У вас есть {attempts} попыток.")
count = 10
for attempt in range(1, attempts + 1):
    guess = int(input("Попробуйте угадать число: "))

    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляем! Вы угадали число {secret_number} за {attempt} попыток.")
        break
    count -= 1
    print(f"Осталось {count} попыток \n")
else:
    print(f"Вы исчерпали все {attempts} попыток. Загаданное число было {secret_number}.")

# 3. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def chek_tranglie(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        print('Треуголника с отрициательными сторонами не существует')
    elif a >= b + c or b >= a + c or c >= a + b:
        print('Трегуольник с такими сторонами не существует')
    elif a == b and b == c:
        print('Это равносторонний треугольник')
    elif a == b or a == c or b == c:
        print('Это равнобедренный треуголник')
    else:
        print('Это разносторонний треугольник')
try:
    a = int(input('Введите 1уюс торону треугольника: '))
    b = int(input('Введите 2ую торону треугольника: '))
    c = int(input('Введите 3ую торону треугольника: '))

    result = chek_tranglie(a, b, c)
    print(result)
except ValueError:
    print("Пожалуйста, введите числовые значения для сторон треугольника.")

# 4. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def convert_namber_1(num_1):
    base = 16
    upper = False
    digits = '0123456789abcdef'
    result = ''
    while num_1 > 0:
        result = digits[num_1 % base] + result
        num_1 //= base
    return result.upper() if upper else result


# Перевод с помощью встроенной функции hex

def convert_namber_2(num_1):
    hex_str = hex(num_1)[2:]  # Преобразование в шестнадцатеричную строку и удаление префикса '0x'
    return hex_str


try:
    num_1 = int(input("Введите целое число: "))
    result_1 = convert_namber_1(num_1)
    result_2 = convert_namber_2(num_1)
    print(f"Шестнадцатеричное представление при вычислении: {result_1}")
    print(f"Шестнадцатеричное представление с встроенной функцией hex: {result_1}")

except ValueError:
    print("Пожалуйста, введите целое число.")

# 5. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def namber_1(a1, b1, a2, b2):
    f1 = fractions.Fraction(a1, b1)
    f2 = fractions.Fraction(a2, b2)
    summ_1 = f1 + f2
    multiplication_1 = f1 * f2
    return print(f'Сумма чисел равна: {summ_1}\nПроизведение равно: {multiplication_1}')


try:
    a1, b1 = map(int, input("Введите 1ую дробь: a1/b1: ").split('/'))
    a2, b2 = map(int, input("Введите 1ую дробь: a2/b2: ").split('/'))
    print(namber_1(a1, b1, a2, b2))
except ValueError:
    print("Пожалуйста, введите дробь в формате: a/b.")

# 6. Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.
import string
from collections import Counter
import itertools
from itertools import islice

list_2 = [1, 1, 2, 2, 2, 'b', 'b', 5, 6, 7, 7, 7]
# Вариант 1
new_dict_2 = Counter(list_2)
new_list_2_1 = set()
for i in list_2:
    if new_dict_2[i] >= 2:
        if i not in new_list_2_1:
            new_list_2_1.add(i)
print(f'Входной список: {list_2}', type(list_2))
print(f'Словарь: {new_dict_2}', type(new_dict_2))
print('Символы встречающиеся более 1го раза:')
print(f'Вариант 1. {new_list_2_1}', type(new_list_2_1))

# Вариант 2 (похож на предыдущий)
new_dict_2_1 = Counter(list_2)
new_list_2_2 = [i for i in new_dict_2_1 if new_dict_2_1[i] >= 2]
print(f'Вариант 2. {new_list_2_2}', type(new_list_2_2))

# Вариант 3 (длинный путь)
new_list_2_3 = [i for i in set(list_2) if list_2.count(i) >= 2]
print(f'Вариант 3. {new_list_2_3}', type(new_list_2_3))
print('')

# 7. В большой текстовой строке подсчитать количество встречаемых слов и
# вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text_3 = '1. Списки, list. List, список является самой часто используемой коллекцией в Python. Прежде чем ' \
         'говорить о списках, я напомню, что такое массив в информатике. Массив - это ' \
         'непрерывная область в оперативной памяти компьютера, поделённая на ячейки ' \
         'одинакового размера хранящие данные одного типа. Массивы могут быть ' \
         'статическими, то есть размер массива нельзя изменить, и динамическими, когда ' \
         'размер массива изменяется при добавлении или удалении элементов. Один из ' \
         'самых больших плюсов в работе с массивами - это доступ к любой из его ячеек за ' \
         'константное время. ' \
         'Массив — упорядоченный набор элементов, каждый из которых хранит одно ' \
         'значение, идентифицируемое с помощью одного или нескольких индексов. В ' \
         'простейшем случае массив имеет постоянную длину и хранит единицы данных ' \
         'одного и того же типа, а в качестве индексов выступают целые числа. ' \
         'В информатике, список (англ. list) — это абстрактный тип данных, представляющий ' \
         'собой упорядоченный набор значений, в котором некоторое значение может ' \
         'встречаться более одного раза. Экземпляр списка является компьютерной ' \
         'реализацией математического понятия конечной последовательности. Экземпляры ' \
         'значений, находящихся в списке, называются элементами списка (англ. item, entry ' \
         'либо element); если значение встречается несколько раз, каждое вхождение ' \
         'считается отдельным элементом. '
# Заменим знаки пунктуации на пусто и разделим текст на слова.
new_text_3 = ''.join((el if el not in string.punctuation else '' for el in text_3))
# print(new_text_3)
# Сделаем список. Разделим текст на слова по пробелу.
new_text_3_1 = new_text_3.split()
# print(new_text_3_1)
# print(set(new_text_3))
# Сделаем словарь из списка по имени и количеству повторов.
new_dict_3 = Counter(new_text_3_1)
print(type(new_dict_3), new_dict_3)
# При этом он автоматически его сортирует, но можно прописать сортировку
new_dict_3_1 = dict(sorted(new_dict_3.items(), key=lambda x: x[1], reverse=True))
print(type(new_dict_3_1), new_dict_3_1)
# new_dict_3_2 = sorted(new_dict_3.items(), key=lambda x: x[1], reverse=True)
# print(type(new_dict_3_2), new_dict_3_2)
# Выберем первые 10 значений словаря
new_dict_3_10 = dict(list(new_dict_3_1.items())[:10])
print(f'Вариант 1: {new_dict_3_10}')
print('Вариант 2:')
i = 0
for key, value in new_dict_3_10.items():
    i += 1
    print(f'{i:<2}. {key:>10} = {value}')

# 8. Создайте словарь со списком вещей для похода в качестве ключа и
# их массой в качестве значения. Определите какие вещи влезут в рюкзак
# передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

things_4 = {
    "термос": 1.0,
    "спички": 0.01,
    "топор": 1.5,
    "нож": 0.4,
    "компас": 0.1,
    "повер_банк": 0.5,
    "палатка": 2.0,
    "сменка": 1.1,
    "кастрюля": 0.5,
    "вода": 1.5,
}
# Можно прописать сортировку от меньшего веса до большего
things_4_sort = dict(sorted(things_4.items(), key=lambda x: x[1], reverse=False))
print(f'Отсортированный список по весу: {things_4_sort}')
max_weight = int(input('Введите максимальный грузоподьемность рюкзака от 1 до 7: '))
weight_1 = 0
weight_2 = 0
i = 1
# print(f'При максимальном весе= {max_weight:.1f}')
print(f'{"№":<2}. {"Имя":<10} {"Масса":<5} {"Нак.Масса"}')
for key, value in things_4_sort.items():
    if weight_1 <= max_weight:
        print(f'{i:<2}. {key:>10}= {value:<5} {weight_1:.1f}')
    else:
        break
    weight_2 = weight_1
    weight_1 += value
    i += 1
print(
    f'Итого вместилось {i - 1} предметов с суммарным весом: {weight_2:.1f} не превышающие грузоподьемность рюкзака: {max_weight:.1f}')

print('\n Вариант с *Верните все возможные варианты комплектации рюкзака')
import itertools


def compbination_things_4(things_4, max_weight):
    val_compinations = []
    for r in range(1, len(things_4) + 1):
        for combination in itertools.combinations(things_4, r):
            combination_weight = sum(things_4[1] for things_4 in combination)
            if combination_weight <= max_weight:
                val_compinations.append([things_4[0:2] for things_4 in combination])
    return val_compinations


i = 1
possible_combinations = compbination_things_4(list(things_4.items()), max_weight)
for combination in possible_combinations:
    print(
        f'Комбинация № {i:>2}. Общая масса: {round(float(sum((dict(combination)).values())), 2):<5} {dict(combination)}')
    i += 1

"""
Задание 9. Напишите функцию для транспонирования матрицы
"""

print('Задание 9')


def transpose_matrix(matrix_1):
    transposed_matrix = [[0 for j in range(len(matrix_1))] for i in range(len(matrix_1[0]))]
    for i in range(len(matrix_1)):
        for j in range(len(matrix_1[0])):
            transposed_matrix[j][i] = matrix_1[i][j]
    return transposed_matrix


data_matrix = ([[1, 4], [2, 5], [3, 6]])
print(f'Исходная матрица: {data_matrix}, {type(data_matrix)}')
print(f'Размеры матрицы: i = {len(data_matrix)}, j = {len(data_matrix[0])}')
print(f'Транспонированная матрица: {transpose_matrix(data_matrix)}')

print()
print('Задание 10')
"""
Задание 10. 
Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
 где ключ — значение переданного аргумента, а значение — имя аргумента. 
 Если ключ не хешируем, используйте его строковое представление.
"""


def create_arg_dict(**kwargs):
    arg_dict = {}
    for key, value in kwargs.items():
        try:
            arg_dict[str(value)] = key
        except:
            arg_dict[str(value)] = key
    return arg_dict


# Пример использования функции
result = create_arg_dict(a=(2, 5), b="hello", c=[1, 2, 3], d=5)
print(result)

print()
print('Задание 11')

"""Задание 11.
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

Rich = 5 * 10 ** 6
Tax = 0.9
Tmin = 30
Tmax = 600
Tfix = 50
Tax_procent = 0.015
Prof_procent = 0.03
amount = 0
op_count = 0
OperDict = {}


def main():
    """
    Выбор операции
    """
    global amount
    global op_count
    while True:
        s = input('Выберите операцию (1-Пополнить, 2-Снять, 3-История операций, 4-Выход): ')
        if s not in ('1', '2', '3', '4'):
            print(f'Некорректный набор, попробуйте еще раз!!! ')
            continue
        if amount > Rich:
            # Налог на богатство
            amount = amount * Tax
            print_amount()
        if s == '1':
            fill()
            print_amount()
        elif s == '2':
            withdraw()
            print_amount()
        elif s == '3':
            history(OperDict)
        elif s == '4':
            print_amount()
            break


def print_amount():
    global amount
    print(f'На счете {amount} у.е.')


def fill():
    """
    Пополнение баланса
    """
    global amount
    global op_count
    while True:
        print(f'Укажите сумму пополнения кратно {Tfix} у.е.:')
        v = input(' ->> ')
        try:
            s = int(v)
        except ValueError:
            continue
        if not s % Tfix == 0:
            print(f'Сумма пополнения должна быть кратна {Tfix} у.е.: ')
            continue
        amount += s
        op_count += 1
        amount = amount + (percent(Prof_procent) if op_count % 3 == 0 else 0)
        log(OperDict, True, op_count, s)
        break


def withdraw():
    """
    Снятие
    """
    global amount
    global op_count
    while True:
        print(f'Укажите сумму снятия кратно {Tfix} у.е.:')
        v = input(' ->> ')
        try:
            s = int(v)
        except ValueError:
            continue
        if not s % Tfix == 0:
            print(f'Сумма пополнения должна быть кратна {Tfix} у.е.: ')
            continue
        p = percent(Tax_procent)
        # не менее 30 и не более 600 у.е.
        if p < Tmin:
            p = Tmin
        if p > Tmax:
            p = Tmax
        if amount < s + p:
            print(f'Недостаточно средств на счете')
            break
        amount = amount - s - p
        op_count += 1
        amount = amount + (percent(Prof_procent) if op_count % 3 == 0 else 0)
        log(OperDict, False, op_count, s)
        break


def percent(procent_percent):
    global amount
    return round(amount * procent_percent, 2)


def log(OperDict_log, bool_log, opCount_log, s_log):
    if bool_log:
        OperDict_log[opCount_log] = f'Внесено {s_log}'
    else:
        OperDict_log[opCount_log] = f'Снято   {s_log}'
    # return OperDict_log


def history(OperDict_histoty):
    print('История операций: ')
    for k, v in OperDict_histoty.items():
        print(k, v)


if __name__ == '__main__':
    main()

print('______Задача_12______')
"""
12. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""

import os.path


def information_file(data):
    # Разделим его на путь и имя файла
    path, full_name = os.path.split(data)
    # Разделим на имя и расширение
    # name, extension = os.path.splitext(full_name)
    name, extension = full_name.split('.')
    return path, name, extension


# string = "C:/Users/Konstantin/Downloads/Profile.pdf"
string_1 = r"\Users\Konstantin\Downloads\Profile_1.pdf"
print(f'Абсолютный путь к файлу: {string_1}')
path, name, extension = information_file(string_1)
print(f'Путь к файлу    : {path}\nИмя файла       : {name}\nРасширение файла: {extension}')
print()

print('______Задача_13______')
"""
13. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии
"""

officers = ['ALex', 'Daniil', 'Ivan']
salaryes = [10_000, 12_000, 15_000]
bonuses = ['10.2%', '12.5%', '15.5%']
print(f'Входные данные:\n{officers}\n{salaryes}\n{bonuses}')
# Вариант 1
print('__вариант_1__')
calculate_3 = {officer: salary * float(bonus.strip('%')) / 100 for officer, salary, bonus in
               zip(officers, salaryes, bonuses)}
print(calculate_3)
# Вариант 2
print('__вариант_2__')
calculate_3_2 = {officer: salary * float(bonus[:-1]) / 100 for officer, salary, bonus in
                 zip(officers, salaryes, bonuses)}
print(calculate_3_2)
print()

print('______Задача_14______')
"""
14. Создайте функцию генератор чисел Фибоначчи 
https://ru.wikipedia.org/wiki/%D0%A7%D0%B8%D1%81%D0%BB%D0%B0_%D0%A4%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8
"""

# n = int(input('Введите число: '))
n = 10


def fibonacci_generation(n):
    a_1, a_2 = 0, 1
    for x in range(n):
        yield a_1
        a_1, a_2 = a_2, a_2 + a_1


print(list(fibonacci_generation(n)))
