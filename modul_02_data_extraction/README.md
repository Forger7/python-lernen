## 🟡 Modul 2: Daten anfassen (Die "Extract"-Phase)

Im echten Leben tippst du deine Daten natürlich nicht händisch in die `main.py` ein. Die Daten liegen in einer Datei auf deiner Festplatte – meistens als **CSV** (*Comma-Separated Values*, also durch Kommas getrennte Werte).

Wir lernen jetzt, wie Python eine Datei von der Festplatte aufmacht und einliest.

---

### Schritt 1: Wir erstellen eine echte CSV-Datei

Damit wir etwas zum Auslesen haben, legen wir uns eine Mini-Datenbank an:

1. Erstelle in VS Code im selben Ordner eine neue Datei und nenne sie `daten.csv`.
2. Kopiere diesen einfachen Text hinein und speichere die Datei:

```csv
Name,Stadt
Anna,Berlin
Ben,Hamburg
Chris,München

```

---

### Schritt 2: Die Theorie (Wie öffnet Python Dateien?)

Um eine Datei zu öffnen, nutzen wir in Python einen sehr eleganten Befehl: `with open(...)`. Das sieht so aus:

```python
with open("daten.csv", "r") as datei:
    for zeile in datei:
        print(zeile)

```

**Was bedeutet das genau?**

* **`with open("daten.csv", "r")`:** „Öffne die Datei `daten.csv` im Modus `r` (read = lesen).“ Das `with` sorgt dafür, dass Python die Datei automatisch wieder sauber schließt, wenn wir fertig sind – so wird nichts blockiert.
* **`as datei`:** Wir geben der geöffneten Datei für den Code den Spitznamen `datei`.
* **`for zeile in datei`:** Das ist der absolute Hammer in Python! Python behandelt die geöffnete Datei einfach wie eine Liste aus Textzeilen. Unsere `for`-Schleife wandert also Zeile für Zeile durch die Datei.

---

### Deine neue Challenge 🚀

Lass uns die `main.py` komplett aufräumen. Lösche am besten alles, was bisher drin war, damit wir eine weiße Leinwand haben.

**Deine Aufgabe:**

1. Schreibe den `with open`-Block, um deine neue `daten.csv` zu öffnen.
2. Baue die `for`-Schleife ein, um jede `zeile` auszugeben.
3. Führe den Code im Terminal aus.

> 💡 **Achtung, Beobachtungs-Aufgabe:** Wenn du das Skript ausführst, wird das Ergebnis im Terminal ein kleines bisschen "merkwürdig" formatiert sein. Schau dir die Ausgabe genau an.