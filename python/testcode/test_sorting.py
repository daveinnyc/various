'''
Simple tests for sorting.py 

Uses traditional test to verify error messages
Use property based tests to verify generator and sort functions

Author: Dave Cuthbert
Copyright: 2017
License: MIT
'''

import pytest
import sorting as s


# TESTS FOR GENERATE_LISTS()
def test_list_length_too_small_error_handling():
    ''' Test error handling in generate_lists()'''
    error_message_check = s.generate_list(0)
    assert error_message_check == "Error: size must be at least 1"


def test_min_value_greater_than_max_value_error_handling():
    ''' Test error handling in generate_lists()'''
    error_message_check = s.generate_list(10, min_value=50, max_value=5)
    assert error_message_check ==  "Error: min_value must be <= max_value"


def test_size_is_integer_error_handling():
    ''' Test error handling in generate_lists()'''
    error_message_check = s.generate_list(10.0)
    assert error_message_check == "Error: size must be an integer"


def test_min_value_is_integer_error_handling():
    ''' Test error handling in generate_lists()'''
    error_message_check = s.generate_list(5, min_value=1.0)
    assert error_message_check == "Error: min_value must be an integer"


def test_max_value_is_integer_error_handling():
    ''' Test error handling in generate_lists()'''
    error_message_check = s.generate_list(20, max_value=25.0)
    assert error_message_check == "Error: max_value must be an integer"


def test_list_length():
    ''' Test generate_lists creates list of proper length '''
    l = s.generate_list(3)
    assert len(l) == 3

    
def test_min_max_parameters():
    ''' Verify that generat_lists produces random nums within bounds'''
    list_length = 1000
    min_bound = 5
    max_bound = 20
    l = s.generate_list(list_length, min_bound, max_bound)
    for i in l:
        assert i >= min_bound
        assert i <= max_bound


# TESTS FOR BUBBLESORT()
def test_sort_order_length():
    unsorted_list = s.generate_list(200, min_value=0, max_value=500)
    sorted_list = s.bubblesort(unsorted_list)
    assert len(unsorted_list) == len(sorted_list)


def test_sort_order_limits():
    min_bound = 0
    max_bound = 999
    unsorted_list = s.generate_list(200, min_value=min_bound, max_value=max_bound)
    sorted_list = s.bubblesort(unsorted_list)
    assert sorted_list[0] >= min_bound
    assert sorted_list[-1] <= max_bound


def test_sort_order_ordering():
    unsorted_list = s.generate_list(200, min_value=0, max_value=500)
    sorted_list = s.bubblesort(unsorted_list)
    i = 0
    while i < (len(sorted_list) - 1):
        assert sorted_list[i] <= sorted_list[i+1]
        i += 1



if __name__ == '__main__':
   test_sort_order_ordering()


#EOF
