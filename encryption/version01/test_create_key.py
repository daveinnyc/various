import unittest
import create_key as ck


#SECRET CLASS
class InitializeSecretTest(unittest.TestCase):
    def runTest(self):
        secret = ck.Secret()
        self.assertEqual(secret.secret_key, [], "Expected empty secret key list")
        secret.create_secret_key('l')  #Could be any form, just need a value there to test get method
        self.assertEqual(secret.secret_key, secret.get_secret_key(), "Expected stored key to match fetched key")
       

class CreateKeyLowerTest(unittest.TestCase):
    def runTest(self):
        #lower case key
        secret = ck.Secret()
        secret.create_secret_key('l')  
        self.assertEqual(len(secret.secret_key), 26, "Expected 26 characters")
        self.assertTrue('a' in secret.secret_key, "Expected 'a'")
        self.assertFalse('A' in secret.secret_key, "Expected 'A' to not be in list")

class CreateKeyUpperTest(unittest.TestCase):        
    def runTest(self):    
        #upper case key
        secret = ck.Secret()
        secret.create_secret_key('u')
        self.assertEqual(len(secret.secret_key), 26, "Expected 26 characters")
        self.assertFalse('b' in secret.secret_key, "Expected 'b' to not be in list")
        self.assertTrue('B' in secret.secret_key, "Expected 'B'")

class CreateKeyMixedTest(unittest.TestCase):
    def runTest(self):       
        #mixed case (long) key
        secret = ck.Secret()
        secret.create_secret_key('a')
        self.assertEqual(len(secret.secret_key), 52, "Expected 52 characters")
        self.assertTrue('c' in secret.secret_key, "Expected 'c'")
        self.assertTrue('C' in secret.secret_key, "Expected 'C'")


#TEXT HOLDER CLASS 
class GetSetplain_textTest(unittest.TestCase):
    def runTest(self):
        #Test get / set methods for plain_text
        t = ck.Text()
        t.set_plain_text('This is a string')
        self.assertEqual(t.plain_text, 'This is a string', "Expected plain_text string")
        self.assertEqual(t.plain_text, t.get_plain_text(), "Expected stored plain_text to match fetched")
        
class GetSetcypher_textTest(unittest.TestCase):
    def runTest(self):
        #Test get / set methods for cypher_text
        t = ck.Text()
        t.set_cypher_text('This is a cypher')
        self.assertEqual(t.cypher_text, 'This is a cypher', "Expected cypher")
        self.assertEqual(t.cypher_text, t.get_cypher_text(), "Expected stored cypher_text to match fetched")
    
class GetSetKeyTest(unittest.TestCase):
    def runTest(self):
        #Test get / set methods for key
        t = ck.Text()
        t.set_key('This is a key')
        self.assertEqual(t.key, 'This is a key', "Expected key")
        self.assertEqual(t.key, t.get_key(), "Expected stored key to match fetched")



#CONVERTER CLASS    
class CreateConverterTest(unittest.TestCase):
    def runTest(self):
        #Create object to hold the key
        c = ck.Converter()
        self.assertEqual(len(c.converter), 53, "Expected 52 keys in Converter object")
        
class GetPlainConverterTest(unittest.TestCase):
    def runTest(self):
        #Check plain_text properly stored
        c = ck.Converter()
        self.assertEquals(c.get_plain(1), 'b', "Expected 'b'" )
        self.assertEquals(c.get_plain(25), 'z', "Expected 'z'" )
        self.assertEquals(c.get_plain(27), 'B', "Expected 'B'" )
        self.assertEquals(c.get_plain(51), 'Z', "Expected 'Z'" )  
        
class SetKeyConverterTest(unittest.TestCase):
    def runTest(self):
        #Check key is stored and retrieved properly
        c = ck.Converter()
        k =['q','w','e','r','t','y','u','i','o','p','a','s','d',
            'f','g','h','j','k','l','z','x','c','v','b','n','m',
            'Q','W','E','R','T','Y','U','I','O','P','A','S','D',
            'F','G','H','J','K','L','Z','X','C','V','B','N','M']
        c.set_key(k)
        self.assertEquals(c.get_key(1), 'w', "Expected 'w'" )
        self.assertEquals(c.get_key(25), 'm', "Expected 'm'" )
        self.assertEquals(c.get_key(27), 'W', "Expected 'W'" )
        self.assertEquals(c.get_key(51), 'M', "Expected 'M'" )  
                  

if "__main__" == __name__:
    unittest.main()        
    
#EOF