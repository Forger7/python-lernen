import pandas as pd
import requests

# Die API für Mitarbeiter-Stammdaten
url = "https://jsonplaceholder.typicode.com/users"

# 1. Daten abrufen
antwort = requests.get(url)
user_daten = antwort.json()

# 2. Der Pandas-Flachklopfer: Macht aus verschachteltem JSON eine flache Tabelle
df = pd.json_normalize(user_daten)

gefiltertes_df = df[df["address.city"] == "South Elvis"]

gefiltertes_df.to_csv("modul_06_json-apis/export_elvis.csv", index=False)