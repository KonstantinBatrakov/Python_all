# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга,
# а значение — кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга?
# Какие вещи уникальны, есть только у одного друга? Какие вещи есть у всех друзей
# кроме одного и имя того, у кого данная вещь отсутствует?
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

hike = {
    'Goran': ("спички", "спальник", "дрова", "топор", "косметичка"),
    'Ivan': ("спальник", "спички", "вода", "еда"),
    'Tamara': ("вода", "спички", "косметичка"),
    'Kirill': ("дрова", "спички", "еда"),
}
# самый удобный сразу задать set и получить уникальный список вещей
at_all = set()
for values in hike.values():
    for value in values:
        at_all.add(value)
print(f'Уникальный спсиок всех вещей: {at_all =}')

# Собираем уникальные вещи которые только у каждого героя
unique = {}
for master_key, master_values in hike.items():
    for slave_key, slave_values in hike.items():
        if master_key != slave_key:
            if unique.get(master_key):
                unique[master_key] -= set(slave_values)
            else:
                unique[master_key] = set(master_values) - set(slave_values)
print(f'Уникальные вещи у каждого героя: {unique =}')

duplicates = set(at_all)
for value in unique.values():
    duplicates -= value
print(f'Дублирующие вещи: {duplicates = }')
for key, value in hike.items():
    # print(set(value))
    # print(duplicates)
    # print((set(value) ^ duplicates))
    # print(set(unique[key]))
    print(f'У {key} отсутствует {(set(value) ^ duplicates) - set(unique[key])}, но есть у остальных')
