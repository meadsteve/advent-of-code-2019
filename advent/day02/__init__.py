from typing import Optional

from advent.day02.computer import IntCodeComputer, run, NounAndVerb
from advent.day02.input import PUZZLE_INPUT


def part_one():
    starting_computer = IntCodeComputer(PUZZLE_INPUT)
    return get_output_for_input(starting_computer, 12, 2)


def part_two():
    starting_computer = IntCodeComputer(PUZZLE_INPUT)
    match = find_target_value(starting_computer, 19690720)
    if match:
        (noun, verb) = match
        return (100 * noun) + verb
    return None


def get_output_for_input(computer: IntCodeComputer, a: int, b: int) -> int:
    computer[1] = a
    computer[2] = b

    result = run(computer)
    return result[0]


def find_target_value(computer: IntCodeComputer, goal: int) -> Optional[NounAndVerb]:
    for noun in range(0, 99):
        for verb in range(0, 99):
            if get_output_for_input(computer, noun, verb) == goal:
                return noun, verb
    return None
