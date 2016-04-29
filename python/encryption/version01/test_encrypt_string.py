import unittest
import encrypt_string as es
import create_key as ck

class EncryptionTest(unittest.TestCase):
    def runTest(self):
        #Instantiate
        e = es.Encryption()
        self.assertEquals(e.description, "Encryption method place holder", "Expected description to match")
        
class EncryptGetplain_textTest(unittest.TestCase):
    def runTest(self):
        #Create an object and populate it with an encryption key
        s = ck.Secret()
        s.create_secret_key('l')
        self.assertEqual(len(s.get_secret_key()), 26, "Expected key length 26 (lower case only)")
        
        #Create a text object and use it to store a plain text string
        text = ck.Text()
        text.set_plain_text("the quick brown fox jumped over the lazy dog")


        #Create an encryption object, pass in the string and the key
        e = es.Encryption()              
        cypher_text = e.encrypt(text.get_plain_text(), s.get_secret_key())
        text.set_cypher_text(cypher_text)   
        self.assertEqual(text.get_cypher_text(), cypher_text, "Expected cypher texts to match")     
        self.assertNotEqual(text.get_cypher_text(), text.get_plain_text(), "Expected texts to not match")

        
class EncryptEncryptTextTest(unittest.TestCase):
    def runTest(self):
        text = ck.Text()
        e = es.Encryption()       
        k =['q','w','e','r','t','y','u','i','o','p','a','s','d',
            'f','g','h','j','k','l','z','x','c','v','b','n','m',
            'Q','W','E','R','T','Y','U','I','O','P','A','S','D',
            'F','G','H','J','K','L','Z','X','C','V','B','N','M',' ']
        text.set_plain_text("abcdefghijk")
        self.assertEquals(text.get_plain_text(), "abcdefghijk", 
                          "Plain text not set properly") 
        text.set_key(k)
        self.assertEquals(text.get_key(), ['q','w','e','r','t',
               'y','u','i','o','p','a','s','d','f','g','h','j',
               'k','l','z','x','c','v','b','n','m','Q','W','E',
               'R','T','Y','U','I','O','P','A','S','D','F','G',
               'H','J','K','L','Z','X','C','V','B','N','M',' '], 
                "Key not set properly")
        
        self.assertEquals(e.encrypt(text.get_plain_text(), k),
                          ['q','w','e','r','t','y','u',
                           'i','o','p','a'])


class DecryptTest(unittest.TestCase):
    def runTest(self):
        #Create an object and populate it with an encryption key
        s = ck.Secret()
        s.create_secret_key('l')
        self.assertEqual(len(s.get_secret_key()), 26, "Expected key length 26 (lower case only)")
        
        #Create a text object and use it to store a plain text string
        text = ck.Text()
        text.set_plain_text("the quick brown fox jumped over the lazy dog")

        #Create an encryption object, pass in the string and the key
        e = es.Encryption()              
        cypher_text = e.encrypt(text.get_plain_text(), s.get_secret_key())
        text.set_cypher_text(cypher_text)          
        self.assertEqual(text.get_cypher_text(), cypher_text, "Expected cypher texts to match")     
        self.assertNotEqual(text.get_cypher_text(), text.get_plain_text(), "Expected texts to not match")
        
        plain_text = e.decrypt(text.get_cypher_text(), s.get_secret_key())
        print plain_text
        print text.get_plain_text()
        self.assertEqual(plain_text, text.get_plain_text(), "Expected plain texts to match")
        


if "__main__" == __name__:
    unittest.main()        
    
#EOF