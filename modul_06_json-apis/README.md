## 🔴 Modul 6: Web-Daten Teil 1 – Die API (JSON)

### 1. Was wollen wir erledigen?

Wir wollen Daten nicht mehr von einer lokalen Datei laden, sondern live aus dem Internet abfragen. Dafür nutzen wir eine **API** (Application Programming Interface). Eine API liefert uns Daten meistens im **JSON-Format** – das sieht in Python fast exakt so aus wie eine Liste voller Dictionaries, die du schon in Modul 1 gelernt hast.

Wir holen uns in dieser Lektion die offiziellen gesetzlichen Feiertage für das aktuelle Jahr **2026** live von einem Server ab und verwandeln sie in ein sauberes Pandas-DataFrame.

### 2. Was nutzen wir dafür, und Beispielcode

Um im Internet an Türen zu klopfen, nutzen wir die Python-Bibliothek **`requests`**.

#### Schritt A: Werkzeug installieren

Tippe zuerst in deinem Hauptordner im Terminal:

```bash
uv add requests

```

#### Schritt B: Der Beispielcode

Wir erstellen einen neuen Ordner `modul_06_api` und darin eine `main6.py`. Der Code sieht so aus:

```python
import pandas as pd
import requests

# Die URL der kostenlosen Feiertags-API (Hier für Deutschland in 2026)
url = "https://date.nager.at/api/v3/PublicHolidays/2026/DE"

# 1. Die Webseite/API abfragen (HTTP GET-Request)
antwort = requests.get(url)

# 2. Den erhaltenen Text als JSON (Liste aus Dictionaries) interpretieren
feiertage_daten = antwort.json()

# 3. Pandas frisst das JSON-Format direkt und baut eine Tabelle daraus!
df = pd.DataFrame(feiertage_daten)

# Zeige die ersten 5 Feiertage an
print(df[["date", "localName", "name"]].head())

```

**Was passiert hier?**

* `requests.get(url)`: Python schickt eine Anfrage ins Web (wie dein Browser, wenn du eine Seite aufrufst).
* `antwort.json()`: Wandelt die Antwort direkt in ein Python-lesbares Format um.
* `pd.DataFrame(...)`: Pandas nimmt diese Liste und baut sofort Spalten und Zeilen daraus.

---

### 3. Meine eigene Anwendung (Deine Challenge) 🚀

Jetzt bist du dran. Wir passen das Szenario an, um zu sehen, ob du die API-Struktur steuern kannst.

**Deine Aufgabe:**

1. Erstelle den Ordner `modul_06_api` und die Datei `main6.py`.
2. Ändere die URL so ab, dass du die Feiertage für **Österreich** (`AT`) abfragst.
3. Lade die Daten in ein DataFrame.
4. **Zusatz-Filter:** Nutze dein Wissen aus Modul 4! Filter die Tabelle so, dass am Ende im Terminal nur noch die Feiertage angezeigt werden, die im **Monat Mai** stattfinden (Tipp: Die Spalte `"date"` ist Text und fängt bei Mai immer mit `"2026-05-"` an. Du kannst in Pandas mit `df[df["date"].str.startswith("2026-05")]` filtern).

Wenn alles klappt, sollte dein Terminal dir eine saubere Liste der österreichischen Mai-Feiertage ausspucken.

Konntest du die Daten erfolgreich aus dem Web abgreifen und filtern?

## Modul 6.1

🟢 API-Übung 1 : Die Todo-Datenbank
1. Was wollen wir erledigen?

Wir wollen eine Liste von Aufgaben (Todos) von einem Live-Server abrufen. Jede Aufgabe im JSON-Paket hat einen Titel und einen Status, der sagt, ob die Aufgabe erledigt ist (True) oder nicht (False). Wir wollen diese Struktur verstehen und gezielt auslesen.
2. Was nutzen wir dafür, und Beispielcode

Wir nutzen requests und steuern die offizielle Test-Plattform an. Lösche bitte den alten Code aus deiner main6_1.py und füge diesen funktionierenden Code ein:
Python

import requests

### Die offizielle Test-API für Entwickler
url = "https://jsonplaceholder.typicode.com/todos"

### 1. API abfragen
antwort = requests.get(url)
aufgaben = antwort.json()  # Das liefert uns eine Liste voller Dictionaries!

### Wir schnappen uns zum Testen mal nur das allererste Todo (Index 0) aus der Liste
erstes_todo = aufgaben[0]

### So sieht die Struktur von jedem einzelnen Todo in dieser Liste aus:
 {
   "userId": 1,
   "id": 1,
  "title": "delectus aut autem",
   "completed": false
 }

### 2. Den Titel des ersten Todos anzeigen
print(erstes_todo["title"])

### 3. Meine eigene Anwendung (Deine Challenge) 🚀

Jetzt bringen wir die Schleifen-Power aus Modul 2 mit dem API-Wissen zusammen.

Deine Aufgabe in main6_1.py:

    Lass das Einlesen der aufgaben genau so stehen.

    Schreibe eine for-Schleife, die durch die Liste aufgaben wandert.

    Da die API insgesamt 200 Aufgaben liefert, wollen wir das Terminal nicht sprengen. Begrenze die Schleife auf die ersten 5 Aufgaben. (Tipp: In Python kannst du eine Liste mit [:5] auf die ersten fünf Elemente kürzen: for todo in aufgaben[:5]:).

    Gib für jedes dieser 5 Todos den Titel ("title") und den Erledigt-Status ("completed") in einem schönen Satz aus.

Gewünschte Ausgabe im Terminal:
Plaintext

Aufgabe: delectus aut autem | Erledigt: False
Aufgabe: quis ut nam facilis et officia qui | Erledigt: False
...