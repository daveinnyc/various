'''
Problem 021

Let d(n) be defined as the sum of proper divisors of n (numbers less than n 
  which divide evenly into n).

If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and 
  each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
   and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 
   and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000. 


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
import math
from collections import defaultdict

class DivisorSums():
    sum_cache = defaultdict(lambda:1)

    def __init__(self):
        self.sum_cache

    def add_value(self, n1, n2):
        self.sum_cache[n1] = n2

    def get_value(self, n1):
        return self.sum_cache[n1]


def find_divisors(n):
    divisors = {1}
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(int(n / i))
            divisors.add(i)

    return divisors


def check_if_amicable(n1, n2):
    if cached.get_value(n1) == 1:
        cached.add_value(n1, sum(find_divisors(n1)))

    if cached.get_value(n1) == n2:
        return True

    return False


def solve_problem(end_number):
    amicable_numbers = set() 

    for n in range(1, end_number):
        divisor_list = find_divisors(n)
        list_sum = sum(divisor_list) 

        cached.add_value(n, list_sum)

        if (list_sum != n): 
            if check_if_amicable(list_sum, n):
                amicable_numbers.update([list_sum, n])

    return(amicable_numbers)


if __name__ == "__main__":
    ending_number = 10000
    cached = DivisorSums()
    print(sum(solve_problem(ending_number)))
