from Domain.vanzare import gettipReducere, getpret, gettitlu, getgen, creareVanzare, getId


class bcolors:
    HEADER = '\033[95m'
    OKMAGENTA = '\033[35m'
    OKBLUE = '\033[94m'
    OKYELLOW = '\033[33m'
    OKCYAN = '\033[96m'
    OKORANGE='\033[43m'
    OKWHITE = '\033[37m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def aplicareDiscount(lista):
    listaNoua = []
    if len(lista) > 0:
        for vanzare in lista:
            a = int(getpret(vanzare))
            if gettipReducere(vanzare) == "Silver":
                vanzare = creareVanzare(getId(vanzare), gettitlu(vanzare), getgen(vanzare), 95/100 * a, gettipReducere(vanzare))
            elif gettipReducere(vanzare) == "Gold":
                vanzare = creareVanzare(getId(vanzare), gettitlu(vanzare), getgen(vanzare), 90/100 * a,
                                        gettipReducere(vanzare))
            listaNoua.append(vanzare)
    return listaNoua


def modificareGen(lista,titlu,gen):
    lista_noua = []
    if len(lista) > 0:
        for vanzare in lista:
            if gettitlu(vanzare) == titlu:
                vanzare1 = creareVanzare(getId(vanzare), gettitlu(vanzare), gen, getpret(vanzare), gettipReducere(vanzare))
                lista_noua.append(vanzare1)
            else:
                lista_noua.append(vanzare)
    return lista_noua


def pretMinimGen(lista,gen):
    minim = 0
    max = 0
    for vanzare in lista:
        if getpret(vanzare) > 0:
            max = getpret(vanzare)
    minim = max
    for vanzare in lista:
        if getgen(vanzare) == gen and getpret(vanzare) < minim:
            minim = getpret(vanzare)
    return minim


def ordonareCrescatoarePret(lista):
    return sorted(lista, key=lambda vanzare:getpret(vanzare),reverse=False)


def afisareNrTitluriDistincteGen(lista):
    titluriPerGen = {}
    for vanzare in lista:
        if getgen(vanzare) in titluriPerGen.keys():
            titluriPerGen[getgen(vanzare)] = titluriPerGen[getgen(vanzare)] + 1
        else:
            titluriPerGen[getgen(vanzare)] = 1
    return titluriPerGen


def comanda_date(date):
    if len(date) == 6 and date[5] == "adauga vanzare":
        optiune2 = "1"
        return optiune2
    elif len(date) == 2 and date[1] == "sterge vanzare":
        optiune2 = "2"
        return optiune2
    elif len(date) == 6 and date[5] == "modifica vanzare":
        optiune2 = "3"
        return optiune2
    elif len(date) == 1 and date[0] == "aplicare discount":
        optiune2 = "4"
        return optiune2
    elif len(date) == 3 and date[2] == "modificare gen":
        optiune2 = "5"
        return optiune2
    elif len(date) == 1 and date[0] == "determinare pret minim":
        optiune2 = "6"
        return optiune2
    elif len(date) == 1 and date[0] == "ordonare vanzari":
        optiune2 = "7"
        return optiune2
    elif len(date) == 1 and date[0] == "afisare numar titluri":
        optiune2 = "8"
        return optiune2
    elif len(date) == 1 and date[0] == "showall":
        optiune2 = "a"
        return optiune2
    elif len(date) == 1 and date[0] == "x":
        optiune2 = "x"
        return optiune2











