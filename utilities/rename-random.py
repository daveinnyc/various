#! python3 

''' rename files in local directory with random integer names.

windows screen saver isn't very good at randomizing fotos shown. 
Change file names regularly to provide more variety
'''

import os
import platform
import re
import random
import shutil
import sys



def set_working_root():
    # Handle windows and cygwin paths 
    system_os = platform.system()
    root = ""
    
    if system_os == "Windows":
       root = "c:\Temp\screen-saver-active"
    elif system_os[0:9] == "CYGWIN_NT":    
       root = "/cygdrive/c/TEMP/screen-saver-active"

    return root 


def change_directories(target):
    try: 
        os.chdir(target)
    except OSError as working_e:    
        print(f"Can't cd to: {working_e}")


def rename_files():
    new_names = set()
    original_files = []

    for entry in os.listdir():
        if os.path.isfile(entry):
            if re.match(".*jpg", entry):
                original_files.append(entry)

    # Create random file names
    for counter in range(0, len(original_files)):
        new_value = random.randint(0,100000)
        while new_value in new_names:
            new_value = random.randint(0,100000)
        new_names.add(new_value)    


    # Rename everything randomly
    for of in original_files:
        nf = str(new_names.pop()).zfill(6) + ".jpg"
        
        try:
            os.rename(of, nf)
        except Exception as e:
            print("{}: {}".format(of, e))


def remove_old_set():
    # Remove the old working dir and files
    fotos_dir = os.path.join(WORKING_ROOT, WORKING)
    try: 
        os.chdir(fotos_dir)
        for f in os.listdir():
            try: 
               os.remove(f)
            except FileNotFoundError as e:
               print(f"Can't remove {f}, error: {e}")
        os.chdir("..")
        os.rmdir(WORKING)
    except Exception as outer_e:
       print(f"Can't find directory {fotos_dir}, error: {outer_e}")


def create_new_set():
    # Create a new working directory
    try: 
        fotos_dir = os.path.join(WORKING_ROOT, WORKING)
        os.mkdir(fotos_dir)
    except OSError as e:
        print(f"Can't create directory: {WORKING} error: {e}")   
        sys.exit()


    # Move about 10% of files to the new directory    
    for entry in os.listdir():
        if os.path.isfile(entry):    
            move = random.randint(0,10)
            if move == 0: 
                try:
                    shutil.move(entry, WORKING)
                except OSError as move_e:
                    print(f"Can't move: {entry}, error: {move_e}")
                

if __name__ == "__main__":
    WORKING_ROOT = set_working_root()
    print(f"DEBUG: {WORKING_ROOT}")  
    WORKING = "fotos"
    random.seed()
    
    change_directories(WORKING_ROOT)

    