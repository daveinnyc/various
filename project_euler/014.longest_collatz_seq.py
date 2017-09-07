'''
Problem 014

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
    10 terms. Although it has not been proved yet (Collatz Problem), it is 
    thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million. 


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
from collections import defaultdict

def extend_sequence(n):
    if n == 1:
        return 1

    if n % 2 == 0:
        next_value = int(n / 2)
    else:
        next_value = 3 * n + 1
   
    return next_value


def solve_problem(cap_value):
    longest_n  = 1
    longest_length = 1
    seq_cache = defaultdict(int)

    for current_n in range(cap_value, 0, -1):
        current_length = 1
        next_n = current_n
        while next_n > 1:
            next_n = extend_sequence(next_n)

            if seq_cache[next_n] > 0:
                current_length += seq_cache[next_n]
                break
            current_length += 1

        
        seq_cache[current_n] = current_length
        if current_length > longest_length:
            longest_n = current_n
            longest_length = current_length

    return(longest_n, longest_length)


if __name__ == "__main__":
    cap_value = 999999
    print(solve_problem(cap_value))
