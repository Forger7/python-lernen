import pandas as pd
df = pd.read_csv("modul_03_extract_and_transform/daten2.csv")
df["Umsatz"] = pd.to_numeric(df["Umsatz"], errors="coerce")
print(df)
gesamtsumme=df["Umsatz"].sum()
gefiltertes_df = df[df["Umsatz"] > 180]
print(gefiltertes_df)