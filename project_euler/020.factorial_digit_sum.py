'''
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
import math

def solve_problem(n):
    factorial = math.factorial(n)
    digit_sum = 0
    for d in str(factorial):
        digit_sum += int(d)

    return(digit_sum)


if __name__ == "__main__":
    n = 100
    print(solve_problem(n))
