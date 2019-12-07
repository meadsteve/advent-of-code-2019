from advent.day04 import digit_neighbours_exist, digits_ascend, part_one


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


def test_part_one():
    assert part_one() == 2814
