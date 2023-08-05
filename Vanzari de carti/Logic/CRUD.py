from Domain.vanzare import getId, creareVanzare, gettitlu, getpret, gettipReducere, getgen
def adaugaVanzare(id, titlu, gen, pret, tipReducere, lista):
    '''
    adauga o vanzare intr-o lista
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipReducere:
    :param lista:
    :return:
    '''
    vanzare = creareVanzare(id, titlu, gen, pret, tipReducere)
    return lista + [vanzare]


def stergereVanzare(id, lista):
    '''
    sterge o vanzare din lista
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipReducere:
    :param lista:
    :return:
    '''
    return [vanzare for vanzare in lista if getId(vanzare) != id]


def modificaVanzare(id, titlu, gen, pret, tipReducere, lista):
    '''
    modifica o vanzare din lista
    :param id:
    :param titlu:
    :param gen:
    :param pret:
    :param tipReducere:
    :param lista:
    :return:
    '''

    listaNoua = []
    for vanzare in lista:
        if getId(vanzare) == id:
            vanzareNoua = creareVanzare(id, titlu, gen, pret, tipReducere)
            listaNoua.append(vanzareNoua)
        else:
            listaNoua.append(vanzare)
    return listaNoua
