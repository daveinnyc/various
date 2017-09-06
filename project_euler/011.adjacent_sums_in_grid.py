'''
Problem 11

In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''

from functools import reduce
from operator import mul

twenty_grid = \
"08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48".split()
twenty_grid = [int(n) for n in twenty_grid]

def evaluate_group(group):
    if 0 in group:
        return 0
    
    return reduce(mul, group)


def check_horizontal():
    product_h = 1
    for i in range(len(twenty_grid) - 3):
        group = twenty_grid[i: i + 4]
        tmp = evaluate_group(group)
        if tmp > product_h:
            product_h = tmp

    return product_h


def check_vertical():
    product_v = 1
    # Vertical slices moving across the grid
    for i in range(20):
        # Vertical slices moving down the grid
        for j in range(17):
            start = (j * 20) + i
            group = [twenty_grid[start],
                     twenty_grid[start + 20],
                     twenty_grid[start + 40],
                     twenty_grid[start + 60]]
            tmp = evaluate_group(group)
            if tmp > product_v:
                product_v = tmp

    return product_v


def check_diagonal_up():
    product_d = 1
    # Move across grid
    for i in range(20 - 3):
        # Slices on a lower left to upper right angle
        for j in range(3, 20):
            start = (j * 20) + i
            group = [twenty_grid[start],
                     twenty_grid[start - 20 + 1],
                     twenty_grid[start - 40 + 2],
                     twenty_grid[start - 60 + 3]]
            tmp = evaluate_group(group)
            if tmp > product_d:
                product_d = tmp
            
    return product_d


def check_diagonal_down():
    product_d = 1
    # Move across grid 
    for i in range(20 - 3):
        # Slices on a upper left to lower right angle
        for j in range(20-3):
            start = (j * 20) + i
            group = [twenty_grid[start],
                     twenty_grid[start + 20 + 1],
                     twenty_grid[start + 40 + 2],
                     twenty_grid[start + 60 + 3]]
            tmp = evaluate_group(group)
            if tmp > product_d:
                product_d = tmp
    return product_d


def solve_problem():
    largest = 0
    horizontal = check_horizontal()
    vertical = check_vertical()
    diagonal_up = check_diagonal_up()
    diagonal_down = check_diagonal_down()

    for product in [horizontal, vertical, diagonal_up, diagonal_down]:
        if product > largest:
            largest = product

    return largest


if __name__ == "__main__":
    #print(twenty_grid)
    print(solve_problem())
