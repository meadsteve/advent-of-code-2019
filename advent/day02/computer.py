from copy import copy
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Tuple, Dict, Callable

Opcode = int
Instruction = List[int]
NounAndVerb = Tuple[int, int]
OPCODE_STOP = 99
OPCODE_ADD = 1
OPCODE_MUL = 2


class ParameterMode(Enum):
    postition_mode = auto()
    immediate_mode = auto()


ParameterModes = List[ParameterMode]


@dataclass
class IntCodeComputer:
    program: List[int]
    position: int = 0

    def __copy__(self):
        return IntCodeComputer(copy(self.program), self.position)

    def __getitem__(self, key):
        try:
            (index, read_mode) = key
            return self.fetch(index, read_mode)
        except:
            return self.fetch(key, ParameterMode.postition_mode)

    def __setitem__(self, key, value):
        self.program[key] = value

    @property
    def running(self):
        return self.read()[0] != OPCODE_STOP

    def read(self, length: int = 1, offset: int = 0) -> Instruction:
        start = self.position + offset
        end = start + length
        data = self.program[start:end]
        return data + [OPCODE_STOP] * (length - len(data))

    def fetch(self, postion: int, mode: ParameterMode):
        if mode == ParameterMode.immediate_mode:
            return postion
        elif mode == ParameterMode.postition_mode:
            return self.program[postion]
        else:
            raise ValueError("unknown mode")


def opcode_add(computer: IntCodeComputer, pos_modes: ParameterModes):
    [a, b, c] = computer.read(3, 1)
    [p_a, p_b, _] = pos_modes
    computer[c] = computer[a, p_a] + computer[b, p_b]
    computer.position = computer.position + 4


def opcode_mul(computer: IntCodeComputer, pos_modes: ParameterModes):
    [a, b, c] = computer.read(3, 1)
    [p_a, p_b, _] = pos_modes
    computer[c] = computer[a, p_a] * computer[b, p_b]
    computer.position = computer.position + 4


InstructionSet = Dict[Opcode, Callable[[IntCodeComputer, ParameterModes], None]]


DEFAULT_INSTRUCTION_SET: InstructionSet = {
    OPCODE_ADD: opcode_add,
    OPCODE_MUL: opcode_mul
}


def next_state(computer: IntCodeComputer, instructions: InstructionSet) -> IntCodeComputer:
    output = copy(computer)
    command = output.read(1)[0]
    opcode = _parse_opcode(command)
    position_modes = _parse_parameter_modes(command)
    try:
        instructions[opcode](output, position_modes)
    except KeyError:
        raise RuntimeError(f"{opcode} isn't a valid opcode")
    return output


def _parse_parameter_modes(command: int) -> ParameterModes:
    command = abs(command)
    opcode = _parse_opcode(command)
    position_string = str(int((command - opcode) / 100))
    padding = ([ParameterMode.postition_mode] * (3 - len(position_string)))
    return list(reversed(padding + [
        ParameterMode.immediate_mode if a == "1" else ParameterMode.postition_mode
        for a in position_string
    ]))


def _parse_opcode(command: int) -> int:
    opcode = command % 100
    return opcode


def run(computer: IntCodeComputer, instructions: InstructionSet = None) -> IntCodeComputer:
    instructions = instructions or DEFAULT_INSTRUCTION_SET
    while computer.running:
        computer = next_state(computer, instructions)
    return computer
