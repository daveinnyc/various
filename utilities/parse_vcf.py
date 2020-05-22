# Open a .vcf file and save relevant field in a .csv format

VCF_FILES = ['001.vcfmod', '002.vcfmod']


def get_file(file):
    with open(file) as f:
        raw_file = f.readlines()

    return(raw_file)
    

def parse_raw(list_of_lines):
    records = []
    new_record = False
    this_record = []
    for line in list_of_lines:
        if line == 'BEGIN:VCARD':
            new_record == True
        if line == 'END:VCARD':
            new_record == False
        
        if new_record:
            if line.startswith() == 'N:':
                pass
            elif line.startswith() == 'TEL:':
                # Might be more than one
                pass
            elif line.startswith() == 'EMAIL:':
                pass
            elif line.startswith() == 'REV:':
                pass
            elif line.startswith() == 'item1':
                pass
            elif line.startswith() == 'item2':
                pass
            elif line.startswith() == 'ORG:':
                pass
            elif line.startswith() == 'NOTE:':
                pass
            elif line.startswith() == 'BDAY:':
                pass
            elif line.startswith() == 'X-SOCIALPROFILE':
                pass
            elif line.startswith() == 'REV:':
                pass
            else:
                pass           
            
    return len(list_of_lines)
    
    
def main():
    output = []
    
    for vcf_file in VCF_FILES:
            output.append(parse_raw(get_file(vcf_file)))
            
    print(output)        

if __name__ == "__main__":
    main()