'''
Compare File Contents and remove duplicate files

    get sha256 hash for each file found
    use dictionary to check for duplicates
    delete duplicates

Dave Cuthbert
(C) 2021-02-12
MIT License
'''

import os
from collections import defaultdict
import hashlib
import sys

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
               # print(f"DUP: {len(compare_list[k])}  {os.path.join(path,f)}")
               try:
                   compare_list[k].append(os.path.join(path,f))
               except:
                   print(f"Could not add {os.path.join(path,f)}" )
                   print(f"{compare_list[k]}")
                   sys.exit()

            else:
               compare_list[k] = [os.path.join(path,f)] 
    
    return compare_list
    
    
def print_list(dups_list):
     for hash_key, file_names in dups_list.items():
         if len(file_names) > 1:
            print(f"HASH: {hash_key}   DUPS: {len(file_names)}")
            for f in file_names:
               print(f"   {f}")
            
                
def find_duplicates():
    starting_dir = os.getcwd()
    list_of_dups = check_files(starting_dir)
    print_list(list_of_dups)
 
    print("\nDONE")            
    
if "__main__" == __name__:
    find_duplicates()
    
#EOF
