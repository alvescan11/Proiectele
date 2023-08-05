def creareVanzare(id, titlu, gen, pret, tipReducere):
    '''
    creeaza un dictionar care reprezinta vanzari de  carti
    :param id: str
    :param titlu: str
    :param gen: str
    :param pret: float
    :param tipReducere: str
    :return:un dictionar ce contine o vanzare
    '''
    return{
        "id": id,
        "titlu" : titlu,
        "gen" : gen,
        "pret" : pret,
        "tipReducere" : tipReducere,
          }

def getId(Vanzare):
    '''
    da id-ul unei vanzari
    :param Vanzare:dictionar ce contine o vanzare
    :return:meniul vanzare
    '''
    return Vanzare["id"]

def gettitlu(Vanzare):
    '''
    da numele unei vanzari
    :param Vanzare:
    :return:
    '''
    return Vanzare["titlu"]

def getgen(Vanzare):
    return Vanzare["gen"]

def getpret(Vanzare):
    return Vanzare["pret"]

def gettipReducere(Vanzare):
    return Vanzare["tipReducere"]

def toString(Vanzare):
    return "Id: {}, titlu: {}, gen: {}, pret: {}, tipReducere: {}".format(
        getId(Vanzare),
        gettitlu(Vanzare),
        getgen(Vanzare),
        getpret(Vanzare),
        gettipReducere(Vanzare),
    )