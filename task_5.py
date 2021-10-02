"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться
после них.
"""
rating_list = [8, 8, 7, 5, 3, 2, 1]
rating = int(input('Введите рейтинг: '))
a = False
for index, item in enumerate(rating_list):
    if rating > item:
        rating_list.insert(index, rating)
        a = True
        break
if not a:
    rating_list.append(rating)

print(rating_list)

