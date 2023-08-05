import Service
from Domain.concert import Concert
from Domain.concert_validator import ConcertValid
from Repository.json_repository import JsonRepository


class ConcertService:
    def __init__(self,concertRepository:JsonRepository,concert_validator:ConcertValid,
                 artistRepository:JsonRepository):
        self.concertRepository = concertRepository
        self.concert_validator = concert_validator
        self.artistRepository = artistRepository

    def getAll(self):
        return self.concertRepository.read()

    def adauga(self,id_concert: str,id: str , nume: str , locatie: str, capacitate: int ):
        if self.artistRepository.read(id) is None:
            raise KeyError("Acest id nu exista")
        concert = Concert(id_concert,id,nume,locatie,capacitate)
        self.concert_validator.valideaza(concert)
        self.concertRepository.create(concert)

       

