""" Митрохин Антон
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
"""
"""1 вариант"""
number_1 = input('Введите любое целое число: ')
sum_number_1 = int(number_1) + int(number_1*2) + int(number_1*3)
print(f'Итоговая сумма: {sum_number_1}')


"""2 вариант"""

number_1 = input('Введите любое целое число: ')
sum_number_1 = (number_1 + str(str(number_1) + str(number_1)) + str(str(number_1) + str(number_1) + str(number_1)))
print(f'Итоговая сумма: {sum_number_1}')