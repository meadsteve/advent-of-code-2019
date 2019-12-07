from typing import Set

from advent.day03.models import Wire, Point


def crosses(wire_one: Wire, wire_two: Wire) -> Set[Point]:
    return set(wire_one).intersection(wire_two)
