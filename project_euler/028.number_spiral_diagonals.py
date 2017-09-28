'''
Problem  028

Starting with the number 1 and moving to the right in a clockwise direction a 5
    by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed 
    in the same way?

DWC: Notice that the top right squares n in the  sequence 1,3,5,7, ..., 1001
     The other values can be calculated as offsets from n

Solution: Copyright 2017 Dave Cuthbert, MIT License
'''

def solve_problem(n):
    sum_of_rounds = 1  # Add 1 for value in the center

    for i in range(n, 1, -2):
        sum_of_rounds += (i ** 2)                   # Top R
        sum_of_rounds += (i ** 2) - (i - 1)         # Top L
        sum_of_rounds += (i ** 2) - (2 * (i - 1))   # Bottom L
        sum_of_rounds += (i ** 2) - (3 * (i - 1))   # Bottom R

    return(sum_of_rounds)


if __name__ == "__main__":
    n = 1001 

    print(solve_problem(n))
