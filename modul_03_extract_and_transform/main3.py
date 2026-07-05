gesamtsumme=0
with open("modul_03_extract_and_transform/daten2.csv","r") as datei:
    for zeile in datei:
        teile=zeile.strip().split(",")
        if teile[1]!="Umsatz":
            if teile[1].isdigit():
                gesamtsumme=int(teile[1])+gesamtsumme
print(gesamtsumme)