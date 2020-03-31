# Test code for find_pairs_pt.py

import pytest
import find_pairs_pt as fp

def test_one_pair():
    assert fp.find_pairs_simple([1,9]) == [(1,9)]
    assert fp.find_pairs([1,9]) == [(1,9)]

'''
>>> find_pairs_simple([9])
    
    >>> find_pairs_simple([1,9])
    1,9
    >>> find_pairs_simple([9,1])
    9,1
    >>> find_pairs_simple([9,1,6])
    9,1
    >>> find_pairs_simple([9,6,1])
    9,1
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