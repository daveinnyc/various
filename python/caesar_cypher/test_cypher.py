import pytest
import cypher as cy

def test_get_key():
    #It's a random value, so test expected 
    #  parameters a bunch of times   
    for i in range(50):
        cypher = cy.get_key()
        assert cypher > 0
        assert cypher < 26

        
def test_get_index():
    assert 0 == cy.get_index('a')
    assert 12 == cy.get_index('m')
    assert 27 == cy.get_index('B')
    assert 51 == cy.get_index('Z')

    
def test_rotate():
    #for triple in [('a',3,'d'), ('m',5,'r'), ('C',13,'P'), ('Y',25,'B')]:
    assert 'd' == cy.rotate('a',3)
    assert 'r' == cy.rotate('m',5)
    assert 'P' == cy.rotate('C',13)
    assert 'X' == cy.rotate('Y',25)


def test_encode():
    test_text = "This is a phrase."

    test_key = 1    
    assert "Uijt jt b qisbtf." == cy.encode(test_text, test_key)    
    
    test_key = 2    
    assert "Vjku ku c rjtcug." == cy.encode(test_text, test_key)
          
pytest.main()
#EOF