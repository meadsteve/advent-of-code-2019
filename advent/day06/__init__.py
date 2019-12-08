from dataclasses import dataclass, field
from typing import List, Dict

from advent.common import lines_from_file


@dataclass
class OrbitalItem:
    name: str
    orbited_by: List["OrbitalItem"]

    def __init__(self, name: str, orbited_by=None):
        self.name = name
        self.orbited_by = orbited_by or []

    def add_orbiter(self, orbiter: "OrbitalItem"):
        self.orbited_by.append(orbiter)

    @property
    def total_orbital_count(self) -> int:
        if not self.orbited_by:
            return 0
        return len(self.orbited_by) + sum([o.total_orbital_count for o in self.orbited_by])

@dataclass
class OrbitalMap:
    _items: Dict[str, OrbitalItem]

    def __init__(self):
        self._items = {}
        self._add("COM")

    def _add(self, item_name: str) -> OrbitalItem:
        new_item = OrbitalItem(item_name)
        self._items[item_name] = new_item
        return new_item

    def __getitem__(self, item_name: str) -> OrbitalItem:
        return self._items.get(item_name) or self._add(item_name)

    def __iter__(self):
        yield from self._items.values()


def new_map() -> OrbitalMap:
    return OrbitalMap()


def add_orbit(orbits: OrbitalMap, orbited: str, orbiter: str):
    orbits[orbited].add_orbiter(orbits[orbiter])


def solve_part_one():
    lines = lines_from_file("advent/day06/input.txt")
    pairs = (line.split(")") for line in lines)

    orbits = new_map()
    for (a, b) in pairs:
        add_orbit(orbits, a, b)

    return sum([o.total_orbital_count for o in orbits])
