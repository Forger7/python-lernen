## 🔴 Modul 4: Der Datenturbo (Einstieg in Pandas)

Jetzt wird es Zeit, das Fahrrad gegen einen Sportwagen einzutauschen. Bisher haben wir alles "zu Fuß" mit purem Python gebaut. Das ist super fürs Verständnis, aber wenn deine CSV-Datei plötzlich 500.000 Zeilen hat und du Durchschnitte, Filter und Gruppierungen brauchst, wird der Code zu Fuß schnell lang und unübersichtlich.

Hier kommt **Pandas** ins Spiel – das absolute Standard-Werkzeug für Data Science weltweit.

---

### Schritt 1: Pandas in dein Projekt holen

Weil du `uv` nutzt, ist das Installieren von neuen Bibliotheken ein absoluter Traum. Du musst dafür deine Konfiguration gar nicht anfassen!

Tippe einfach in deinem Terminal (während du im Ordner `python-lernen` bist):

```bash
uv add pandas

```

**Was passiert?** `uv` lädt Pandas und alles, was dazu gehört, blitzschnell herunter und installiert es isoliert in deiner virtuellen Umgebung (`.venv`).

---

### Die Theorie: Der Einstieg in Pandas

Pandas bricht komplett mit der alten Methode, Zeile für Zeile händisch durchzugehen. Stattdessen lädt Pandas die gesamte Tabelle auf einmal in den Arbeitsspeicher und baut daraus ein sogenanntes **DataFrame** (in der Data-Science-Welt standardmäßig als `df` abgekürzt). Ein DataFrame ist im Grunde ein Excel-Datenblatt auf Steroiden.

Um Pandas zu nutzen, importiert man es ganz oben im Skript. Die weltweite Entwicklergemeinschaft hat sich hierbei auf eine feste Abkürzung geeinigt: `import pandas as pd`.

Der Befehl, um eine CSV einzulesen, ist ein einziger Einzeiler:

```python
import pandas as pd

# Liest die komplette Datei ein und erstellt das DataFrame 'df'
df = pd.read_csv("pfad/zur/datei.csv")

```

---

### Deine neue Challenge 🚀

Lass uns Pandas das erste Mal in Aktion sehen und beobachten, was es mit unseren "dreckigen" Daten (inklusive Dieters "FEHLER"-Eintrag) anstellt.

**Deine Aufgabe in `modul_04_pandas_introduction/main4.py`:**

1. Importiere Pandas mit dem Standard-Spitznamen `pd`.
2. Nutze `pd.read_csv()`, um die `daten2.csv` aus dem Modul-3-Ordner einzulesen. *(Achte auf den richtigen Pfad!)*
3. Nutze `print(df)`, um die geladene Tabelle im Terminal auszugeben.

> 🔍 **Beobachtung:** Schau dir die Ausgabe im Terminal genau an. Wie stellt Pandas die Tabelle dar, und was hat es aus Dieters "FEHLER"-Text gemacht?

---

### Die Theorie: Der Pandas-Sicherheitsgurt (`to_numeric`)

In Pandas müssen wir nicht jede Zeile einzeln prüfen. Wir jagen einfach die ganze Spalte auf einmal durch eine Konvertierungs-Maschine: `pd.to_numeric()`.

Damit sagst du Pandas: *"Mach mir hier Zahlen draus!"* Und mit dem genialen Zusatz `errors='coerce'` (engl. für *erzwingen*) sagst du: *"Und alles, was keine Zahl ist (wie Dieters FEHLER), verwandelst du bitte eiskalt in ein NaN"*.

**NaN** steht für *Not a Number*. Das ist der weltweite Data-Science-Standard für *"Hier fehlt ein Wert / hier war ein Fehler"*.

Das sieht im Code so aus:

```python
# Wir überschreiben die alte Spalte mit der gesäuberten Zahlen-Spalte
df["Umsatz"] = pd.to_numeric(df["Umsatz"], errors="coerce")

```

**Der absolute Clou bei Pandas:** Wenn du danach die Summe der Spalte berechnest, ignoriert Pandas alle NaN-Felder vollautomatisch! Kein `if`, kein `.isdigit()`, kein Schleifen-Code nötig.

---

### Deine neue Challenge 🚀

Lass uns die `main4.py` umschreiben, um den echten Pandas-Zauber zu sehen.

**Deine Aufgabe in `main4.py`:**

1. Lass das Einlesen der CSV-Datei genau so stehen.
2. Füge darunter die Zeile ein, die die Spalte `"Umsatz"` mit `pd.to_numeric(..., errors='coerce')` konvertiert.
3. Drucke danach noch mal die Tabelle mit `print(df)` aus, um zu sehen, was aus Dieters "FEHLER" geworden ist.
4. Berechne ganz unten den Gesamtumsatz mit der eingebauten Pandas-Summe:

```python
gesamtsumme = df["Umsatz"].sum()
print(gesamtsumme)

```

> 🎯 **Das Ziel:** Wenn alles klappt, solltest du im Terminal sehen, dass aus "FEHLER" ein "NaN" geworden ist, und direkt darunter ploppt wie von Zauberhand wieder die `700.0` auf.
> Schaffst du es, den Sportwagen zu steuern und die Spalte im Ganzen zu transformieren?

---

### Die Theorie: Filtern ohne Schleifen

Erinnerst du dich, wie wir in Modul 2 mühsam mit `if teile[1] != "Stadt"` händisch filtern mussten? In Pandas geht das für die gesamte Tabelle in einer einzigen Zeile.

Man wirft Pandas einfach eine Bedingung in eckigen Klammern hin:

```python
# Gib mir nur die Zeilen, bei denen der Umsatz größer als 160 ist
hoher_umsatz = df[df["Umsatz"] > 160]
print(hoher_umsatz)

```

Das liest sich rückwärts wie: *"Filter das df, wo im df der Umsatz > 160 ist."*

---

### Deine finale Modul-4-Challenge 🚀

Lass uns einen schnellen Filter in deine `main4.py` einbauen, um nur noch die echten Top-Performer anzuzeigen.

**Deine Aufgabe:**

1. Behalte deinen bisherigen Code (Einlesen und `to_numeric`) bei.
2. Lösche das `print(gesamtsumme)` unten weg.
3. Erstelle eine neue Variable `gefiltertes_df` und filtere die Tabelle so, dass nur noch Zeilen angezeigt werden, bei denen der Umsatz größer als `180` ist.
4. Drucke dieses `gefiltertes_df` ganz unten aus.

> 🎯 **Das Ziel:** Wenn alles klappt, sollten Anna (150) und Dieter (NaN) wie vom Erdboden verschluckt sein und nur noch Ben und Chris im Terminal auftauchen.
> Schaffst du es, den Filter mit nur einer Zeile Code scharf zu schalten?