import pytest
import string
import encryption_decryption as ed

def test_create_secret_key():
    sk = ed.create_secret_key()
    
    assert 53 == len(sk)
    assert ' ' == sk[52]
    for l in string.letters:
        assert l in sk
 


def test_create_letter_iteration():
    cypher_key = ['q','w','e','r','t','y','u','i',
                  'o','p','a','s','d','f','g','h',
                  'j','k','l','z','x','c','v','b',
                  'n','m','Q','W','E','R','T','Y',
                  'U','I','O','P','A','S','D','F',
                  'G','H','J','K','L','Z','X','C',
                  'V','B','N','M',' ']
    li = ed.create_letter_iteration(cypher_key)

    assert ('a','q') == li[0]
    assert ('f','y') == li[5]
    assert ('k','a') == li[10]
    assert (' ',' ') == li[52]


def test_encrypt():
    cypher_key = ['q','w','e','r','t','y','u','i',
                  'o','p','a','s','d','f','g','h',
                  'j','k','l','z','x','c','v','b',
                  'n','m','Q','W','E','R','T','Y',
                  'U','I','O','P','A','S','D','F',
                  'G','H','J','K','L','Z','X','C',
                  'V','B','N','M',' ']
    plain_text = "Abcd efg"
    encrypted_text = ed.encrypt(plain_text, cypher_key)

    assert "Qwer tyu" == encrypted_text
    

def test_decrypt():
    cypher_key = ['q','w','e','r','t','y','u','i',
                  'o','p','a','s','d','f','g','h',
                  'j','k','l','z','x','c','v','b',
                  'n','m','Q','W','E','R','T','Y',
                  'U','I','O','P','A','S','D','F',
                  'G','H','J','K','L','Z','X','C',
                  'V','B','N','M',' ']
    cypher_text = "Qwer tyu"
    plain_text = ed.decrypt(cypher_text, cypher_key)

    assert "Abcd efg" == plain_text
    
pytest.main()
#EOF