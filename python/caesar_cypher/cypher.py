'''Inspired by chap 1 Invent With python
   https://inventwithpython.com/hacking/chapter1.html

   Author: Dave Cuthbert
   Copyright: 2016
   License: MIT
'''
import random
import string 

def get_key():
    '''Get a random number to rotate text
    25 not 26 because cypher should shift at least 1 place
    '''
    random.seed()
    cypher_key = random.randint(1,25)
    
    return cypher_key


def rotate(letter, rotation_key):
    index = 0
    if letter in string.uppercase:
        index = string.uppercase.index(letter)
    elif letter in string.lowercase:
        index = string.lowercase.index(letter)
    else:
        print "Error -- not a letter"
    index += rotation_key
    if index > 26:
        index -= 26
    
    if letter in string.uppercase:
        return string.uppercase[index]
    elif letter in string.lowercase:
        return string.lowercase[index]
        
    
def encode(text, rotation_key):
    result = ''
    for t in text:
        if t in string.uppercase:
            result += rotate(t, rotation_key)
        elif t in string.lowercase:
            result += rotate(t, rotation_key)
        else:
            result += t
    
    return result


def get_index(letter):
    return string.letters.index(letter)