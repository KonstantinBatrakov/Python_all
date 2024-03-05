# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.


with open('file_5.txt', 'w') as file_obj:
    numb = input('Введите цифры через пробел \n')
    file_obj.writelines(numb)

with open('file_5.txt', 'r') as file_obj:
    list_1 = file_obj.read().split()
    print(list)
    res_sum = 0
    for el in list_1:
        res_sum += float(el)
    print(res_sum)
