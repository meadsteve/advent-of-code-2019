from advent.day03.solutions import part_one
from advent.day03.wire_logic import crosses
from advent.day03.models import Wire, Point
from advent.day03.movement import move_left, move_up, move_down, move_right, from_strings


def test_moving_right():
    line: Wire = move_right([Point(0, 0)], 3)
    assert line == [Point(0, 0), Point(1, 0), Point(2, 0), Point(3, 0)]


def test_moving_left():
    line: Wire = move_left([Point(3, 0)], 3)
    assert line == [Point(3, 0), Point(2, 0), Point(1, 0), Point(0, 0)]


def test_moving_up():
    line: Wire = move_up([Point(1, 0)], 2)
    assert line == [Point(1, 0), Point(1, 1), Point(1, 2)]


def test_moving_down():
    line: Wire = move_down([Point(1, 2)], 2)
    assert line == [Point(1, 2), Point(1, 1), Point(1, 0)]


def test_find_crossing_points():
    wire_one = [Point(1, 2), Point(1, 1), Point(1, 0), Point(2, 0), Point(2, 1)]
    wire_two = [Point(0, 1), Point(1, 1), Point(2, 1), Point(3, 1)]

    assert crosses(wire_one, wire_two) == {Point(1, 1), Point(2, 1)}


def test_distance_from_origin():
    assert Point(1, 2).distance_from_o == 3


def test_string_decoding():
    result = from_strings(["U2", "R3"])
    assert result == [Point(0, 0), Point(0, 1), Point(0, 2), Point(1, 2), Point(2, 2), Point(3, 2)]


def test_part_one():
    assert part_one() == []