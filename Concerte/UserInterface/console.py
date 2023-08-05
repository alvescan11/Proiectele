from Service.artistService import ArtistService
from Service.concertService import ConcertService


class Console:
    def __init__(self, artistService:ArtistService, concertService:ConcertService):
        self.artistService = artistService
        self.concertService = concertService

    def runMenu(self):
        while True:
            print("1.Adauga artist")
            print("a1.Afisare artisti")
            print("2.Adauga concert")
            print("a2.Afisare concerte")
            print("3.Afisare artisti dupa categorie")
            print("4.Afisare nr concerte")
            print("5.Export Json")
            print("x.Iesire")

            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.AdaugaArtist()
            elif optiune == "a1":
                self.Afisare(self.artistService.getAll())
            elif optiune == "2":
                self.AdaugaConcert()
            elif optiune == "a2":
                self.Afisare(self.concertService.getAll())
            elif optiune == "3":
                categorie = input("dati categoria: ")
                self.Afisare(self.artistService.AfisareArtisti(categorie))
            elif optiune == "4":
                self.AfisareDictioner(self.artistService.NumarConcerte())
            elif optiune == "5":
                self.ExportJson()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita!")

    def AfisareArtisti(self):
        try:
            categorie = input("Dati o categorie: ")

            self.artistService.AfisareArtisti(categorie)
        except Exception as e:
            print(e)

    def Afisare(self,entitati):
        for entitate in entitati:
            print(entitate)

    def AfisareDictioner(self,entitati):
        for keys in entitati:
            print(str(keys) + " "+ str(entitati[keys]))

    def AdaugaArtist(self):
        try:
            id = input("Dati id ul artistului: ")
            nume = input("Dati numele artistului: ")
            categorie = input("Dati categoria: ")
            tarif = float(input("Dati tariful: "))
            self.artistService.adaug(id,nume,categorie,tarif)
        except Exception as e:
            print(e)

    def AdaugaConcert(self):
        try:
            id_concert = input("Dati id ul concertului: ")
            id = input("Dati id-ul artistului: ")
            nume = input("Dati numele concertului: ")
            locatie = input("Dati locatia: ")
            capacitate = int(input("Dati capacitatea: "))
            self.concertService.adauga(id_concert,id,nume,locatie,capacitate)
        except Exception as e:
            print(e)

    def ExportJson(self):
        try:
            filename = input("Dati numele fisierului in care se va face exportul: ")
            self.artistService.ExportJson(filename)
        except Exception as e:
            print(e)

