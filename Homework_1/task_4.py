"""Митрохин Антон
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

number_1 = int(input('Целое положительное число'))
max_number = 0
while number_1 > 0:
    if number_1 % 10 > max_number:
        max_number = number_1 % 10
    number_1 //= 10
print(f'Самая большая цифра в числе: {max_number}')


