"""
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
rus = {
    'One': "Один",
    'Two': "Два",
    'Three': "Три",
    'Four': "Четыре",
}

with open("task_4_text.txt") as file, open('new_task_4_text.txt', 'w') as new_file_1:
    content = file.readlines()
    for i in content:
        g = i.split()
        num_rus = rus.get(g[0])
        new_file_1.write(f'{i.replace(g[0], num_rus)}')