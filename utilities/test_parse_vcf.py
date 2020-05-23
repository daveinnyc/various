import pytest
import parse_vcf as pv



def test_get_file():
    # There is a list of files to parse in the main script
    #   test to make sure a file is opened and returns a list
    assert str(type(pv.get_file(pv.VCF_FILES[0]))) == "<class 'list'>"


def test_parse_raw():
    test_list = ['BEGIN:VCARD', 'junk', 'END:VCARD']
    (good, bad) = pv.parse_raw(test_list)
    
    # Don't check any of the sub parses, just that there is parsing 
    #   and that junk gets caught
    assert len(good) == 0
    assert len(bad) == 1


