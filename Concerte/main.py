from Domain.artist_validator import ArtistValid
from Domain.concert_validator import ConcertValid
from Repository.json_repository import JsonRepository
from Service.artistService import ArtistService
from Service.concertService import ConcertService
from UserInterface.console import Console


def main():
    artistRepository = JsonRepository("artisti.json")
    artist_validator = ArtistValid()
    concertRepository = JsonRepository("concerte.json")
    concert_validator = ConcertValid()

    artistService = ArtistService(artistRepository, artist_validator,concertRepository)
    concertService = ConcertService(concertRepository,concert_validator,artistRepository)

    console = Console(artistService,concertService)
    console.runMenu()
if __name__ == '__main__':
    main()
