# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep


class Trafficlight:
    _color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 4}

    @staticmethod
    def running():
        for key, value in Trafficlight._color.items():
            print(f'Светофор переключился в режим {key} \n_____Ожидание {value} секкунд')
            sleep(value)


TL = Trafficlight()
TL.running()

a = Trafficlight()
print(a.running())

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса; атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:
    __weight = 0.025

    def __init__(self, length, width, thickness):
        self._length = length
        self._width = width
        self._thickness = thickness

    def weight_all(self):
        return self._length * self._width * self._thickness * self.__weight


r1 = Road(5000, 20, 5)
print(
    f'Проектная масса дороги длиной {r1._length}м, шириной {r1._width}м и толщиной {r1._thickness}см составит: {r1.weight_all()}т')

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: float, bonus: float):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


a = Position('Иванов', 'Иван', 'Программист', 200000, 50000)
print(a.get_full_name())
print(a.position)
print(a.get_total_income())

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
# turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Разгоняемся до {speed} км/ч')

    def stop(self):
        self.speed = 0
        print('Останавливаемся')

    def turn(self, direction: str):
        if self.speed > 0:
            print(f'Поворачиваем на {direction}')
        else:
            print(f'Не можем повернуть {direction} - мы стоим на месте')

    def show_speed(self):
        print(f'Скорость автомобиля {self.speed} км/ч')


class TownCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        Car.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print('!!!Внимание! Превышение скорости, сбросьте скрорость до 60 км/ч')


class SportCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        Car.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        Car.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print('!!!Внимание! Превышение скорости, сбросьте скрорость до 40 км/ч')


class PoliceCar(Car):
    def __init__(self, color: str, name: str):
        self.color = color
        self.name = name
        Car.is_police = True

def test_drive(test):
    print(f"Начинаем тест-драйв {'полицейского' if test.is_police else 'гражданского'} автомобиля {test.name}, цвет {test.color}")
    test.go(40)
    test.show_speed()
    test.turn('направо')
    test.stop()
    test.show_speed()
    test.turn('налево')
    test.go(60)
    test.show_speed()
    test.go(120)
    test.show_speed()
    test.stop()
    print("Тест-драйв окончен", end="\n\n")


car = Car('белый', 'Kia', False)
test_drive(car)

polo = TownCar('коричневый', 'Volkswagen Polo')
test_drive(polo)

veyron = SportCar('желтый', 'Bugatti Veyron')
test_drive(veyron)

largus = WorkCar('красный', 'Lada')
test_drive(largus)

mondeo = PoliceCar('синий', 'Ford')
test_drive(mondeo)

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title: str):
        self.title = title
    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

stationery = Stationery('Гусиное перо')
stationery.draw()

pen = Pen('синяя')
pen.draw()

pencil = Pencil('HD')
pencil.draw()

handle = Handle('для доски')
handle.draw()