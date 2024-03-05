# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
# (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Data:
    day_month_year = input("Введите дату в формате «день - месяц - год», например 12 - 2 - 2022: ")
#    print(day_month_year)

    @classmethod
    def extract(cls):
        my_date = [int(el) for el in cls.day_month_year.split() if el != '-']
        cls.day, cls.month, cls.year = my_date
#        print(my_date)

    @staticmethod
    def valid():

        if 1 <= Data.day <= 31:
            if 1 <= Data.month <= 12:
                if 2022 >= Data.year >= 0:
                    return f"Все в порядке"
                else:
                    return f"Неправильный год"
            else:
                return f"Неправильный месяц"
        else:
            return f"Неправильный день"


Data.extract()
print(Data.valid())

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, par0):
        self.par0 = par0


def del_na_nol(par1, par2):
    try:
        if par2 == 0:
            raise OwnError("Деление на ноль недопустимо")
        print(par1 / par2)
    except OwnError as err:
        print(err)


del_na_nol(10, 0)

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода
# пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если
# введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.

class MyOwn(Exception):
    def __init__(self, par):
        self.par = par


res_list = []

while True:
    try:
        elem = input("Введите число или exit для завершения: ")
        if elem == 'exit':
            break
        elif elem.isdigit():
            res_list.append(int(elem))
        else:
            raise MyOwn("Неправильный ввод, прочтите условие выше")
    except MyOwn as w:
        print(w.par)

print(res_list)

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class MyOwnExc(Exception):
    def __init__(self, txt):
        self.txt = txt


class OfficeEquipment:
    def __init__(self, name, price, quantity, number_of_lists):
        self.name = name
        self.price = price
        self.numb = number_of_lists
        try:
            if isinstance(quantity, int):

                self.quantity = quantity

                self.my_unit = {
                    'Модель устройства': self.name,
                    'Цена за ед': self.price,
                    'Количество': self.quantity}
            else:
                self.my_unit = {}
                raise MyOwnExc("Вы ввели не число, словарь будем пустым")

        except MyOwnExc as e:
            print(e.txt)


class Warehouse:
    goods = []

    @classmethod
    def reception(cls, obj):
        cls.goods.append(obj.my_unit)

    @classmethod
    def put_to_div(cls, obj, div):
        pass


class Printer(OfficeEquipment):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Samsung', 800, 80, 5)
Warehouse.reception(unit_1)
Warehouse.reception(unit_2)
Warehouse.reception(unit_3)

print(Warehouse.goods)

print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())

# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

class ComplexNumber:

    def __init__(self, re1, re2):
        self.re1 = re1
        self.re2 = re2

    def __add__(self, other):
        return ComplexNumber(self.re1 + other.re1, self.re2 + other.re2)

    def __mul__(self, other):
        return ComplexNumber((self.re1 * other.re1 - self.re2 * other.re2),
                             (self.re1 * other.re1 + other.re2 * self.re2))

    def __str__(self):
        return f'{self.re1}{" +" if self.re2 >= 0 else " "}{self.re2}i'


cn_1 = ComplexNumber(4, -1)
cn_2 = ComplexNumber(1, -2)
cn_3 = ComplexNumber(0, 0)

print(cn_1 + cn_2)
print(cn_1 * cn_2)
print(cn_1 + cn_2 + cn_3)
print(cn_1 * cn_2 * cn_3)
