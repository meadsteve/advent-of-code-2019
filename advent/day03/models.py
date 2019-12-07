from dataclasses import dataclass
from typing import List, Dict


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
    _length_at_point: Dict[int, int]
    _current_length: int = -1

    def __init__(self, initial_path: List[Point]):
        self.path = []
        self._length_at_point = {}
        for point in initial_path:
            self.append(point)

    def append(self, point: Point):
        self._current_length = self._current_length + 1
        self.path.append(point)
        if self._length_at_point.get(hash(point)) is None:
            self._length_at_point[hash(point)] = self._current_length

    def __getitem__(self, k):
        return self.path[k]

    def signal_delay(self, end: Point) -> int:
        return self._length_at_point[hash(end)]
