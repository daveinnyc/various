# Open a .vcf file and save relevant field in a .csv format

VCF_FILES = ['001.vcfmod', '002.vcfmod']


def openfile(file):
    with open(file) as f:
        raw_file = f.readlines()

    return(raw_file)
    



if __name__ == "__main__":
    main()