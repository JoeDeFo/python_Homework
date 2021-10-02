"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.
"""

word = input('Введите строку: ')
test_list = []
number = 1
for i in range(word.count(' ') + 1):
    test_list = word.split()
    if len(str(test_list)) <= 10:
        print(f'{number} {test_list [i]}')
        number += 1
    else:
        print(f'{number} {test_list [i] [0:10]}')
        number += 1

