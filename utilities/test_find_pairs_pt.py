# Test code for find_pairs_pt.py

import pytest
import find_pairs_pt as fp


def test_no_pairs():
    test_array = [9]
    response = []
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response


def test_one_pair():
    test_array = [1,9]
    response = [(1,9)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response
    
    # Same thing, order reversed 
    test_array = [9,1]
    response = [(9,1)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response
    
    
def test_values_to_skip():
    test_array = [9,1,6]
    response = [(9,1)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response


def test_use_both_end_values():
    test_array = [9,6,1]
    response = [(9,1)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response

  
'''
    >>> find_pairs_simple([9,6,1,4,7])
    9,1
    6,4
    >>> find_pairs_simple([5])
    
    >>> find_pairs_simple([5,5])
    5,5
    >>> find_pairs_simple([1,3,7,5,9])
    1,9
    3,7
    >>> find_pairs_simple([1,3,7,5,9], 14)
    5,9
    >>> find_pairs_simple([13,-3,7,5,9])
    13,-3
'''    