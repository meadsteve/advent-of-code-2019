from advent.day01 import fuel_required, total_fuel, solve_part_one


def test_all_is_okay():
    assert True


def test_mass_12_requires_2_fuel():
    assert fuel_required(12) == 2


def test_total_fuel_can_be_summed():
    assert total_fuel([12, 14]) == 4


def test_solution_to_part_one():
    assert solve_part_one() == 3362507
