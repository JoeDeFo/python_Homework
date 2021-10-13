"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""

with open("task_3_text.txt") as file:
    text_3 = file.readlines()
    salary = 0
    employees = {}
    for i in text_3:
        i_info = i.split()
        employees.update({i_info[0]: float(i_info[1])})
        salary += float(i_info[1])

average_salary = salary / len(employees)
print(f"Средняя велечина дохода: {average_salary}")

for n, c in employees.items():
    if c < 20000:
        print(f"{n}")





