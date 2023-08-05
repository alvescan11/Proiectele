from Domain.vanzare import getId


def validate_pret(pret):
    try:
        if float(pret) < 0:
            return False
        return True
    except ValueError as er:
        return False


def validate_unique_id(id,lista):
    for vanzare in lista:
        if getId(vanzare) == id:
            return False
    return True


def validate_len_lista(lista):
    if len(lista) < 1:
        return False
    return True


def validate_adaugaVanzare_meniu2(date,lista):
    if validate_unique_id(date[0], lista) is False:
        return False
    if validate_pret(date[3]) is False:
        return False
    if date[4] == "None" or date[4] == "Silver" or date[4] == "Gold":
        return True
    else:
        return False


def validate_modificareVanzare_meniu2(date,lista):
    if validate_unique_id(date[0], lista) is True:
        return False
    if validate_pret(date[3]) is False:
        return False
    if date[4] == "None" or date[4] == "Silver" or date[4] == "Gold":
        return True
    else:
        return False

