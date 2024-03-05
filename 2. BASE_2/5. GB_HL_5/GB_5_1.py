# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

fname = input('Файл: ')
f = open(fname, 'w', encoding='utf-8')
# f = open("test.txt",'w')
while True:
    s = input()
    if s == '':
        break
    f.write(s + '\n')
f.close()

# чтение файла для проверки корректности ввода
my_f = open("test.txt", "r", encoding='utf-8')
content = my_f.readlines()
print(my_f.readlines())
my_f.close()


