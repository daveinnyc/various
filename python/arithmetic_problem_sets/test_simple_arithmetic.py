''' Test file for simple_arithmetic.py
    
    Author: Dave Cuthbert
    Copyright: 2016
    License: MIT
''' 

import pytest
import simple_arithmetic as sa

def test_num_range():   
    num_list = sa.num_range(10)
    for n in range(0,11):
        assert n in num_list
       
    num_list = sa.num_range(20)
    for n in range(0,21):
        assert n in num_list
 

def test_addition():
    problem_set = sa.addition(5)
    
    expected_problem_set = [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)]
    for e in expected_problem_set:
        assert e in problem_set
    assert 11 == len(problem_set)

        
def test_subtraction():
    problem_set = sa.subtraction(5)
    
    expected_problem_set = [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5),
                            (6,5),(7,5),(8,5),(9,5),(10,5)]
    for e in expected_problem_set:
        assert e in problem_set
    assert 11 == len(problem_set)    
         
pytest.main()