# Based on https://www.learnpython.org/en/Generators
# Using pytest to create propety based tests for the generator functions


import random 

def lottery(): 
# returns 6 numbers between 1 and 40 
   for i in range(6): 
      yield random.randint(1, 40) 

   # returns a 7th number between 1 and 15 
   yield random.randint(1,15) 


# fill in this function 
def fib():
    first = 0
    second = 1

    while True:
        first, second = second, first + second
        yield first, second
