"""
Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def draw(self):
        return f'Запуск отрисовки ручкой: {self.title}'


class Pencil(Stationary):
    def draw(self):
        return f'Запуск отрисовки карандашом: {self.title}'


class Handle(Stationary):
    def draw(self):
        return f'Запуск отрисовки маркером: {self.title}.'


pen = Pen('Hellow')
pencil = Pencil('World')
handle = Handle('My name is Anton')
print(pen.draw())
print(pencil.draw())
print(handle.draw())