'''
Problem  034

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the 
    factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

NOTE:
Upper limit of 8 digits since
   8 * 9! has 
   8 * 362880 == 2903040

   (It requires at least 8 9s to get that high but there are 
    only 7 digits in the number)


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
import math

class factorials():
    digits = {}

    def __init__(self):
        digit_list = [math.factorial(digit) for digit in range(0,10)]
        for key, value in enumerate(digit_list):
            self.digits[key] = value

    def get_factorial(self, n):
        return self.digits[n]
        

def get_digits(number):
    digit_list = []
    while number > 0:
        digit_list.append(number % 10)
        number = number // 10

    return digit_list


def solve_problem():
    a = factorials()   

    digits = []
    digit_factorial_sum = 0
    for i in range(3, 2903040):  # Upper limit: 8 * 9!, 1 & 2 excluded by def.
        digit_sum = 0
        digits = get_digits(i)
        for d in digits:
             digit_sum += a.get_factorial(d)
   
        if digit_sum == i:
            digit_factorial_sum += i

    return digit_factorial_sum


if __name__ == "__main__":
    print(solve_problem())
