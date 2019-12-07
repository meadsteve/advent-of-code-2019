# does python not have this
from typing import Iterable

from advent.day03.models import Wire, Point


def from_strings(input: Iterable[str]) -> Wire:
    wire = Wire([Point(0, 0)])
    for statement in input:
        direction = statement[0: 1]
        distance = int(statement[1:])
        if direction == "R":
            move_right(wire, distance)
        elif direction == "L":
            move_left(wire, distance)
        elif direction == "U":
            move_up(wire, distance)
        elif direction == "D":
            move_down(wire, distance)
        else:
            raise ValueError("unexpected instruction")
    return wire


sign = lambda a: (a > 0) - (a < 0)


# TODO: make refactor the common stuff in these four
def move_right(wire: Wire, distance) -> Wire:
    """ Danger: for now the path mutates"""
    start = wire[-1]
    direction = sign(distance)
    for x in range(start.x + direction, start.x + distance + direction, direction):
        wire.append(Point(x, start.y))
    return wire


def move_left(wire: Wire, distance) -> Wire:
    return move_right(wire, distance * -1)


def move_up(wire: Wire, distance):
    """ Danger: for now the path mutates"""
    start = wire[-1]
    direction = sign(distance)
    for y in range(start.y + direction, start.y + distance + direction, direction):
        wire.append(Point(start.x, y))
    return wire


def move_down(wire: Wire, distance) -> Wire:
    return move_up(wire, distance * -1)
