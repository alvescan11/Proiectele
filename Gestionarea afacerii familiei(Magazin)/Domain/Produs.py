from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Produs(Entity):
    nume: str
    pret: float
    tip: str
    furnizor: str
