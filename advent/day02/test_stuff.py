from copy import copy

import pytest

from advent.day02.computer import IntCodeComputer, next_state, run, DEFAULT_INSTRUCTION_SET
from advent.day02 import part_one, part_two


def test_computer_can_be_copied_but_still_compares_as_its_a_value_object():
    start = IntCodeComputer([1, 2])
    end = copy(start)

    assert start == end  # they are value objects


def test_computer_can_be_copied_and_when_the_list_is_mutated_they_are_not_equal():
    start = IntCodeComputer([1, 2])
    end = copy(start)
    end.program[0] = 5

    assert start != end


def test_opcode_1():
    prog = IntCodeComputer([1, 0, 0, 0, 99])
    (next_machine_state, _) = next_state(prog, DEFAULT_INSTRUCTION_SET)

    assert next_machine_state == IntCodeComputer([2, 0, 0, 0, 99], position=4)


def test_opcode_2():
    prog = IntCodeComputer([2, 3, 0, 3, 99])
    (next_machine_state, _) = next_state(prog, DEFAULT_INSTRUCTION_SET)

    assert next_machine_state == IntCodeComputer([2, 3, 0, 6, 99], position=4)


def test_opcode_99_marks_the_program_as_done():
    prog = IntCodeComputer([1, 0, 0, 0, 99])
    (next_machine_state, _) = next_state(prog, DEFAULT_INSTRUCTION_SET)

    assert prog.running
    assert not next_machine_state.running


def test_running():
    result = run(IntCodeComputer([1, 1, 1, 4, 99, 5, 6, 0, 99]))
    assert result == IntCodeComputer([30, 1, 1, 4, 2, 5, 6, 0, 99], position=8)


@pytest.mark.slowish
def test_part_one():
    assert part_one() == 4090701


@pytest.mark.slowish
def test_part_two():
    assert part_two() == 6421
