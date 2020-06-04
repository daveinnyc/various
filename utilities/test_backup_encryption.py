import backup_encryption as be
import base64 as b64
import os

from datetime import datetime


### SETUP NOTES
#   Many tests require existence of 'development.key' file


### TESTS
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
    except IOError as ioe:
        print(f"ERR: IO problem {ioe}") 
    except EOFError:
        print(f"ERR: Unexpected EOF in {test_file}")        
    except Exception as e:
        print(f"ERR: Unknown exception {e}")
    finally: 
        os.remove(test_file)

    # Data format specified in https://cryptography.io/en/latest/fernet/
    # Encrypted data is in bytes and URL-safe base64-encoded
    assert str(type(encrypted_data)) == "<class 'bytes'>"
    assert b64.urlsafe_b64encode(b64.urlsafe_b64decode(encrypted_data)) == encrypted_data
    

def test_write_encrypted_file():
    test_file_contents = '''A short test file'''
    test_file = 'TEST_FILE'
   
    with open(test_file, "w") as tf:
        tf.write(test_file_contents)
        
    try: 
        key = be.load_key(key="development.key") 
        encrypted_data = be.encrypt_file(test_file, key)
        file_name = be.write_encrypted_file(test_file, encrypted_data)
        file_size = os.path.getsize(file_name)
    except IOError as ioe:
        print(f"ERR: IO problem {ioe}") 
    except EOFError:
        print(f"ERR: Unexpected EOF in {test_file}")        
    except Exception as e:
        print(f"ERR: Unknown exception {e}")
    finally: 
        os.remove(test_file)
        os.remove(test_file + '.enc')

    assert file_name == test_file + '.enc'
    assert file_size > 0
    
    
def test_decrypt_file():
    test_file_contents = 'A short test file'
    test_file = 'TEST_FILE'
    
    with open(test_file, "w") as tf:
        tf.write(test_file_contents)
        
    try: 
        key = be.load_key(key="development.key") 
        encrypted_data = be.encrypt_file(test_file, key)     
        encrypted_file = be.write_encrypted_file(test_file, encrypted_data)     
        decrypted_data = be.decrypt_file(encrypted_file, key)
    except Exception as e:
        print(f"ERR: Unknown exception {e}")
    finally: 
        os.remove(test_file)

    assert decrypted_data == test_file_contents
    
    
###############################
# Testing the write encrypted file function
