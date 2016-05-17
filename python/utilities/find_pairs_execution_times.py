''' Get timing data for the find_pairs algorithms'''

import cProfile
import random
import find_pairs

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

print "SIMPLE: 10"
cProfile.run('find_pairs.find_pairs_simple(array_10)')
print "EFFICIENT: 10"
cProfile.run('find_pairs.find_pairs(array_10)')

print "SIMPLE: 1000"
cProfile.run('find_pairs.find_pairs_simple(array_1000)')
print "EFFICIENT: 1000"
cProfile.run('find_pairs.find_pairs(array_1000)')

print "SIMPLE: 100000"
cProfile.run('find_pairs.find_pairs_simple(array_100000)')
print "EFFICIENT: 100000"
cProfile.run('find_pairs.find_pairs(array_100000)')

'''
RESULTS
SIMPLE: 10
         25 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 find_pairs.py:2(find_pairs_simple)
       11    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       11    0.000    0.000    0.000    0.000 {range}


EFFICIENT: 10
         22 function calls in 0.003 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.001    0.001    0.002    0.002 collections.py:1(<module>)
        1    0.000    0.000    0.000    0.000 collections.py:26(OrderedDict)
        1    0.000    0.000    0.000    0.000 collections.py:390(Counter)
        1    0.001    0.001    0.003    0.003 find_pairs.py:39(find_pairs)
        1    0.001    0.001    0.001    0.001 heapq.py:31(<module>)
        1    0.000    0.000    0.000    0.000 keyword.py:11(<module>)
        2    0.000    0.000    0.000    0.000 {len}
       10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {range}


SIMPLE: 1000
         2005 function calls in 0.038 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.038    0.038 <string>:1(<module>)
        1    0.035    0.035    0.038    0.038 find_pairs.py:2(find_pairs_simple)
     1001    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1001    0.003    0.000    0.003    0.000 {range}


EFFICIENT: 1000
         1007 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 find_pairs.py:39(find_pairs)
        2    0.000    0.000    0.000    0.000 {len}
     1000    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {range}


SIMPLE: 100000
         200005 function calls in 371.121 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000  371.121  371.121 <string>:1(<module>)
        1  338.864  338.864  371.121  371.121 find_pairs.py:2(find_pairs_simple)
   100001    0.016    0.000    0.016    0.000 {len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   100001   32.240    0.000   32.240    0.000 {range}


EFFICIENT: 100000
         100007 function calls in 1.970 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    1.970    1.970 <string>:1(<module>)
        1    1.959    1.959    1.968    1.968 find_pairs.py:39(find_pairs)
        2    0.000    0.000    0.000    0.000 {len}
   100000    0.007    0.000    0.007    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.002    0.001    0.002    0.001 {range}
'''        
