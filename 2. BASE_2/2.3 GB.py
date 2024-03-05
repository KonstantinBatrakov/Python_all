# 2. 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и dict.

# Решение №1
month = int(input("Введите месяц от 1 до 12 : "))
mlist = ["зима", "весна", "лето", "осень"]
while True:
    if month > 12 or month <= 0:
        print(f"\tНеыерное число!!! \n\tПожалуйста введите число от 1 до 12!")
        month = int(input("Please enter month id from 1 to 12 : "))
        continue
    mlist = ["зима", "весна", "лето", "осень"]
    if month == 12 or (month >= 1 and month < 3):
        print(f"\tМесяц #{month}  относится к сезону '{mlist[0]}'")
        break
    elif month >= 3 and month < 6:
        print(f"\tМесяц # {month} относится к сезону '{mlist[1]}'")
        break
    elif month >= 6 and month < 9:
        print(f"\tМесяц # {month} относится к сезону '{mlist[2]}'")
        break
    elif month >= 9 and month < 12:
        print(f"\tМесяц # {month} относится к сезону '{mlist[3]}'")
        break

# Решение №2
my_dict = {1: "Winter", 2: "Winter", 3: "Spring", 4: "Spring", 5: "Spring", 6: "Summer", 7: "Summer", 8: "Summer",
           9: "Autumn", 10: "Autumn", 11: "Autumn", 12: "Winter"}
# my_dict = {"Winter": [1, 2, 12], "Spring": [3, 4, 5], "Summer": [6, 7, 8], "Autumn": [9, 10, 11]}
month_num = int(input("Input number month from 1 to 12: "))
print(f"As a Result you choice: {my_dict.get(month_num)}")
