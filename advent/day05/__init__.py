from typing import Callable, List, Tuple

from advent.day02.computer import DEFAULT_INSTRUCTION_SET, IntCodeComputer, ParameterModes, next_state, OPCODE_STOP
from advent.day05.input import INPUT

OutputData = List[int]


def run(computer: IntCodeComputer, input_value=OPCODE_STOP) -> Tuple[IntCodeComputer, OutputData]:
    output: OutputData = []

    def add_output(new, existing: OutputData):
        existing.append(new)

    extended_instructions = DEFAULT_INSTRUCTION_SET.copy()
    extended_instructions[3] = create_read_instruction(lambda: input_value)
    extended_instructions[4] = create_output_instruction(lambda o: add_output(o, output))
    while computer.running:
        computer = next_state(computer, extended_instructions)
    return computer, output


def create_read_instruction(reader: Callable[[], int]):
    def _opcode_read(computer: IntCodeComputer, _pos_modes: ParameterModes):
        memory_location = computer.read(1, 1)[0]
        computer[memory_location] = reader()
        computer.position = computer.position + 2
    return _opcode_read


def create_output_instruction(outputer: Callable[[int], None]):
    def _opcode_write(computer: IntCodeComputer, pos_modes: ParameterModes):
        memory_location = computer.read(1, 1)[0]
        [mode, _, _] = pos_modes
        outputer(computer[memory_location, mode])
        computer.position = computer.position + 2
    return _opcode_write


def part_one():
    starting_computer = IntCodeComputer(INPUT)
    output = run(starting_computer, 1)
    return output[1]
