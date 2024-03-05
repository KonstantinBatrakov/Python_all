# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

my_file = open('file_3.txt', 'r', encoding='utf-8')
print(f'Содержимое файла:\n{my_file.read()}')

with open('file_3.txt', 'r', encoding='utf-8') as my_file:
    workers = {}
    values = {}
    i = 0
    sum_values = 0
    for line in my_file:
        key, values = line.split()
        workers[key] = values
        sum_values += float(values)
        i += 1
        if float(values) < 20000:
            print(f'{key} меньше 20000')
    print(f'\nCредняя величина дохода сотрудников = {sum_values / i}')
