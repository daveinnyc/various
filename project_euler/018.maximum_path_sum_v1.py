'''
Problem 018

By starting at the top of the triangle below and moving to adjacent numbers on
    the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by 
   trying every route. However, Problem 67, is the same challenge with a 
   triangle containing one-hundred rows; it cannot be solved by brute force, 
   and requires a clever method! ;o)



Solution: Copyright 2017 Dave Cuthbert, MIT License
'''

triangle = { 1: [75,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
             2: [95, 64,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
             3: [17, 47, 82,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
             4: [18, 35, 87, 10,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
             5: [20,  4, 82, 47, 65,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
             6: [19,  1, 23, 75,  3, 34,  0,  0,  0,  0,  0,  0,  0,  0,  0],
             7: [88,  2, 77, 73,  7, 63, 67,  0,  0,  0,  0,  0,  0,  0,  0],
             8: [99, 65,  4, 28,  6, 16, 70, 92,  0,  0,  0,  0,  0,  0,  0],
             9: [41, 41, 26, 56, 83, 40, 80, 70, 33,  0,  0,  0,  0,  0,  0],
            10: [41, 48, 72, 33, 47, 32, 37, 16, 94, 29,  0,  0,  0,  0,  0],
            11: [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,  0,  0,  0,  0],
            12: [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,  0,  0,  0],
            13: [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,  0,  0],
            14: [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,  0],
            15: [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
          }

small_triangle = { 1: [3, 0, 0, 0],
                   2: [7, 4, 0, 0],
                   3: [2, 4, 6, 0],
                   4: [8, 5, 9, 3]
                 }


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
    for r in range(len(triangle.keys()),1,-1):
        answer = process_row(r)
    return(answer[0])


if __name__ == "__main__":
    print(solve_problem())
