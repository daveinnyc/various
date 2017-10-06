'''
Problem 024

A permutation is an ordered arrangement of objects. For example, 3124 is one 
  possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
  are listed numerically or alphabetically, we call it lexicographic order. The
  lexicographic permutations of 0, 1 and 2 are:

  012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5,
    6, 7, 8 and 9?

Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
from itertools import permutations

def get_permutations(limit):
    digits = [digit for digit in range(0, limit + 1)]
    digit_str = ''.join([str(digit) for digit in digits])
    for p in permutations(digit_str):
        yield p

    

def solve_problem(limit):
    count = 0
    perms = get_permutations(limit)
    while count < 1000000:
        sequence = next(perms)
        count += 1

    return ''.join([str(s) for s in sequence]) 


if __name__ == "__main__":
    limit = 9
    print(solve_problem(limit))
