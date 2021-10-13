"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def summary():
    try:
        with open("task_5_text.txt", "w+") as file:
            i = input("Введите числа через пробел: \n")
            file.writelines(i)
            number = i.split()
            print(sum(map(int, number)))
    except ValueError:
        print("Неправильно набран номер")

summary()