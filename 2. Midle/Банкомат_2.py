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

Tax = 1.015
TMin = 30
TMax = 600
Percent = 1.03
Rich = 5000000
CTax = 1.1

OperDict = {}


def menuAtm():
    print('--' * 20)
    print(f'Показать остаток счете, нажмите : 1')
    print(f'Снять со счета, нажмите         : 2')
    print(f'Положить на счет, нажмите       : 3')
    print(f'История операций                : 4')
    print('--' * 20)
    print(f'Для выхода нажмите              : 0')
    print('--' * 20)


def log(OperDict, bool, opCount, cash):
    if bool:
        OperDict[opCount] = f'на счет добавлено {cash}'
    else:
        OperDict[opCount] = f'снято со счета {cash}'
    return OperDict


def printLog(OperDict):
    for k, v in OperDict.items():
        print(k, v)


def invoiceOut(money, opCount):
    printInvoice(money)
    while True:
        if money > Rich:
            money = money - (money - money / CTax)
        print(f'Сколько хотите снять со счета? ')
        outMoney = int(input(' ->> '))
        if outMoney > money:
            print(f'{printInvoice(money)}, введите сумму корректно')
            continue
        if TMax > outMoney - outMoney / Tax > TMin:
            money = money - (outMoney - outMoney / Tax)
            break
        elif TMin > outMoney - outMoney / Tax:
            money = money - (outMoney - TMin)
            if money <= 0:
                print(f'Превышен лимит счёта, введите другую сумму')
                continue
            break
        else:
            outMoney = outMoney - TMax
            money = money - outMoney - TMin
            if money <= 0:
                print(f'Превышен лимит счёта, введите другую сумму')
                continue
            break
    opCount += 1
    log(OperDict, False, opCount, outMoney)
    return money, opCount


def invoiceIn(money, opCount):
    while True:
        if opCount % 3 == 0: money = money * Percent
        print(f'Сколько хотите положить? (кратно 50)')
        moneyIn = int(input(' ->> '))
        if moneyIn % 50 != 0:
            print(f'Введите сумму кратную 50 ')
            continue
        elif moneyIn % 50 == 0:
            money = money + moneyIn
            opCount += 1
            break
    log(OperDict, True, opCount, moneyIn)
    return money, opCount


def printInvoice(money):
    print(f'На вашем счету: {round(money, 2)} у.е')


money = 0
opCount = 0
while True:
    menuAtm()
    button = input(' ->> ')
    if button == '1':
        printInvoice(money)
    elif button == '2':
        money, opCount = invoiceOut(money, opCount)
    elif button == '3':
        money, opCount = invoiceIn(money, opCount)
    elif button == '4':
        printLog(OperDict)
    elif button == '0':
        break
    else:
        print(f'Непонятно чего там нажали, повторите ')
