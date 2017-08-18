'''
Problem 6

The sum of the squares of the first ten natural numbers is,
     1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
     (1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural 
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred 
natural numbers and the square of the sum.



Solution:
Dave Cuthbert copyright 2017
License MIT
'''
def sum_of_squares(start_num, end_num):
    sum_sqs = sum(n*n for n in range(start_num, end_num + 1))
    return sum_sqs

def sum_of_numbers(start_num, end_num):
    sum_nums = sum(n for n in range(start_num, end_num + 1))
    return sum_nums

def solve_problem(start_num, end_num):
    sum_nums = sum_of_numbers(start_num, end_num)
    sum_sqs = sum_of_squares(start_num, end_num) 

    return ((sum_nums**2) - sum_sqs)
           

if __name__ == "__main__":
    START_NUM = 1
    END_NUM = 100
    print(solve_problem(START_NUM, END_NUM))
