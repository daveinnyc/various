''' rename files in local directory with random integer names.

windows screen saver isn't very good at randomizing fotos shown. 
Change file names regularly to provide more variety
'''

import os
import re
import random


random.seed()
new_names = set()
original_files = []

for entry in os.listdir():
    if os.path.isfile(entry):
        if re.match(".*jpg", entry):
            original_files.append(entry)


for counter in range(0, len(original_files)):
    new_value = random.randint(0,100000)
    while new_value in new_names:
        new_value = random.randint(0,100000)
    new_names.add(new_value)    


for of in original_files:
    nf = str(new_names.pop()).zfill(6) + ".jpg"
    
    try:
        os.rename(of, nf)
    except Exception as e:
        print("{}: {}".format(of, e))
