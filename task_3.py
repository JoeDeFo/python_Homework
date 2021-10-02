"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""

list_of_the_months = ['winter', 'spring', 'summer', 'autumn']
dict_of_the_months = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month_number = int(input('Номер месяца: '))
if month_number == 1 or month_number == 2 or month_number == 12:
    print(list_of_the_months[0])
    print(dict_of_the_months.get(1))
elif month_number == 3 or month_number == 4 or month_number == 5:
    print(list_of_the_months[1])
    print(dict_of_the_months.get(2))
elif month_number == 6 or month_number == 7 or month_number == 8:
    print(list_of_the_months[2])
    print(dict_of_the_months.get(3))
else:
    print(list_of_the_months[3])
    print(dict_of_the_months.get(4))