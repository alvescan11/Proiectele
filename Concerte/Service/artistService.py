import jsonpickle

from Domain.artist import Artist
from Domain.artist_validator import ArtistValid
from Repository.json_repository import JsonRepository


class ArtistService:
    def __init__(self, artistRepository: JsonRepository, artist_validator: ArtistValid,concertRepository:JsonRepository):
        self.artistRepository = artistRepository
        self.artist_validator = artist_validator
        self.concertRepository =concertRepository

    def adaug(self, id_artist: str, nume: str, categorie: str, tarif: float):
        artist = Artist(id_artist, nume, categorie, tarif)
        self.artist_validator.valid(artist)
        self.artistRepository.create(artist)

    def getAll(self):
        return self.artistRepository.read()

    def AfisareArtisti(self , categorie: str):
        lista = []
        for artist in self.artistRepository.read():
            if categorie == artist.categorie:
                lista.append(artist)
        return sorted(lista,key= lambda x:x.tarif, reverse=True)

    def NumarConcerte(self):
        dictionar = {}
        for artist in self.artistRepository.read():
            dictionar[artist.categorie] = 0
        for concert in self.concertRepository.read():
            artist = self.artistRepository.read(concert.id)
            dictionar[artist.categorie] += 1
        return dictionar

    def ExportJson(self, filename: str):
        dictionar = {}
        for artist in self.artistRepository.read():
            dictionar[artist.nume] = []
        for concert in self.concertRepository.read():
            artist = self.artistRepository.read(concert.id)
            dictionar[artist.nume].append(concert.locatie)

        with open(filename, "w") as f:
            f.write(jsonpickle.dumps(dictionar))








