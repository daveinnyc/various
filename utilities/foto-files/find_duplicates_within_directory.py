'''
Compare File Contents

    take a starting directory (or directories)
    walk down the tree
    get sha256 hash for each file found
    use dictionary to check for duplicates
    report duplicates

Dave Cuthbert
(C) 2016-03-25
MIT License
'''

import os
from collections import defaultdict
import hashlib


def get_hash(file_name):
    BLOCK_SIZE = 1048576        #1MB - Protect against reading large files
    hasher = hashlib.sha256()
    
    f = open(file_name, 'rb')
    read_buffer = f.read(BLOCK_SIZE)
    while len(read_buffer) > 0:
        hasher.update(read_buffer) 
        read_buffer = f.read(BLOCK_SIZE)
        
    return hasher.hexdigest()
    

def check_files(start_dir):
    compare_list = defaultdict()
    num_duplicates = 0
    
    for path, dirs, files in os.walk(start_dir):     
        for f in files:
            file_name = os.path.join(path, f)
            k = get_hash(file_name)
            if k in compare_list:
                # FOR DEV _DEBUG
                # print("DUP: {} --  {}".format(compare_list[k][1], f))
                try:
                    os.remove(f)
                except OSError as e:
                    print("Could not delete {} -- {}".format(f, e.strerror))
                    
                num_duplicates += 1
            else:
                compare_list[k] = [1, f, path] 

    print("Unique: {}     Duplicate: {}".format(len(compare_list), num_duplicates))            

                
def find_duplicates():
    starting_dir = os.getcwd()
    check_files(starting_dir)

    
# for k,v in compare_list.items():
    # if compare_list[k][0] > 1:
        # #Print number of duplicates and unique names
        # print "\n[ " + str(compare_list[k][0]) + ": ",
        # for f in sorted(set(v[1])):
            # print f,
        # print "]"
        # #Print full path and filename
        # for file_name,file_path in zip(v[1], v[2]):
            # print os.path.join(file_path, file_name)

    print("\nDONE")            
    
if "__main__" == __name__:
    find_duplicates()
    
#EOF
