# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

# Example 1
text = input("Пожалуйста введите текст : ")
T = text.split()
for x, y in enumerate(T, start=1):
    if len(y) > 10:
        y = y[:10]
        print(x, y)
    else:
        print(x, y)

# Example 2
my_list = input("Please write text: ").split()
n = 1
for elem in my_list:
    if len(my_list) > 10:
        print(f"{n}. {elem[:10]}")
    else:
        print(f"{n}. {elem}")
        n += 1

# Example 3
for i, el in enumerate(my_list, 1):
    print(f"{i}) {el[:10]}")
