from typing import Iterable


def lines_from_file(path: str) -> Iterable[str]:
    with open(path) as open_file:
        lines = (line.rstrip('\n') for line in open_file)
        yield from lines
