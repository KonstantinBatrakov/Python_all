d = {'a': 100, 'b': 5, 'c': 150, 'd': 60}
from collections import Counter
from random import choice

d_1 = choice(Counter(d).most_common(4))[0:2]
print(d_1)

import random

dict = {
    'hopper': 'DKH',
    'eleven': 'MBB',
    'mike': 'FW',
    'dustin': 'GM'
}
key = random.choice(list(dict))
print(f"Random key value pair from the dictionary is:- {key}: {dict[key]}")
# Источник: https://python-lab.ru/chto-takoe-funktsiya-random-choice-v-python
