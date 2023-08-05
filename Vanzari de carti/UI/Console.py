from Domain.vanzare import toString, getId, gettitlu, getgen, gettipReducere
from Logic.CRUD import adaugaVanzare, stergereVanzare, modificaVanzare
from Logic.Functionalitati import bcolors, aplicareDiscount, modificareGen, pretMinimGen, ordonareCrescatoarePret, \
    afisareNrTitluriDistincteGen, comanda_date

#Main Menu
from Validator.validatori import validate_pret, validate_unique_id, validate_len_lista, \
    validate_adaugaVanzare_meniu2, validate_modificareVanzare_meniu2


def PrintMainMenu():
    print(f"{bcolors.OKCYAN}>>>>>>>>>>>>>{bcolors.ENDC}")
    print(f"{bcolors.OKYELLOW}{bcolors.BOLD}1. Meniul 1:")
    print(f"2. Meniul 2:{bcolors.ENDC}")
    print(f"{bcolors.FAIL}x. Iesire: {bcolors.ENDC}")
    print(f"{bcolors.OKCYAN}>>>>>>>>>>>>>{bcolors.ENDC}")


#Meniu 1
def PrintMenu1():
    print(f"{bcolors.OKGREEN}+++++++++++++++++++++++++++++++++++++++++{bcolors.ENDC}")
    print(f"{bcolors.OKMAGENTA}1. Adaugare Vanzare")
    print("2. Stergere Vanzare")
    print("3. Modificare Vanzare")
    print("4. Undo")
    print("r. Redo")
    print(f"{bcolors.OKBLUE}5. Aplicarea unui discount de 5% pt reducerile de"
          f" tip silver si de 10% pt cele gold ")
    print("6. Modificarea genului pentru un titlu dat")
    print("7. Determinarea pretului minim pt fiecare gen")
    print("8. Ordonarea vanzarilor crescator dupa pret")
    print("9. Afisarea numarului de titluri distincte pt fiecare gen")
    print(f"{bcolors.WARNING}{bcolors.BOLD}s. Șterge toate rezervarile!")
    print(f"{bcolors.OKCYAN}a. Afisare Vanzari {bcolors.ENDC}")
    print(f"{bcolors.FAIL}x. Iesire {bcolors.ENDC}")
    print(f"{bcolors.OKGREEN}+++++++++++++++++++++++++++++++++++++++++{bcolors.ENDC}")


#Meniu 2
def PrintMenu2():
    print(f"{bcolors.OKBLUE}************{bcolors.ENDC}")
    print(f"{bcolors.HEADER}s. Start{bcolors.ENDC}")
    print(f"{bcolors.BOLD}a. Ajutor{bcolors.ENDC}")
    print(f"{bcolors.FAIL}x. Iesire{bcolors.ENDC}")
    print(f"{bcolors.OKBLUE}************{bcolors.ENDC}")


def printTipReducereVanzare():
    print(f"{bcolors.OKCYAN}    Meniu tip reducere:")
    print(f"{bcolors.OKGREEN}            1.None")
    print(f"{bcolors.OKGREEN}            2.Silver")
    print(f"{bcolors.OKGREEN}            3.Gold{bcolors.ENDC}")


def getTipReducere():
    printTipReducereVanzare()
    while True:
        tip_reducere = input(f"{bcolors.OKCYAN}    Selectati tipul reducerii: {bcolors.ENDC}")
        if tip_reducere == "1":
            return "None"
        elif tip_reducere == "2":
            return "Silver"
        elif tip_reducere == "3":
            return "Gold"
        else:
            print("acest tip de reducere nu exista,incearca din nou")


def meniuAjutor():
    print("Acesta este meniul de ajutor!!!")
    print("1. ADAUGARE VANZARE:1.Id 2.Titlu 3.Gen 4.Pret 5.Tip reducere(None,Silver sau Gold) + comanda 'adauga vanzare'")
    print("2.STERGERE VANZARE:Id ul vanzarii + comanda 'sterge vanzare'")
    print("3.MODIFICA VANZARE:1.Id ul de modificat 2.Titlu nou 3.gen nou 4.pret nou 5.tip reducere nou + comanda 'modifica vanzare'")
    print("4.APLICARE DISCOUNT: doar comanda 'aplicare discount'")
    print("5.MODIFICARE GEN:numele tilului +  noul gen + comanda 'modificare gen'")
    print("6.DETERMINARE PRET MINIM:doar comanda 'determinare pret minim'")
    print("7.ORDONARE VANZARI:doar comanda 'ordonare vanzari'")
    print("8.AFISARE NUMAR TITLURI: doar comanda 'afisare numar titluri'")
    print("a.AFISAREA VANZARILOR: doar comanda 'showall'")


