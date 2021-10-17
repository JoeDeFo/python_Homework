"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("go")
    def stop(self):
        print("stop")
    def turn(self, direction):
        print(f'Машина повернула на {direction}')
    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")
        else: print("Нормальная скорость")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")
        else:
            print("Нормальная скорость")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} из полиции'
        else:
            return f'{self.name} не из полиции'


Town_Car = TownCar(120, 'yellow', 'mazda', False)
Sport_Car = SportCar(300, 'red', 'bmw', False)
Work_Car = WorkCar(30, 'black', 'opel', False)
Police_Car = PoliceCar(90, 'blue and white', 'police', True)

Town_Car.show_speed()
Sport_Car.show_speed()
Work_Car.show_speed()
Police_Car.show_speed()

Town_Car.turn("право")
print(Police_Car.police())
Work_Car.go()