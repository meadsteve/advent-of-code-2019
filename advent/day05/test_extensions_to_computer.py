from advent.day02 import IntCodeComputer
from advent.day05 import run, part_one
from advent.day05.part_two import part_two


def test_writing_to_output():
    prog = IntCodeComputer([4, 3, 99, 101])
    output = run(prog)

    assert list(output)[0] == 101


def test_example():
    prog = IntCodeComputer([3, 0, 4, 0, 99])
    output = list(run(prog, [56]))
    assert output[0] == 56


def test_part_one():
    assert part_one() == 9938601


def test_part_two():
    assert part_two() == 4283952
