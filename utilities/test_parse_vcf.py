import pytest
import parse_vcf as pv



def test_openfile():
    assert pv.openfile('test_parse_vcf.py')[0] == True
