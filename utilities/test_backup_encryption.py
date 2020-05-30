import backup_encryption as be
from datetime import datetime


def test_create_key():
    test_date = datetime.datetime(1969, 7, 16, 4, 17, 0)
    key = 'aa'
    assert be.create_key(test_date) == False
        
def test_load_key():
    assert be.load_key(key="development.key") == False
    

def test_encrypt_file(filename, key):
    assert be.encrypt_file(filename, key) == False