import pytest
import parse_vcf as pv



def test_openfile():
    # The real input file is called: 001.vcfmod 
    assert pv.openfile('001.vcfmod')[0] == True
