import pytest
import generators_example as ge

def test_lottery_types():
    # function w/o parens, should be a generator with them
    # x.__name__ returns a string for the type
    assert type(ge.lottery).__name__ == "function"
    assert type(ge.lottery()).__name__ == "generator"
    

def test_lottery_values():
    # Putting all the asserts in 1 test to avoid regenerating the array 
    #    multiple times
    
    NUM_OF_NUMS = 7
    MIN_VAL = 0
    MAX_VAL_NORMAL = 40
    MAX_VAL_BONUS = 15
    numbers = []
    for n in ge.lottery():
        numbers.append(n)
    
    # Check length of returned set
    assert len(numbers) == NUM_OF_NUMS
      
    # Check size of last value
    assert type(numbers[-1]).__name__ == "int"
    assert numbers[-1] > MIN_VAL 
    assert numbers[-1] <= MAX_VAL_BONUS

    # Check size of other values
    for i in range(NUM_OF_NUMS - 1):
        assert type(numbers[i]).__name__ == "int"
        assert numbers[i] > MIN_VAL 
        assert numbers[i] <= MAX_VAL_NORMAL


def test_fib():
    fibs = list()
    gen = ge.fib()
    for i in range(11):
        fibs.append(next(gen))

    for index, first in enumerate(fibs):
        if index < (len(fibs) - 2):
            second = fibs[index + 1]
            third = fibs[index + 2]
            assert third == first + second