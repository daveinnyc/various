# Open a .vcf file and save relevant field in a .csv format

# TODO: Add the remaining parsers
# TODO: Add a function to print to file 


VCF_FILES = ['001.vcfmod', '002.vcfmod']


def get_file(file):
    with open(file) as f:
        raw_file = f.readlines()

    return(raw_file)
    

def get_fresh_record():
    return {'fname':'', 'lname':'', 'tel':'', 'email':'', 'item1':'', 
            'item2':'', 'itme3':'', 'org':'', 'note':'', 'bday':'', 
            'rev':'', 'social':''}
    
       
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
    line = line.strip()
    *junk, email = line.split(':')
    print(f"{line} --> {email}")
    return email


def parse_item1(line):
    # Multiple formats; many are broken probably by , \n etc. in original
    # Lines of interest look like this: 
    # item1.EMAIL;type=INTERNET;type=pref:julia.dadiomov@venafi.com
    # item1.ADR;type=HOME;type=pref:;;Am Heistersiek 12;Spenge;Nordrhein-Westfale
    # item1.ADR;type=WORK;type=pref:;;530 Lytton Ave\, 2nd Floor\nSuite 202\n\n;Palo Alto;CA;94301;United States
    # item1.TEL;type=pref:+441277202041
    # item1.X-ABLabel:England home
    # X-ABLabel sometimes follows TEL tag
    line = line.strip()
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
        

def parse_item1_xlabel(line):
    # Lines look like this:
    # item1.X-ABLabel:England home
    line = line.strip()
    target_value = ''
    
    *junk, target_value = line.split(':')       
    print(target_value)    
    return target_value
    


def parse_raw(list_of_lines):
    records = []
    new_record = False
    # NOTE: Indivivual record elements are gathered in a dictionary so the 
    #       order of fields will be correct later when serialized for output
    this_record = get_fresh_record()
    unparsed_records = []
    
    for line in list_of_lines:
        if line.startswith('BEGIN:VCARD', 0):
            new_record = True
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
            elif line.startswith('TEL:', 0):
                # Might be more than one
                pass
            elif line.startswith('EMAIL:', 0):
                emails = []
                emails.append(parse_email(line))
            elif line.startswith('item1', 0):
                items = []
                if 'TEL' in line:
                    telephone_flag = True
                    items.append(parse_item1(line))
                if 'X-ABLabel' in line and item1_telephone_flag == True:
                    items.append(parse_item1_xlabel(line))
                    telephone_flag = False
            elif line.startswith('item2', 0):
                pass
            elif line.startswith('ORG:', 0):
                this_record['org'] = parse_org(line)
            elif line.startswith('NOTE:', 0):
                pass
            elif line.startswith('BDAY:', 0):
                this_record['bday'] = parse_bday(line)
            elif line.startswith('REV:', 0):
                this_record['rev'] = parse_rev(line)              
            elif line.startswith('X-SOCIALPROFILE', 0): 
                # Ignore this field
                pass
            elif line.startswith('VERSION', 0): 
                # Ignore this field
                pass
            elif line.startswith('PRODID', 0): 
                # Ignore this field
                pass           
            elif line.startswith('BEGIN', 0):
                # Ignore the new record toggle
                pass    
            else:
                unparsed_records.append(line)           
    
    return (records, unparsed_records)
    
    
def main():
    output = []
    unparsed_output = []
    
    for vcf_file in VCF_FILES:
            records = parse_raw(get_file(vcf_file))
            output.extend(records[0])
            unparsed_output.extend(records[1])
    
    return (len(output), len(unparsed_output))
    
    
if __name__ == "__main__":
    (good, bad) = main()
    print(f"GOOD: {good}  BAD: {bad}")

