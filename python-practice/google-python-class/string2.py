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


# D. verbing
# Given a string, if its length is at least 3, add 'ing' to its end.
# Unless it already ends in 'ing', in which case add 'ly' instead.
# If the string length is less than 3, leave it unchanged.

def verbing(s):
  if len(s) > 2:
      if s[-3:] == 'ing':
          s = s + 'ly'
      else:
          s = s + 'ing'

  return s


# E. not_bad
# Given a string, find the first appearance of the substring 'not' and 'bad'. 
# If the 'bad' follows 'not', replace the whole 'not'...'bad' substring with 'good'.
def not_bad(s):
  start_not = s.find('not')
  if start_not >= 0:
      start_bad = s[(start_not + 2):].find('bad')
      if start_bad >= 0:
          s = s.replace(s[start_not:((start_not + 2) + (start_bad + 3))], 'good')
  
  return s


# F. front_back
# If the length is odd, we'll say that the extra char goes in the front half.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  return_front = ''
  return_back = ''
  for whole in [a,b]:
      n = len(whole) // 2
      if (len(whole) % 2) != 0:
          n += 1

      return_front += whole[:n]
      return_back += whole[n:]

  return return_front + return_back


# Simple provided test() function used in main() to print()
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")
  # Additional tests
  test(not_bad("not at the beginning bad at the beginning"), "good at the beginning")
  test(not_bad("and notbad no space between"), "and good no space between")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
