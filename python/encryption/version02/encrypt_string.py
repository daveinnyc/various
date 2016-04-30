import string
import random
from collections import defaultdict

'''
Working, but harder than it should be:
    string to list
    list encoded as numbers
    key to list
    key encoded as numbers
    numbers used to link value from string to value from list
    
Better solution --> rewrite to get rid of numbers

Note: there is an extra value for spaces which doens't get encoded 
to preserve words in the encrypted output. 
''' 


def create_secret_key():
    '''
    Creates a key that is 52 characters long, mixed case
    NOTE: not using a function like: 
            key_permuted = list(itertools.permutations(key_original))
         because computing all 52 char permutations takes forever 
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
        
    return key_permuted 

        
def create_letter_iteration(cypher_key):
    '''Create a dictionary matching position to key value
       F,d,f,E,r,t,....
       0,1,2,3,4,5,....
    '''
    letter_iter = defaultdict(list)
    for c in cypher_key:
        letter_iter[cypher_key.index(c)].append(c)

    #Add fixed ' ' to preserve location of spaces
    letter_iter[52].append(' ')
    
    return letter_iter
             
            
def numeric_encode(plain_text):  
    '''Take a plain text and encode the letters as numbers'''  
    numeric_text = []
    for p in plain_text:
        if p in string.letters:
            numeric_text.append(string.letters.index(p))
        else:
            #Will drop punctuation and preserve spaces
            numeric_text.append(52)
    return numeric_text

        
def create_single_cypher_key():
    '''Create a key to map standard alphabet to permuted one
        e.g.    0[d][a]
                1[F][b]
                2[c][c]
                3[w][d]
                4[S][e]
                5[a][f]
    Perhaps later generalize to allow more encryption rounds so 
    second value is not just a-zA-Z
    '''
    secret_key = create_secret_key()
    cypher_key = create_letter_iteration(secret_key)
    for l in string.letters:
        cypher_key[string.letters.index(l)].append(l)
    #Add fixed ' ' to preserve location of spaces
    cypher_key[52].append(' ')
        
    return cypher_key


def get_num_from_cypher_key(cypher_key):
    nums = [None for i in range(53)]
    for k in cypher_key.keys():
        if 52 == k:
            nums[52] = cypher_key[k][0]
        else:
            nums[k] = cypher_key[k][0]
    
    return nums


def encrypt(plain_text, cypher_key):
    num_text = numeric_encode(plain_text)
    cypher_text = []
    for n in num_text:
        cypher_text.append(cypher_key[n][0])
    return(cypher_text)
    
    
def decrypt(cypher_text, cypher_key):
    num_cypher_key = get_num_from_cypher_key(cypher_key)
    num_cypher_text = []
    
    for c in cypher_text:
        num_cypher_text.append(num_cypher_key.index(c))
        
    plain_text = []
    for n in num_cypher_text:
        plain_text.append(cypher_key[n][1])
            
    return plain_text


#EOF    