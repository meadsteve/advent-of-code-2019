from advent.day02 import IntCodeComputer
from advent.day02.computer import DEFAULT_INSTRUCTION_SET, ParameterModes
from advent.day05 import INPUT, run


def opcode_jump_if_true(computer: IntCodeComputer, pos_modes: ParameterModes):
    [a, b] = computer.read(2, 1)
    [p_a, p_b, _] = pos_modes
    if computer[a, p_a] != 0:
        computer.position = computer[b, p_b]
    else:
        computer.position = computer.position + 3


def opcode_jump_if_false(computer: IntCodeComputer, pos_modes: ParameterModes):
    [a, b] = computer.read(2, 1)
    [p_a, p_b, _] = pos_modes
    if computer[a, p_a] == 0:
        computer.position = computer[b, p_b]
    else:
        computer.position = computer.position + 3


def opcode_less_than(computer: IntCodeComputer, pos_modes: ParameterModes):
    [a, b, c] = computer.read(3, 1)
    [p_a, p_b, _] = pos_modes
    computer[c] = 1 if computer[a, p_a] < computer[b, p_b] else 0
    computer.position = computer.position + 4


def opcode_equals(computer: IntCodeComputer, pos_modes: ParameterModes):
    [a, b, c] = computer.read(3, 1)
    [p_a, p_b, _] = pos_modes
    computer[c] = 1 if computer[a, p_a] == computer[b, p_b] else 0
    computer.position = computer.position + 4


def part_two():
    extended_instructions = DEFAULT_INSTRUCTION_SET.copy()

    extended_instructions[5] = opcode_jump_if_true
    extended_instructions[6] = opcode_jump_if_false
    extended_instructions[7] = opcode_less_than
    extended_instructions[8] = opcode_equals

    starting_computer = IntCodeComputer(INPUT)
    output = run(starting_computer, [5], extended_instructions)
    return list(output)[0]
