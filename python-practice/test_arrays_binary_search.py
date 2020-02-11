import arrays

# Reverse an array in place
def test_reverse_array():
    input = [1, 2, 3]

    assert arrays.reverse_array(input) == [3, 2, 1]


# Search a sorted list
def test_binary_search_no_list():
    input_array = []
    target = 1

    assert arrays.binary_search(input_array, target) == -1


def test_binary_search_short_list_found():
    input_array = [1]
    target = 1

    assert arrays.binary_search(input_array, target) == 0


def test_binary_search_short_list_not_found():
    input_array = [1]
    target = 10

    assert arrays.binary_search(input_array, target) == -1


def test_binary_search_even_list():
    input_array = [1, 4, 8, 10]
    target = 4

    assert arrays.binary_search(input_array, target) == 1


def test_binary_search_odd_list():
    input_array = [1, 5, 10]
    target = 1

    assert arrays.binary_search(input_array, target) == 0


def test_binary_search_last_in_list():
    input_array = [1, 5, 10]
    target = 10

    assert arrays.binary_search(input_array, target) == 2


def test_binary_search_not_in_list_big():
    input_array = [1, 5, 10]
    target = 100

    assert arrays.binary_search(input_array, target) == -1


def test_binary_search_not_in_list_small():
    input_array = [1, 5, 10]
    target = -100

    assert arrays.binary_search(input_array, target) == -1

