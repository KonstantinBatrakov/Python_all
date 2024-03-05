import pandas as pd

print("\n"
      "1. Использовать датасет с текущего урока и построить сегментированную воронку конверсии пользователей интернет-магазина по полу.")
# -------read-----------------
user_table = pd.read_csv("user_table.csv")
home_page = pd.read_csv("home_page_table.csv")
search_page = pd.read_csv("search_page_table.csv")
payment_page = pd.read_csv("payment_page_table.csv")
payment_confirmation = pd.read_csv("payment_confirmation_table.csv")

# -------rename-----------------
home_page = home_page.rename(columns={"page": "home_page"})
search_page = search_page.rename(columns={"page": "search_page"})
payment_page = payment_page.rename(columns={"page": "payment_page"})
payment_confirmation = payment_confirmation.rename(columns={"page": "payment_confirmation"})

print("\n-------merge-------------------")
df = user_table.merge(home_page, on="user_id", how="left").merge(search_page, on="user_id", how="left") \
    .merge(payment_page, on="user_id", how="left").merge(payment_confirmation, on="user_id", how="left")
print(df.head())
print(df.shape)

print("\n-------change simbols-------------------")
df["home_page"] = df["home_page"].apply(lambda x: 1 if x == "home_page" else 0)
df["search_page"] = df["search_page"].apply(lambda x: 1 if x == "search_page" else 0)
df["payment_page"] = df["payment_page"].apply(lambda x: 1 if x == "payment_page" else 0)
df["payment_confirmation"] = df["payment_confirmation"].apply(lambda x: 1 if x == "payment_confirmation_page" else 0)
print(df.head())

print("\n-------aggregate analysis-------------------")
dfg = df.groupby("sex")[["home_page", "search_page", "payment_page", "payment_confirmation"]].sum(). \
    unstack("sex").unstack("sex").reset_index()
dfg.columns.name = None
dfg = dfg.rename(columns={"index": "Page"})
print(dfg.head())

print("\n-------graff analysis-------------------")
from plotly import graph_objects as go

fig = go.Figure(go.Funnel(
    y=dfg["Page"],
    x=dfg["Female"],
    textinfo="value + percent previous",
    name="Female",
    constraintext="outside"

))
fig.add_trace(go.Funnel(
    y=dfg["Page"],
    x=dfg["Male"],
    textinfo="value + percent previous",
    name="Male",
    constraintext="outside"
))

fig.update_layout(
    title="Воронка конверсии по типу устройств",
    title_x=0.5,
    autosize=False,
    width=1200,
    height=600
)
# ig.show()

print("\n"
      "2. Создать 2 новые фичи на основе колонки “date”: месяц и день недели (пример https://stackoverflow.com/a/62624729,"
      "https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.dt.weekday.html)")

print('\n     Общая статистика датасета')
df.info()
# Замена типа дат с object на datetime64[ns]
date_cols = ["date"]
df[date_cols] = df[date_cols].astype("datetime64[ns]")
df.info()
print(df.head())

print('\n     Добавить фичу год, месяц, день и день недели')
# Добавить фичу год
df["year"] = df["date"].dt.year
# Добавить фичу месяц
df["month"] = df["date"].dt.month
# Добавить фичу день
df["day"] = df["date"].dt.day
# Добавить фичу день недели
df["day_of_week"] = df["date"].dt.dayofweek
print(df.head())
print(df.shape)

print("\n"
      "3. Определить самый топовый по продажам месяц и день недели с помощью базовых методов агрегации (sum или count)")
print("\n-------analys_groupby-------------------")
analys_month = df.groupby(["month"])["payment_confirmation"].sum().reset_index()
analys_day_of_week = df.groupby(["day_of_week"])["payment_confirmation"].sum().reset_index()
print(analys_month)
print(analys_day_of_week)

print("\n-------max_date month and day_of_week-------------------")
max_month = analys_month[analys_month["payment_confirmation"] == analys_month["payment_confirmation"].max()]
print(max_month)
max_month = analys_day_of_week[
    analys_day_of_week["payment_confirmation"] ==
    analys_day_of_week["payment_confirmation"].max()]
print(max_month)

print("\n"
      "4. Выяснить, в какой день недели лучше покупают женщины, а в какой мужчины с помощью одного из методов построения "
      "сводных таблиц (groupby, pivot_table или crosstab)")

# группировка по признаку пол
print("\n-------analys_pivot_table-------------------")
analys_pivot_table = df.pivot_table(index=["sex", "day_of_week"], values="payment_confirmation", aggfunc="sum",
                                    margins=True).reset_index()
print(analys_pivot_table)

print("\n-------analys_crosstab-------------------")
analys_crosstab = pd.crosstab(index=[df["sex"], df["day_of_week"]], columns=df["payment_confirmation"]).reset_index()
print(analys_crosstab)

print("\n-------analys_groupby-------------------")
analys_groupby = df.groupby(["sex", "day_of_week"])["payment_confirmation"].sum().reset_index()
print(analys_groupby)

# поиск максимума лоя каждого из полов
print("\n-------max_for_male-------------------")
groupby_male = analys_groupby[analys_groupby["sex"] == "Male"]
max_analys_groupby_male = groupby_male[
    groupby_male["payment_confirmation"] == groupby_male["payment_confirmation"].max()]
print(max_analys_groupby_male)

print("\n-------max_for_female-------------------")
groupby_male = analys_groupby[analys_groupby["sex"] == "Female"]
max_analys_groupby_male = groupby_male[
    groupby_male["payment_confirmation"] == groupby_male["payment_confirmation"].max()]
print(max_analys_groupby_male)

print("\n-------max_for_female_var_2-------------------")
data_fm = df.query('sex == "Female"').groupby('day_of_week')['payment_confirmation'].agg(
    sum='sum').max().reset_index()
data_fm = data_fm.rename(columns={"index": "sum", 0: "max"})
print(data_fm)

