#! python3 

''' rename files in local directory with random integer names.

windows screen saver isn't very good at randomizing fotos shown. 
Change file names regularly to provide more variety
'''

import os
import re
import random
import time


random.seed()
new_names = set()
original_files = []

for entry in os.listdir():
    if os.path.isfile(entry):
        if re.match(".*jpg", entry):
            original_files.append(entry)


for counter in range(0, len(original_files)):
    new_value = random.randint(0,1000000000)
    # Make sure the new names are unique
    # -- note this is only the new set, the new name
    #    may still duplicate an old name. The set is 
    #    to minimize this chance     
    while new_value in new_names:
        new_value = random.randint(0,1000000000)
    new_names.add(new_value)    


for of in original_files:
    nf = str(new_names.pop()).zfill(10) + ".jpg"
    
    try:
        os.rename(of, nf)
    except Exception as e:
        print("{}: {}".format(of, e))
        
time.sleep(5)        
