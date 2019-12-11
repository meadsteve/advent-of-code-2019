import pytest

from advent.day03.models import Wire, Point
from advent.day03.solutions import part_two


def test_wire_tracks_how_far_away_a_point_is():
    wire = Wire([Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1)])
    assert wire.signal_delay(Point(2, 1)) == 3


def test_a_wire_that_loops_is_shorter_than_it_appears():
    wire = Wire([Point(0, 0), Point(0, 1), Point(1, 1), Point(2, 1), Point(3, 1), Point(3, 2), Point(2, 2),
                                                        Point(2, 1), Point(2, 0)])
    assert wire.signal_delay(Point(2, 0)) == 8
    assert wire.signal_delay(Point(2, 1)) == 3  # not 7


@pytest.mark.slowish
def test_part_two():
    assert part_two() == 66076
