'''
Problem 015

Starting in the top left corner of a 2×2 grid, and only being able to move to
   the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid? 


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
import math


def solve_problem():
    ''' The problem is a cominatorics question askign for a permutation. The
        general solution is: 
                  (number of objects)! / ((type 1)! * (type 2)! * .. * (type n)!)
    '''

    number_of_objects = math.factorial(40)
    number_of_down = math.factorial(20)
    number_of_right = math.factorial(20)

    return( int(number_of_objects / (number_of_down * number_of_right)))


if __name__ == "__main__":
    print(solve_problem())
