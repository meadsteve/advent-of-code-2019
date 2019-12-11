from typing import Callable, List, Iterable

import typing

from advent.day02.computer import DEFAULT_INSTRUCTION_SET, IntCodeComputer, ParameterModes, next_state, OPCODE_STOP, \
    InstructionSet
from advent.day05.input import INPUT


def run(
    computer: IntCodeComputer,
    input_stream: typing.Optional[Iterable[int]] = None,
    instructions: InstructionSet = None
) -> typing.Generator[int, None, None]:
    extended_instructions = instructions.copy() if instructions else DEFAULT_INSTRUCTION_SET.copy()

    extended_instructions[3] = create_read_instruction(input_stream or [])
    extended_instructions[4] = create_output_instruction()

    while computer.running:
        (computer, output) = next_state(computer, extended_instructions)
        if output is not None:
            yield output


def create_read_instruction(input_stream: Iterable[int]):
    def _iter():
        yield from input_stream
        while True:
            yield 0  # pad out short inputs
    iter_stream = _iter()

    def _opcode_read(computer: IntCodeComputer, _pos_modes: ParameterModes):
        memory_location = computer.read(1, 1)[0]
        computer[memory_location] = next(iter_stream)
        computer.position = computer.position + 2
    return _opcode_read


def create_output_instruction():
    def _opcode_write(computer: IntCodeComputer, pos_modes: ParameterModes):
        memory_location = computer.read(1, 1)[0]
        [mode, _, _] = pos_modes
        result = computer[memory_location, mode]
        computer.position = computer.position + 2
        return result

    return _opcode_write


def part_one():
    starting_computer = IntCodeComputer(INPUT)
    output = run(starting_computer, [1])
    return list(output)[-1]
