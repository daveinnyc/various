'''  Import the main file and then run cProfile against it

     Results are at end of this file. 

    Copyright 2017 Dave Cuthbert, MIT License
'''
import cProfile
import word_appearances as w
import os


if __name__ == '__main__':
    file_names = ['word_appearances.short_input', 'word_appearances.test_input', 
                  'word_appearances.long_input']

    for input_file in file_names:
        print('\n\n\n### RUNNING {} ###'.format(input_file))
        print('## PROCESS FILE ##')
        cProfile.run('counts = w.read_file(input_file)')
        print('\n\n## SORT FILE ##')
        cProfile.run('w.print_to_file()')
        print('Number of input lines: {}'.format(counts[0]))
        print('Number of input words: {}'.format(counts[1]))
        print('Number of unique words: {}'.format(len(w.words_by_line)))
        if os.path.exists('output'):
            os.remove('output')



'''
(EDITED) RESULTS BELOW HERE
### RUNNING word_appearances.short_input ###
## PROCESS FILE ##
149 function calls in 0.000 seconds

## SORT FILE ##
37 function calls in 0.000 seconds

Number of input lines: 5
Number of input words: 37
Number of unique words: 14



### RUNNING word_appearances.test_input ###
## PROCESS FILE ##
18173 function calls in 0.019 seconds

## SORT FILE ##
2111 function calls in 0.004 seconds

Number of input lines: 500
Number of input words: 4776
Number of unique words: 1051



### RUNNING word_appearances.long_input ###
## PROCESS FILE ##
15957126 function calls in 16.075 seconds

## SORT FILE ##
167405 function calls in 0.660 seconds

Number of input lines: 567050
Number of input words: 4974582
Number of unique words: 83698


'''    
#EOF
