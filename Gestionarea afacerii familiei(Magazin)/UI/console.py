from Domain.Produs import Produs
from Service.produsService import ProdusService


class Console:
    def __init__(self, produsService: ProdusService):
        self.produsService = produsService

    def printMenu(self):
        print("1. Adauga produs")
        print("2. Sterge produs")
        print("3. Modifica produs")
        print("4. Sortare dupa tip")
        print("5. Sortare dupa furnizor")
        print("a. Afiseaza produse")
        print("x. Iesire program")

    def runMenu(self):
        while True:
            self.printMenu()
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.AdaugaProdus()
            elif optiune == "2":
                self.StergeProdus()
            elif optiune == "3":
                self.ModificaProdus()
            elif optiune == "4":
                tip = input("Dati tipul dupa care doriti sortarea: ")
                print(self.produsService.SortareDupaTip(tip))
            elif optiune == "5":
                furnizor = input("Dati furnizorul dupa care doriti sortarea: ")
                print(self.produsService.SortareDupaFurnizor(furnizor))
            elif optiune == "a":
                self.Afisare(self.produsService.getAll())
            elif optiune == "x":
                break
            else:
                print("Optiune gresita!!!")

    def AdaugaProdus(self):
        try:
            id = input("Dati id-ul produsului: ")
            nume = input("Dati numele produsului: ")
            pret = float(input("Dati pretul produsului: "))
            tip = input("Dati tipul produsului: ")
            furnizor = input("Dati furnizorul produsului: ")
            self.produsService.adauga(id,nume,pret,tip,furnizor)
        except Exception as e:
            print(e)

    def Afisare(self,lista):
        for entitate in lista:
            print(entitate)

    def StergeProdus(self):
        try:
            id_produs = input("Dati id-ul produsului de sters: ")
            self.produsService.sterge(id_produs)
        except Exception as e:
            print(e)

    def ModificaProdus(self):
        try:
            id = input("Dati id-ul produsului de modificat: ")
            nume = input("Dati noul nume al produsului: ")
            pret = float(input("Dati noul pret al produsului: "))
            tip = input("Dati noul tip al produsului: ")
            furnizor = input("Dati noul furnizor al produsului: ")
            self.produsService.update_entity(id,nume,pret,tip,furnizor)
        except Exception as e:
            print(e)

