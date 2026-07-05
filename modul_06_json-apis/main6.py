import pandas as pd
import requests

# Die URL der kostenlosen Feiertags-API (Hier für Deutschland in 2026)
url = "https://date.nager.at/api/v3/PublicHolidays/2026/AT"

# 1. Die Webseite/API abfragen (HTTP GET-Request)
antwort = requests.get(url)

# 2. Den erhaltenen Text als JSON (Liste aus Dictionaries) interpretieren
feiertage_daten = antwort.json()

# 3. Pandas frisst das JSON-Format direkt und baut eine Tabelle daraus!
df = pd.DataFrame(feiertage_daten)

# Zeige die ersten 5 Feiertage an
print(df[df["date"].str.startswith("2026-05")])
      