def citireDate():
    givenString = input("Dati comanda, cu elementele separate prin virgula: ")
    date = givenString.split(",")
    print(len(date))
    return date


def getPret():
    pret = input(f"{bcolors.UNDERLINE}{bcolors.OKYELLOW}Dati pretul cartii: {bcolors.ENDC}")
    while validate_pret(pret) is False:
        print("pretul este invalid,reincercati")
        pret = input(f"{bcolors.UNDERLINE}{bcolors.OKYELLOW}Dati pretul cartii: {bcolors.ENDC}")
    return float(pret)


def uiAdaugaVanzare(lista,undoLista,redoLista):
    id = getIdUI(lista)
    titlu = input(f"dati numele cartii: {bcolors.ENDC}")
    gen = input("dati genul")
    pret = getPret()
    tip_reducere = getTipReducere()

    rezultat = adaugaVanzare(id,titlu,gen,pret,tip_reducere,lista)
    undoLista.append(lista)
    redoLista.clear()
    return rezultat


def uiStergeVanzare(lista,undoLista,redoLista):
    if validate_len_lista(lista) is False:
        print(f"{bcolors.FAIL}Nu este nicio vanzare de sters "
              f"incearcă să adaugi o vanzare: {bcolors.ENDC}")
        return lista
    else:
        id = getIdUI(lista, True)
        rezultat = stergereVanzare(id, lista)
        undoLista.append(lista)
        redoLista.clear()
        return rezultat


def uiModificaVanzare(lista,undoLista,redoLista):
    if validate_len_lista(lista) is False:
        print(f"{bcolors.FAIL}Nu este nicio vanzare de modificat "
              f"incearca sa adaugi o vanzare: {bcolors.ENDC}")
        return lista
    else:
        id = getIdUI(lista,True)
        titlu = input(f"dati noul titlu al cartii: {bcolors.ENDC}")
        gen = input("dati noul gen ")
        pret = getPret()
        tip_reducere = getTipReducere()
        rezultat = modificaVanzare(id,titlu,gen,pret,tip_reducere,lista)
        undoLista.append(lista)
        redoLista.clear()
        return rezultat


def getIdUI(lista,desiredResult = False):
    id = input(f"{bcolors.BOLD}{bcolors.OKYELLOW}Introduceti ID: {bcolors.ENDC}")
    while validate_unique_id(id,lista) is desiredResult:
        print("Id-ul este invalid,incearca din nou")
        id = input(f"{bcolors.BOLD}{bcolors.OKYELLOW}Introduceti ID: {bcolors.ENDC}")
    return id


def uinrTitluriDistincte(lista):
    rezultat = afisareNrTitluriDistincteGen(lista)
    for gen in rezultat.keys():
        print("Gen {0}, Numar Titluri: {1}".format(gen, rezultat[gen]))


def uiModificareGenLista(lista,undoLista,redoLista):
    if validate_len_lista(lista) is False:
        print(f"{bcolors.FAIL}Nu este nicio vanzare facută "
              f"incearcă să adaugi o vanzare: {bcolors.ENDC}")
    else:
        print("avem urmatoarele vanzari")
        for vanzare in lista:
            print("titlu: {0} , gen:{1}".format(gettitlu(vanzare), getgen(vanzare)))
        titlu = input("titlul pentru care modificam genul: ")
        gen = input("noul gen: ")
        rezultat = modificareGen(lista, titlu, gen)
        undoLista.append(lista)
        redoLista.clear()
        return rezultat

def uiaplicareDiscount(lista, undoLista, redoLista):
    rezultat = aplicareDiscount(lista)
    undoLista.append(lista)
    redoLista.clear()
    return rezultat

def uiPretMinimGen(lista):
    if validate_len_lista(lista) is False:
        print(f"{bcolors.FAIL}Nu este nicio vanzare facută "
              f"incearcă să adaugi o vanzare: {bcolors.ENDC}")
        return lista
    else:
        gen = input("dati genul dorit")
        minim = pretMinimGen(lista, gen)
        print("pretul minim pentru genul {} este ".format(gen) + str(minim))
        return minim


def uiOrdonareCrescatorLista(lista,undoLista,redoLista):
    if validate_len_lista(lista) is False:
        print(f"{bcolors.FAIL}Nu este nicio vanzare facută "
              f"incearcă să adaugi o vanzare: {bcolors.ENDC}")
    else:
        rezultat = ordonareCrescatoarePret(lista)
        undoLista.append(lista)
        redoLista.clear()
        return rezultat


