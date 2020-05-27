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




############################
###  get_fresh_record()  ###
############################
def test_get_fresh_record():
    new_record = pv.get_fresh_record()
    assert new_record == {'fname':'', 'lname':'', 'tel':'', 'email':'', 'item1':'', 
            'item2':'', 'item3':'', 'org':'', 'bday':'', 
            'rev':''}
            
            
#####################
###  parse_raw()  ###
#####################
def test_parse_raw():
    # Don't check any of the sub parses, just that there is parsing 
    #   and that junk gets caught

    test_list = ['BEGIN:VCARD', 'junk', 'END:VCARD']
    (good, bad) = pv.parse_raw(test_list)
    # There is always at least one empty, good record
    assert len(good) == 1
    assert len(bad) == 1


def test_parse_raw_case_statement():
    list_of_lines = ['BEGIN:VCARD',
                     'N:LName;FName;;;'
                     'TEL;type=CELL;type=VOICE;type=pref:(123) 456-9876',
                     'EMAIL;type=INTERNET;type=WORK;type=pref:usr.name@domain.tld',
                     'item1.EMAIL;type=INTERNET;type=pref:julia.dadiomov@venafi.com',
                     'item2.ADR;type=HOME;type=pref:;;Am Heistersiek 12;Spenge;Nordrhein-Westfale',
                     'item3.TEL;type=pref:+441277202041',
                     'item3.X-ABLabel:England home',                  
                     'ORG:Aaaa;\n',
                     'BDAY;value=date:1972-03-26\n',
                     'REV:2014-07-07T02:21:17Z',
                     'FN: and more stuff',
                     'NOTE: and more stuff',
                     'X-SOCIALPROFILE and more stuff',
                     'VERSION and more stuff',
                     'PRODID and more stuff',
                     'Some unknown string',
                     'END:VCARD']
    records, unparsed_records = pv.parse_raw(list_of_lines)
    print(f"R: {records},  UP: {unparsed_records}")
    assert False
    
    
def test_parse_raw_xable_precondition():
    # There X-ABLabel call needs a setup toggle
    list_of_lines = ['BEGIN:VCARD',
                     'item3.TEL;type=pref:+441277202041',
                     'item3.X-ABLabel:England home',                  
                     'END:VCARD']
    records, unparsed_records = pv.parse_raw(list_of_lines)
    assert records[0]['item3'] == ['+441277202041', 'England home']
    

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
# Lots of variation in the fields, only some chars stripped out
def test_parse_org():
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

    test_line = r'ORG:Aaa\, Bbb;'
    assert pv.parse_org(test_line) == 'Aaa  Bbb'

    test_line = 'ORG:Aaa;Bbb' 
    assert pv.parse_org(test_line) == 'Aaa Bbb'
    
    test_line = 'ORG:Aaa, Bbb' 
    assert pv.parse_org(test_line) == 'Aaa  Bbb'

    test_line = 'ORG:Aaa (BB & Ccc Ddd);' 
    assert pv.parse_org(test_line) == 'Aaa (BB & Ccc Ddd)'


#####################
###  parse_bday()  ###
#####################
def test_parse_bday():
    test_line = 'BDAY;value=date:1972-03-26\n' 
    assert pv.parse_bday(test_line) == '1972-03-26'


#######################
###  parse_email()  ###
#######################
def test_parse_email():
    test_line = 'EMAIL;type=INTERNET;type=WORK;type=pref:usr.name@domain.tld' 
    assert pv.parse_email(test_line) == 'usr.name@domain.tld'


######################
###  parse_item()  ###
######################
def test_parse_item1_email():
        test_line = 'item1.EMAIL;type=INTERNET;type=pref:julia.dadiomov@venafi.com'
        assert pv.parse_item(test_line) == 'julia.dadiomov@venafi.com'


def test_parse_item1_address():
        test_line = 'item1.ADR;type=HOME;type=pref:;;Am Heistersiek 12;Spenge;Nordrhein-Westfale'
        assert pv.parse_item(test_line) == 'Am Heistersiek 12 Spenge Nordrhein-Westfale'

        test_line = r'item1.ADR;type=WORK;type=pref:;;530 Lytton Ave\, 2nd Floor\nSuite 202\n\n;Palo Alto;CA;94301;United States'
        assert pv.parse_item(test_line) == '530 Lytton Ave  2nd Floor Suite 202   Palo Alto CA 94301 United States'


def test_parse_item1_telephone_tel():
        test_line = 'item1.TEL;type=pref:+441277202041'
        assert pv.parse_item(test_line)== '+441277202041'


def test_parse_item1_telephone_ablabel():
        test_line = 'item1.X-ABLabel:England home'
        assert pv.parse_item_xlabel(test_line)== 'England home'


#####################
###  parse_tel()  ###
#####################
def test_parse_tel_char_string():    
    test_line = 'TEL;type=CELL;type=VOICE;type=pref:CharacterString'
    (phone_number, phone_type) = pv.parse_tel(test_line)
    assert phone_number == ''
    assert phone_type == ''
    
    
def test_parse_tel_home_type():    
    test_line = 'TEL;type=HOME;type=VOICE:1234567891011'
    (phone_number, phone_type) = pv.parse_tel(test_line)
    assert phone_number == '1234567891011'
    assert phone_type == 'home'    
        
    
def test_parse_tel_remove_parens():    
    test_line = 'TEL;type=CELL;type=VOICE;type=pref:(123) 456-9876'
    phone_number, phone_type = pv.parse_tel(test_line)
    assert phone_number == '123 456 9876'
    assert phone_type == 'cell'    
    
    
def test_parse_tel_remove_dashes():    
    test_line = 'TEL;type=CELL;type=VOICE;type=pref:1-555-321-8765'
    phone_number, phone_type = pv.parse_tel(test_line)
    assert phone_number == '1 555 321 8765'
    assert phone_type == 'cell'        

    
def test_parse_tel_cell_and_work_types():    
    test_line = 'TEL;type=CELL;type=WORK;type=pref:1-555-321-8765'
    phone_number, phone_type = pv.parse_tel(test_line)
    assert phone_number == '1 555 321 8765'
    assert phone_type == 'work'            