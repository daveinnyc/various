'''
Problem 023

A perfect number is a number for which the sum of its proper divisors is exactly
   equal to the number. For example, the sum of the proper divisors of 28 would 
   be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
   and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest 
   number that can be written as the sum of two abundant numbers is 24. By 
   mathematical analysis, it can be shown that all integers greater than 28123 
   can be written as the sum of two abundant numbers. However, this upper limit 
   cannot be reduced any further by analysis even though it is known that the 
   greatest number that cannot be expressed as the sum of two abundant numbers
   is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
   two abundant numbers.


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
import math
from collections import defaultdict

class AbundantNumbers():
    abundant = defaultdict(lambda: False)

    def __init__(self):
        self.abundant

    def is_abundant(self, n):
        return self.abundant[n] 
    
    def set_abundant(self, n):
        self.abundant[n] = True


def find_factors(number):
    last_divisor = int(math.sqrt(number)) + 1
    factors = set([1])
    for divisor in range(2, last_divisor):
        if (number % divisor == 0):
            factors.add(divisor)
            factors.add(int(number / divisor))

    return factors

        
def solve_problem(n):
    UPPER_LIMIT = n
    abundants = AbundantNumbers()
    non_abundant_sum = 0
    
    # Find all the abundants
    for i in range(1, UPPER_LIMIT): 
        if abundants.is_abundant(i):
            pass
        else: 
            factor_sum = 0
            factors_i = find_factors(i)
            for f in factors_i :
                factor_sum += f

            if factor_sum > i:
                count = 1
                while i < UPPER_LIMIT:
                    i *= count
                    abundants.set_abundant(i) 
                    count += 1
    
    # Check if sum of 2 abundants
    for current_number in range(1, UPPER_LIMIT + 1):
        flag = True
        for number_to_subtract in range(1, current_number):
            if abundants.is_abundant(number_to_subtract):    
                remainder = current_number - number_to_subtract
                if abundants.is_abundant(remainder):
                    flag = False
                    break
        if flag:
            non_abundant_sum += current_number    
    
    return(non_abundant_sum)


if __name__ == "__main__":
    n = 28123
    print(solve_problem(n))
