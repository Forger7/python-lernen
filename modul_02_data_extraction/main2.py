with open("modul_02_data_extraction/daten.csv","r") as datei:
    for zeile in datei: 
        teile=zeile.strip().split(",") #.strip entfernt überflüssige umbrüche etc. in csv, #.split teilt in einn dictionary auf
        if teile[1]!="Stadt":
            print(teile[1])
