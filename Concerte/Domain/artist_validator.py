from Domain.artist import Artist


class ArtistValid:
    def valid(self, artist: Artist):
        erori = []
        if artist.nume == '':
            erori.append("Numele nu poate sa fie nul")
        if erori:
            raise ValueError(erori)
