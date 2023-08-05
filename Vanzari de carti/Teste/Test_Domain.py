from Domain.vanzare import creareVanzare, getId, gettitlu, getgen, getpret, gettipReducere


def test_CreeazaVanzare():
    vanzare = creareVanzare("1","Harap-Alb", "basm", "1000", "None")
    assert getId(vanzare) == "1"
    assert gettitlu(vanzare) == "Harap-Alb"
    assert getgen(vanzare) == "basm"
    assert getpret(vanzare) == "1000"
    assert gettipReducere(vanzare) == "None"