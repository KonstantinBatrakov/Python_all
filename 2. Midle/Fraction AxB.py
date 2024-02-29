# Задание 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
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
