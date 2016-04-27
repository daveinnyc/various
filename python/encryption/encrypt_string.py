import create_key as ck
import string as s


class Encryption: 
    def __init__(self):
        self.description = "Encryption method place holder"
        
        
    def numeric_encode(self, plain_text):    
        numeric_text = []
        for p in plain_text:
            if p in s.letters:
                numeric_text.append(s.letters.index(p))
            else:
                #Will drop punctuation and preserve spaces
                numeric_text.append(99)
        return numeric_text

        
    def encrypt(self, plain_text, secret_key):
        conv = ck.Converter()
        conv.set_key(secret_key) 
        num_text = self.numeric_encode(plain_text)
        cypher_text = []
        for n in num_text:
            cypher_text.append(conv.get_key(n))
        return(cypher_text)
        
        
    def decrypt(self, cypher_text, key):
        plain_text = cypher_text
        return plain_text
    
#EOF