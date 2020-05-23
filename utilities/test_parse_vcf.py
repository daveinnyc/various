import pytest
import parse_vcf as pv



def test_get_file():
    # There is a list of files to parse in the main script
    #   test to make sure a file is opened and returns a list
    assert str(type(pv.get_file(pv.VCF_FILES[0]))) == "<class 'list'>"


def test_parse_raw():
    # Don't check any of the sub parses, just that there is parsing 
    #   and that junk gets caught

    test_list = ['BEGIN:VCARD', 'junk', 'END:VCARD']
    (good, bad) = pv.parse_raw(test_list)
    assert len(good) == 0
    assert len(bad) == 1


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
    '''
                  ['BEGIN:VCARD', 'N:LName WSpace;FName WSpace;;;', 'END:VCARD'],
                  ['BEGIN:VCARD', 'N:Lname;;;;', 'END:VCARD'],
                  ['BEGIN:VCARD', 'N:;FName;;;', 'END:VCARD'],
                  ['BEGIN:VCARD', 'N:;;;;', 'END:VCARD'],
                  ['BEGIN:VCARD', 'N:;Too;ManyFields;;;;;;', 'END:VCARD']]
    '''              
    results = pv.parse_n(test_line)
    assert results[0] == 'FName WSpace'
    assert results[1] == 'LName'


#########################
def parse_n(line):
    # Lines look like this: 
    #  N:LName;FName;;; 
    
    lname, fname, *other_elements = line[2:].split(';')
    return [fname, lname]