def uiNrTitluriDistincte(lista):
    if len(lista) < 1:
        print(f"{bcolors.FAIL}Nu este nicio vanzare facută "
              f"incearcă să adaugi o vanzare: {bcolors.ENDC}")
        return lista
    else:
        uinrTitluriDistincte(lista)


def ShowAll(lista):
    if len(lista) == 0:
        print(f"{bcolors.OKGREEN}{bcolors.BOLD}Momentan nu sunt vanzari.")
        print(f"Puteti face vanzare folosind optiunea 1{bcolors.ENDC}")
    else:
        for vanzare in lista:
            print(toString(vanzare))
    while True:
        input("apasa orice tasta daca vrei sa iesi: ")
        break


def uiAdaugaVanzare2(date,lista):
    if validate_adaugaVanzare_meniu2(date,lista) is True:
        return adaugaVanzare(date[0],date[1],date[2],int(date[3]),date[4],lista)
    else:
        print("eroare,reincercati!")
        return lista


def uiStergereVanzare2(lista,date):
    if validate_unique_id(date[0],lista) is False:
        return stergereVanzare(date[0],lista)
    else:
        print(f"{bcolors.FAIL}Id ul nu se afla in lista de vanzari,reincercati{bcolors.ENDC}")
        return lista


def uiModificaVanzare2(date,lista):
    if validate_modificareVanzare_meniu2(date,lista) is True:
        return modificaVanzare(date[0],date[1],date[2],int(date[3]),date[4],lista)
    else:
        print("eroare,reincercati!")
        return lista


def runMenu():
    undoLista = []
    redoLista = []
    lista = []
    ok = True
    while ok == True:
        PrintMainMenu()
        mainoptiune = input("Dați optiunea: ")
        if mainoptiune == "1":
            while True:
                PrintMenu1()
                optiune = input("Dați optiunea: ")
                if optiune == "1":
                    lista = uiAdaugaVanzare(lista,undoLista,redoLista)
                elif optiune == "2":
                    lista = uiStergeVanzare(lista,undoLista,redoLista)
                elif optiune == "3":
                    lista = uiModificaVanzare(lista,undoLista,redoLista)
                elif optiune == "4":
                    if len(undoLista) > 0:
                        redoLista.append(lista)
                        lista = undoLista.pop()
                    else:
                        print("nu se poate face undo!")
                elif optiune == "5":
                    lista = uiaplicareDiscount(lista, undoLista, redoLista)
                elif optiune == "6":
                    lista = uiModificareGenLista(lista,undoLista,redoLista)
                elif optiune == "7":
                    uiPretMinimGen(lista)
                elif optiune == "8":
                    lista = uiOrdonareCrescatorLista(lista,undoLista,redoLista)
                elif optiune == "9":
                    uiNrTitluriDistincte(lista)
                elif optiune == "s" or optiune == "S":
                    lista = []
                elif optiune == "r" or optiune == "R":
                    if len(redoLista) > 0:
                        undoLista.append(lista)
                        lista = redoLista.pop()
                    else:
                        print("nu se poate face redo")
                elif optiune == "a":
                    ShowAll(lista)
                elif optiune == "x" or optiune == "X":
                    break
                else:
                    print("Optiune gresita, reincercati: ")
        elif mainoptiune == "2":
            while True:
                PrintMenu2()
                optiune = input("Dati optiunea: ")
                if optiune == "s":
                    while True:
                        date = citireDate()
                        optiune2 = comanda_date(date)
                        if optiune2 == "1":
                            lista = uiAdaugaVanzare2(date,lista)
                        elif optiune2 == "2":
                            lista = uiStergereVanzare2(lista,date)
                        elif optiune2 == "3":
                            lista = uiModificaVanzare2(date, lista)
                        elif optiune2 == "4":
                            lista = aplicareDiscount(lista)
                        elif optiune2 == "5":
                            lista = uiModificareGenLista(lista,undoLista,redoLista)
                        elif optiune2 == "6":
                            uiPretMinimGen(lista)
                        elif optiune2 == "7":
                            lista = uiOrdonareCrescatorLista(lista,undoLista,redoLista)
                        elif optiune2 == "8":
                            uiNrTitluriDistincte(lista)
                        elif optiune2 == "x":
                            break
                        elif optiune2 == "a":
                            ShowAll(lista)
                        elif optiune2 == "u":
                            pass
                        elif optiune2 == "r":
                            pass
                        else:
                            print("Opțiunea nu este validă, incearcă din nou!")
                elif optiune == "a":
                    meniuAjutor()
                elif optiune == "x" or optiune == "X":
                    break
                else:
                    print("Optiune gresita, reincercati: ")
        elif mainoptiune == "x" or mainoptiune == "X":
            break
        else:
            print("Optiune gresita, reincercati: ")

