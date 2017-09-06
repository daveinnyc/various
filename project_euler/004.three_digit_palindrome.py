'''
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from
  the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.


Solution:
Copyright 2017 Dave Cuthbert 
License MIT
'''

def check_if_palindrome(number):
    end_index = -1
    mid_point = int(len(number) / 2)
    for begin_index in range(mid_point + 1):
        if number[begin_index] != number[end_index]:
            break
        if begin_index >= mid_point:
            return True

        end_index -= 1
    return False


def get_biggest_palindrome(upper_limit):
    for number in reversed(range(10000, upper_limit)):
        if check_if_palindrome(str(number)):
            return number    


def factor_number(number):
    # Range upper limit = 999 + 1
    for divisor_1 in reversed(range(100,1000)):
        if number % divisor_1 == 0:
            divisor_2 = int(number / divisor_1)
            if ((len(str(divisor_1)) == len(str(divisor_2))) and
                (len(str(divisor_1)) == 3)):
                # If factorable and 3 digits return the divisors
                return (0, divisor_1, divisor_2)

    # If no factors, return the palindrome instead
    return (number, 0, 0)


def check_palindromes():
    # Range upper limit starts with (999 * 999) + 1
    upper_limit = 998002
    
    while True:
        palindrome = get_biggest_palindrome(upper_limit)
        solution = factor_number(palindrome)
    
        if solution[0] == 0:
            # Factors were found
            return(solution[1], solution[2])
        else:
            # No factors were found
            upper_limit = solution[0]


def solve_problem():
    solution = check_palindromes()

    return (solution[0], solution[1], solution[0] * solution[1])
           

if __name__ == "__main__":
        print(solve_problem())
