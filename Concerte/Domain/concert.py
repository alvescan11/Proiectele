from dataclasses import dataclass

from Domain.entity import Entity

@dataclass
class Concert(Entity):
    id: str
    nume: str
    locatie: str
    capacitate: int
