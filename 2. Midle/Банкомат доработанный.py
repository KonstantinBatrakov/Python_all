"""
Напишите программу банкомат.
Начальная сумма равна нулю. Допустимые действия: поплнить, снять, выйти.
Сумма попоплнения и снятия кратны 50 у.е. ПРоцент за снятие - 1,5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третей операции пополнения или снятия начисляются проценты - 3%.
Нельзя снимать больше, чем на счете. При превышении в 5 млн., вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
Любое действие выводит сумму денег.
"""
"""Задание 3.
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
