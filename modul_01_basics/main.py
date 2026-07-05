#Liste von Altern
alter_liste = [28,34,42]

for alter in alter_liste:
    alter=alter + 1
    print(alter)

#Dictionary bauen und ausgeben

kunde_objekt = {
    "name":"Ben",
    "alter":"34"
}
print(kunde_objekt["name"])
print(kunde_objekt["alter"])


mitarbeiter_liste = [
    {"name": "Anna", "abteilung": "Marketing"},
    {"name": "Ben", "abteilung": "IT"},
    {"name": "Chris", "abteilung": "Vertrieb"}
]

for zeile in mitarbeiter_liste:
    print(zeile["abteilung"])