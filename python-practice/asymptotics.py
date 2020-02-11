''' p15 

Compare append to a list O(1)
 with insert at a location O(n)

Show example syntax for cProfile, timeit

Copytright 2017, Dave CUthbert, MIT License
'''
def _append():
    num_list = []
    for i in range(LIMIT):
       num_list.append(1)


def _insert():
    num_list = []
    for i in range(LIMIT):
       num_list.insert(0,i)


if "__main__" == __name__:
    import cProfile as p
    import timeit

    LIMIT = 1000

    # cProfile example
    p.run('_append()')
    p.run('_insert()')

    # timeit example
    print(timeit.timeit('_append()', setup='from __main__ import _append', number = 10))
 

      
# RESULTS
'''
LIMIT = 100000
python asymptotics.py 
         100004 function calls in 0.030 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.030    0.030 <string>:1(<module>)
        1    0.021    0.021    0.030    0.030 asymptotics.py:10(_append)
        1    0.000    0.000    0.030    0.030 {built-in method builtins.exec}
   100000    0.009    0.000    0.009    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         100004 function calls in 3.023 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    3.023    3.023 <string>:1(<module>)
        1    0.043    0.043    3.022    3.022 asymptotics.py:16(_insert)
        1    0.000    0.000    3.023    3.023 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   100000    2.979    0.000    2.979    0.000 {method 'insert' of 'list' objects}


###################################################################################################

LIMIT = 1000000
python asymptotics.py 
         1000004 function calls in 0.299 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.003    0.003    0.299    0.299 <string>:1(<module>)
        1    0.202    0.202    0.296    0.296 asymptotics.py:8(_append)
        1    0.000    0.000    0.299    0.299 {built-in method builtins.exec}
  1000000    0.094    0.000    0.094    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


         1000004 function calls in 473.236 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.013    0.013  473.236  473.236 <string>:1(<module>)
        1    2.389    2.389  473.223  473.223 asymptotics.py:14(_insert)
        1    0.000    0.000  473.236  473.236 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
  1000000  470.834    0.000  470.834    0.000 {method 'insert' of 'list' objects}

'''

