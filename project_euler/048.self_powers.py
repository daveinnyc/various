'''
Problem 048

he series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 
             1**1 + 2**2 + 3**3 + ... + 1000**1000.


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''


def solve_problem(power):
    total = 0
    for num in range(1,power+1):
        total += num ** num

    answer = total % (10 ** 10)    
    return(answer)


if __name__ == "__main__":
    print(solve_problem(1000))
