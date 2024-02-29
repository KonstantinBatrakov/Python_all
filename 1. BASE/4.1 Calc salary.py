"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

import sys


f_obj, name_v, rate_v, hours_v = sys.argv
print(f_obj)


def calculate_salary(rate, hours):
    try:
        print(f'Сотрудник {name_v} заработал {int(rate) * int(hours) * 1.25}')
    except TypeError:
        print("Операция применена к объекту несоответствующего типа")
        exit()


calculate_salary(rate_v, hours_v)

"""
Скрипт с параметрами можно запустить средствами Пичарм
1) откройте окно Edit Configurations
2) в поле parameters укажите нужные параметры, 
например, "Иван Иванов" 100 10 для вашего выбранного скрипта
3) запустите скрипт горячими клавишами Ctrl+Shift+F10
"""