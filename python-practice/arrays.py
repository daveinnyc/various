def reverse_array(input_array):
    left = 0
    right = len(input_array) - 1   # Array is 0 indexed
    tmp_array = input_array

    while right > left:
        tmp_array[left], tmp_array[right] = tmp_array[right], tmp_array[left]
        left += 1
        right -= 1

    return tmp_array


def binary_search(input_array, target):
    # Assumes an incrementally  sorted array

    array_length = len(input_array)
    # Basic checks
    if array_length == 0:             # Empty array
        return -1
    if array_length == 1:             # Singleton array
        if input_array[0] == target:
            return 0
        return -1
    if target > input_array[-1]:     # Too big
        return -1
    if target < input_array[0]:      # Too small
        return -1


    lo = 0
    hi = array_length - 1
    guess = -1

    while lo <= hi:
        guess = lo + int((hi - lo) / 2)

        if input_array[guess] == target:
            return guess
        if input_array[guess] < target:
            lo = guess + 1
        else:
            hi = guess - 1

    return guess


if __name__ == "__main__":
    print("Consider running tests instead")

    input = [1, 4, 8, 10]
    print(binary_search(input, 4))
