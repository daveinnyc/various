'''
Problem 036

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in 
   base 10 and base 2.

(Please note that the palindromic number, in either base, may not include 
   leading zeros.)


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
def is_palindrome(number):
    if str(number) == str(number)[::-1]:
        return True

    return False


def solve_problem(limit):
    palindromes = []

    for n in range(1, limit):
        if is_palindrome(n):
            if is_palindrome(format(n, 'b')):
                palindromes.append(n)


    return(sum(palindromes))


if __name__ == "__main__":
    limit = 1000000
    print(solve_problem(limit))
