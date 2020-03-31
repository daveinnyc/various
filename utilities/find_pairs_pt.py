# Two versions of working with a list. The first is a nested loop, the second 
#     uses a dictionary for better access time.
#
# NOTE: This version has been updated to python3 

def find_pairs_simple(candidate_array, TARGET_VALUE=10):
    for i in range(len(candidate_array)):
        for j in range(i + 1, len(candidate_array)):
            if (TARGET_VALUE == candidate_array[i] + candidate_array[j]):
                if RUN_STANDALONE:
                   print(f"{candidate_array[i]}, {candidate_array[j]}")
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
                       print(f"{candidate_array[i]}, {pair_value}")
                    else:
                       None
    return 0
      
    

if "__main__" == __name__:
   RUN_STANDALONE = True
   
   # A few demo tests for printing in case the file is run standalone. 
   # Proper tests are in the pytest file
   
   smoke_tests = [([9,1,6], "9,1"), ([1,3,7,5,9], "1,9  3,7"), ([13,-3,7,5,9], "13,-3")]
   for test_pair in smoke_tests:
       test_list, response = test_pair
       print(f"\n\nTEST LIST: {test_list}  RESPONSE: {response}")
       print("SIMPLE VERSION")
       find_pairs_simple(test_list)
       print("DICTIONARY VERSION")
       find_pairs(test_list)
   
#EOF
