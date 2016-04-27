import string
import random
from collections import defaultdict


class Secret:
    def __init__(self):
        self.secret_key = []
      
      
    def get_secret_key(self):
        return self.secret_key
    
    
    def create_secret_key(self, key_type):
        '''
        Creates a key that is 26 characters long, upper case or lower case
           or else 52 characters long, mixed case
           
           NOTE: not using a function like: 
                    key_permuted = list(itertools.permutations(key_original))
                 because python tries to compute all 26 char permutations which takes forever 
        '''           
        key_original = []
        
        if "l" == key_type:
            for ltr in string.lowercase:
                key_original.append(ltr)
        elif "u" == key_type: 
            for ltr in string.uppercase:
                key_original.append(ltr)
        else:
            for ltr in string.letters:
                key_original.append(ltr)
                
        key_permuted = []
        random.seed()
        while len(key_original)> 0:
            i = random.randint(0, len(key_original)-1)
            key_permuted.append(key_original[i])
            del key_original[i]
            
        self.secret_key = key_permuted 

        
class Text:
    def __init__(self):
        self.plain_text = ''
        self.cypher_text = ''
        self.key = ''
     
        
    def set_plain_text(self, text):
        self.plain_text = text


    def get_plain_text(self):
        return self.plain_text
    
    
    def set_cypher_text(self, text):
        self.cypher_text = text
    
    
    def get_cypher_text(self):
        return self.cypher_text
    
    
    def set_key(self, k):
        self.key = k


    def get_key(self):
        return self.key


class Converter:
    def __init__(self):
        self.converter = defaultdict(list)
        count = 0
        for l in string.letters:
            self.converter[count].append(l)
            count += 1
        #Fake value for ' ' in 
        self.converter[99].append(' ')
                  
            
    def get_plain(self,i):
        return self.converter[i][0]
    
    
    def get_key(self,i):
        print str(i) + ' ' + str(self.converter[i])
        return self.converter[i][1]
    
    
    def set_key(self, cypher_key):
        count = 0
        for k in cypher_key:
            self.converter[count].append(k)
            count += 1
        #Fake values for ' ' out
        self.converter[99].append(' ')
        print self.converter[99]
                

#EOF    