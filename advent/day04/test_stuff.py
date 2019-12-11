import pytest

from advent.day04 import digit_neighbours_exist, digits_ascend, part_one, digit_neighbours_exist_only_as_a_pair, \
    part_two


def test_digit_neighbours():
    assert digit_neighbours_exist(112345)
    assert digit_neighbours_exist(142355)
    assert digit_neighbours_exist(183345)

    assert not digit_neighbours_exist(123456)


def test_digits_ascend():
    assert digits_ascend(123456)
    assert digits_ascend(123446)
    assert digits_ascend(145678)

    assert not digits_ascend(123454)
    assert not digits_ascend(121456)


def test_digit_neighbours_exist_only_as_a_pair():
    assert digit_neighbours_exist_only_as_a_pair(113456)
    assert digit_neighbours_exist_only_as_a_pair(123455)
    assert digit_neighbours_exist_only_as_a_pair(111445)

    assert not digit_neighbours_exist_only_as_a_pair(111456)
    assert not digit_neighbours_exist_only_as_a_pair(123555)
    assert not digit_neighbours_exist_only_as_a_pair(125556)


@pytest.mark.slowish
def test_part_one():
    assert part_one() == 2814


@pytest.mark.slowish
def test_part_two():
    assert part_two() == 1991
