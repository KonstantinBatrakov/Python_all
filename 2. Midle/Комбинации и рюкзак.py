import itertools

current_weight_1 = {}


def find_possible_combinations(items, max_weight):
    valid_combinations = []
    for r in range(1, len(items) + 1):
        for combination in itertools.combinations(items, r):
            combination_weight = sum(item[1] for item in combination)
            if combination_weight <= max_weight:
                valid_combinations.append([item[0:2] for item in combination])
    #    print(f'\n {valid_combinations} {type(valid_combinations)} \n')
    return valid_combinations


# Пример использования
items = {
    'фонарик': 1,
    'спальный мешок': 3,
    'еда': 2,
    'вода': 4,
    'тент': 2
}

max_weight = 10
i = 1
possible_combinations = find_possible_combinations(list(items.items()), max_weight)
for combination in possible_combinations:
    print(
        f'Комбинация № {i:>2}. Общая масса: {round(float(sum((dict(combination)).values())), 2):<5} {dict(combination)}')
    i += 1
