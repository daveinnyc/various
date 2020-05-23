import pytest
import parse_vcf as pv



def test_get_file():
    # There is a list of files to parse in the main script
    #   test to make sure a file is opened and returns a list
    assert str(type(pv.get_file(pv.VCF_FILES[0]))) == "<class 'list'>"


def test_parse_raw():
    test_list = ['BEGIN:VCARD', 'junk', 'END:VCARD']
    (good, bad) = pv.parse_raw(test_list)
    
    assert len(good) == 0
    assert len(bad) == 1


def parse_raw(list_of_lines):
    records = []
    new_record = False
    this_record = []
    unparsed_records = []
    
    for line in list_of_lines:
        if line.startswith('BEGIN:VCARD', 0):
            new_record = True
        if line.startswith('END:VCARD', 0):
            new_record = False