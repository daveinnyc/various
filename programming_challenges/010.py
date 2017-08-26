'''
Problem 010

Solutionum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

Copyright 2017 Dave Cuthbert, MIT License
'''
import math


def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1


def is_prime(number):   
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def solve_problem(maximum_value):
    running_sum = 0
    for next_prime in get_primes(2):
        if next_prime < maximum_value:
            running_sum += next_prime
        else:
            return running_sum


if __name__ == "__main__":
    maximum_value = 2000000
    print(solve_problem(maximum_value))
