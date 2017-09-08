'''
Problem 025

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits? 


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''


def gen_fibonacci():
    term_1 = 1
    term_2 = 1

    while True:
       next_term = term_1 + term_2
       yield next_term
       term_2 = term_1
       term_1 = next_term


def solve_problem():
    get_fibonacci = gen_fibonacci()
    
    count = 3    # Not starting with first term in sequence    
    while True:
        current_fib = next(get_fibonacci)
        if len(str(current_fib)) >= 1000:
            return(count)
      
        count +=1


if __name__ == "__main__":
    print(solve_problem())
