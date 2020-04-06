# From https://challenges.wolfram.com/challenge/butterflied-strings
# Join a string with its reversal.
#  More Details
#  To butterfly the string "Wolfram", take its reversal "marfloW" 
#  and join them to form "WolframmarfloW". 


def butterfly(str_in):
    str_reversed = "".join(reversed(str_in))
    
    return str_in + str_reversed
