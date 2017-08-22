'''
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 
     to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the 
     numbers from 1 to 20?


Since 5 is in the list the LCM has to end in 0 or 5, so only check those values.
     Will also speed up by dividing by the largest values first when checking if
     it is a possible factor and breaking out on first failure.


Solution:
Dave Cuthbert copyright 2017
License MIT
'''

from collections import defaultdict

def solve_problem(start_num, end_num):
    num_list = [number for number in range(start_num, end_num + 1)]

    # Since 5 is in the list, LCM has to end in 5 or 0
    least_common_multiple = 5 

    while True:
        found = True
        for num in reversed(num_list):
            if (least_common_multiple % num != 0):
               found = False           
               least_common_multiple += 5
               break

        if (num == 1) and (found == True):
            return least_common_multiple
      
           
if __name__ == "__main__":
    START_NUM = 1
    END_NUM = 20
    print(solve_problem(START_NUM, END_NUM))
