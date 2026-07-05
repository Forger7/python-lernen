import requests

# Die offizielle, unzerstörbare Test-API für Entwickler
url = "https://jsonplaceholder.typicode.com/todos"

# 1. API abfragen
antwort = requests.get(url)
aufgaben = antwort.json()  # Das liefert uns eine Liste voller Dictionaries!

for aufgabe in aufgaben[:5]:
    print(f"Aufgabe: {aufgabe['title']} | Erledigt: {aufgabe['completed']}")