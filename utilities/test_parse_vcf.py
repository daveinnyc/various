import pytest
import parse_vcf as pv



def test_get_file():
    # There is a list of files to parse in the main script
    #   test to make sure a file is opened and returns a list
    assert str(type(pv.get_file(pv.VCF_FILES[0]))) == "<class 'list'>"
