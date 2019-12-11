import pytest

from advent.day07 import amplifier, part_one


def test_example():
    thrust = amplifier([4, 3, 2, 1, 0], input_code=[3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0])
    assert thrust == 43210


def test_next_example():
    thrust = amplifier([0, 1, 2, 3, 4], input_code=[3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23,
                                                    101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0])
    assert thrust == 54321


def test_next_next_example():
    thrust = amplifier([1, 0, 4, 3, 2], input_code=[3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33,
                                                    1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0])
    assert thrust == 65210


@pytest.mark.slowish
def test_part_one():
    assert part_one() == 116680
