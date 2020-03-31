# Two versions of working with a list. The first is a nested loop, the second 
#     uses a dictionary for better access time.


def find_pairs_simple(candidate_array, TARGET_VALUE=10):
    for i in range(len(candidate_array)):
        for j in range(i + 1, len(candidate_array)):
            if (TARGET_VALUE == candidate_array[i] + candidate_array[j]):
                if RUN_STANDALONE:
                   print "%d,%d" % (candidate_array[i], candidate_array[j])
               else:
                   None

    return 0



def find_pairs(candidate_array, TARGET_VALUE=10):
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
                    if RUN_STANDALONE:
                       print "%d,%d" % (candidate_array[i], pair_value)
                   else:
                       None
    return 0
      
    

if "__main__" == __name__:
   RUN_STANDALONE = True
   test_pairs = [ :

#EOF
