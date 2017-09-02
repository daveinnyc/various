'''
Problem  016

215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''

def solve_problem():
    two_raised = 2 ** 1000
    digit_sum = 0
    for ch in str(two_raised):
        digit_sum += int(ch)

    return digit_sum



if __name__ == "__main__":
    print(solve_problem())
