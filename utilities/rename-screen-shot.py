# Rename OS X sreenshots 

import glob
import os
import sys

if len(sys.argv) != 2:
   print("USAGE: python3 rename-screen-shot.py PREFIX")
   sys.exit()

prefix = sys.argv[1]
files = glob.glob("Screen Shot*png")
current_date = ''
for f in files:
   foto_date = f[12:22]
   if foto_date != current_date:
       current_date = foto_date
       count = 0
   count += 1
   new_name = f"{prefix}..{foto_date}..{count:02}.png"
   os.rename(f, new_name)
