'''
Problem 030

Surprisingly there are only three numbers that can be written as the sum of 
  fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
  of their digits.

Solution: Copyright 2017 Dave Cuthbert, MIT License
'''


def solve_problem(power):
    max_int = power * (9 ** power)

    answer = 0
    for number in range(2,max_int):
        digit_sum = 0
        for digit in str(number):
            digit_sum += (int(digit) ** power)

        if digit_sum == number:        
            answer += number

    return(answer)


if __name__ == "__main__":
    print(solve_problem(5))
