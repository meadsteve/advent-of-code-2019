from dataclasses import dataclass
from typing import List, Dict, Optional

from advent.common import lines_from_file


@dataclass
class OrbitalItem:
    name: str
    orbited_by: List["OrbitalItem"]
    orbits: Optional["OrbitalItem"]

    def __init__(self, name: str, orbits=None, orbited_by=None):
        self.name = name
        self.orbited_by = orbited_by or []
        self.orbits = None

    def add_orbiter(self, orbiter: "OrbitalItem"):
        self.orbited_by.append(orbiter)
        orbiter.orbits = self

    @property
    def total_orbital_count(self) -> int:
        if not self.orbited_by:
            return 0
        return len(self.orbited_by) + sum([o.total_orbital_count for o in self.orbited_by])

    def __eq__(self, other):
        return self.name == other.name

@dataclass
class OrbitalMap:
    _items: Dict[str, OrbitalItem]

    def __init__(self):
        self._items = {}

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


def orbital_chain(start: OrbitalItem, target: OrbitalItem) -> List[str]:
    if not target.orbits:
        return [target.name]
    return [target.name] + orbital_chain(start, target.orbits)


def _orbits_from_input():
    lines = lines_from_file("advent/day06/input.txt")
    pairs = (line.split(")") for line in lines)
    orbits = new_map()
    for (a, b) in pairs:
        add_orbit(orbits, a, b)
    return orbits


def solve_part_one():
    orbits = _orbits_from_input()
    return sum([o.total_orbital_count for o in orbits])


def solve_part_two():
    # Assumption: The path between the two can be found
    #             by tracing the path back to the common
    #             planet they both orbit.
    orbits = _orbits_from_input()
    chain_for_target = orbital_chain(orbits["COM"], orbits["SAN"])
    chain_for_origin = orbital_chain(orbits["COM"], orbits["YOU"])
    common_points = list(set(chain_for_target) & set(chain_for_origin))
    for point in common_points:
        chain_for_target.remove(point)
        chain_for_origin.remove(point)
    return len(chain_for_origin) + len(chain_for_target) - 2

