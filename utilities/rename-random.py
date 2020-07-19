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
    print(f"Checking system")

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
    print(f"Renaming Files")

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


def remove_old_set(root, target_dir):
    # Remove the old working dir and files
    fotos_dir = os.path.join(root, target_dir)  
    print(f"Removing files")
    
    if os.path.isdir(fotos_dir):
        try: 
            print(f"     Removing files from: {fotos_dir}")
            os.chdir(fotos_dir)
            for f in os.listdir():
                try: 
                   os.remove(f)
                except FileNotFoundError as e:
                   print(f"Can't remove {f}, error: {e}")
            os.chdir("..")
            print(f"     Removing directory: {target_dir}")
            os.rmdir(target_dir)
        except Exception as outer_e:
            print(f"Can't cd to directory {fotos_dir}, error: {outer_e}")
    else:
        print(f"Can't find directory {fotos_dir}")


def create_new_set(root, target_dir):
    # Create a new working directory
    fotos_dir = os.path.join(root, target_dir)
    print(f"Creating directory: {fotos_dir}")

    try: 
        os.mkdir(fotos_dir)
    except OSError as e:
        print(f"Can't create directory: {target_dir} error: {e}")   

    # Move about 10% of files to the new directory    
    print(f"Populating directory: {fotos_dir}")

    for entry in os.listdir():
        if os.path.isfile(entry):    
            move = random.randint(0,10)
            if move == 0: 
                try:
                    shutil.move(entry, target_dir)
                except OSError as move_e:
                    print(f"Can't move: {entry}, error: {move_e}")

                

if __name__ == "__main__":
    WORKING = "fotos"   
    random.seed()

    WORKING_ROOT = set_working_root()
    change_directories(WORKING_ROOT)
    rename_files()
    remove_old_set(WORKING_ROOT, WORKING)
    create_new_set(WORKING_ROOT, WORKING)
    