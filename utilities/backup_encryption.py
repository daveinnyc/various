### A collection of utlities for encrypting files and saving them to gdrive

from cryptography.fernet import Fernet
from datetime import datetime


def create_key():
    key = Fernet.generate_key()
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H%M%S")
    keyfile = "backup_file_encryption.." + timestamp + ".key"
    with open(keyfile, "wb") as key_file:
        key_file.write(key)
    
    return keyfile
    
        
def load_key(key="development.key"):
    return open(development.key, "rb").read()
    
    
if __name__ == "__main__":
   # Be careful not too lose or overwrite the key as that will render 
   #    previously encrypted files useless
   print(f"CREATED KEYFILE: {create_key()}")
   