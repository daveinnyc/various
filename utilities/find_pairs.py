
def find_pairs_simple(candidate_array, TARGET_VALUE=10):
    """Find pairs of numbers that sum to TARGET_VALUE, e.g. 10.
       This version runs slower than the modified one below

    >>> find_pairs_simple([9])
    
    >>> find_pairs_simple([1,9])
    1,9
    >>> find_pairs_simple([9,1])
    9,1
    >>> find_pairs_simple([9,1,6])
    9,1
    >>> find_pairs_simple([9,6,1])
    9,1
    >>> find_pairs_simple([9,6,1,4,7])
    9,1
    6,4
    >>> find_pairs_simple([5])
    
    >>> find_pairs_simple([5,5])
    5,5
    >>> find_pairs_simple([1,3,7,5,9])
    1,9
    3,7
    >>> find_pairs_simple([1,3,7,5,9], 14)
    5,9
    >>> find_pairs_simple([13,-3,7,5,9])
    13,-3
    """
    for i in range(len(candidate_array)):
        for j in range(i, len(candidate_array)):
            if (TARGET_VALUE == candidate_array[i] + candidate_array[j]):
                #print "%d,%d" % (candidate_array[i], candidate_array[j])
                None



def find_pairs(candidate_array, TARGET_VALUE=10):
    """Find pairs of numbers that sum to TARGET_VALUE, e.g. 10.
       
    
    >>> find_pairs([9])
    
    >>> find_pairs([1,9])
    1,9
    >>> find_pairs([9,1])
    9,1
    >>> find_pairs([9,1,6])
    9,1
    >>> find_pairs([9,6,1])
    9,1
    >>> find_pairs([9,6,1,4,7])
    9,1
    6,4
    >>> find_pairs([5])
    
    >>> find_pairs([5,5])
    5,5
    >>> find_pairs([1,3,7,5,9])
    1,9
    3,7
    >>> find_pairs([1,3,7,5,9], 14)
    5,9
    >>> find_pairs([13,-3,7,5,9])
    13,-3   
    """
    
    from collections import defaultdict
    positions = defaultdict(list)
     
    #Read everything into a dictionary, storing the original array position 
    for i in range(len(candidate_array)):
        positions[candidate_array[i]].append(i)

    #Read list comparing value to TARGET_VALUE 
    for i in range(len(candidate_array)):
        pair_value = TARGET_VALUE - candidate_array[i]
        if positions[pair_value]:
            for p in positions[pair_value]:
                if p > i:
                    #print "%d,%d" % (candidate_array[i], pair_value)
                    None
      
    

if "__main__" == __name__:
    import doctest
    doctest.testmod()
    
#EOF
