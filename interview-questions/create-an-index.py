''' TASK: 
    Open up a file
    Produce an index of words in it
    Don't repeat the line number for duplicate words
'''    
    
from collections import defaultdict
import pprint as pp
    
def read_file(filename):
    try:
        f = open(filename, 'r')
    except Exception as e:
        print("Error opening file: {}".format(e))
        
    while True:
        line = f.readline()
        if line == '':
            break
        yield line
        
    f.close()
        
        
        
    
def create_index(input_file):
    word_locations = defaultdict(list)
    count = 0
    for line in read_file(TEST_FILE):
        count += 1
        words = line.split()
        for w in words:
            word_locations[w].append(count)

    # FOR DEBUGING
    # pp.pprint(word_locations)
    
    for k,v in sorted(word_locations.items()):
        lines = set(v) 
        lines = list(lines) # Python prints sets as 'set([val1, val2, ..., valn])'
        print("{}: {}".format(k, lines))
    
    
    
if "__main__" == __name__:
    TEST_FILE = "words" 
    create_index(TEST_FILE)
