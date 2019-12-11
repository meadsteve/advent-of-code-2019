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


INSTRUCTION_SET = DEFAULT_INSTRUCTION_SET.copy()

INSTRUCTION_SET[5] = opcode_jump_if_true
INSTRUCTION_SET[6] = opcode_jump_if_false
INSTRUCTION_SET[7] = opcode_less_than
INSTRUCTION_SET[8] = opcode_equals


def part_two():
    starting_computer = IntCodeComputer(INPUT)
    output = run(starting_computer, [5], INSTRUCTION_SET)
    return list(output)[0]
