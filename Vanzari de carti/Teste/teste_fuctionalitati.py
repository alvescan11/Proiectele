from Domain.vanzare import getpret, getgen
from Logic.CRUD import adaugaVanzare
from Logic.Functionalitati import aplicareDiscount, modificareGen, pretMinimGen, ordonareCrescatoarePret, \
    afisareNrTitluriDistincteGen
from Teste.TestCRUD import getById


def testAplicarediscount():
    lista = []
    lista = adaugaVanzare("1","Harap-Alb","Basm",100,"Silver",lista)
    lista = adaugaVanzare("1", "Baltagul", "Roman", 50, "Gold",lista)

    lista =  aplicareDiscount(lista)
    assert len(lista) == 2
    assert getpret(lista[0]) == 95
    assert getpret(lista[1]) == 45

def testAplicareDiscountUndoRedo():
    undoLista = []
    redoLista = []
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Roman", 50, "Gold", lista)

    lista = aplicareDiscount(lista)
    assert len(lista) == 2
    assert getpret(lista[0]) == 95
    assert getpret(lista[1]) == 45
    if len(undoLista) > 0:
        redoLista.append(lista)
        lista = undoLista.pop()
        assert len(lista) == 2
        assert getpret(lista[0]) == 100
        assert getpret(lista[1]) == 50
    if len(redoLista) > 0:
        undoLista.append(lista)
        lista = redoLista.pop()
        assert len(lista) == 2
        assert getpret(lista[0]) == 95
        assert getpret(lista[1]) == 45

def testModificareGen():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Roman", 50, "Gold", lista)

    lista = modificareGen(lista,"Harap-Alb","Fabula")
    assert len(lista) == 2
    assert getgen(lista[0]) == "Fabula"
    assert getgen(lista[1]) == "Roman"


def testModificareGenUndoRedo():
    undoLista = []
    redoLista = []
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Roman", 50, "Gold", lista)

    lista = modificareGen(lista, "Harap-Alb", "Fabula")
    assert len(lista) == 2
    assert getgen(lista[0]) == "Fabula"
    assert getgen(lista[1]) == "Roman"
    if len(undoLista) > 0:
        redoLista.append(lista)
        lista = undoLista.pop()
        assert len(lista) == 2
        assert getgen(lista[0]) == "Basm"
        assert getgen(lista[1]) == "Roman"
    if len(redoLista) > 0:
        undoLista.append(lista)
        lista = redoLista.pop()
        assert len(lista) == 2
        assert getpret(lista[0]) == "Fabula"
        assert getpret(lista[1]) == "Roman"


def testPretMinimGen():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Basm", 50, "Gold", lista)

    min_p = pretMinimGen(lista,"Basm")
    assert len(lista) == 2
    assert min_p == 50

def testOrdonareCrescatorPret():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Basm", 50, "Gold", lista)

    lista = ordonareCrescatoarePret(lista)
    assert len(lista) == 2
    assert getpret(lista[0]) == 50
    assert getpret(lista[1]) == 100

def testOrdonareCrescatorPretUndoRedo():
    undoLista = []
    redoLista = []
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Basm", 50, "Gold", lista)

    lista = ordonareCrescatoarePret(lista)
    assert len(lista) == 2
    assert getpret(lista[0]) == 50
    assert getpret(lista[1]) == 100

    if len(undoLista) > 0:
        redoLista.append(lista)
        lista = undoLista.pop()
        assert len(lista) == 2
        assert getgen(lista[0]) == 100
        assert getgen(lista[1]) == 50
    if len(redoLista) > 0:
        undoLista.append(lista)
        lista = redoLista.pop()
        assert len(lista) == 2
        assert getpret(lista[0]) == 50
        assert getpret(lista[1]) == 100

def testNrTitluriDistincteGen():
    lista = []
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("1", "Baltagul", "Basm", 50, "Gold", lista)
    lista = adaugaVanzare("1", "Ion","Roman",200,"None",lista)

    nrt = afisareNrTitluriDistincteGen(lista)
    assert len(lista) == 3
    assert nrt["Basm"] == 2
    assert nrt["Roman"] == 1

