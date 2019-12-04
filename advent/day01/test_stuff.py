from advent.day01 import fuel_required, solve_part_one, simple_fuel_required, solve_part_two


def test_all_is_okay():
    assert True


def test_mass_12_requires_2_fuel_when_fuel_weight_is_ignore():
    assert simple_fuel_required(12) == 2


def test_mass_2_requires_0_fuel_when_fuel_weight_is_ignore():
    assert simple_fuel_required(2) == 0


def test_mass_1969_requires_966_fuel_when_the_mass_of_fuel_is_considered():
    assert fuel_required(1969) == 966


def test_solution_to_part_one():
    assert solve_part_one() == 3362507


def test_solution_to_part_two():
    assert solve_part_two() == 5040874
