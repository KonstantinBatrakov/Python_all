# Домашнее задание
# 1. Скачать датасет о качестве КРАСНОГО вина по ссылке. https://archive.ics.uci.edu/ml/datasets/wine+quality
# 2. На основе переменной quality с оценками вина создать новую переменную good:если quality > 5, то 1, иначе 0.
# 3. Исследовать, какие химические характеристики вина влияют на то, окажется оно хорошим или плохим, с применением не менее 5 диаграмм из урока.
# 4. Отчет сделать в формате storytelling: дополнить каждый график письменными выводами и наблюдениями.
# Импортируем нужные библиотеки
import pandas as pd
import requests
import zipfile
import io
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Считываем датасет
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

# Из них физико химические показатели следующие:
# 1 - фиксированная кислотность 2 - летучая кислотность 3 - лимонная кислота 4 - остаточный сахар 5 - хлориды 6 - свободный диоксид серы 7 - общий диоксид серы 8 - плотность 9 - pH 10 - сульфаты 11 - алкоголь Выходная переменная (на основе сенсорных данных): 12 - качество (оценка от 0 до 10)
#
# 1 - fixed acidity 2 - volatile acidity 3 - citric acid 4 - residual sugar 5 - chlorides 6 - free sulfur dioxide 7 - total sulfur dioxide 8 - density 9 - pH 10 - sulphates 11 - alcohol Output variable (based on sensory data): 12 - quality (score between 0 and 10)

# Добавить good: если quality > 5, то 1, иначе 0.
df["good"] = df["quality"].apply(lambda x: 1 if x > 5 else 0)
print(df.head())

# Строим корреляциогнную матрицу
correlation = df.corr()
correlation

# Строим хитмэп по матрице корреляций
plt.figure(figsize=(10, 7))
sns.heatmap(correlation, cmap='Reds', annot=True)
plt.title('Корреляционаая матрица')
plt.show()

# Проанализировав общую матрицу влияние показателей на качество можно разделить на 3 группы:
# 1. не влияют (корр <= abs(0.2)):
# fixed acidity
# residual sugar
# chlorides
# free sulfur dioxide
# total sulfur dioxide
# density
# pH
# 2. Слабое влияние (abs(0.2) < корр <= abs(0.3))
# citric acid
# sulphates
# 3. Есть влияние (abs(0.3) < корр)
# volatile acidity
# alcohol

# Разделим таблицу на 2 части по столбцу good
df_best = df.query('good == 1')
df_worst = df.query('good == 0')
df_best.head()

# Готовим данные
data = df[['citric acid', 'alcohol', 'quality']]
data.head()

# Строим попарные отношения переменных
sns.pairplot(data)
plt.show()

# Построим совместное распределение по двум переменным
sns.jointplot(x=df['quality'], y=df['citric acid'], data=df, kind='reg')
plt.show()

# Построим совместное распределение по двум переменным
sns.jointplot(x=df['quality'], y=df['alcohol'], data=df, kind='reg')
plt.show()
