# Open a .vcf file and save relevant field in a .csv format

VCF_FILES = ['001.vcfmod', '002.vcfmod']


def get_file(file):
    with open(file) as f:
        raw_file = f.readlines()

    return(raw_file)
    
    
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
            if len(this_record) > 0 :
                records.append(this_record)
            this_record = []
        
        if new_record:
            if line.startswith('N:', 0):
                this_record.extend(parse_n(line))
                print(this_record)
            elif line.startswith('TEL:', 0):
                # Might be more than one
                pass
            elif line.startswith('EMAIL:', 0):
                pass
            elif line.startswith('item1', 0):
                pass
            elif line.startswith('item2', 0):
                pass
            elif line.startswith('ORG:', 0):
                pass
            elif line.startswith('NOTE:', 0):
                pass
            elif line.startswith('BDAY:', 0):
                pass
            elif line.startswith('X-SOCIALPROFILE', 0):            
                pass
            elif line.startswith('REV:', 0):
                this_record.extend(parse_rev(line))
                print(this_record)               
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

