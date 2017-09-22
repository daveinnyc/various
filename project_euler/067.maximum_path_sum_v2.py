'''
Problem 067

By starting at the top of the triangle below and moving to adjacent numbers on
    the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom from the input file



Solution: Copyright 2017 Dave Cuthbert, MIT License
'''

from collections import defaultdict


def populate_triangle():
    row = 1
    data = defaultdict(list)

    # Read in each row
    with open('067.triangle.input', 'r') as input_file:
        for line in input_file.readlines():
            if len(line) > 1:
                data[row] = [int(n) for n in line.split()]
                row += 1

    # Pad out the row with 0s   
    for k in range(1,len(data)):
        while len(data[k]) < 100:
            data[k].append(0)

    return data


def process_row(row):
    processed_row = []
    left = right = 0
    for r in range(0,len(triangle[row]) - 1):
        if row > 1:
            left = triangle[row][r] + triangle[row-1][r]
            right = triangle[row][r + 1] + triangle[row-1][r]          
        if left > right:
            processed_row.append(left)
        else:
            processed_row.append(right)

    while len(processed_row) < len(triangle[row]):
        processed_row.append(0)

    triangle[row - 1] = processed_row

    return processed_row


def solve_problem():
    global triangle 
    triangle = populate_triangle()
    for r in range(len(triangle),1,-1):
        answer = process_row(r)
    return(answer[0])


if __name__ == "__main__":
    print(solve_problem())
