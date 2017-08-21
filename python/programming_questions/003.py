'''
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?



There are a few failed attempts in this archive, 003_bad*. They aal work on 
   small numbers but fail on larger ones for various reasons. 

This version tries a different technique. 
   Divide the target number (TN) by some small value
     If even division, larger divisor is potential largest prime
     If not, try next small divisor

Solution:
Copyright 2017 Dave Cuthbert 
License MIT
'''

import math


def find_largest_factor(target_number):
    last_possible_divisor = int(math.sqrt(target_number)) + 1
    possible_prime = target_number
    for small_divisor in range(2, last_possible_divisor):
        if (target_number % small_divisor == 0):
            possible_prime = int(target_number / small_divisor)
            break

    return possible_prime
   
 
def solve_problem(target_number):
    possible_largest_prime = find_largest_factor(target_number)
    while True:
        if possible_largest_prime ==  2:
            # smallest possible prime, base case
            return 2
    
        another_possibility = possible_largest_prime
        possible_largest_prime = find_largest_factor(another_possibility)
        if another_possibility == possible_largest_prime:
            return possible_largest_prime


if __name__ == "__main__":
    TARGET_NUMBER = 600851475143
    #TARGET_NUMBER = 214      # 2 * 107 
    #TARGET_NUMBER = 2000     # 2**4 * 5**3  
    #TARGET_NUMBER = 1079     # 13 * 83 

    print(solve_problem(TARGET_NUMBER))
