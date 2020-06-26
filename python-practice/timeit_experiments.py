import timeit

def add(num, reps):
    return_value = 0
    for i in range(reps):
        return_value += num
    
    return return_value

    
def multiply(num, reps):
    return num * reps
        

if __name__ == "__main__":
    NUM = [5, 50, 500]
    REPS = [10, 1000, 10000000]

    for (n,r) in zip(NUM, REPS):
        # Can't pass a function directly. Timeit needs a callable thing so use lambda
        # number defaults to 3 repetitions, left at default to show syntax
        print(f"ADD: {n} {r}  -> ", end="")
        print(min(timeit.repeat(lambda: add(n, r), number=50)))
        print(f"MULTIPLY: {n} {r}  -> ", end="")
        print(min(timeit.repeat(lambda: multiply(n, r), number=50)))
        print()
