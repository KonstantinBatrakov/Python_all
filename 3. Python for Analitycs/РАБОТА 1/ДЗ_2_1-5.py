# Выполните задание:
# 1. Загрузить, просмотреть, определить количество строк и склеить 3 датасета: marketing_campaign.csv, users.csv и subscribers.csv.
# 2. Определить количество, типы и описательные статистики колонок (столбцов) получившегося датасета.
# 3. Определить эффективность маркетинговых каналов по привлечению платящих игроков.
# 4. Определить самую раннюю дату подписки на сервис.
# 5. Определить портрет аудитории удержанных подписчиков (по возрасту и языку).
# Результат - ссылка на готовый ноутбук в Colab.

# Импортируем в свой скрипт библиотеку Pandas
import pandas as pd

print(
    '1. Загрузить, просмотреть, определить количество строк и склеить 3 датасета: marketing_campaign.csv, users.csv и subscribers.csv.')
print('---------------------------------------')

# Загружаем данные в Python c помощью бибилиотеки Pandas
df_m_c = pd.read_csv('marketing_campaign.csv')
df_s = pd.read_csv('subscribers.csv')
df_u = pd.read_csv('users.csv')

# У метода read есть доп. параметры, которые можно указывать в скобках:
df_m_c = pd.read_csv('marketing_campaign.csv', header=0, sep=',')
df_s = pd.read_csv('subscribers.csv', header=0, sep=',')
df_u = pd.read_csv('users.csv', header=0, sep=',')

print('количество строк в датафрейме')
print(f"    marketing_campaign.csv: {len(df_m_c)}")
print(f"    subscribers.csv: {len(df_s)}")
print(f"    users.csv: {len(df_u)}\n")

print('количество строк и столбцов в датафрейме')
print(f"    marketing_campaign.csv: {df_m_c.shape}")
print(f"    subscribers.csv: {df_s.shape}")
print(f"    users.csv: {df_u.shape}\n")
print('---------------------------------------')

# Посмотрим данные
print(f"DATA marketing_campaign.csv\n{df_m_c}\n")
print(f"DATA subscribers.csv\n{df_s}\n")
print(f"DATA users.csv\n{df_u}\n")
print('---------------------------------------')

# Объдинение датасетов
df_all = df_m_c.merge(df_s, on='user_id', how='inner').merge(df_u, on='user_id', how='inner')
print(f"Результирующий датасет: \n {df_all}")
print('---------------------------------------')

print('2. Определить количество, типы и описательные статистики колонок (столбцов) получившегося датасета.')
print(f"количество строк и столбцов: {df_all.shape}")

print('\n     Общая статистика датасета')
df_all.info()
print('\n     Описательная статистика для нечисловых столбцов датасета')
print(df_all.describe(include=['object', 'bool']))
print('---------------------------------------')

print('3. Определить эффективность маркетинговых каналов по привлечению платящих игроков.')
df_group = df_all.groupby(['marketing_channel', 'converted']).size()
print(f"Срез данных источник рекламы и кол-во False и True:\n{df_group}\n")

df_1 = df_all[df_all["converted"] == True]['marketing_channel'].value_counts() / df_all[
    'marketing_channel'].value_counts()
df_2 = df_all[df_all["converted"] == True]['marketing_channel'].value_counts() / df_all.shape[0]

print(f"Эффективность внутри каналов\n{round(df_1, 2)}\n")
print(f"Эффективность относительно всех каналов\n{round(df_2, 2)}\n")
print('---------------------------------------')

print('4. Определить самую раннюю дату подписки на сервис.')
# Замена типа дат с object на datetime64[ns]
date_cols = ["date_served", "date_subscribed", "date_canceled"]
df_all[date_cols] = df_all[date_cols].astype("datetime64[ns]")
df_all.info()

# print('Самая ранняя дата:', df_all['date_served'].min())
print("\nСамая ранняя дата:", df_all['date_served'].min().strftime("%d/%m/%y"))

# import datetime
# d1 = datetime.date(df_all["date_served"],"%m/%d/%Y")
print('---------------------------------------')

print('5. Определить портрет аудитории удержанных подписчиков (по возрасту и языку).')
df_3 = df_all[df_all["is_retained"] == True]['age_group'].value_counts()
df_4 = df_all[df_all["is_retained"] == True]['language_preferred'].value_counts()
print(f"Срез удержанных подписчиков по возрасту\n{df_3}\n")
print(f"Срез удержанных подписчиков по языку\n{df_4}\n")