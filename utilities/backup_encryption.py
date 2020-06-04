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

    return (key, keyfile)
    
        
def load_key(key="development.key"):
    return open(key, "rb").read()
    

def encrypt_file(filename, key):
    encrypter = Fernet(key)
    
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = encrypter.encrypt(file_data)

    return encrypted_data


def write_encrypted_file(filename, encrypted_data):
    filename = filename + '.enc'
    
    with open(filename, "wb") as file:
        file.write(encrypted_data)

    return filename

    
def decrypt_file(filename, key):
    decrypter = Fernet(key)
    
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = decrypter.decrypt(encrypted_data)

    return str(decrypted_data.decode())
   
    
if __name__ == "__main__":
   # Be careful not too lose or overwrite the key as that will render 
   #    previously encrypted files useless
   print(f"CREATED KEYFILE: {create_key()}")
   