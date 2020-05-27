# Open a .vcf file and save relevant field in a .csv format

# TODO: Add the remaining parsers
# TODO: Add a function to print to file 


VCF_FILES = ['001.vcfmod', '002.vcfmod']


def get_file(file):
    with open(file) as f:
        raw_file = f.readlines()

    return(raw_file)
    

def get_fresh_record():
    return {'fname':'', 'lname':'', 'tel':'', 'email':[], 'item1':'', 
            'item2':'', 'item3':'', 'org':'', 'bday':'', 
            'rev':''}
    
       
def parse_n(line):
    # Lines look like this: 
    # N:LName;FName;;;    
    line_wo_prefix = line[2:]
    lname, fname, *other_elements = line_wo_prefix.split(';')
    return [fname, lname]
    

def parse_rev(line):
    # Lines look like this: 
    # REV:2014-07-07T02:21:17Z
    date = line[4:14]
    return date  


def parse_org(line):
    # Lines look like this: 
    # ORG:Aaaa;
    # ORG:aaa - bbb;
    # ORG:Aaa Bbb;
    # ORG:Aaa \ Bbb;
    # ORG:Aaa\, Bbb;
    # ORG:Aaa;Bbb
    # ORG:Aaa,Bbb
    # ORG:Aaa;Bbb;
    # ORG:Aaa (BB & Ccc Ddd);
    line_wo_prefix = line[4:]
    cleaned_line = ' '.join(line_wo_prefix.split(';'))
    cleaned_line = cleaned_line.strip()
    cleaned_line = cleaned_line.replace(r'\,', ' ')
    cleaned_line = cleaned_line.replace(',', ' ')
    return cleaned_line

    
def parse_bday(line):
    # Lines look like this: 
    # BDAY;value=date:1972-03-26
    date = line[16:26]
    return date  


def parse_email(line):
    # Lines look like this: 
    # EMAIL;type=INTERNET;type=WORK;type=pref:usr.name@domain.tld
    *junk, email = line.split(':')
    return email


def parse_item(line):
    # Multiple formats; many are broken probably by , \n etc. in original
    # Lines of interest look like this: 
    # item1.EMAIL;type=INTERNET;type=pref:julia.dadiomov@venafi.com
    # item1.ADR;type=HOME;type=pref:;;Am Heistersiek 12;Spenge;Nordrhein-Westfale
    # item1.ADR;type=WORK;type=pref:;;530 Lytton Ave\, 2nd Floor\nSuite 202\n\n;Palo Alto;CA;94301;United States
    # item1.TEL;type=pref:+441277202041
    # item1.X-ABLabel:England home
    # X-ABLabel sometimes follows TEL tag
    target_value = ''
    
    if 'EMAIL' in line:
        *junk, target_value = line.split(':')
    elif 'ADR' in line:
        *junk, target_value = line.split('type=pref')
        target_value = target_value[3:]
        target_value = target_value.replace(';', ' ')
        target_value = target_value.replace(r'\,', ' ')
        target_value = target_value.replace(r'\n', ' ')
    elif 'TEL' in line:
        *junk, target_value = line.split('type=pref:')        
    else:
        pass

    return target_value
        

def parse_item_xlabel(line):
    # Lines look like this:
    # item1.X-ABLabel:England home
    target_value = ''
    
    *junk, target_value = line.split(':')       
    return target_value


def parse_tel(line):    
    # Lines look like this:
    # TEL;type=CELL;type=VOICE;type=pref:CharacterString
    # TEL;type=HOME;type=VOICE:1234567891011
    # TEL;type=CELL;type=VOICE;type=pref:(123) 456-9876
    # TEL;type=CELL;type=VOICE;type=pref:1-555-321-8765
    phone_number = ''
    phone_type = ''
    
    if any(char.isdigit() for char in line):
        *phone_type, phone_number = line.split(':')       
        if phone_number:
            phone_number = phone_number.replace('(', '')
            phone_number = phone_number.replace(')', ' ')
            phone_number = phone_number.replace('-', ' ')
            phone_number = phone_number.replace('  ', ' ')
        phone_type = str(phone_type)    
        if 'HOME' in phone_type:
            phone_type = 'home'
        elif 'WORK' in phone_type:
            # Some phones are WORK and CELL, record as WORK
            phone_type = 'work'
        elif 'CELL' in phone_type:
            phone_type = 'cell'
        elif 'OTHER' in phone_type:
            phone_type = ''
        elif 'MAIN' in phone_type:
            phone_type = ''            
        else:
            pass
    return (phone_number, phone_type)    


