from advent.common import lines_from_file

Mass = int
Fuel = int


def fuel_required(mass: Mass) -> Fuel:
    """Also considers the weight of the fuel itself"""
    fuel_required_for_mass = simple_fuel_required(mass)
    if fuel_required_for_mass == 0:
        return 0
    return fuel_required_for_mass + fuel_required(fuel_required_for_mass)


def simple_fuel_required(mass):
    """Fuel required ignoring fuel weight"""
    return max((mass // 3) - 2, 0)


def solve_part_one():
    raw_masses = lines_from_file("advent/day01/input.txt")
    masses = (int(raw_mass) for raw_mass in raw_masses)
    return sum(simple_fuel_required(mass) for mass in masses)


def solve_part_two():
    raw_masses = lines_from_file("advent/day01/input.txt")
    masses = (int(raw_mass) for raw_mass in raw_masses)
    return sum(fuel_required(mass) for mass in masses)
