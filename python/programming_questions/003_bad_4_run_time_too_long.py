'''
Problem 3
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

This version shrinks the memory footprint. It looks like it would work but it
   is way too slow. Stopped after 22 minutes and only checked for primes up to 
   number 1887616

Solution:
Dave Cuthbert copyright 2017
License MIT
'''

import math

def create_list_of_primes(maximum_value): 
    maximum_value = int(maximum_value / 2) + 1  # 2x is biggest multiplier 
    list_of_primes = set([2,3,5])               # Seed a few primes to start
  
    is_prime = True  
    for number in range(6, maximum_value + 1):  # Start after last seeded prime
        for prime in list_of_primes:
            if number % prime == 0:
                is_prime = False
                print("break:   number: {}  prime: {}".format(number, prime))
                break
        if is_prime == True:
           list_of_primes.add(number)
        is_prime = True
   
    return list(list_of_primes)


def check_if_prime(number_to_factor):
    primes = create_list_of_primes(number_to_factor)
    for p in reversed(primes):
        if (number_to_factor % p == 0):
            return p 

    return -1

    
def solve_problem(number_to_factor):
    largest_prime = check_if_prime(number_to_factor)

    return(largest_prime)


if __name__ == "__main__":
    #NUMBER_TO_FACTOR = 600851475143
    NUMBER_TO_FACTOR = 214    # 107 largest prime factor
    #NUMBER_TO_FACTOR = 20     # 5 largest prime factor

    print(solve_problem(NUMBER_TO_FACTOR))
