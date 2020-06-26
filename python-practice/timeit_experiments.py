import timeit

def add(num, reps):
    return_value = 0
    for i in range(reps):
        return_value += num
    
    return return_value

    
def multiply(num, reps):
    return num * reps
        

if __name__ == "__main__":
    NUM = [12345, 12345, 12345, 12345, 12345]
    REPS = [10, 1000, 10000, 100000, 10000000]

    for (n,r) in zip(NUM, REPS):
        # Can't pass a function directly. Timeit needs a callable thing so use lambda
        # number defaults to 3 repetitions, left at default to show syntax
        print(f"ADD: {n} {r}  -> ", end="")
        print(min(timeit.repeat(lambda: add(n, r), number=50)))
        print(f"MULTIPLY: {n} {r}  -> ", end="")
        print(min(timeit.repeat(lambda: multiply(n, r), number=50)))
        print()

##### Results
# NB: Remember the e part of the expression moves the decimal point
'''
ADD: 12345 10  -> 5.661800969392061e-05
MULTIPLY: 12345 10  -> 1.3364944607019424e-05

ADD: 12345 1000  -> 0.003082380979321897
MULTIPLY: 12345 1000  -> 1.2878095731139183e-05

ADD: 12345 10000  -> 0.032534003956243396
MULTIPLY: 12345 10000  -> 1.3364944607019424e-05

ADD: 12345 100000  -> 0.3284715060144663
MULTIPLY: 12345 100000  -> 1.3121054507791996e-05

'''