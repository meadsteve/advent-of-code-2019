from advent.day02 import IntCodeComputer
from advent.day05 import run, part_one


def test_value_mode():
    prog = IntCodeComputer([11101, 0, 0, 0, 99])
    output = run(prog)

    assert output[0] == IntCodeComputer([0, 0, 0, 0, 99], position=4)


def test_reading_from_input():
    prog = IntCodeComputer([3, 1, 99])
    output = run(prog, 55)

    assert output[0] == IntCodeComputer([3, 55, 99], position=2)


def test_writing_to_output():
    prog = IntCodeComputer([4, 3, 99, 101])
    output = run(prog)

    assert output[1] == [101]


def test_example():
    prog = IntCodeComputer([3, 0, 4, 0, 99])
    output = run(prog, 56)[1][0]
    assert output == 56


def test_part_one():
    assert part_one() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 9938601]
