import arrays

# Reverse an array in place
def test_reverse_array_zero_length():
    input = []

    assert arrays.reverse_array(input) == []


def test_reverse_array():
    input = [1, 2, 3]

    assert arrays.reverse_array(input) == [3, 2, 1]


def test_reverse_array_same_values():
    input = [1, 2, 2, 3]

    assert arrays.reverse_array(input) == [3, 2, 2, 1]

