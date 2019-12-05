from copy import copy
from dataclasses import dataclass
from typing import List, Tuple, Optional

from advent.day02.input import INPUT

Instruction = Tuple[int, int, int, int]


@dataclass
class IntCodeComputer:
    program: List[int]
    position: int = 0

    def __copy__(self):
        return IntCodeComputer(copy(self.program), self.position)

    def __getitem__(self, key):
        return self.program[key] if key < len(self.program) else None

    def __setitem__(self, key, value):
        self.program[key] = value

    @property
    def running(self):
        (opcode, _, _, _) = self.instruction
        return opcode != 99

    @property
    def instruction(self) -> Instruction:
        return self[self.position], self[self.position + 1], self[self.position + 2], self[self.position + 3]


def next_state(computer: IntCodeComputer) -> IntCodeComputer:
    output = copy(computer)
    (opcode, a, b, c) = output.instruction
    if opcode == 1:
        output[c] = output[a] + output[b]
    elif opcode == 2:
        output[c] = output[a] * output[b]
    else:
        raise RuntimeError(f"{opcode} isn't a valid opcode")
    output.position = output.position + 4
    return output


def run(computer: IntCodeComputer) -> IntCodeComputer:
    while computer.running:
        computer = next_state(computer)
    return computer


def part_one():
    result = run(IntCodeComputer(INPUT))
    return result[0]
