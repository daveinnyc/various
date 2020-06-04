import backup_encryption as be
import hashlib
import os

from datetime import datetime


def test_create_key():
    # Results should look like this
    #   key:  b'5jApZKjlxj4SjH5FU05tHx4abfUkzHxgYc3LxFmf4HM='
    #   keyfile: 'backup_file_encryption..2020-05-31-122543.key'
    (key, key_file) = be.create_key()
    assert len(key) == 44
    assert type(key) is bytes
    assert len(key_file) == 45
        
        
def test_load_key():
    (generated_key, key_file) = be.create_key()
    loaded_key = be.load_key(key=key_file) 
    
    try: 
        os.remove(key_file)
        assert loaded_key == generated_key
    except Exception as e:
        print(f"ERR: Unknown exception {e}")
        assert "Passed Test" == False
    

def test_encrypt_file():
    test_file_contents = '''A short test file'''
    test_file = 'TEST_FILE'
    
    with open(test_file, "w") as tf:
        tf.write(test_file_contents)
        
    try: 
        key = be.load_key(key="development.key") 
        encrypted_data = be.encrypt_file(test_file, key)     
    except IOError:
        print(f"ERR: Cannot open {test_file}") 
    except EOFError:
        print(f"ERR: Unexpected EOF in {test_file}")        
    except Exception as e:
        print(f"ERR: Unknown exception {e}")
    finally: 
        os.remove(test_file)

    assert str(type(encrypted_data)) == "<class 'bytes'>"
    

###############################
'''
# Need to figure out how to verify file was encrypted
tests> cat > testfile
This is a string

tests> gpg -c testfile
tests> md5sum testfile.gpg
7ecc8b905e76d913680539da5ee92f6c *testfile.gpg

tests> rm testfile.gpg
tests> gpg -c testfile
tests> md5sum testfile.gpg
62b96de01c7a294982a333a10ec37034 *testfile.gpg
'''

'''
https://cryptography.io/en/latest/fernet/

Returns bytes:	A secure message that cannot be read or altered without the key. It is URL-safe base64-encoded. This is referred to as a “Fernet token”.
'''