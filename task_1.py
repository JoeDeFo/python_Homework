"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

name, output_in_hours, rate_per_hour, the_prize = argv
try:
    output_in_hours = float(output_in_hours)
    rate_per_hour = float(rate_per_hour)
    the_prize = float(the_prize)
    result = output_in_hours * rate_per_hour + the_prize
    print(f'Заработная плата сотрудника: {result}')
except ValueError:
    print('Ошибка ввода данных')



