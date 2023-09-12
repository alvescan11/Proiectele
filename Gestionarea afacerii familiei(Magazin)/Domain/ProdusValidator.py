from Domain.Produs import Produs


class ProdusValidator:
    def valideaza(self, prosus: Produs):
        if prosus.nume == "":
            raise ValueError("Numele produsului nu poate fi gol")

        if prosus.pret <= 0:
            raise ValueError("Pretul produsului nu poate fi negativ")

        if len(prosus.nume) <= 3:
            raise ValueError("Produsul trebuie sa aiba minim 3 caractere")

        if prosus.tip == "":
            raise ValueError("Tipul produsului nu poate fi gol")

        if len(prosus.tip) <= 3:
            raise ValueError("Tipul trebuie sa aiba minim 3 caractere")

        if prosus.tip not in ["Gradinarit","Uz casnic","Bucatarie","Curatenie"]:
            raise ValueError("Tipul produsului poate fi doar Gradinarit, Uz casnic, Bucatarie sau Curatenie")

        if len(prosus.furnizor) <= 3:
            raise ValueError("Furnizorul trebuie sa aiba minim 3 caractere")

        if prosus.furnizor == "":
            raise ValueError("Furnizorul produsului nu poate fi gol")

        if prosus.furnizor not in ["Viacom","Loriand","Neves","Sano","Agrosem"]:
            raise ValueError("Furnizorii pot fi doar Viacom, Loriand, Neves, Sano sau Agrosem")


        