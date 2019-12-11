import itertools
from typing import Iterable

from advent.day02 import IntCodeComputer
from advent.day05 import run
from advent.day07.input import INPUT


def _link(input: int, stream: Iterable[int]):
    yield input
    yield from stream


def amplifier(values, input_code=None) -> int:
    """ 3,1,2,4,0 """
    code = IntCodeComputer(input_code or INPUT)

    [a, b, c, d, e] = values

    amp_1 = run(code, [a, 0])
    amp_2 = run(code, _link(b, amp_1))
    amp_3 = run(code, _link(c, amp_2))
    amp_4 = run(code, _link(d, amp_3))
    amp_5 = run(code, _link(e, amp_4))

    return list(amp_5)[0]


def part_one():
    inputs = itertools.combinations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    thrusts = [amplifier(i) for i in inputs]
    return max(thrusts)
