from Domain.vanzare import getId, gettitlu, getgen, getpret, gettipReducere
from Logic.CRUD import adaugaVanzare, stergereVanzare, modificaVanzare


def testAdaugaVanzare():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 1200,"None", lista)
    assert len(lista) == 1
    assert getId(getById("1",lista)) == "1"
    assert gettitlu(getById("1", lista)) == "Harap-Alb"
    assert getgen(getById("1", lista)) == "Basm"
    assert getpret(getById("1", lista)) == 1200
    assert gettipReducere(getById("1", lista)) == "None"


def getById(id, lista):
    """
    da rezervarea cu id-ul dintr-o lista
    :param id:id-ul
    :param lista:
    :return:
    """

    for vanzare in lista:
        if getId(vanzare) == id:
            return vanzare
    return None


def testStergereVanzare():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 1200, "None", lista)
    lista = adaugaVanzare("2", "Baltagul", "roman", 1000, "Gold", lista)
    lista = stergereVanzare("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None


def testModificaVanzare():
    lista = []
    lista = adaugaVanzare("1","Harap-Alb","Basm",100,"gold",lista)
    assert len(lista) == 1
    vanzare = getById("1",lista)
    assert gettitlu(vanzare) == "Harap-Alb"
    assert getgen(vanzare) == "Basm"
    assert getpret(vanzare) == 100
    assert gettipReducere(vanzare) == "gold"
    lista_noua = modificaVanzare("1","Baltagul","Roman",110,"silver",lista)
    vanzare_noua = getById("1",lista_noua)
    assert len(lista_noua) == 1
    assert gettitlu(vanzare_noua) == "Baltagul"
    assert getgen(vanzare_noua) == "Roman"
    assert getpret(vanzare_noua) == 110
    assert gettipReducere(vanzare_noua) == "silver"

