''' Get timing data for the find_pairs algorithms'''

import cProfile
import random
import find_pairs_pt 

array_10 = []
array_100 = []
array_1000 = []
array_100000 = []
for i in range(10):
    array_10.append(random.randrange(-100,100)) 
for i in range(1000):
    array_1000.append(random.randrange(-100,100)) 
for i in range(100000):
    array_100000.append(random.randrange(-100,100)) 

print("SIMPLE: 10")
cProfile.run('find_pairs_pt.find_pairs_simple(array_10)')
print("EFFICIENT: 10")
cProfile.run('find_pairs_pt.find_pairs(array_10)')

print("SIMPLE: 1000")
cProfile.run('find_pairs_pt.find_pairs_simple(array_1000)')
print("EFFICIENT: 1000")
cProfile.run('find_pairs_pt.find_pairs(array_1000)')

print("SIMPLE: 100000")
cProfile.run('find_pairs_pt.find_pairs_simple(array_100000)')
print("EFFICIENT: 100000")
cProfile.run('find_pairs_pt.find_pairs(array_100000)')


'''
RESULTS
SIMPLE: 10
         15 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 find_pairs_pt.py:4(find_pairs_simple)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       11    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


EFFICIENT: 10
         19 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:997(_handle_fromlist)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 find_pairs_pt.py:16(find_pairs)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


SIMPLE: 1000
         3326 function calls in 0.067 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.067    0.067 <string>:1(<module>)
        1    0.066    0.066    0.067    0.067 find_pairs_pt.py:4(find_pairs_simple)
        1    0.000    0.000    0.067    0.067 {built-in method builtins.exec}
     1001    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     2321    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


EFFICIENT: 1000
         3330 function calls in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:997(_handle_fromlist)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
        1    0.001    0.001    0.002    0.002 find_pairs_pt.py:16(find_pairs)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
     3321    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


SIMPLE: 100000
         23716816 function calls in 632.172 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    1.428    1.428  632.172  632.172 <string>:1(<module>)
        1  624.703  624.703  630.744  630.744 find_pairs_pt.py:4(find_pairs_simple)
        1    0.000    0.000  632.172  632.172 {built-in method builtins.exec}
   100001    0.040    0.000    0.040    0.000 {built-in method builtins.len}
 23616811    6.001    0.000    6.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


EFFICIENT: 100000
         23716820 function calls in 17.902 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:997(_handle_fromlist)
        1    1.281    1.281   17.902   17.902 <string>:1(<module>)
        1   11.758   11.758   16.621   16.621 find_pairs_pt.py:16(find_pairs)
        1    0.000    0.000   17.902   17.902 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.len}
 23716811    4.863    0.000    4.863    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
