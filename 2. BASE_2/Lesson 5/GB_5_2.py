# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

my_file = open('file_2.txt', 'r')
print(f'Содержимое файла: \n{my_file.read()}\n')

my_file = open('file_2.txt', 'r')
print(f'Количество строк в файле = {len(my_file.readlines())}')

my_file = open('file_2.txt', 'r')
for line in my_file:
    i = 0
    print(f'Кол-во слов в строке {i + 1} = {len(line.split())}')

my_file = open('file_2.txt', 'r')
content = my_file.read().split()
print(f'Общее кол-во слов = {len(content)}')
my_file.close()
