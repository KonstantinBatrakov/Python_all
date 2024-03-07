import pandas as pd
# -------read-----------------
# df = pd.read_csv('mor_reports_АВ1_3.csv', encoding='latin-1')
df = pd.read_csv('mor_reports_А1.csv', sep=";", encoding="utf-8")
print(df)
df["1"] = df["1"].astype(str)
print(df)

wells = pd.read_excel("wells.xlsx")
wells["DOB"] = wells["DOB"].astype(str)
print(wells)

wells_name = wells["PPD"].value_counts()
print(wells_name)

for name in wells_name.index:
    wells_for = list(wells[wells["PPD"] == name]["DOB"])
    rslt_df = df[df['1'].isin(wells_for)]
    rslt_df.to_csv(f"{name}.csv", sep=";", index=False)