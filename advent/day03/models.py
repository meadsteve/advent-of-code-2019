from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int

    @property
    def distance_from_o(self):
        return abs(self.x) + abs(self.y)

    def __hash__(self):
        return hash(f'{self.x}-{self.y}')


@dataclass
class Wire:
    path: List[Point]

    def append(self, point: Point):
        self.path.append(point)

    def __getitem__(self, k):
        return self.path[k]