def parse_raw(list_of_lines):
    records = []
    new_record = False
    # NOTE: Individual record elements are gathered in a dictionary so the 
    #       order of fields will be correct later when serialized for output
    unparsed_records = []
    
    for line in list_of_lines:
        line = line.strip()
        if line.startswith('BEGIN:VCARD', 0):
            new_record = True
            this_record = get_fresh_record()
            emails = []
            items1 = []
            items2 = []
            items3 = []
            item1_telephone_flag = False
            item2_telephone_flag = False
            item3_telephone_flag = False
        if line.startswith('END:VCARD', 0):
            new_record = False
            records.append(this_record)
        
        if new_record:
            if line.startswith('N:', 0):
                (first, last) = parse_n(line)
                this_record['fname'] = first
                this_record['lname'] = last
            elif line.startswith('TEL', 0):
                this_record['tel'] = parse_tel(line)
            elif line.startswith('EMAIL', 0):              
                this_record['email'].append(parse_email(line))
            elif line.startswith('item1', 0):
                if 'TEL' in line:
                    item1_telephone_flag = True
                    items1.append(parse_item(line))
                elif 'EMAIL' in line:
                    items1.append(parse_item(line))   
                elif 'ADR' in line:
                    items1.append(parse_item(line))   
                elif 'X-ABLabel' in line and item1_telephone_flag == True:
                    items1.append(parse_item_xlabel(line))
                    item1_telephone_flag = False
                else:
                    pass
                this_record['item1'] = items1
            elif line.startswith('item2', 0):
                if 'TEL' in line:
                    item2_telephone_flag = True
                    items2.append(parse_item(line))
                elif 'EMAIL' in line:
                    items2.append(parse_item(line))   
                elif 'ADR' in line:
                    items2.append(parse_item(line))   
                elif 'X-ABLabel' in line and item2_telephone_flag == True:
                    items2.append(parse_item_xlabel(line))
                    telephone_flag = False
                else:
                    pass
                this_record['item2'] = items2
            elif line.startswith('item3', 0):
                if 'TEL' in line:
                    item3_telephone_flag = True                    
                    items3.append(parse_item(line))
                if 'EMAIL' in line:
                    items3.append(parse_item(line))   
                if 'X-ABLabel' in line and item3_telephone_flag == True:
                    items3.append(parse_item_xlabel(line))
                    telephone_flag = False
                this_record['item3'] = items3   
            elif line.startswith('ORG', 0):
                this_record['org'] = parse_org(line)
            elif line.startswith('BDAY', 0):
                this_record['bday'] = parse_bday(line)
            elif line.startswith('REV', 0):
                this_record['rev'] = parse_rev(line)                            
            elif line.startswith('FN:', 0):
                # Ignore this field, get names from N lines
                pass              
            elif line.startswith('NOTE:', 0):
                # Ignore this field
                pass
            elif line.startswith('X-SOCIALPROFILE', 0): 
                # Ignore this field
                pass
            elif line.startswith('TITLE', 0): 
                # Ignore this field
                pass
            elif line.startswith('IMPP', 0): 
                # Ignore this field
                pass
            elif line.startswith('VERSION', 0): 
                # Ignore this field
                pass
            elif line.startswith('PRODID', 0): 
                # Ignore this field
                pass           
            elif line.startswith('BEGIN', 0):
                # Ignore the new record toggle once flipped
                pass    
            else:
                unparsed_records.append(line)           
        
    return (records, unparsed_records)


def print_csv_record(record):
    emails = ' '.join(record['email'])
    items1 = ' '.join(record['item1'])
    items2 = ' '.join(record['item2'])
    items3 = ' '.join(record['item3'])
    telephone = ','.join(record['tel'])
    output_fields = [record['fname'],  
                     record['lname'], 
                     emails, 
                     telephone,
                     items1, 
                     items2, 
                     items3, 
                     record['org'],
                     record['bday'],
                     record['rev']]
    
    record =  ','.join(output_fields)    
    record += '\n'
    return record
    
    
def main():
    output = []
    unparsed_output = []
    
    for vcf_file in VCF_FILES:
            records = parse_raw(get_file(vcf_file))
            output.extend(records[0])
            unparsed_output.extend(records[1])
    
    return (output, unparsed_output)
    
    
if __name__ == "__main__":
    '''
    # Used to discover fields and line formats
    (good, bad) = main()
    for b in bad:
        print(f"UNPARSED: {b}")
            
    print(f"GOOD: {len(good)}  BAD: {len(bad)}")
    '''
    with open('converted_vcf.csv', 'w') as outfile:
        for vcf_file in VCF_FILES:
            records = parse_raw(get_file(vcf_file))
            for record in records[0]:
                outfile.write(print_csv_record(record))
