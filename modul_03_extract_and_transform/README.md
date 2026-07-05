## 🟠 Modul 3: Das ETL-Prinzip (Daten-Aufbereitung & Berechnung)

Jetzt gehen wir einen Schritt weiter in Richtung echter Datenanalyse. Im echten Leben wollen wir Text nicht nur anzeigen, sondern mit Zahlen rechnen (z. B. Summen bilden, Durchschnitte berechnen, Filter setzen).

Dabei stoßen wir auf ein typisches Problem beim Einlesen von Dateien: **Datentypen**.

---

### Schritt 1: Neue Testdaten anlegen

Wir erstellen eine neue Datei für dieses Modul, in der echte Zahlen stecken.

1. Erstelle in VS Code eine neue Datei namens `daten2.csv`.
2. Kopiere diesen Inhalt hinein (diesmal geht es um den Umsatz, den Kunden gebracht haben):

```csv
Name,Umsatz
Anna,150
Ben,200
Chris,350

```

---

### Die Theorie: Der Datentyp-Schock (`int()`)

Wenn Python eine CSV-Datei liest, ist alles für Python erst mal reiner Text (ein sogenannter **String**).

Selbst wenn in der Datei `150` steht, sieht Python im Speicher `"150"` (mit Anführungszeichen).

* **Das Problem:** Man kann mit Text nicht rechnen. Wenn du in Python `"150" + "200"` rechnest, baut Python die Texte einfach nur aneinander und das Ergebnis ist `"150200"`.

Um aus dem Text `"150"` eine echte Zahl zu machen, mit der man rechnen kann, müssen wir sie konvertieren (Typ-Konvertierung). Dafür gibt es die Funktion `int()` (steht für *Integer*, also Ganzzahl):

```python
text_zahl = "150"
echte_zahl = int(text_zahl)  # Jetzt ist es die echte Zahl 150!

```

---

### Deine neue Challenge (in einer neuen `main3.py`) 🚀

Wir wollen jetzt den Gesamtumsatz aller drei Kunden berechnen.

1. Erstelle eine neue Datei `main3.py`.
2. Erstelle ganz oben vor der Schleife eine Variable für die Gesamtsumme und setze sie auf Null: `gesamtsumme = 0`.
3. Öffne die neue Datei `daten2.csv` im Lese-Modus.
4. Baue deine bekannte Schleife: Zeile säubern, am Komma splitten, die Überschrift "Umsatz" ignorieren.
5. **Jetzt neu innerhalb der Schleife:**
* Schnapp dir den Umsatz (`teile[1]`).
* Wandle ihn mit `int(...)` in eine echte Zahl um.
* Addiere diese Zahl auf deine `gesamtsumme` drauf *(Tipp: `gesamtsumme = gesamtsumme + echte_zahl`)*.


6. Ganz am Ende (wenn die Schleife komplett fertig ist und du **nicht mehr eingerückt** bist!), nutzt du `print(gesamtsumme)`, um das Endergebnis anzuzeigen.

> 🎯 **Das Ziel:** Wenn alles klappt, sollte dein Terminal nach dem Start von `main3.py` am Ende genau eine Zahl ausspucken: **700** ($150 + 200 + 350$).
> Schaffst du es, die Text-Zahlen zum Rechnen zu bringen?

---

Damit hast du die Grundlagen von **Extract** (Einlesen) und **Transform** (Berechnen) verstanden. Jetzt machen wir den letzten Schritt in Modul 3, bevor wir den Datenturbo (Pandas) zünden: Die Datenbereinigung (**Data Cleaning**).

Im echten Leben sind Datensätze nämlich fast immer "dreckig". Da vergisst ein Kollege eine Zahl, tippt aus Versehen Text ein oder es entstehen leere Zeilen. Wenn wir so etwas ungefiltert in ein `int()` jagen, stürzt unser ganzes Programm sofort ab.

---

### Schritt 1: Wir machen die Daten absichtlich kaputt

1. Öffne deine `daten2.csv` in VS Code.
2. Füge ganz unten eine neue, fehlerhafte Zeile hinzu:

```csv
Name,Umsatz
Anna,150
Ben,200
Chris,350
Dieter,FEHLER

```

3. Speichere die Datei und führe deine `main3.py` im Terminal noch mal aus.

> ⚠️ **Spoiler:** Du wirst jetzt deinen allerersten fetten, roten Python-Fehler (`ValueError`) sehen. Das ist völlig okay und gehört zum Entwickler-Alltag!

---

### Die Theorie: Der Datentyp-Schutzschild (`.isdigit()`)

Um uns vor solchen Abstürzen zu schützen, müssen wir prüfen, ob der Text wirklich eine Zahl ist, bevor wir `int()` darauf anwenden.

Python hat dafür eine geniale Funktion für Texte: `.isdigit()` (auf Deutsch: *ist eine Ziffer?*). Sie schaut sich den Text an und gibt entweder `True` (wahr) oder `False` (falsch) zurück:

```python
print("150".isdigit())    # Spuckt True aus
print("FEHLER".isdigit()) # Spuckt False aus

```

---

### Deine neue Challenge 🚀

Wir bauen jetzt einen Sicherheitsgurt in deine `main3.py` ein, damit das Programm trotz der kaputten Zeile von Dieter nicht abstürzt und trotzdem das richtige Ergebnis (700) ausrechnet.

**Deine Aufgabe in `main3.py`:**

1. Erweitere deine `if`-Bedingung innerhalb der Schleife.
2. Du filterst ja schon, dass es nicht `"Umsatz"` sein darf. Sorge jetzt dafür (entweder durch ein zweites `if` darunter oder durch ein cleveres Kombinieren), dass der Umsatz nur dann addiert wird, wenn `teile[1]` eine echte Ziffer ist (nutze `.isdigit()`).

**Tipp für die Struktur (verschachteltes if):**

```python
if teile[1] != "Umsatz":
    if teile[1].isdigit():
        # Hier wird gerechnet und addiert...

```

> 🎯 **Das Ziel:** Wenn du den Sicherheitsgurt richtig angelegt hast, ignoriert Python die Zeile von Dieter einfach komplett, stürzt nicht ab und spuckt dir am Ende wieder fröhlich die **700** aus.
> Schaffst du es, dein Programm absturzsicher zu machen?