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


# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. 

def remove_adjacent(nums):
  if len(nums) < 1:
      return nums

  index = 0
  new_list = [nums[0]]
  
  while index < len(nums):
      if new_list[-1] != nums[index]:
          new_list.append(nums[index])
      index += 1    
  return new_list


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. Solution should work making a single
# pass of both lists.

def linear_merge(list1, list2):
  index1 = 0
  index2 = 0
  output = []

  while index1 < len(list1):
      # Is there anything left in list2
      if index2 < len(list2):
          if list1[index1] <= list2[index2]:
              output.append(list1[index1])
              index1 += 1
          else:
              output.append(list2[index2])
              index2 += 1
      # Nothing left in list2, flush any remaining list1 items        
      else: 
          output.extend(list1[index1:])
          index1 = len(list1)

  # Check if anything left in list2        
  if index2 < len(list2):
      output.extend(list2[index2:])

  return output


# Simple provided test() function used in main() to print()
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
