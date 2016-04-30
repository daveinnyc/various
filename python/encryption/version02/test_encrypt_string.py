import pytest
import encrypt_string as es
from encrypt_string import create_secret_key

def test_create_secret_key():
    '''Key should be random, but has certain characteristics 
       that can be checked
    ''' 
    sk = create_secret_key()
    
    assert len(sk) == 52
    assert 'a' in sk
    assert 'd' in sk
    assert 'F' in sk
    assert 'S' in sk
    assert '3' not in sk


def test_create_letter_iteration(): 
    letter_list = ['a','s','d','f','g','h','j','k','l']
    li = es.create_letter_iteration(letter_list)
      
    assert letter_list[0] == li[0][0]
    assert letter_list[3] == li[3][0]
    assert letter_list[8] == li[8][0]
    assert ' ' == li[52][0]


def test_numeric_encode():
    #Check for letters and spaces
    plain_text = "abcd ABcd efg"
    encoded_text = es.numeric_encode(plain_text)
    
    assert 0 == encoded_text[0]
    assert 1 == encoded_text[1]
    assert 52 == encoded_text[4]
    assert 26 == encoded_text[5]
    assert 4 == encoded_text[10]

    #Check for punctuation replacement
    plain_text = "abcd,abcd.efg"
    encoded_text = es.numeric_encode(plain_text)
    
    assert 0 == encoded_text[0]
    assert 52 == encoded_text[4]
    assert 52 == encoded_text[9]  
    

def test_create_single_cypher_key():
    sck = es.create_single_cypher_key()
    
    assert 'a' == sck[0][1]
    assert 'A' == sck[26][1]
    assert 'b' == sck[1][1]
    assert sck[52][0] == sck[52][1]  #52 == ' ' 


def test_get_num_from_cypher_key():
    ck = {0:['A','a'], 1:['B','b'], 2:['C','c'], 
          3:['D','d'], 4:['E','e'], 5:['F','f'], 
          52:[' ',' ']}
     
    num_list = es.get_num_from_cypher_key(ck)
    
    assert 'A' == num_list[0]
    assert 'E' == num_list[4]
    assert ' ' == num_list[52]
    
    
def test_encrypt():
    pt = "ab cde f"
    ck = {0:['A','a'], 1:['B','b'], 2:['C','c'], 
          3:['D','d'], 4:['E','e'], 5:['F','f'], 
          52:[' ',' ']}
    
    encyphered = es.encrypt(pt, ck)
    assert 'A' == encyphered[0]
    assert ' ' == encyphered[2]
    assert 'D' == encyphered[4]
    assert ' ' == encyphered[6]


def test_decrypt(): 
    et = "AB CDE F"
    ck = {0:['A','a'], 1:['B','b'], 2:['C','c'], 
          3:['D','d'], 4:['E','e'], 5:['F','f'], 
          52:[' ',' ']}
    
    plain_text = es.decrypt(et, ck)
    assert 'a' == plain_text[0]
    assert ' ' == plain_text[2]
    assert 'd' == plain_text[4]
    assert ' ' == plain_text[6]

    
pytest.main()
#EOF