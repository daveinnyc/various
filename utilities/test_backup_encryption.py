import backup_encryption as be
from datetime import datetime


def test_create_key():
    # Key should look like this
    # key =  b'5jApZKjlxj4SjH5FU05tHx4abfUkzHxgYc3LxFmf4HM='
    (key, keyfile) = be.create_key()
    assert len(key) == 44
    assert len(keyfile) == 45
        
def test_load_key():
    assert be.load_key(key="development.key") == False
    

def test_encrypt_file():
    assert be.encrypt_file(filename, key) == False
    
#######################
'''
b'PrZBGII55Gs4sVpogQpddmOJ83rJEnVCaCixpdPF3zc='
b'5jApZKjlxj4SjH5FU05tHx4abfUkzHxgYc3LxFmf4HM='
b'PiW6myoHpzRkLuLIhe2Vd4sQ6wj7hri0PnFFN1ButCM='
b'CIFiBtvSJt04DAWgz-e6hRN9boJLnJrA7YkjcVjLQH8='
b'QKWJH8F4_VuRpY3fwO3NLZRVPU0szpfXN4q6LsJO6nM='
b'e9L6IPkG1TZOVgqQ5et-OgUGPPWJQA4aDztDea1sTdo='
b'cP2HOftDBubRBaRxAoCbXJnKR5Khu3bcbmEPptyiqPI='
b'BVMNNs97mlGdf72iv93RDlw7IDJbup4LryUPE1pIYzE='
b'nhPOmGjoteRIclQYnW0Az8n1EN-DIhYbmzktFQW-tdc='
b'NjLVQo0xARjQFM1Lobw1CBpE3KPxnUCHAGeEMoUdvJY='
b'bHgyYfPDKVZ1j7gjZhoRqaLzwKpra1XB7sGmn0vQ_Ps='
'''