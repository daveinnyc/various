''' Read in a text file
    For every word, print the line number it appears on


    The long file is made from about 20 book files that were taken from 
    project gutenberg and concatenated into a single large text file
  
    prompt> wc word_appearances.long_input 
    567050  4974570 28646326 word_appearances.long_input

    Copyright 2017 Dave Cuthbert, MIT License
'''
from collections import defaultdict
import string

## Some (more or less arbitrary) filter constants
MAXIMUM_NUMBER_OF_INSTANCES = 20    # Cut down on noise from frequent words

# Shared data store
words_by_line = defaultdict(list)


def read_file(input_words_file):
    line_count = 0
    word_count = 0
    with open(input_words_file, 'r') as f:
        for line in f:
            line_count += 1
            words = line.split()
            for w in words:
                word_count += 1
                clean = apply_filters(w)
                if clean != False:
                    if (words_by_line[clean]) and (words_by_line[clean][-1] \
                        ==  line_count):
                        pass
                    else:
                        words_by_line[clean].append(line_count)

    return (line_count, word_count)


def apply_filters(word):
    clean_word = ''
    word = word.lower()
    for letter in word:
         if letter in (string.ascii_lowercase or string.digits):
             clean_word += letter
    
    # Filter out some noisy results
    if len(words_by_line[clean_word]) > MAXIMUM_NUMBER_OF_INSTANCES - 1:
        return False

    return clean_word


def print_dictionary():
    for key in sorted(words_by_line):
        print('{}\t\t{}'.format(key, words_by_line[key]))


def print_to_file():
    with open('output','w') as output_file:
        for key in sorted(words_by_line):
            output_file.write('{}\t\t{}'.format(key, words_by_line[key]))



if __name__ == '__main__':
    #input_file = 'word_appearances.short_input'
    input_file = 'word_appearances.long_input'
    #input_file = 'word_appearances.test_input'  #1st 500 lines of long_input

    counts = read_file(input_file)
    print_dictionary()

    print('Number of input lines: {}'.format(counts[0]))
    print('Number of input words: {}'.format(counts[1]))
    print('Number of unique words: {}'.format(len(words_by_line)))
    
#EOF
