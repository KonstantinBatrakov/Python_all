def div(*args):

    try:
        arg1 = int(input("Введите Делитель "))
        arg2 = int(input("Введите Делитель "))
        res = arg1 / arg2
    except ValueError:
        return 'Ошибка значения'
    except ZeroDivisionError:
        return "На ноль делить нельзя!"
    return res

print(f'result  {div()}')
print(div())