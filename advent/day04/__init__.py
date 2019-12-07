
def digit_neighbours_exist(number: int) -> bool:
    digits = str(number)
    for i in range(1, len(digits) - 1):
        if digits[i] == digits[i-1] or digits[i] == digits[i+1]:
            return True
    return False


def digit_neighbours_exist_only_as_a_pair(number: int) -> bool:
    digits = str(number)
    for i in range(0, len(digits) - 1):
        has_neighbour = (digits[i] == digits[i + 1])
        ok_forward = (digits[i] != digits[i + 2]) if (i + 2) < len(digits) else True
        ok_backward = (digits[i] != digits[i - 1]) if (i - 1) >= 0 else True
        if has_neighbour and ok_forward and ok_backward:
            return True
    return False


def digits_ascend(number: int) -> bool:
    digits = str(number)
    for i in range(0, len(digits) - 1):
        if digits[i] > digits[i+1]:
            return False
    return True


def part_one():
    input_range = range(109165, 576723 + 1)
    with_neighbours = (x for x in input_range if digit_neighbours_exist(x))
    with_ascending = (x for x in with_neighbours if digits_ascend(x))
    possible_values = list(with_ascending)
    return len(possible_values)


def part_two():
    input_range = range(109165, 576723 + 1)
    with_neighbours = (x for x in input_range if digit_neighbours_exist_only_as_a_pair(x))
    with_ascending = (x for x in with_neighbours if digits_ascend(x))
    possible_values = list(with_ascending)
    return len(possible_values)
