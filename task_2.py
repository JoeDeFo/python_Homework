"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
"""

test_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = []
for num, el in enumerate(test_list):
    if test_list[num - 1] < test_list[num]:
        new_list.append(el)

print(f'Исходный список: {test_list}')
print(f'Новый список: {new_list}')

