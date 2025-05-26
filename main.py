from singer import *

kontener = ConcertOrganizer()

try:
    with open("enekesek.txt", "r") as f:
        enekesekszama = int(f.readline())
        for i in range(enekesekszama):
            sor = f.readline().strip()
            elemek = sor.split(",")
            nev = elemek[0]
            mufaj = elemek[1]
            if not isinstance(nev,str):
                raise TypeError("a fájlban a névnek (első elem) stringnek kell lennie")
            if not isinstance(mufaj,str):
                raise TypeError("a fájlban a műfajnak (második elem) stringnek kell lennie")
            helyszindatum = []
            try:
                for j in range(2, len(elemek)):
                    (helyszin, datum) = elemek[j].split(";")
                    helyszindatum.append((helyszin, datum))
            except ValueError:
                print("a koncertek listájának elemeinek ;-vel elválasztva kell lenniük, helyszín és dátum formátumban")
            enekes = Singer(nev,mufaj,helyszindatum)
            kontener.add_singer(enekes)
            print("\nLegtöbb koncerttel rendelkező énekes:", kontener.legtobbkoncert())
except FileNotFoundError:
    print("a fájl nem található")
except Exception as e:
    print("egyéb hiba történt", e)