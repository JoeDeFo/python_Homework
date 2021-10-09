"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import count, cycle

for el in count(int(input('Введите первое число: '))):
    print(el)
    n = 500
    if el >= n:
        break

test_list = input('Введите элементы списка: ')
n = 0
for el in cycle(test_list):
    if n >= 500:
        break
    print(el)
    n += 1





