'''
A basic sorting algorithm and a function to generate some data

Author: Dave Cuthbert
Copyright: 2017
License: MIT
'''

import random
import cProfile

#GLOBAL TEST VALUES
SIZE = 200
MIN_VALUE = 0
MAX_VALUE = 100


def generate_list(size, min_value=0, max_value=1000):
    random.seed()
    num_list = []

    if(size < 1):
        return "Error: size must be at least 1"
    if(min_value > max_value):
        return "Error: min_value must be <= max_value"
    if(type(size) is not int):
        return "Error: size must be an integer"
    if(type(min_value) is not int):
        return "Error: min_value must be an integer"
    if(type(max_value) is not int):
        return "Error: max_value must be an integer"
    
    for i in range(size):
        num_list.append(random.randint(min_value, max_value))

    return num_list


def bubblesort(num_list=[]):
    if len(num_list) == 0:
        num_list = generate_list(SIZE, MIN_VALUE, MAX_VALUE)
    for i in range(len(num_list)):
        for j in range(len(num_list)-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

    return num_list


if __name__ == '__main__':
    cProfile.runctx('bubblesort()', globals=globals(), locals=locals())

#EOF
