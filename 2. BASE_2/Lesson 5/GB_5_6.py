# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и
# наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open("file_6.txt") as read_file:
    res_dict = {}
    all_read_lines = read_file.readlines()
    for line in all_read_lines:
        if len(line):
            subject = line.split()
            hours_sum = 0
            for hours in subject[1:]:
                if len(hours) > 0:
                    hours_sum += int(hours.split('-')[0])
            res_dict[subject[0]] = hours_sum
    print(f"\t{res_dict}\n")

#subj = {}
#with open('file_6.txt', 'r') as init_f:
#    for line in init_f:
#        subject, lecture, practice, lab = line.split()
#        subj[subject] = int(lecture) + int(practice) + int(lab)
#    print(f'Общее количество часов по предмету -\n {subj}')
