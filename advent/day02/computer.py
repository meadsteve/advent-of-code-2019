from copy import copy
from dataclasses import dataclass
from typing import List, Tuple, Dict, Callable

Opcode = int
Instruction = List[int]
NounAndVerb = Tuple[int, int]
OPCODE_STOP = 99
OPCODE_ADD = 1
OPCODE_MUL = 2


@dataclass
class IntCodeComputer:
    program: List[int]
    position: int = 0

    def __copy__(self):
        return IntCodeComputer(copy(self.program), self.position)

    def __getitem__(self, key):
        return self.program[key]

    def __setitem__(self, key, value):
        self.program[key] = value

    @property
    def running(self):
        return self.read()[0] != OPCODE_STOP

    def read(self, length: int = 1, offset: int = 0) -> Instruction:
        start = self.position + offset
        end = start + length
        data = self[start:end]
        return data + [OPCODE_STOP] * (length - len(data))


def opcode_add(computer: IntCodeComputer):
    [a, b, c] = computer.read(3, 1)
    computer[c] = computer[a] + computer[b]
    computer.position = computer.position + 4


def opcode_mul(computer: IntCodeComputer):
    [a, b, c] = computer.read(3, 1)
    computer[c] = computer[a] * computer[b]
    computer.position = computer.position + 4


InstructionSet = Dict[Opcode, Callable[[IntCodeComputer], None]]


DEFAULT_INSTRUCTION_SET: InstructionSet = {
    OPCODE_ADD: opcode_add,
    OPCODE_MUL: opcode_mul
}


def next_state(computer: IntCodeComputer, instructions: InstructionSet = None) -> IntCodeComputer:
    instructions = instructions or DEFAULT_INSTRUCTION_SET
    output = copy(computer)
    opcode = output.read(1)[0]
    try:
        instructions[opcode](output)
    except KeyError:
        raise RuntimeError(f"{opcode} isn't a valid opcode")
    return output


def run(computer: IntCodeComputer) -> IntCodeComputer:
    while computer.running:
        computer = next_state(computer)
    return computer
