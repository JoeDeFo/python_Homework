"""
Необходимо создать (не программно) текстовый файл, где каждая строка
описывает учебный предмет и наличие лекционных, практических и лабораторных
занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.
"""

subj = {}
with open('task_6_text.txt') as file:
    content = file.readlines()
    for line in content:
        i = line.split()
        hours = 0
        for item in i[1:]:
            if item != '-':
                num = '0'
                for g in item:
                    if g.isdigit():
                        num += g
                    else:
                        break
                    hours += int(num)
        subj.update({i[0].strip(':'): hours})
print(subj)