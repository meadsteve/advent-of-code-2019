from advent.common import lines_from_file
from advent.day03.models import Point
from advent.day03.movement import from_strings
from advent.day03.wire_logic import crosses


def part_one():
    wires = lines_from_file("advent/day03/input.txt")
    [a, b] = [from_strings(wire.split(",")) for wire in wires]
    intersections = crosses(a, b)
    intersections.remove(Point(0, 0))
    with_distances = [(point, point.distance_from_o) for point in intersections]
    sorted_points = sorted(with_distances, key=lambda x: x[1])
    nearest_intersection = sorted_points[0][1]
    return nearest_intersection
