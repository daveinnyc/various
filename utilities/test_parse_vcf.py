import pytest
import parse_vcf as pv



####################
###  get_file()  ###
####################
def test_get_file():
    # There is a list of files to parse in the main script
    #   test to make sure a file is opened and returns a list
    # Doesn't test any error handling, there isn't any
    assert str(type(pv.get_file(pv.VCF_FILES[0]))) == "<class 'list'>"


#####################
###  parse_raw()  ###
#####################
def test_parse_raw():
    # Don't check any of the sub parses, just that there is parsing 
    #   and that junk gets caught

    test_list = ['BEGIN:VCARD', 'junk', 'END:VCARD']
    (good, bad) = pv.parse_raw(test_list)
    assert len(good) == 0
    assert len(bad) == 1


###################
###  parse_n()  ###
###################
def test_parse_n():
    test_line = 'N:LName;FName;;;'
    results = pv.parse_n(test_line)
    assert results[0] == 'FName'
    assert results[1] == 'LName'
        

def test_parse_n_lname_with_space():
    test_line = 'N:LName WSpace;FName;;;'
    results = pv.parse_n(test_line)
    assert results[0] == 'FName'
    assert results[1] == 'LName WSpace'

                                    
def test_parse_n_fname_with_space():
    test_line = 'N:LName;FName WSpace;;;'
    results = pv.parse_n(test_line)
    assert results[0] == 'FName WSpace'
    assert results[1] == 'LName'

    
def test_parse_n_both_with_spaces():
    test_line = 'N:LName WSpace;FName WSpace;;;'
    results = pv.parse_n(test_line)
    assert results[0] == 'FName WSpace'
    assert results[1] == 'LName WSpace'    


def test_parse_n_no_fname():
    test_line = 'N:LName;;;;'
    results = pv.parse_n(test_line)
    assert results[0] == ''
    assert results[1] == 'LName'    


def test_parse_n_no_lname():
    test_line = 'N:;FName;;;'
    results = pv.parse_n(test_line)
    assert results[0] == 'FName'
    assert results[1] == ''    


def test_parse_n_no_names():
    test_line = 'N:;;;;'
    results = pv.parse_n(test_line)
    assert results[0] == ''
    assert results[1] == ''    


def test_parse_n_too_many_fields():
    test_line = 'N:ManyFields;Too;;;;;;;'
    results = pv.parse_n(test_line)
    assert results[0] == 'Too'
    assert results[1] == 'ManyFields'    


#####################
###  parse_rev()  ###
#####################
def test_parse_rev():
    test_line = 'REV:2014-07-07T02:21:17Z'
    assert pv.parse_rev(test_line) == '2014-07-07'


#####################
###  parse_org()  ###
#####################
def test_parse_org():
    # Lots of variation in the fields, only some stripped out
    test_line = 'ORG:Aaaa;\n' 
    assert pv.parse_org(test_line) == 'Aaaa'

    test_line = 'ORG:Aaaa;' 
    assert pv.parse_org(test_line) == 'Aaaa'

    test_line = 'ORG:aaa - bbb;' 
    assert pv.parse_org(test_line) == 'aaa - bbb'

    test_line = 'ORG:Aaa Bbb;' 
    assert pv.parse_org(test_line) == 'Aaa Bbb'

    test_line = r'ORG:Aaa\ Bbb;'
    assert pv.parse_org(test_line) == r'Aaa\ Bbb'

    test_line = r'ORG:Aaa\\, Bbb;'
    assert pv.parse_org(test_line) == 'Aaa  Bbb'

    test_line = 'ORG:Aaa;Bbb' 
    assert pv.parse_org(test_line) == 'Aaa Bbb'
    
    test_line = 'ORG:Aaa, Bbb' 
    assert pv.parse_org(test_line) == 'Aaa  Bbb'

    test_line = 'ORG:Aaa (BB & Ccc Ddd);' 
    assert pv.parse_org(test_line) == 'Aaa (BB & Ccc Ddd)'



#########################
