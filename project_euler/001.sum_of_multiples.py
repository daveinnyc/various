'''
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.


Solution:
Copyright 2017 Dave Cuthbert 
License MIT
'''

def find_multiples(factor, limit):
    list_of_factors = []
    for num in range(limit):
        if num % factor == 0:
            list_of_factors.append(num)

    return list_of_factors

def sum_of_list(list_to_sum):
    list_sum = 0
    for i in list_to_sum:
        list_sum += i

    return list_sum


def clean_up_lists(list1, list2):
    tmp_list = list1[:]     
    tmp_list.extend(list2)

    return set(tmp_list)

    
def solve_problem(factor1, factor2, maximum):
    list_factor_1 = find_multiples(factor1, maximum)
    list_factor_2 = find_multiples(factor2, maximum)

    return(sum_of_list(clean_up_lists(list_factor_1, list_factor_2)))


if __name__ == "__main__":
    MAX_VALUE = 1000
    LIST_FACTOR_1 = 3
    LIST_FACTOR_2 = 5

    print(solve_problem(LIST_FACTOR_1, LIST_FACTOR_2, MAX_VALUE))
