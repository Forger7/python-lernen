## 🔴 Modul 5: Daten visualisieren (Die Visualisierungs-Phase)

Jetzt kommt der Teil, der im Reporting am meisten Spaß macht: Wir machen aus den nackten Zahlen ein echtes, greifbares Diagramm.

Pandas hat dafür eine eingebaute Funktion (`df.plot()`), aber um die Bilder auf dem Bildschirm darzustellen, braucht Python im Hintergrund den weltweiten Standard für Grafiken: **Matplotlib**.

---

### Schritt 1: Die Grafik-Bibliothek installieren

Hol dir das Werkzeug wieder ganz entspannt über dein Terminal in deinem Hauptordner `python-lernen`:

```bash
uv add matplotlib

```

---

### Schritt 2: Die Theorie (Diagramme auf Knopfdruck)

Wenn Matplotlib installiert ist, können wir Pandas sagen, dass es uns ein Balkendiagramm zeichnen soll:

```python
df.plot(kind="bar", x="Name", y="Umsatz")

```

Damit sich danach auf deinem MacMini ein echtes Fenster mit der Grafik öffnet, importieren wir `matplotlib.pyplot` und rufen ganz unten den Befehl `plt.show()` auf.

---

### Deine neue Challenge 🚀

Lass uns das nächste Kapitel aufschlagen:

1. Erstelle einen neuen Ordner namens `modul_05_visualization` und darin eine `main5.py`.
2. Kopiere den funktionierenden Code aus deiner `main4.py` (Einlesen und `to_numeric`) hinein – wir wollen die sauberen Daten inklusive Dieter als `NaN` nutzen (ohne den `>180` Filter, damit wir alle sehen!).
3. Baue den Plot-Befehl und das `plt.show()` ein.

Der komplette Code in deiner `main5.py` sollte dann so aussehen:

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Daten einlesen & säubern (aus Modul 3 & 4)
df = pd.read_csv("modul_03_extract_and_transform/daten2.csv")
df["Umsatz"] = pd.to_numeric(df["Umsatz"], errors="coerce")

# 2. Diagramm erstellen (bar = Balken, Farbe = skyblue)
df.plot(kind="bar", x="Name", y="Umsatz", color="skyblue")

# 3. Grafik-Fenster öffnen
plt.show()

```

Starte das Skript wie gewohnt über dein Terminal.

> 🎯 **Das Ziel:** Wenn alles klappt, sollte auf deinem Mac ein neues Fenster aufpoppen, das dir die Umsätze als schicke blaue Balken anzeigt.
> Hat die Installation geklappt und öffnet sich das Diagramm-Fenster erfolgreich bei dir?