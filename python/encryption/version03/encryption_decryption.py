import string
import random

'''
This version uses tuples instead to bind the 
plain and cypher texts together
''' 

def create_secret_key():
    '''
    Creates a key that is 53 characters long, mixed case. a-zA-Z + ' '
    ''' 
    #Creates a list of a-zA-Z
    key_original = []        
    for l in string.letters:
        key_original.append(l)  

    #Uses list to build a randomly ordered key
    key_permuted = []
    random.seed()
    while len(key_original)> 0:
        i = random.randint(0, len(key_original)-1)
        key_permuted.append(key_original[i])
        del key_original[i]
    #Adds a space to preserve word boundaries    
    key_permuted.append(' ')        
        
    return key_permuted 

        
def create_letter_iteration(cypher_key):
    plain_text_list = []
    for l in string.letters:
        plain_text_list.append(l)
    plain_text_list.append(' ')
        
    list_of_tuples = zip(plain_text_list, cypher_key)
    
    return list_of_tuples


def encrypt(plain_text, cypher_key):
    tuples_list = create_letter_iteration(cypher_key)
    encrypted_text = ''
    for p in plain_text:
        encode_index = [x[0] for x in tuples_list].index(p)
        encrypted_text += tuples_list[encode_index][1]
    return encrypted_text

    
def decrypt(cypher_text, cypher_key):
    tuples_list = create_letter_iteration(cypher_key)
    decrypted_text = ''
    for c in cypher_text:
        decode_index = [x[1] for x in tuples_list].index(c)
        decrypted_text += tuples_list[decode_index][0]
    return decrypted_text

#EOF    
