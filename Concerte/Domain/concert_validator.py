from Domain.concert import Concert


class ConcertValid:
    def valideaza(self, concert:Concert):
        erori = []
        if concert.nume == '':
            erori.append("Numele nu poate sa fie gol")
        if concert.id == '':
            erori.append("Id-ul artistului nu poate fi gol")
        if erori:
            raise ValueError(erori)