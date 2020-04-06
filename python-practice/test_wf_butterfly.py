import pytest
import wf_butterfly as target

def test_butterfly():
    # Sample test strings from site
    assert target.butterfly("Wolfram") == "WolframmarfloW"
    assert target.butterfly("butterfly") == "butterflyylfrettub"
    assert target.butterfly("race") == "raceecar"
    assert target.butterfly("Hello world!") == "Hello world!!dlrow olleH"
    
    
def test_butterfly_properties():
    test_strs = ['abc', 'a b c', '2 3 44 3 2', '$$ 1 2 3 %%', '']
    for test_str in test_strs:
        # Length should be double input
        doubled_str = target.butterfly(test_str)
        assert len(doubled_str) == 2 * len(test_str)
    
        # Check inverse positions
        halfway = len(test_str)
        for index, value in enumerate(doubled_str):
            if index < halfway:
                assert doubled_str[index] == doubled_str[ (index + 1) * -1 ]             