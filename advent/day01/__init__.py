from typing import Iterable

from advent.common import lines_from_file

Mass = int
Fuel = int


def fuel_required(mass: Mass) -> Fuel:
    return (mass // 3) - 2


def total_fuel(masses: Iterable[Mass]) -> Fuel:
    return sum(fuel_required(mass) for mass in masses)


def solve_part_one():
    raw_masses = lines_from_file("advent/day01/input.txt")
    masses = (int(raw_mass) for raw_mass in raw_masses)
    return total_fuel(masses)
