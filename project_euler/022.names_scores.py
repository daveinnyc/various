'''
Problem 022

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
   containing over five-thousand first names, begin by sorting it into 
   alphabetical order. Then working out the alphabetical value for each name, 
   multiply this value by its alphabetical position in the list to obtain a 
   name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
    worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN 
    would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file? 


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''
import string
from collections import defaultdict

def count_values(name):
    values = defaultdict()
    for position, letter in enumerate(string.ascii_uppercase):
        values[letter] = position + 1

    count = 0
    for ltr in name:
        count += values[ltr]

    return count


def solve_problem():
    with open('022.names.input', 'r') as names_file:
        names = names_file.read().split(',')
        names = [name.strip('"') for name in names]
    names = sorted(names)
    
    total = 0
    for position, value in enumerate(names):
        total += count_values(value) * (position + 1)
    return(total)


if __name__ == "__main__":
    print(solve_problem())
