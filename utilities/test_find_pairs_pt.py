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


def test_avoid_repeated_single_value():
    test_array = [5]
    response = []
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response


def test_repeated_values():
    test_array = [5,5]
    response = [(5,5)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response


def test_multiple_pairs():
    test_array = [9,6,1,4,7]
    response = [(9,1), (6,4)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response


def test_multiple_pairs_repeated_value():
    test_array = [9,6,1,4,7,1]
    response = [(9,1), (9,1), (6,4)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response


def test_alternate_target():
    test_array = [1,3,7,5,9]
    target_value = 14
    response = [(5,9)]
    assert fp.find_pairs_simple(test_array, target_value) == response
    assert fp.find_pairs(test_array, target_value) == response
 
 
def test_negative_values():
    test_array = [13,-3,7,5,9]
    response = [(13,-3)]
    assert fp.find_pairs_simple(test_array) == response
    assert fp.find_pairs(test_array) == response 
