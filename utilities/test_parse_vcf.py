import pytest
import parse_vcf as pv



def test_openfile():
    # There is a list of files to parse in the main script
    #   test to make sure a file is opened and returns a list
    assert str(type(pv.openfile(pv.VCF_FILES[0]))) == "<class 'list'>"
