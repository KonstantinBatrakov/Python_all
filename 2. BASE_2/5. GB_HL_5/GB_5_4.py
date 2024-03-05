# 4. 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

my_file = open('file_4.txt', 'r', encoding='utf-8')
print(my_file.read())

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('file_4.txt', 'r', encoding='utf-8') as file_obj:
    for line in file_obj:
        lin = line.split(' — ')
        new_file.append(rus[lin[0]] + ' — ' + lin[1])
    print(new_file)

with open('file_4_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
