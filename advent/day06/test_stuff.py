from advent.day06 import new_map, add_orbit, OrbitalItem, solve_part_one


def test_adds_an_orbital_relationship():
    orbits = new_map()
    add_orbit(orbits, "COM", "B")

    assert orbits["COM"].orbited_by == [OrbitalItem("B")]


def test_can_chain_add_relationships():
    orbits = new_map()
    add_orbit(orbits, "COM", "B")
    add_orbit(orbits, "B", "C")

    assert orbits["B"].orbited_by == [OrbitalItem("C")]


def test_total_orbiters_can_be_counted():
    orbits = new_map()
    add_orbit(orbits, "COM", "B")
    add_orbit(orbits, "B", "C")

    assert orbits["COM"].total_orbital_count == 2


def test_total_orbiters_can_be_counted_if_defined_backwards():
    orbits = new_map()
    add_orbit(orbits, "B", "C")
    add_orbit(orbits, "COM", "B")

    assert orbits["COM"].total_orbital_count == 2


def test_part_one():
    assert solve_part_one() == 453028
