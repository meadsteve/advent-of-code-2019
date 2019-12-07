from dataclasses import dataclass
from typing import List

Wire = List["Point"]


@dataclass
class Point:
    x: int
    y: int

    @property
    def distance_from_o(self):
        return abs(self.x) + abs(self.y)

    def __hash__(self):
        return hash(f'{self.x}-{self.y}')
