import backup_encryption as be
import base64 as b64
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

    # https://cryptography.io/en/latest/fernet/
    # Encrypted data is in bytes and URL-safe base64-encoded
    assert str(type(encrypted_data)) == "<class 'bytes'>"
    assert b64.urlsafe_b64encode(b64.urlsafe_b64decode(encrypted_data)) == encrypted_data
    
    
###############################
