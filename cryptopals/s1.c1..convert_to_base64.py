# the cryptopals crypto challenges
# http://cryptopals.com/sets/1/challenges/1
#
# Convert hex to base64
# The string:
#
# 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
# Should produce:
#
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
#
# Solution: Dave Cuthbert
# MIT License, 2019

import base64
  
def convert_string_to_b64(string):
    return base64.b64encode(string)

def convert_b64_to_string(string):
    return base64.b64decode(string)


def convert_hex_to_string(hex_string):
    hex_chars = [hex_string[pos:pos+2] for pos in range(0, len(hex_string), 2)]
    ascii_chars = [chr(int(hc, 16)) for hc in hex_chars]
    return "".join(ascii_chars)
    
        

if __name__ == "__main__":  
    # Test input for set 1, challenge 1
    input="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
   
    print(convert_string_to_b64(convert_hex_to_string(input)))