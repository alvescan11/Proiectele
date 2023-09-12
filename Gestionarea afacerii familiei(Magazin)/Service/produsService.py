from Domain.Produs import Produs
from Domain.ProdusValidator import ProdusValidator
from Repository.json_repository import JsonRepository


class ProdusService:
    def __init__(self, produsRepository: JsonRepository, produsValidator: ProdusValidator):
        self.produsRepository = produsRepository
        self.produsValidator = produsValidator

    def adauga(self, id_produs: str, nume: str, pret: float, tip: str, furnizor: str):
        produs = Produs(id_produs,nume,pret,tip,furnizor)
        self.produsValidator.valideaza(produs)
        self.produsRepository.create(produs)

    def sterge(self,id_entity):
        entity = self.produsRepository.read(id_entity)
        if entity is None:
            raise KeyError(f'Nu există entitate cu id-ul {id_entity} pe care să o ștergem.')
        self.produsRepository.delete(id_entity)

    def update_entity(self, id_produs: str, nume: str, pret: float, tip: str, furnizor: str):
        produs = Produs(id_produs,nume,pret,tip,furnizor)
        self.produsValidator.valideaza(produs)
        self.produsRepository.update(produs)

    def getAll(self):
        return self.produsRepository.read()

    def SortareDupaTip(self,tip):
        lista = []
        for produs in self.produsRepository.read():
            if produs.tip == tip:
                lista.append(produs)
            else:
                print("Nu exista niciun produs de acest tip")
        return lista

    def SortareDupaFurnizor(self,furnizor):
        lista = []
        for produs in self.produsRepository.read():
            if produs.furnizor == furnizor:
                lista.append(produs)
            else:
                print("Nu exita produs cu acest furnizor")
        return lista