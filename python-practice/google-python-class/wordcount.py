#!/usr/bin/python3 -tt

# Original was:
# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Comments stripped out, answered and updated for python3 
# Copyright 2020 Dave Cuthbert
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.


"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Store all the words as lowercase, so 'The' and 'the' count as the same word.

2. For the --topcount flag, print just the top 20 most common words 
"""

from collections import defaultdict
import sys

# Dictionary to store word frequencies
word_counts = defaultdict(int)

def get_word_list(filename):
    with open(filename) as f:
        for line in f:
            for word in line.split():
                word_counts[word.lower()] += 1


def print_words(filename):
    get_word_list(filename)

    for item in sorted(word_counts.items()):
        print(f"{item[0]} {item[1]}")


def print_top(filename):
    get_word_list(filename)

    count = 0
    for item in sorted(word_counts.items(),  reverse=True, key=lambda x: x[1]):
        if count < 5:
            print(f"{item[0]} {item[1]}")
            count += 1
        else:
            return     


# This basic command line argument parsing code is provided 
def main():
  if len(sys.argv) != 3:
    print('usage: ./wordcount.py {--count | --topcount} file')
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print('unknown option: ' + option)
    sys.exit(1)

if __name__ == '__main__':
  main()
