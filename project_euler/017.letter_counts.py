'''
Problem 017

If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
  then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in 
  words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
  forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 
  letters. The use of "and" when writing out numbers is in compliance with 
  British usage. 


Solution: Copyright 2017 Dave Cuthbert, MIT License
'''

ones_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
              'eight', 'nine', 'ten', 'eleven',  'twelve', 'thirteen',
              'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
              'nineteen']
              
tens_names = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
              'seventy', 'eighty', 'ninety']


def build_words(n):
    if n == 1000:
        return 'one' + 'thousand'
    elif n > 99:
        hundreds = ones_names[int(n / 100)] + 'hundred'
        n = n % 100
        if n == 0:
            return hundreds
        return hundreds + 'and' + build_words(n)
    elif n > 19:
        tens = tens_names[int(n / 10)]
        n = n % 10
        if n == 0:
            return tens
        return tens + ones_names[n]
    else:
        return ones_names[n]

    

def solve_problem():
    total_letters = 0
    for n in range(1,1001):
        total_letters += len(build_words(n))


    return(total_letters)


if __name__ == "__main__":
    print(solve_problem())
