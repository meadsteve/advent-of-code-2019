from typing import Iterable, List

from advent.day02 import IntCodeComputer
from advent.day05 import run
from advent.day05.part_two import INSTRUCTION_SET
from advent.day07.input import INPUT


def _link(input: int, stream: Iterable[int]):
    yield input
    yield from stream


def _run(code, input_stream):
    return run(code, input_stream, INSTRUCTION_SET)


def amplifier(values, input_code=None) -> int:
    """ 3,1,2,4,0 """
    code = IntCodeComputer(input_code or INPUT)

    [a, b, c, d, e] = values

    amp_1 = _run(code, [a, 0])
    amp_2 = _run(code, _link(b, amp_1))
    amp_3 = _run(code, _link(c, amp_2))
    amp_4 = _run(code, _link(d, amp_3))
    amp_5 = _run(code, _link(e, amp_4))

    return list(amp_5)[0]


def _combinations() -> Iterable[List[int]]:
    for a in range(0, 10):
        for b in range(0, 10):
            for c in range(0, 10):
                for d in range(0, 10):
                    for e in range(0, 10):
                        yield [a, b, c, d, e]


def part_one():
    thrusts = [amplifier(i) for i in _combinations()]
    return max(thrusts)