def testUndoRedoCerintaLive():
    undoLista = []
    redoLista = []
    lista = []
    assert getById("1", lista) is None
    assert getById("1", lista) is None
    assert getById("1", lista) is None
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("2", "Baltagul", "Basm", 50, "Gold", lista)
    lista = adaugaVanzare("3", "Ion", "Roman", 200, "None", lista)
    if len(undoLista) > 0:
        undoLista.append(lista)
        redoLista.clear()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert lista[1] == ("2", "Baltagul", "Basm", 50, "Gold")
        assert getById("3",lista ) is None
        undoLista.append(lista)
        redoLista.clear()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert getById("2", lista) is None
        assert getById("3", lista) is None
        undoLista.append(lista)
        redoLista.clear()
        assert getById("1", lista) is None
        assert getById("2", lista) is None
        assert getById("3", lista) is None
        undoLista.append(lista)
        redoLista.clear()
        assert getById("1", lista) is None
        assert getById("2", lista) is None
        assert getById("3", lista) is None
    lista = adaugaVanzare("1", "Harap-Alb", "Basm", 100, "Silver", lista)
    lista = adaugaVanzare("2", "Baltagul", "Basm", 50, "Gold", lista)
    lista = adaugaVanzare("3", "Ion", "Roman", 200, "None", lista)
    if len(redoLista) > 0:
        undoLista.append(lista)
        lista = redoLista.pop()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert lista[1] == ("2", "Baltagul", "Basm", 50, "Gold")
        assert lista[2] == ("3", "Ion", "Roman", 200, "None")
    if len(undoLista) > 0:
        undoLista.append(lista)
        redoLista.clear()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert lista[1] == ("2", "Baltagul", "Basm", 50, "Gold")
        assert getById("3", lista) is None
        undoLista.append(lista)
        redoLista.clear()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert getById("2", lista) is None
        assert getById("3", lista) is None
    if len(redoLista) > 0:
        undoLista.append(lista)
        lista = redoLista.pop()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert lista[1] == ("2", "Baltagul", "Basm", 50, "Gold")
        assert getById("3", lista) is None
        undoLista.append(lista)
        lista = redoLista.pop()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert lista[1] == ("2", "Baltagul", "Basm", 50, "Gold")
        assert lista[2] == ("3", "Ion", "Roman", 200, "None")
    if len(undoLista) > 0:
        undoLista.append(lista)
        redoLista.clear()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert lista[1] == ("2", "Baltagul", "Basm", 50, "Gold")
        assert getById("3", lista) is None
        undoLista.append(lista)
        redoLista.clear()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert getById("2", lista) is None
        assert getById("3", lista) is None
    lista = adaugaVanzare("4","Morometii" , "Roman" , 200,"Gold",lista)
    if len(undoLista) > 0:
        undoLista.append(lista)
        redoLista.clear()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert getById("2", lista) is None
        assert getById("3", lista) is None
        assert getById("4", lista) is None
        undoLista.append(lista)
        redoLista.clear()
        assert getById("1" , lista) is None
        assert getById("2", lista) is None
        assert getById("3", lista) is None
        assert getById("4", lista) is None
    if len(redoLista) > 0:
        undoLista.append(lista)
        lista = redoLista.pop()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert getById("2", lista) is None
        assert getById("3", lista) is None
        assert getById("4", lista) is None
        undoLista.append(lista)
        lista = redoLista.pop()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert getById("2", lista) is None
        assert getById("3", lista) is None
        assert lista[3]("4", "Morometii","Roman",200,"Gold")
        undoLista.append(lista)
        lista = redoLista.pop()
        assert lista[0] == ("1", "Harap-Alb", "Basm", 100, "Silver")
        assert getById("2", lista) is None
        assert getById("3", lista) is None
        assert lista[3]("4", "Morometii", "Roman", 200, "Gold")




