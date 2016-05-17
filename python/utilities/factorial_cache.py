'''
Experiment to create a simple lookup cache 

Author: Dave Cuthbert
Copyright: 2016
License: MIT
'''


def func_fact(x):
    """
    >>> func_fact(0) 
    0
    >>> func_fact(1) 
    1
    >>> func_fact(4) 
    24
    >>> func_fact(10) 
    3628800
    >>> func_fact(20) 
    2432902008176640000L
    
    """
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * func_fact(x-1)
    

def func_f_cache(x):
    """
    >>> func_f_cache(0) 
    0
    >>> func_f_cache(1) 
    1
    >>> func_f_cache(4) 
    24
    >>> func_fact(10) 
    3628800
    >>> func_fact(20) 
    2432902008176640000L
   
    """
    if x in f_cache:
        return f_cache[x]
    else:
        f_cache[x] = x * func_f_cache(x-1)
        return f_cache[x] 



#Cache should be accessible between function invocations
f_cache = dict()
f_cache[0] = 0
f_cache[1] = 1
 

#Profile running code to see if the cache makes any difference    
#Code runs too fast to see much, the extra runs magnify differences
import cProfile
cProfile.run('for i in range(100): func_fact(750)')
cProfile.run('for i in range(100): func_f_cache(750)')


if "__main__" == __name__:
    import doctest
    doctest.testmod()

'''
RESULTS
NOTE: Results were the same w/ and w/o running doctest (so no precaching)

         75003 function calls (103 primitive calls) in 0.053 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.001    0.001    0.053    0.053 <string>:1(<module>)
75000/100    0.052    0.000    0.052    0.001 factorial_cache.py:1(func_fact)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {range}


         852 function calls (103 primitive calls) in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
  849/100    0.001    0.000    0.001    0.000 factorial_cache.py:28(func_f_cache)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {range}
'''
