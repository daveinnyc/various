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

compare_list = defaultdict()
starting_dirs = ["C:\\dir1\\sub1", "C:\\dir2\\sub2"]



def get_hash(file_name):
    BLOCK_SIZE = 1048576        #1MB - Protect against reading large files
    hasher = hashlib.sha256()
    
    f = open(file_name, 'rb')
    read_buffer = f.read(BLOCK_SIZE)
    while len(read_buffer) > 0:
        hasher.update(read_buffer) 
        read_buffer = f.read(BLOCK_SIZE)
        
    return hasher.hexdigest()
    

def walk_dir(d):
    for path, dirs, files in os.walk(d):     
        for f in files:
            file_name = os.path.join(path, f)
            k = get_hash(file_name)
            if k in compare_list:
                compare_list[k][0] += 1       #Number of copies
                compare_list[k][1].append(f)  #Possible alternate file names
                compare_list[k][2].append(path)  #Path to files
            else:
                compare_list[k] = [1, [f], [path]]  #Exists in 2d dir tree



for d in starting_dirs:
    walk_dir(d)        
    
for k,v in sorted(compare_list.items()):
    if compare_list[k][0] > 1:
        #Print number of duplicates and unique names
        print "\n[ " + str(compare_list[k][0]) + ": ",
        for f in sorted(set(v[1])):
            print f,
        print "]"
        #Print full path and filename
        for file_name,file_path in zip(v[1], v[2]):
            print os.path.join(file_path, file_name)

print "\nDONE"            
#EOF