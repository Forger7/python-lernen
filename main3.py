gesamtsumme=0
with open("daten2.csv","r") as datei:
    for zeile in datei:
        teile=zeile.strip().split(",")
        if teile[1]!="Umsatz":
            gesamtsumme=int(teile[1])+gesamtsumme
print(gesamtsumme)

