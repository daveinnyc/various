"""
    A collection of utlities for encrypting files and saving them to gdrive
"""

from datetime import datetime
from cryptography.fernet import Fernet

def create_key():
    """
    Generate an encryption key. During development this was run once
    and the key renamed to 'development.key'. To avoid saving keys to
    github, .gitignore was updated to ignore *.key files
    """
    key = Fernet.generate_key()
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H%M%S")
    keyfile = "backup_file_encryption.." + timestamp + ".key"
    with open(keyfile, "wb") as key_file:
        key_file.write(key)

    return (key, keyfile)


def load_key(key="development.key"):
    """
    Read in a previously generated key. Defaults to the dev key
    """
    secret_key = 'Not yet loaded'
    
    try:
        #loaded = open(key, "rb")
        loaded = open("THIS_WILL_FAIL", "rb")
        secret_key = loaded.read()
    except IOError as ioe:
        print(f"ERR: IO Error {ioe}")
    
    return secret_key


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
   