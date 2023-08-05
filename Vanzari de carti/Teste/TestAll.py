from Teste.TestCRUD import testAdaugaVanzare, testStergereVanzare, testModificaVanzare
from Teste.Test_Domain import test_CreeazaVanzare
from Teste.teste_fuctionalitati import testAplicarediscount, testModificareGen, testPretMinimGen, \
    testOrdonareCrescatorPret, testNrTitluriDistincteGen, testAplicareDiscountUndoRedo, testModificareGenUndoRedo, \
    testOrdonareCrescatorPretUndoRedo, testUndoRedoCerintaLive


def runAllTests():
    test_CreeazaVanzare()
    testAdaugaVanzare()
    testStergereVanzare()
    testModificaVanzare()
    testAplicarediscount()
    testModificareGen()
    testPretMinimGen()
    testOrdonareCrescatorPret()
    testNrTitluriDistincteGen()
    testAplicareDiscountUndoRedo()
    testModificareGenUndoRedo()
    testOrdonareCrescatorPret()
    testOrdonareCrescatorPretUndoRedo()
    testUndoRedoCerintaLive()