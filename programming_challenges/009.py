'''
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
   a**2 + b**2 = c**2

For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

ie:     a + b + c == 1000   
        a**2 + b**2 == c**2

Find the product abc.

Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
import math

def generate_list_of_squares():
    list_of_squares = [n for n in range(1,1000001) if math.sqrt(n) == int(math.sqrt(n))]

    return list_of_squares

def check_for_triplets(list_of_squares):
    list_of_triplets = []
    # Rule is a < b < c so there are at least 2 sqs after first
    for first in range(0, len(list_of_squares) - 2):
        # And at least 1 sq after second
        for second in range(first + 1, len(list_of_squares) - 1):
            for third in range(second + 1, len(list_of_squares)):
                if (list_of_squares[first] + list_of_squares[second] == list_of_squares[third]):
                    a = int(math.sqrt(list_of_squares[first]))
                    b = int(math.sqrt(list_of_squares[second])) 
                    c = int(math.sqrt(list_of_squares[third]))
                    list_of_triplets.append((a,b,c))

    return list_of_triplets


def check_for_sum(triplet):
    if (triplet[0] + triplet[1] + triplet[2] == 1000):
        return True

    return False

def solve_problem():
    list_of_squares = generate_list_of_squares()
    list_of_triplets = check_for_triplets(list_of_squares)

    for t in list_of_triplets:
        if check_for_sum(t):
            return t[0] * t[1] * t[2]
           

if __name__ == "__main__":
    print(solve_problem())
